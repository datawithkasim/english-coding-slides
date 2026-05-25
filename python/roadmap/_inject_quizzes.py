"""
Injects supplementary slides into the hand-authored course-week HTML decks
(rs001-4, web001-3, ai001) so every deck conforms to the 12-slot PRIMM template
defined in TEMPLATE.md + PEDAGOGY.md + Desktop/dev/teaching-philosophy/README.md.

Pillars injected (conditionally — only if the deck doesn't already have the slot):
  - Slot 2  Recap & Retrieve     (per-week question, hidden answer)
  - Slot 3  Predict (Hook)       (code snippet with hidden output)
  - Slot 4  Vocab Preview        (Tier 3 terms with Korean glosses)
  - Slot 8  Common Mistake       (Debug pair — buggy vs fixed, language-aware)
  - Slot 10 Code Talk Frame      (ESL sentence frame per language)
  - "Extras" (non-pillar): Edge-cases card, MCQ quiz, Practice slide.

Insertion point: just before <div class="nav">.
The existing course-week close slide stays as the narrative wrap-up.

Idempotent: re-running first strips previously injected blocks (marked with
<!-- INJECTED-EXTRAS-START --> / <!-- INJECTED-EXTRAS-END -->), then re-adds.

Language detection is by course slug — so Python lessons get Python debug, JS
lessons get JS debug, etc. No more `pirnt` typos in CSS lessons.

Run: python _inject_quizzes.py
"""
from pathlib import Path
import html as html_mod
import re

ROOT = Path(__file__).resolve().parent.parent.parent  # english-coding-slides/

COURSE_GLOBS = [
    "python/rs001-text-adventure/week-*.html",
    "python/rs002-pokedex/week-*.html",
    "python/rs003-pygame-turret/week-*.html",
    "python/rs004-platformer/week-*.html",
    "webdev/web001-css/week-*.html",
    "webdev/web002-javascript/week-*.html",
    "webdev/web003-portfolio/week-*.html",
    "ai-coding/ai001-replit-agent/week-*.html",
]

TITLE_RE = re.compile(r"<title>(.*?)</title>", re.I | re.S)
SLIDE_COUNT_RE = re.compile(r'<span class="counter" id="counter">(\d+)\s*/\s*\d+</span>')
NAV_OPEN_RE = re.compile(r'<div class="nav">')

INJECTED_BLOCK_RE = re.compile(
    r"<!--\s*INJECTED-EXTRAS-START\s*-->.*?<!--\s*INJECTED-EXTRAS-END\s*-->",
    re.S,
)

PRE_RE = re.compile(r"<pre[^>]*>(.*?)</pre>", re.S | re.I)
H_RE = re.compile(r"<h[12][^>]*>(.*?)</h[12]>", re.S | re.I)
TAG_RE = re.compile(r"<[^>]+>")
BR_RE = re.compile(r"<br\s*/?>", re.I)
SLOT_BADGE_RE = re.compile(r'<span class="slot-badge">\s*SLOT\s*(\d+)\s*</span>', re.I)


# ----------------------------------------------------------------------
# Language detection by course slug
# ----------------------------------------------------------------------
# Used to keep auto-injected fallbacks language-correct — no more Python
# `pirnt` typos in CSS lessons. The audit (AUDIT-2026-05-13.md) flagged
# 30+ paste-error contaminations rooted in language-agnostic fallbacks.

LANG_BY_COURSE = {
    "rs001-text-adventure": "python",
    "rs002-pokedex": "python",
    "rs003-pygame-turret": "python",
    "rs004-platformer": "python",
    "web001-css": "html",         # weeks 1 = HTML, 2-7 = CSS; treat as html/css family
    "web002-javascript": "js",
    "web003-portfolio": "html",   # mixed HTML/CSS/JS; treat as html family for fallbacks
    "ai001-replit-agent": "prompt",
}


def detect_lang(path: Path) -> str:
    """Infer language from the course folder containing the deck."""
    course = path.parent.name
    return LANG_BY_COURSE.get(course, "python")


def strip_tags(s: str) -> str:
    # Replace <br> variants with a space BEFORE stripping tags so multi-line
    # headings like "<h1>Pokémon<br>Lists</h1>" don't collapse to "PokémonLists".
    # (Audit AUDIT-2026-05-13.md surfaced this as the MCQ Q2 garbled-title bug.)
    s = BR_RE.sub(" ", s)
    s = TAG_RE.sub("", s)
    s = s.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&").replace("&quot;", '"').replace("&#39;", "'").replace("&#x27;", "'")
    # Collapse internal whitespace runs.
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def present_slots(text: str) -> set:
    """Return the set of slot numbers already present in the deck (as ints).
    Used so we don't double-inject pillars that the deck author hand-wrote."""
    return {int(m.group(1)) for m in SLOT_BADGE_RE.finditer(text)}


def extract_corpus(text: str) -> dict:
    """Pull code blocks + headings out of a course-week HTML, BEFORE injection.
    Used so MCQs reference things students actually saw."""
    # Only look at non-injected part
    clean = INJECTED_BLOCK_RE.sub("", text)
    code_blocks = [strip_tags(m.group(1)) for m in PRE_RE.finditer(clean)]
    headings = [strip_tags(m.group(1)) for m in H_RE.finditer(clean)]
    return {"code_blocks": code_blocks, "headings": headings}


# ----------------------------------------------------------------------
# Pattern-based question builders. Each takes corpus → 0 or 1 MCQ tuple.
# ----------------------------------------------------------------------

DICT_LITERAL_RE = re.compile(r"(\w+)\s*=\s*\{([^{}]+)\}", re.S)
KEY_VAL_RE = re.compile(r"['\"](\w+)['\"]\s*:\s*([^,\n}]+)")
SUBSCRIPT_RE = re.compile(r"(\w+)\[['\"](\w+)['\"]\]")
PRINT_LIT_RE = re.compile(r"print\(\s*['\"]([^'\"]+)['\"]\s*\)")
ASSIGN_NUM_RE = re.compile(r"^\s*(\w+)\s*=\s*(\d+(?:\.\d+)?)\s*$", re.M)
FROM_IMPORT_RE = re.compile(r"from\s+(\w+)\s+import\s+(\w+)")


def q_subscript_lookup(corpus):
    """If slides show `x = {'a': 5, ...}` AND `x['a']`, ask what x['a'] returns."""
    # Find dict literals and their key -> value mapping
    var_to_kvs = {}
    for code in corpus["code_blocks"]:
        for dm in DICT_LITERAL_RE.finditer(code):
            varname, body = dm.group(1), dm.group(2)
            kvs = {k: v.strip() for k, v in KEY_VAL_RE.findall(body)}
            if kvs:
                var_to_kvs[varname] = kvs

    # Find subscripts referenced in slides
    for code in corpus["code_blocks"]:
        for sm in SUBSCRIPT_RE.finditer(code):
            v, k = sm.group(1), sm.group(2)
            if v in var_to_kvs and k in var_to_kvs[v]:
                val = var_to_kvs[v][k]
                # Build distractors from OTHER values in the same dict
                others = [vv for kk, vv in var_to_kvs[v].items() if kk != k]
                if not others:
                    others = ["None", "an empty string", "an error"]
                opts = [val] + others[:3]
                while len(opts) < 4:
                    opts.append("an error")
                return (
                    f"In the example, what does <code>{v}[{repr(k)}]</code> evaluate to?",
                    [html_mod.escape(o.strip("\"'")) for o in opts[:4]],
                    0,
                    f"{v}[{repr(k)}] looks up the key {repr(k)} → {val}",
                )
    return None


def q_print_literal(corpus):
    """If slides show `print("hello")`, ask what it prints."""
    for code in corpus["code_blocks"]:
        m = PRINT_LIT_RE.search(code)
        if m:
            lit = m.group(1)
            if len(lit) > 60:
                continue
            return (
                f"In the example, what does <code>print({repr(lit)})</code> output?",
                [lit, lit.upper(), "None", "an error"],
                0,
                f"print() writes its argument followed by a newline. Output: {lit}",
            )
    return None


def q_dict_syntax(corpus):
    """If a dict literal appears in slides, ask which is valid dict syntax."""
    for code in corpus["code_blocks"]:
        if DICT_LITERAL_RE.search(code):
            return (
                "In the example, which character pair creates a dict?",
                ["<code>{ }</code>", "<code>[ ]</code>", "<code>( )</code>", "<code>&lt; &gt;</code>"],
                0,
                "Curly braces { } with key: value pairs separate by commas.",
            )
    return None


def q_list_syntax(corpus):
    """If a list literal appears, ask which char pair creates one."""
    for code in corpus["code_blocks"]:
        if re.search(r"\w+\s*=\s*\[[^\[\]]*\]", code):
            return (
                "In the example, which character pair creates a list?",
                ["<code>[ ]</code>", "<code>{ }</code>", "<code>( )</code>", "<code>&lt; &gt;</code>"],
                0,
                "Square brackets [ ] create a list.",
            )
    return None


def q_from_import(corpus):
    """If slides show `from X import Y`, ask which line imports Y from X."""
    for code in corpus["code_blocks"]:
        m = FROM_IMPORT_RE.search(code)
        if m:
            mod, name = m.group(1), m.group(2)
            return (
                f"In the example, which line imports <code>{name}</code> from <code>{mod}.py</code>?",
                [
                    f"<code>from {mod} import {name}</code>",
                    f"<code>import {name} from {mod}</code>",
                    f"<code>include {mod}.{name}</code>",
                    f"<code>require('{mod}')</code>",
                ],
                0,
                f"Python uses `from MODULE import NAME` — note the order.",
            )
    return None


def q_assignment_value(corpus):
    """If slides show `x = 42`, ask what's stored in x."""
    for code in corpus["code_blocks"]:
        m = ASSIGN_NUM_RE.search(code)
        if m:
            var, val = m.group(1), m.group(2)
            if len(var) <= 12:
                return (
                    f"In the example, what value does <code>{var}</code> hold after the assignment?",
                    [val, "None", '"' + val + '"', "0"],
                    0,
                    f"{var} = {val} stores the integer/number {val}.",
                )
    return None


def q_heading_summary(corpus, topic, lang="python"):
    """Ask what the lesson is about — answer references the actual <h1>/<h2>."""
    # strip_tags now collapses <br>→space + whitespace runs, so headings like
    # "Pokémon<br>Lists" come back as "Pokémon Lists" instead of "PokémonLists".
    headings = [h for h in corpus["headings"] if 4 < len(h) < 60]
    if not headings:
        return None
    h = headings[0]
    # Language-aware distractors — no Python-only jargon in JS/HTML/CSS quizzes.
    distractors_by_lang = {
        "python": ["List comprehensions", "Decorators and metaclasses", "Multi-threaded I/O"],
        "js":     ["Async generators",     "Proxy + Reflect metaprogramming", "Service workers"],
        "html":   ["XML namespaces",       "Web Components shadow DOM",       "ARIA live regions"],
        "css":    ["CSS Houdini paint API","Container query units",           "Cascade layers"],
        "prompt": ["RLHF fine-tuning",     "Chain-of-thought distillation",   "Mixture-of-experts routing"],
    }
    distractors = distractors_by_lang.get(lang, distractors_by_lang["python"])
    return (
        f"Looking at the slide titles, what is this lesson mainly about?",
        [h, *distractors],
        0,
        f"The lesson title says it: {h}",
    )


# Generic fallbacks — only used when corpus yields nothing useful
def q_debug_from_corpus(corpus, topic_lc, lang="python"):
    debug = pick_debug(topic_lc, lang)
    code, bug, _ = debug
    short_bug = strip_tags(bug).replace("Bug: ", "")
    # Language-aware distractors — avoids the audit-flagged paste-errors like
    # "Variable not declared with let" appearing in Python lessons.
    distractors_by_lang = {
        "python": ["Nothing — works as written.", "Missing <code>import sys</code>.", "Wrong indentation depth."],
        "js":     ["Nothing — works as written.", "Missing semicolon.", "Variable not declared with <code>let</code>."],
        "html":   ["Nothing — renders fine.", "Missing <code>&lt;!DOCTYPE html&gt;</code>.", "Wrong attribute quote style."],
        "css":    ["Nothing — looks fine.", "Missing semicolon after a value.", "Selector doesn't match any element."],
        "prompt": ["Nothing — clear enough.", "Too long for the AI to handle.", "Missing a file extension hint."],
    }
    distractors = distractors_by_lang.get(lang, distractors_by_lang["python"])
    return (
        "What's wrong with this code?<br>"
        f'<pre style="font-size:.8em;margin-top:.4em">{html_mod.escape(code)}</pre>',
        [short_bug, *distractors],
        0,
        "Spot the typo or wrong logic.",
    )


def q_meta_done(topic):
    short = topic if len(topic) < 50 else topic[:50] + "..."
    return (
        f"For <b>{html_mod.escape(short)}</b>, what counts as 'done'?",
        [
            "Code runs without errors AND produces the expected output for several inputs.",
            "Code compiles.",
            "It looks neat in the editor.",
            "The IDE shows no red squiggles.",
        ],
        0,
        "No error ≠ correct. Test with multiple inputs.",
    )


CONTENT_BUILDERS = [
    q_subscript_lookup,
    q_print_literal,
    q_from_import,
    q_assignment_value,
    q_dict_syntax,
    q_list_syntax,
]

# ----------------------------------------------------------------------
# Per-week content overrides
# ----------------------------------------------------------------------
# Key: lowercased filename stem (e.g. "week-05-dictionaries")
# Each value can override any of: edges, debug (code, bug, fix), mcqs, practice

OVERRIDES = {
    # Per-week hand-authored overrides go here. Each key = filename stem.
    # Without an entry, MCQs are derived from THIS file's actual code blocks.
}


# ----------------------------------------------------------------------
# WEEK_VOCAB — Slot 4 (Vocab Preview)
# ----------------------------------------------------------------------
# Each entry: list of (term, english_meaning, korean_gloss) tuples.
# 3-4 terms per week. Tier 3 (domain-specific) only.
# Korean glosses follow the canonical brand form (영어코딩 house style).
# Glossary page (glossary.html) is the source of truth for rs001;
# remaining courses are authored here and should be mirrored into the
# glossary page on the next cleanup pass.

WEEK_VOCAB = {
    # rs002-pokedex
    "week-01-input-variables": [
        ("input()", "function that reads what the user types", "입력 받기"),
        ("variable", "a named box that holds a value", "변수"),
        ("f-string", "string with variables inside { }", "f-문자열"),
    ],
    "week-02-pokemon-lists": [
        ("list", "an ordered group of values in [ ]", "리스트"),
        ("index", "the number that locates an item in a list", "인덱스"),
        (".append()", "add an item to the end of a list", "리스트에 추가"),
    ],
    "week-03-cleaning-input": [
        (".strip()", "remove blank space from start and end", "공백 제거"),
        (".lower()", "change all letters to lowercase", "소문자로"),
        ("case sensitive", "'A' and 'a' count as different", "대소문자 구분"),
    ],
    "week-04-validation": [
        ("if / else", "two-way branch on a condition", "조건 분기"),
        ("in / not in", "test whether a value is inside a list", "포함 여부"),
        ("while", "repeat as long as a condition is true", "~동안 반복"),
    ],
    "week-05-dictionaries": [
        ("dict", "key-value mapping in { }", "딕셔너리"),
        ("key", "the label used to look up a value", "키 (이름표)"),
        ("value", "the data stored under a key", "값"),
        ("KeyError", "asked for a key that isn't in the dict", "없는 키 에러"),
    ],
    "week-06-functions": [
        ("def", "keyword that defines a function", "함수 정의"),
        ("parameter", "input the function expects", "매개변수"),
        ("return", "value the function gives back", "반환값"),
    ],
    "week-07-random-battle": [
        ("import", "load a Python module to use it", "가져오기"),
        ("random.choice", "pick one item from a list at random", "무작위 선택"),
        ("randint", "random whole number between two ends", "정수 무작위"),
    ],
    "week-08-final-showdown": [
        ("game loop", "the while-true that keeps the game running", "게임 루프"),
        ("game state", "the variables that describe what's happening now", "게임 상태"),
        ("end condition", "what makes the loop stop", "종료 조건"),
    ],

    # rs003-pygame-turret
    "week-01-pygame-window": [
        ("pygame.init()", "wake up the pygame engine", "파이게임 시작"),
        ("display.set_mode", "open a game window of a given size", "창 만들기"),
        ("event loop", "the loop that checks for clicks and keys", "이벤트 루프"),
        ("QUIT event", "the signal that the user closed the window", "종료 이벤트"),
    ],
    "week-02-turret-base": [
        ("surface", "any drawable image in pygame", "표면 (그림판)"),
        ("blit", "paste one surface onto another", "이미지 붙이기"),
        ("rect", "rectangle that holds x, y, width, height", "사각형 영역"),
    ],
    "week-03-functions-gun": [
        ("def", "keyword that defines a function", "함수 정의"),
        ("parameter", "input the function expects", "매개변수"),
        ("call site", "the place where you use the function", "함수 호출 위치"),
    ],
    "week-04-keyboard-movement": [
        ("pygame.key.get_pressed", "which keys are held down right now", "눌린 키 확인"),
        ("K_LEFT / K_RIGHT", "key constants for arrow keys", "방향키 상수"),
        ("velocity", "how fast something moves per frame", "속도"),
    ],
    "week-05-limit-range": [
        ("clamp", "force a value to stay inside a range", "값 가두기"),
        ("min / max", "smallest / largest allowed value", "최소 / 최대"),
        ("boundary", "the edge of the playable area", "경계선"),
    ],
    "week-06-for-loops": [
        ("for loop", "repeat once per item", "반복문"),
        ("range()", "sequence of numbers from start to end-1", "숫자 범위"),
        ("iteration", "one pass through the loop", "한 번의 반복"),
    ],
    "week-07-multiple-functions": [
        ("modular code", "code split into small reusable pieces", "모듈화"),
        ("single responsibility", "one function does one thing", "단일 책임"),
        ("naming", "good function names describe the action", "함수 이름 짓기"),
    ],
    "week-08-final-mini-game": [
        ("score", "the number that tracks player success", "점수"),
        ("game over", "the state when the player has lost", "게임 오버"),
        ("frame rate", "how many frames are drawn per second (FPS)", "초당 프레임 수"),
    ],

    # rs004-platformer
    "week-01-game-window": [
        ("pygame.init()", "wake up the pygame engine", "파이게임 시작"),
        ("display.set_mode", "open a game window of a given size", "창 만들기"),
        ("clock.tick(60)", "limit to 60 frames per second", "프레임 제한"),
    ],
    "week-02-player-keyboard": [
        ("sprite", "a movable character or object", "스프라이트"),
        ("rect", "rectangle that tracks position and size", "위치 사각형"),
        ("delta", "the amount to move per frame", "이동량"),
    ],
    "week-03-gravity-jump": [
        ("gravity", "constant downward pull each frame", "중력"),
        ("velocity_y", "current vertical speed", "수직 속도"),
        ("jump impulse", "sudden upward velocity from a jump", "점프 추진력"),
        ("ground", "the surface that stops downward motion", "지면"),
    ],
    "week-04-platforms-collision": [
        ("collision", "two rects overlap", "충돌"),
        ("colliderect", "pygame method that detects overlap", "겹침 확인"),
        ("platform", "a surface the player can stand on", "발판"),
    ],
    "week-05-level-design": [
        ("level", "the layout of one stage", "레벨 (단계)"),
        ("tile", "one piece of a level grid", "타일"),
        ("coordinates", "the (x, y) location on screen", "좌표"),
    ],
    "week-06-coins-score": [
        ("collectible", "an item the player picks up", "수집 아이템"),
        ("score", "the number that tracks progress", "점수"),
        ("remove", "delete an item from a list once collected", "리스트에서 제거"),
    ],
    "week-07-enemies-gameover": [
        ("enemy", "a sprite that hurts the player on contact", "적"),
        ("game state", "playing / dead / won — current mode", "게임 상태"),
        ("respawn", "put the player back at the start", "재시작"),
    ],
    "week-08-multi-level-final": [
        ("level transition", "moving from one level to the next", "레벨 전환"),
        ("level list", "list of level layouts to load in order", "레벨 목록"),
        ("polish", "final touch-ups before shipping", "마무리 다듬기"),
    ],

    # web001-css (week 1 = HTML, weeks 2-7 = CSS, week 8 = combine)
    "week-01-html-basics": [
        ("tag", "the angle-bracket label that names an element", "태그"),
        ("element", "an open tag, its content, and a close tag", "요소"),
        ("attribute", "extra info inside a tag (e.g. src, href)", "속성"),
        ("nesting", "putting one element inside another", "중첩"),
    ],
    "week-02-css-colors": [
        ("selector", "which element the style applies to", "선택자"),
        ("property", "what you're changing (color, font-size)", "속성"),
        ("value", "the new setting for the property", "값"),
        ("hex code", "6-digit color like #ff7849", "16진수 색상"),
    ],
    "week-03-box-model": [
        ("padding", "space INSIDE the box, around the content", "안쪽 여백"),
        ("margin", "space OUTSIDE the box, between boxes", "바깥 여백"),
        ("border", "the line at the edge of the box", "테두리"),
        ("box-sizing", "whether width includes padding or not", "박스 크기 기준"),
    ],
    "week-04-flexbox": [
        ("flex container", "the parent that arranges its children in a row/column", "플렉스 컨테이너"),
        ("justify-content", "spacing along the main axis", "주축 정렬"),
        ("align-items", "spacing along the cross axis", "교차축 정렬"),
        ("gap", "space between flex items", "항목 간격"),
    ],
    "week-05-images-hero": [
        ("hero section", "the big banner at the top of a page", "히어로 섹션"),
        ("background-image", "CSS image set behind an element", "배경 이미지"),
        ("alt text", "description of an image for screen readers", "대체 텍스트"),
    ],
    "week-06-responsive": [
        ("media query", "CSS that only applies at certain screen sizes", "미디어 쿼리"),
        ("breakpoint", "the width where the layout changes", "분기점"),
        ("viewport", "the visible area of the browser window", "뷰포트"),
    ],
    "week-07-hover-animations": [
        (":hover", "style that applies when the mouse is over an element", "호버 상태"),
        ("transition", "smooth change between two states", "전환"),
        ("transform", "move, rotate, or scale an element", "변형"),
    ],
    "week-08-final-site": [
        ("layout", "the overall arrangement of sections", "레이아웃"),
        ("hierarchy", "what looks most important to the eye", "시각적 위계"),
        ("polish", "small fixes that make a site feel finished", "마무리 다듬기"),
    ],

    # web002-javascript
    "week-01-hello-js": [
        ("console.log", "print a message to the browser console", "콘솔 출력"),
        ("script tag", "<script>…</script> — runs JS in HTML", "스크립트 태그"),
        ("statement", "one instruction that ends with a semicolon", "구문"),
    ],
    "week-02-variables-dom": [
        ("let / const", "declare a variable (const can't be reassigned)", "변수 선언"),
        ("DOM", "the tree of elements the browser builds from HTML", "문서 객체 모델"),
        ("querySelector", "find one element by CSS selector", "요소 찾기"),
        ("textContent", "the text inside an element", "텍스트 내용"),
    ],
    "week-03-events": [
        ("event", "something that happens (click, keypress)", "이벤트"),
        ("addEventListener", "run a function when an event fires", "이벤트 등록"),
        ("callback", "the function passed in to run later", "콜백 함수"),
    ],
    "week-04-user-input": [
        ("input element", "<input> tag the user types into", "입력 요소"),
        (".value", "the current text in an input field", "입력값"),
        ("submit", "the action of sending a form", "제출"),
    ],
    "week-05-conditionals": [
        ("if / else if / else", "three-way branch on a condition", "조건 분기"),
        ("=== / !==", "strict equal / strict not equal", "엄격 비교"),
        ("boolean", "value that is either true or false", "참/거짓 값"),
    ],
    "week-06-arrays-loops": [
        ("array", "an ordered list of values in [ ]", "배열"),
        ("for loop", "repeat code a fixed number of times", "반복문"),
        (".forEach", "run a function once per array item", "각각 실행"),
        ("index", "the number that locates an item in an array", "인덱스"),
    ],
    "week-07-functions": [
        ("function", "a reusable block of code", "함수"),
        ("parameter", "input the function expects", "매개변수"),
        ("return", "value the function gives back", "반환값"),
        ("arrow function", "short syntax: () => { … }", "화살표 함수"),
    ],
    "week-08-final-quiz": [
        ("state", "the data that describes what's currently on screen", "상태"),
        ("render", "update the DOM to match the state", "화면 갱신"),
        ("event-driven", "code that reacts to user actions", "이벤트 기반"),
    ],

    # web003-portfolio
    "week-01-planning": [
        ("information architecture", "how content is grouped and ordered", "정보 구조"),
        ("wireframe", "rough sketch of a page layout", "와이어프레임"),
        ("section", "a named block of related content", "섹션"),
    ],
    "week-02-html-structure": [
        ("semantic HTML", "tags that describe meaning (header, nav, main)", "의미있는 태그"),
        ("header / footer", "top and bottom landmarks of a page", "머리/꼬리 영역"),
        ("nav", "navigation links group", "내비게이션"),
    ],
    "week-03-design-system": [
        ("design tokens", "named colors, fonts, spacing in CSS variables", "디자인 토큰"),
        ("CSS variables", "--name: value reusable everywhere", "CSS 변수"),
        ("consistency", "the same look across every page", "일관성"),
    ],
    "week-04-hero-about": [
        ("hero section", "the big banner at the top of a page", "히어로 섹션"),
        ("CTA", "call-to-action — the main button you want clicked", "행동 유도 버튼"),
        ("about section", "short bio that introduces you", "소개 섹션"),
    ],
    "week-05-project-gallery": [
        ("grid", "rows-and-columns layout in CSS", "그리드"),
        ("card", "small box that previews one project", "카드"),
        ("thumbnail", "small preview image", "썸네일"),
    ],
    "week-06-dark-mode": [
        ("color scheme", "the set of colors used together", "색상 테마"),
        ("prefers-color-scheme", "browser hint for light/dark preference", "사용자 색상 선호도"),
        ("toggle", "a button that switches between two states", "토글 버튼"),
    ],
    "week-07-form-smooth-scroll": [
        ("form", "set of inputs for collecting user data", "양식"),
        ("smooth scroll", "animated scrolling between sections", "부드러운 스크롤"),
        ("anchor link", "link that jumps to an id on the same page", "앵커 링크"),
    ],
    "week-08-publish": [
        ("hosting", "the service that serves your site to visitors", "웹 호스팅"),
        ("deploy", "push your site live to the internet", "배포"),
        ("domain", "the address visitors type (e.g. mysite.com)", "도메인"),
    ],

    # ai001-replit-agent
    "week-01-first-prompt": [
        ("prompt", "the instruction you give the AI", "프롬프트"),
        ("specificity", "the more concrete, the better the answer", "구체성"),
        ("scope", "how much you ask for in one prompt", "범위"),
    ],
    "week-02-good-prompts": [
        ("context", "background info the AI needs to be useful", "맥락"),
        ("constraint", "a rule the AI must follow", "제약 조건"),
        ("expected output", "what you want back, described upfront", "원하는 결과"),
    ],
    "week-03-context-examples": [
        ("few-shot", "showing examples of what you want", "예시 제공"),
        ("anchor example", "one sample answer that sets the pattern", "기준 예시"),
        ("explicit", "say it plainly — don't expect the AI to guess", "명시적"),
    ],
    "week-04-step-by-step": [
        ("decomposition", "breaking one big problem into small steps", "분해"),
        ("milestone", "a checkpoint you can verify before moving on", "이정표"),
        ("scope creep", "asking the AI for too much in one prompt", "범위 확장"),
    ],
    "week-05-iteration": [
        ("iterate", "improve through repeated small changes", "반복 개선"),
        ("refine", "make a working answer better", "다듬기"),
        ("revert", "go back to a previous working version", "되돌리기"),
    ],
    "week-06-debugging": [
        ("expected vs actual", "what should happen vs what does", "기대 vs 실제"),
        ("trace", "the error path the program took", "오류 경로"),
        ("reproduce", "make the bug happen on demand", "재현"),
    ],
    "week-07-understand-code": [
        ("annotate", "add comments that explain what the code does", "주석 달기"),
        ("explain back", "describe code in your own words", "되설명하기"),
        ("ownership", "knowing your code well enough to change it", "코드 소유"),
    ],
    "week-08-final-project": [
        ("MVP", "minimum viable product — smallest useful version", "최소 기능 제품"),
        ("ship", "release something real to real users", "출시"),
        ("retrospective", "review what worked and what didn't", "회고"),
    ],
}


# ----------------------------------------------------------------------
# WEEK_RECAP — Slot 2 (Recap & Retrieve)
# ----------------------------------------------------------------------
# Each entry: (recall_question, answer). Question pulls the previous week's
# concept; the student answers BEFORE clicking the reveal (retrieval, not re-read).
# Week 1 entries are intentionally absent — first week has nothing to recall.

WEEK_RECAP = {
    # rs002-pokedex (W2+ recalls W1, etc.)
    "week-02-pokemon-lists": ("Last week: how do you store a player's name from input()?", "<code>name = input('Name? ')</code> — input() returns a string, assigned to a variable."),
    "week-03-cleaning-input": ("Last week: what's the index of the first item in a list?", "<code>0</code>. Lists are 0-indexed. <code>team[0]</code> is the first Pokémon."),
    "week-04-validation": ("Last week: how do you ignore the difference between 'YES' and 'yes'?", "Use <code>.lower()</code> before comparing. <code>answer.lower() == 'yes'</code>."),
    "week-05-dictionaries": ("Last week: what does <code>'fire' in types</code> return?", "<code>True</code> if 'fire' is in the list, <code>False</code> otherwise."),
    "week-06-functions": ("Last week: how do you look up the HP of a Pokémon stored in a dict?", "<code>p['hp']</code> — square brackets with the key in quotes."),
    "week-07-random-battle": ("Last week: what does a function need to send a value back?", "A <code>return</code> statement. Without it, the function returns <code>None</code>."),
    "week-08-final-showdown": ("Last week: how do you pick one Pokémon from a list at random?", "<code>random.choice(team)</code> — import random first."),

    # rs003-pygame-turret
    "week-02-turret-base": ("Last week: what does <code>pygame.init()</code> do?", "Starts up pygame's subsystems so you can use display, fonts, sound."),
    "week-03-functions-gun": ("Last week: how do you paste an image onto the screen?", "<code>screen.blit(surface, (x, y))</code> — blit = paste at position."),
    "week-04-keyboard-movement": ("Last week: what does a function 'return' to the caller?", "Whatever value follows the <code>return</code> keyword. Default is <code>None</code>."),
    "week-05-limit-range": ("Last week: how do you check if the left arrow is held down?", "<code>keys = pygame.key.get_pressed()</code> then <code>if keys[pygame.K_LEFT]:</code>."),
    "week-06-for-loops": ("Last week: how do you stop the player going past the screen edge?", "Clamp the x value: <code>x = max(0, min(x, SCREEN_WIDTH))</code>."),
    "week-07-multiple-functions": ("Last week: how many times does <code>for i in range(5)</code> loop?", "<code>5</code> times — i takes values 0, 1, 2, 3, 4."),
    "week-08-final-mini-game": ("Last week: why split your game into multiple functions?", "Each function does one thing → easier to read, change, and debug."),

    # rs004-platformer
    "week-02-player-keyboard": ("Last week: what limits the game to 60 frames per second?", "<code>clock.tick(60)</code> in the main loop."),
    "week-03-gravity-jump": ("Last week: how do you move the player to the right by 5 pixels?", "<code>player.x += 5</code> (or update a rect: <code>rect.x += 5</code>)."),
    "week-04-platforms-collision": ("Last week: how do you simulate gravity?", "Add a constant to velocity_y each frame, then move y by velocity_y."),
    "week-05-level-design": ("Last week: how do you detect two rects overlap in pygame?", "<code>rect1.colliderect(rect2)</code> — returns True if they overlap."),
    "week-06-coins-score": ("Last week: how do you store a level layout?", "As a list of tile rows — each row is a string or list of tile types."),
    "week-07-enemies-gameover": ("Last week: how do you remove a coin once it's collected?", "<code>coins.remove(coin)</code> after detecting collision with the player."),
    "week-08-multi-level-final": ("Last week: how do you check if the player has died?", "Compare player rect against each enemy rect; if any collide, set game state to 'dead'."),

    # web001-css
    "week-02-css-colors": ("Last week: what does the <code>&lt;p&gt;</code> tag mean?", "Paragraph — a block of body text. Pairs with <code>&lt;/p&gt;</code>."),
    "week-03-box-model": ("Last week: how do you turn the text red?", "<code>color: red;</code> (or a hex code like <code>#ff0000</code>)."),
    "week-04-flexbox": ("Last week: where does <code>padding</code> sit — inside or outside the border?", "<b>Inside</b> the border. Margin is outside."),
    "week-05-images-hero": ("Last week: how do you put three boxes in a row that share space evenly?", "<code>display: flex;</code> on the parent + <code>flex: 1;</code> on each child."),
    "week-06-responsive": ("Last week: how do you set a background image in CSS?", "<code>background-image: url('hero.jpg');</code> on the section."),
    "week-07-hover-animations": ("Last week: what does <code>@media (max-width: 600px)</code> mean?", "Apply these styles only when the screen is 600px wide or smaller."),
    "week-08-final-site": ("Last week: how do you make a button slowly change color when hovered?", "<code>transition: background 0.3s;</code> on the button + a <code>:hover</code> rule."),

    # web002-javascript
    "week-02-variables-dom": ("Last week: how do you print a message to the browser console?", "<code>console.log('hello')</code> — open DevTools (F12) to see it."),
    "week-03-events": ("Last week: how do you find the element with id 'title'?", "<code>document.querySelector('#title')</code> — returns one element."),
    "week-04-user-input": ("Last week: how do you run a function when a button is clicked?", "<code>btn.addEventListener('click', myFn)</code>."),
    "week-05-conditionals": ("Last week: how do you read what the user typed into an input?", "<code>document.querySelector('input').value</code>."),
    "week-06-arrays-loops": ("Last week: what's the difference between <code>==</code> and <code>===</code>?", "<code>===</code> compares without type coercion. Always prefer <code>===</code>."),
    "week-07-functions": ("Last week: how do you loop through every item in an array?", "<code>arr.forEach(item =&gt; { … })</code> or <code>for (let i = 0; i &lt; arr.length; i++)</code>."),
    "week-08-final-quiz": ("Last week: what does a function 'return' do?", "Sends a value back to whoever called the function."),

    # web003-portfolio
    "week-02-html-structure": ("Last week: why plan sections before writing code?", "Saves rework — structure first, styling second. Hard to fix layout retroactively."),
    "week-03-design-system": ("Last week: what's a semantic tag and why use one?", "Tags like <code>&lt;nav&gt;</code> and <code>&lt;main&gt;</code> describe meaning — better for SEO and screen readers than generic <code>&lt;div&gt;</code>."),
    "week-04-hero-about": ("Last week: how do you define a reusable color in CSS?", "<code>:root { --accent: #ff7849; }</code> then use <code>var(--accent)</code> anywhere."),
    "week-05-project-gallery": ("Last week: what's the one thing the hero CTA should do?", "Lead the visitor to the single most important action — usually 'see my work'."),
    "week-06-dark-mode": ("Last week: how do you put project cards in a 3-column grid?", "<code>display: grid; grid-template-columns: repeat(3, 1fr);</code>."),
    "week-07-form-smooth-scroll": ("Last week: how do you let the browser pick light or dark based on user setting?", "Listen to <code>prefers-color-scheme</code> with a media query, or toggle a class."),
    "week-08-publish": ("Last week: how do you make clicking a nav link scroll smoothly to a section?", "<code>scroll-behavior: smooth;</code> on <code>html</code> + anchor links to ids."),

    # ai001-replit-agent
    "week-02-good-prompts": ("Last week: why is 'build me a game' a bad first prompt?", "Too vague. The AI guesses at scope, language, features. You get random output that won't match what you want."),
    "week-03-context-examples": ("Last week: what does specificity in a prompt look like?", "Naming the file, function, inputs, expected output — not just the goal."),
    "week-04-step-by-step": ("Last week: what's a 'few-shot' prompt?", "A prompt that includes 1-3 example answers so the AI matches your pattern."),
    "week-05-iteration": ("Last week: what's wrong with 'build the whole thing' as one prompt?", "Too big — the AI hallucinates structure and you can't tell where it went wrong."),
    "week-06-debugging": ("Last week: when do you revert instead of refining?", "When the AI's latest change broke something that was working. Revert, then make a smaller change."),
    "week-07-understand-code": ("Last week: what 4 parts make a good debug prompt?", "Code + expected behaviour + actual behaviour + what you've already tried."),
    "week-08-final-project": ("Last week: why annotate AI-generated code?", "Forces you to understand it. If you can't explain a line, you don't own the code."),
}


# ----------------------------------------------------------------------
# WEEK_MODIFY — Slot 9 (Modify / Faded)
# ----------------------------------------------------------------------
# Each entry: (code_with_blanks, hint).
# Code is the week's worked example with 1-2 key tokens replaced by ___.
# Faded scaffolding (Renkl): removing one step at a time is faster than
# asking for a full solution. Blanks guide toward the concept being practiced.

WEEK_MODIFY = {
    # rs002-pokedex
    "week-01-input-variables": ("name = ___('What is your name? ')\nprint(f'Hello, {___}!')", "Use the function that reads keyboard input. Then put the variable inside the f-string."),
    "week-02-pokemon-lists": ("team = ['Pikachu', 'Charmander', 'Bulbasaur']\nprint(team[___])   # show the first one\nteam.___('Squirtle')   # add to the end\nprint(team)", "First index is 0. Method that adds to the end of a list."),
    "week-03-cleaning-input": ("answer = input('yes or no? ')\nclean = answer.___().___()    # remove spaces, lowercase\nif clean == 'yes':\n    print('great!')", "Two string methods chained — order matters: strip then lower."),
    "week-04-validation": ("types = ['fire', 'water', 'grass']\nguess = input('Type? ')\n___ guess.lower() ___ types:\n    print('valid')\n___:\n    print('try again')", "Two-way branch — and the keyword that tests list membership."),
    "week-05-dictionaries": ("p = {'name': 'Pikachu', 'hp': 35, 'type': 'electric'}\nprint(p[___])      # show the HP\np[___] = 100       # set HP to 100\nprint(p)", "Square brackets with the key in quotes."),
    "week-06-functions": ("def battle(attacker, defender):\n    damage = attacker['attack'] - defender['defense']\n    ___ max(damage, 0)\n\nresult = ___('Pikachu', 'Squirtle')   # call site\nprint(result)", "Keyword that sends a value back. And pass the function the two dicts as arguments."),
    "week-07-random-battle": ("import ___\nteam = ['Pikachu', 'Charmander', 'Bulbasaur']\nfighter = random.___(team)\nprint(f'{fighter} steps up!')", "Module name. Method that picks one item from a list."),
    "week-08-final-showdown": ("hp = 30\n___ hp > 0:\n    damage = random.randint(5, 15)\n    hp ___ damage\n    print(f'HP: {hp}')\nprint('Knocked out!')", "Loop keyword that repeats while a condition is true. Compound-assign operator that subtracts in place."),

    # rs003-pygame-turret
    "week-01-pygame-window": ("import pygame\npygame.___()\nscreen = pygame.display.set_mode((___, ___))\npygame.display.set_caption('Turret')\nrunning = True\nwhile running:\n    for event in pygame.event.get():\n        if event.type == pygame.___:\n            running = False", "Function that starts pygame. Window width and height. Event type for the close button."),
    "week-02-turret-base": ("turret = pygame.image.load('turret.png')\nturret_rect = turret.get_rect()\nturret_rect.center = (___, ___)   # center bottom of screen\nscreen.fill((0, 0, 0))\nscreen.___(turret, turret_rect)", "Half the screen width, near the bottom. Method that pastes one surface onto another."),
    "week-03-functions-gun": ("def draw_gun(screen, x, y):\n    pygame.draw.rect(screen, (200, 200, 200), (x, y, 10, 40))\n\n# call site\n___(screen, 400, 300)", "Call the function with the surface and two coordinates."),
    "week-04-keyboard-movement": ("keys = pygame.key.___()\nif keys[pygame.K_LEFT]:\n    turret_x ___ 5\nif keys[pygame.K_RIGHT]:\n    turret_x ___ 5", "Method that returns the current pressed-key state. Left arrow subtracts; right arrow adds."),
    "week-05-limit-range": ("turret_x = ___(0, min(turret_x, SCREEN_WIDTH - turret_width))", "Clamp pattern — outer function picks the larger of two values."),
    "week-06-for-loops": ("# fire 5 bullets in a fan\n___ angle in range(-30, 31, 15):\n    bullet = make_bullet(angle)\n    bullets.append(bullet)", "Loop keyword for iterating a sequence."),
    "week-07-multiple-functions": ("def update_bullets():\n    ___\n\ndef draw_everything():\n    ___\n\nwhile running:\n    update_bullets()\n    draw_everything()", "Single-keyword placeholder used when a function has no body yet."),
    "week-08-final-mini-game": ("score = 0\nlives = 3\nwhile lives > 0:\n    if bullet_hit_enemy():\n        score ___ 10\n    if enemy_hit_player():\n        lives ___ 1\nprint(f'Final score: {score}')", "Compound-assignment operators — gain points, lose lives."),

    # rs004-platformer
    "week-01-game-window": ("import pygame\npygame.init()\nWIDTH, HEIGHT = ___, ___\nscreen = pygame.display.set_mode((WIDTH, HEIGHT))\nclock = pygame.time.Clock()\nrunning = True\nwhile running:\n    clock.tick(___)", "Pick a window size (e.g. 800, 600). Frame rate cap — typically 60."),
    "week-02-player-keyboard": ("keys = pygame.key.get_pressed()\nif keys[pygame.K_LEFT]:\n    player.x ___ SPEED\nif keys[pygame.K_RIGHT]:\n    player.x ___ SPEED", "Left subtracts; right adds."),
    "week-03-gravity-jump": ("GRAVITY = 0.7\nvelocity_y = 0\nwhile running:\n    velocity_y ___ GRAVITY   # add a little speed downward each frame\n    player.y ___ velocity_y  # move y by current vertical speed\n    if jump_pressed and on_ground:\n        velocity_y = ___       # sudden negative = jump up", "Compound-add for both lines. Jump impulse is a large negative number, e.g. -14."),
    "week-04-platforms-collision": ("for plat in platforms:\n    if player.___(plat):\n        # land on top of the platform\n        player.bottom = plat.___\n        velocity_y = 0\n        on_ground = True", "Method that detects two rects overlap. Edge of the platform's top side."),
    "week-05-level-design": ("level = [\n    '#########',\n    '#.......#',\n    '#..@....#',     # @ = player start\n    '#########',\n]\nfor row_idx, row in enumerate(level):\n    for col_idx, cell in enumerate(row):\n        if cell == '___':\n            make_wall(col_idx, row_idx)", "Wall character — see the legend at the top of the level."),
    "week-06-coins-score": ("score = 0\nfor coin in coins[:]:        # copy so we can remove safely\n    if player.colliderect(coin):\n        coins.___(coin)        # remove this coin\n        score ___ 10            # +10 per coin", "List method that removes an item. Compound-add."),
    "week-07-enemies-gameover": ("state = 'playing'\nfor enemy in enemies:\n    if player.colliderect(enemy):\n        state = '___'           # mark the game as lost\n        break\nif state == 'dead':\n    draw_game_over_screen()", "What the game state becomes when an enemy hits the player."),
    "week-08-multi-level-final": ("levels = [LEVEL_1, LEVEL_2, LEVEL_3]\ncurrent = 0\nif player_reached_goal():\n    current ___ 1                 # advance to next level\n    if current ___ len(levels):    # past the last level?\n        show_credits()", "Add one. Then check if it's reached the length."),

    # web001-css
    "week-01-html-basics": ("<!DOCTYPE html>\n<html>\n<head><title>My Page</title></head>\n<___>\n  <h1>Welcome</h1>\n  <___>This is my first page.</___>\n</___>\n</html>", "Two tags: body (wraps the visible content) and p (paragraph)."),
    "week-02-css-colors": ("h1 {\n  color: ___;          /* main heading color */\n  background: ___;     /* background behind the heading */\n}", "Hex codes (#rrggbb) or named colors like blue / #faf6f0."),
    "week-03-box-model": (".card {\n  ___-sizing: border-box;     /* width includes padding */\n  width: 300px;\n  padding: ___;                 /* space inside */\n  margin: ___;                  /* space outside */\n}", "box-sizing property. Pick px values like 1em or 20px for padding/margin."),
    "week-04-flexbox": (".row {\n  display: ___;\n  justify-content: ___;       /* spread items along the main axis */\n  gap: 1em;\n}", "The layout mode + a value like space-between or center."),
    "week-05-images-hero": (".hero {\n  background-image: ___('hero.jpg');\n  background-size: ___;       /* fill the section without distortion */\n  height: 60vh;\n}", "The url() function. Value: cover (or contain)."),
    "week-06-responsive": ("@___ (max-width: 600px) {\n  body {\n    font-size: 14px;\n  }\n}", "Keyword that starts a responsive rule — applies styles only at certain screen sizes."),
    "week-07-hover-animations": (".btn {\n  background: blue;\n  ___: background 0.3s;       /* smooth change */\n}\n.btn:___ {\n  background: red;\n}", "Property that animates between states. Pseudo-class that applies on mouse over."),
    "week-08-final-site": ("body {\n  max-width: ___;\n  margin: 0 ___;              /* center horizontally */\n  font-family: system-ui, sans-serif;\n}", "Reasonable cap like 800px or 1100px. Then auto on the side margins."),

    # web002-javascript
    "week-01-hello-js": ("// Print 1 + 2 + 3 to the console\nconsole.___(1 + 2 + 3);\n\n// Print your name in a friendly message\nconst name = '___';\nconsole.log('Hi, ' + name + '!');", "The log method. Pick any name string."),
    "week-02-variables-dom": ("const heading = document.___('#title');\nheading.___ = 'Hello world';", "Selector-by-CSS method. The property that changes the visible text."),
    "week-03-events": ("const btn = document.querySelector('#go');\nbtn.___('click', () => {\n  console.log('clicked');\n});", "The method that registers an event handler."),
    "week-04-user-input": ("const input = document.querySelector('#name');\nconst btn = document.querySelector('#submit');\nbtn.addEventListener('click', () => {\n  console.log('Hi, ' + input.___);\n});", "The property that holds the current text typed into an input."),
    "week-05-conditionals": ("const score = 75;\nif (score ___ 90) {\n  console.log('A');\n} else ___ (score >= 60) {\n  console.log('B or C');\n} else {\n  console.log('F');\n}", "Comparison operator (>=). And the keyword that joins to make a three-way branch."),
    "week-06-arrays-loops": ("const nums = [10, 20, 30, 40];\nlet total = 0;\nnums.___((n) => {\n  total ___ n;\n});\nconsole.log(total);", "Array method that runs a callback per item. Compound-add operator."),
    "week-07-functions": ("const square = (n) => n ___ n;\nconst double = (n) => n ___ 2;\n\nconsole.log(square(double(3)));   // expect 36", "Multiplication operator both times."),
    "week-08-final-quiz": ("let score = 0;\nconst answers = ['B', 'A', 'C'];\nconst correct = ['B', 'B', 'C'];\nanswers.forEach((a, i) => {\n  if (a ___ correct[i]) {\n    score ___ 1;\n  }\n});\nconsole.log(score);", "Strict-equal operator. Compound-add."),

    # web003-portfolio
    "week-01-planning": ("Sections (in order):\n1. ___       (big intro, name + tagline + CTA)\n2. ___       (short bio)\n3. Projects   (3-6 cards)\n4. ___       (contact / email)", "Pick standard names: Hero / About / Contact."),
    "week-02-html-structure": ("<___>\n  <nav>...</nav>\n</___>\n<___>\n  <section id='hero'>...</section>\n  <section id='about'>...</section>\n</___>\n<footer>...</footer>", "Semantic tags: header wraps nav at the top; main wraps the page body."),
    "week-03-design-system": (":root {\n  --accent: #ff7849;\n  --bg: ___;\n  --ink: ___;\n}\n.btn { background: ___(--accent); }", "Pick hex codes for background + text. Function name that reads a CSS variable."),
    "week-04-hero-about": ("<section class='hero'>\n  <h1>___</h1>                       <!-- your name -->\n  <p>___</p>                          <!-- one-line tagline -->\n  <a class='cta' href='___'>See work</a>\n</section>", "Hero needs: your name, your one-line value prop, and a hash link to the projects section."),
    "week-05-project-gallery": (".grid {\n  display: ___;\n  grid-template-columns: repeat(___, 1fr);   /* 3 columns */\n  gap: 1em;\n}", "Layout mode. Number of columns."),
    "week-06-dark-mode": ("@media (prefers-color-scheme: ___) {\n  body {\n    background: #1a1a2e;\n    color: white;\n  }\n}", "The keyword that names the dark color scheme."),
    "week-07-form-smooth-scroll": ("html {\n  scroll-behavior: ___;\n}\n<a href='___contact'>Contact</a>     <!-- jumps smoothly to #contact -->", "Value that turns on smooth scrolling. Symbol that links to an element by id."),
    "week-08-publish": ("# Steps to ship\n1. git add .\n2. git commit -m '___'\n3. git push\n4. Open vercel.com → import GitHub repo → Deploy\n5. Visit https://___.vercel.app", "Short message describing what changed. Pick a project name for the URL slug."),

    # ai001-replit-agent — modify the PROMPT, not code
    "week-01-first-prompt": ('Vague:  "Make a website."\n\nSpecific:  "Make a one-page website with a ___ section, a ___ section, and a ___ button at the top."', "Pick three concrete section names — hero, about, contact — so the AI knows what to build."),
    "week-02-good-prompts": ('Prompt skeleton:\n  File: ___\n  Function: ___\n  Current behaviour: ___\n  Expected behaviour: ___\n  Constraint: don\'t change ___', "Fill in the file name, the function name, what's broken, what it should do, and what to leave alone."),
    "week-03-context-examples": ('Add a sub() function. Match this pattern:\n  add(2, 3) → 5\n  mul(2, 3) → 6\n  sub(___, ___) → ___', "Pick two numbers and the expected result (e.g. 5, 2, 3)."),
    "week-04-step-by-step": ('Break this into steps:\n  Goal: build a quiz app.\n  Step 1: ___\n  Step 2: ___\n  Step 3: ___\n  Step 4: ___', "Decompose into 4 verifiable mini-prompts (skeleton → questions → scoring → deploy)."),
    "week-05-iteration": ('Refine, don\'t restart:\n  "The layout is good but the spacing is too tight. ___ the gap between cards from 8px to ___."', "Verb that means 'change one thing'. Pick a wider gap like 16px or 24px."),
    "week-06-debugging": ('Good debug prompt has 4 parts:\n  1. Code: ___\n  2. Expected: ___\n  3. Actual: ___\n  4. Already tried: ___', "Paste the failing function. State what it should output. State what it outputs now. Note any fixes you've attempted."),
    "week-07-understand-code": ('Annotate this AI output:\n  "Explain each line of ___() and rewrite it using a ___ instead of a recursive call."', "The function name AI generated. The non-recursive structure (e.g. a for loop)."),
    "week-08-final-project": ('5-prompt build plan:\n  Prompt 1: skeleton — ___\n  Prompt 2: core feature — ___\n  Prompt 3: polish — ___\n  Prompt 4: edge cases — ___\n  Prompt 5: deploy — ___', "Fill each step with one verifiable outcome (e.g. 'shows a working hero section')."),
}


# ----------------------------------------------------------------------
# WEEK_PREDICT — Slot 3 (Predict / Hook)
# ----------------------------------------------------------------------
# Each entry: (code_snippet, expected_output, lang_hint).
# Snippet is short (3-6 lines). Output is hidden behind <details>.
# Forces the student to predict before running.

WEEK_PREDICT = {
    # rs002-pokedex
    "week-01-input-variables": ("name = 'Ash'\nprint(f'Hello, {name}!')", "Hello, Ash!", "python"),
    "week-02-pokemon-lists": ("team = ['Pikachu', 'Charmander', 'Bulbasaur']\nprint(team[1])", "Charmander", "python"),
    "week-03-cleaning-input": ("answer = '  YES  '\nprint(answer.strip().lower())", "yes", "python"),
    "week-04-validation": ("types = ['fire', 'water', 'grass']\nguess = 'Fire'\nprint(guess.lower() in types)", "True", "python"),
    "week-05-dictionaries": ("p = {'name': 'Pikachu', 'hp': 35}\nprint(p['hp'])", "35", "python"),
    "week-06-functions": ("def double(n):\n    return n * 2\nprint(double(7))", "14", "python"),
    "week-07-random-battle": ("import random\nrandom.seed(1)\nprint(random.choice(['A', 'B', 'C']))", "B", "python"),
    "week-08-final-showdown": ("hp = 30\nwhile hp > 0:\n    hp -= 10\nprint(hp)", "0", "python"),

    # rs003-pygame-turret
    "week-01-pygame-window": ("import pygame\npygame.init()\nscreen = pygame.display.set_mode((400, 300))\nprint(screen.get_size())", "(400, 300)", "python"),
    "week-02-turret-base": ("rect = pygame.Rect(10, 20, 50, 50)\nprint(rect.right)", "60", "python"),
    "week-03-functions-gun": ("def fire(power):\n    return power * 2\nprint(fire(5))", "10", "python"),
    "week-04-keyboard-movement": ("x = 100\nx -= 5  # left arrow\nprint(x)", "95", "python"),
    "week-05-limit-range": ("x = -10\nx = max(0, min(x, 400))\nprint(x)", "0", "python"),
    "week-06-for-loops": ("for i in range(3):\n    print('shot', i)", "shot 0\nshot 1\nshot 2", "python"),
    "week-07-multiple-functions": ("def add(a, b): return a + b\ndef double(n): return n * 2\nprint(double(add(2, 3)))", "10", "python"),
    "week-08-final-mini-game": ("score = 0\nfor hit in [True, False, True, True]:\n    if hit: score += 1\nprint(score)", "3", "python"),

    # rs004-platformer
    "week-01-game-window": ("WIDTH, HEIGHT = 800, 600\nprint(WIDTH * HEIGHT)", "480000", "python"),
    "week-02-player-keyboard": ("x = 100\nfor _ in range(3):\n    x += 5\nprint(x)", "115", "python"),
    "week-03-gravity-jump": ("vy = 0\nGRAVITY = 1\nfor _ in range(5):\n    vy += GRAVITY\nprint(vy)", "5", "python"),
    "week-04-platforms-collision": ("a = pygame.Rect(0, 0, 50, 50)\nb = pygame.Rect(40, 40, 50, 50)\nprint(a.colliderect(b))", "True", "python"),
    "week-05-level-design": ("level = ['###', '#.#', '###']\nprint(len(level), len(level[0]))", "3 3", "python"),
    "week-06-coins-score": ("coins = ['A', 'B', 'C']\ncoins.remove('B')\nprint(coins)", "['A', 'C']", "python"),
    "week-07-enemies-gameover": ("state = 'playing'\nif True:  # hit by enemy\n    state = 'dead'\nprint(state)", "dead", "python"),
    "week-08-multi-level-final": ("levels = ['L1', 'L2', 'L3']\ncurrent = 0\ncurrent += 1\nprint(levels[current])", "L2", "python"),

    # web001-css
    "week-01-html-basics": ("<p>Hello <b>world</b>!</p>", "Hello world!  (the word 'world' is bold)", "html"),
    "week-02-css-colors": ("/* h1 { color: red; } */\n<h1>Welcome</h1>", "The text 'Welcome' appears in red.", "html"),
    "week-03-box-model": (".box { width: 100px; padding: 20px; border: 5px solid; }\n/* default box-sizing */", "Rendered width = 100 + 20 + 20 + 5 + 5 = 150px.", "css"),
    "week-04-flexbox": (".row { display: flex; gap: 10px; }\n<div class='row'><div>A</div><div>B</div><div>C</div></div>", "A, B, C sit in a row with 10px gaps between them.", "html"),
    "week-05-images-hero": (".hero { background-image: url('cat.jpg'); background-size: cover; height: 300px; }", "A 300px-tall section showing the cat image filling the width.", "css"),
    "week-06-responsive": ("@media (max-width: 600px) {\n  body { background: yellow; }\n}", "Yellow background ONLY on screens 600px wide or less.", "css"),
    "week-07-hover-animations": (".btn { background: blue; transition: background 0.3s; }\n.btn:hover { background: red; }", "Button starts blue; on hover, fades to red over 0.3s.", "css"),
    "week-08-final-site": ("body { font-family: system-ui; max-width: 800px; margin: 0 auto; }", "Body text uses the OS UI font, capped at 800px wide, centered horizontally.", "css"),

    # web002-javascript
    "week-01-hello-js": ("console.log(2 + 3 * 4);", "14", "js"),
    "week-02-variables-dom": ("const el = document.querySelector('#title');\nel.textContent = 'Hi!';", "The element with id 'title' now shows the text 'Hi!'.", "js"),
    "week-03-events": ("btn.addEventListener('click', () => {\n  console.log('clicked');\n});", "Each click logs 'clicked' to the console.", "js"),
    "week-04-user-input": ("const v = document.querySelector('input').value;\nconsole.log(v.length);", "Prints the number of characters the user typed.", "js"),
    "week-05-conditionals": ("const n = 7;\nif (n > 10) console.log('big');\nelse if (n > 5) console.log('mid');\nelse console.log('small');", "mid", "js"),
    "week-06-arrays-loops": ("const xs = [1, 2, 3];\nlet sum = 0;\nxs.forEach(x => sum += x);\nconsole.log(sum);", "6", "js"),
    "week-07-functions": ("const square = n => n * n;\nconsole.log(square(5));", "25", "js"),
    "week-08-final-quiz": ("let score = 0;\nconst correct = [true, false, true];\ncorrect.forEach(c => { if (c) score++; });\nconsole.log(score);", "2", "js"),

    # web003-portfolio — mostly conceptual; use HTML/CSS snippets
    "week-01-planning": ("Sections planned:\n1. Hero\n2. About\n3. Projects\n4. Contact", "The page has 4 sections in this order.", "html"),
    "week-02-html-structure": ("<header><nav>...</nav></header>\n<main>...</main>\n<footer>...</footer>", "Page has a top header (with nav), a main content area, and a footer at the bottom.", "html"),
    "week-03-design-system": (":root { --accent: #ff7849; }\n.btn { background: var(--accent); }", "The button is colored with the orange defined once at :root.", "css"),
    "week-04-hero-about": ("<section class='hero'>\n  <h1>Kasim</h1>\n  <p>I build things.</p>\n  <a class='cta' href='#projects'>See work</a>\n</section>", "Hero section: big name, short tagline, one CTA button linking to #projects.", "html"),
    "week-05-project-gallery": (".grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1em; }", "Project cards arranged in 3 equal columns with 1em gaps.", "css"),
    "week-06-dark-mode": ("@media (prefers-color-scheme: dark) {\n  body { background: #1a1a2e; color: white; }\n}", "Page automatically switches to dark theme when the user's OS is set to dark mode.", "css"),
    "week-07-form-smooth-scroll": ("html { scroll-behavior: smooth; }\n<a href='#contact'>Contact</a>", "Clicking the Contact link smoothly scrolls down to the contact section instead of jumping.", "css"),
    "week-08-publish": ("Push to GitHub → Vercel/Netlify auto-deploys → live URL.", "Within ~30 seconds of pushing, the new version is live at your domain.", "html"),

    # ai001-replit-agent — predict the OUTCOME of a prompt, not code output
    "week-01-first-prompt": ('Prompt: "Make a game"', 'AI returns a vague snake game or asks 5 clarifying questions. Output won\'t match what you actually wanted.', "prompt"),
    "week-02-good-prompts": ('Prompt: "In game.py, make the player jump when SPACE is pressed. Use pygame.K_SPACE. Don\'t change collision."', "AI edits only the keyboard-handling section and adds a jump impulse — leaving collision alone, as requested.", "prompt"),
    "week-03-context-examples": ('Prompt: "Like this: add(2,3)→5, sub(4,1)→3. Now add a mul function."', 'AI infers the pattern from your two examples and produces mul(a,b)→a*b matching the style.', "prompt"),
    "week-04-step-by-step": ('Prompts in order:\n1. Make a window\n2. Add a player rect\n3. Make it move with arrows', "Each step ships a working app. Easy to verify after each. No mystery failures.", "prompt"),
    "week-05-iteration": ('First prompt: "Make a calculator"\nFollow-up: "Keep the layout, but make the buttons rounder."', 'AI preserves the calculator structure and only modifies button styling.', "prompt"),
    "week-06-debugging": ('Prompt: "Expected: print 5 when user types 5. Actual: prints \'5\' with quotes. Code: <paste>. What\'s the fix?"', 'AI explains input() returns a string, suggests int() conversion, shows the diff.', "prompt"),
    "week-07-understand-code": ('Prompt: "Explain this function line by line. Then suggest a simpler version."', 'AI gives an annotated breakdown + a refactored simpler version. You can now change it without breaking it.', "prompt"),
    "week-08-final-project": ('Build plan: 5 prompts, each producing a working app:\n1. Skeleton\n2. Core feature\n3. Polish\n4. Edge cases\n5. Deploy', "Final working app, fully understood by you, deployed to the internet.", "prompt"),
}


# ----------------------------------------------------------------------
# Generic content (used when no override exists)
# ----------------------------------------------------------------------

GENERIC_EDGES_BY_KEYWORD = [
    # if topic contains any of these substrings, prefer these edges
    (["variable", "input"], [
        ("input() returns str", "Even if user types '7', it's the string '7'. Cast with int(input(...)) to do math."),
        ("Name = case sensitive", "<code>hp</code> and <code>Hp</code> are different variables. Pick a style and stick to it."),
        ("Snake_case in Python", "PEP 8: <code>player_name</code>, not <code>playerName</code> or <code>PlayerName</code>."),
        ("Re-assign freely", "x = 5 then x = 'hello' is legal. Python infers the type from the value."),
    ]),
    (["list"], [
        ("Lists are 0-indexed", "First item is <code>items[0]</code>, not <code>items[1]</code>."),
        ("IndexError out of range", "<code>items[99]</code> on a 3-item list raises IndexError. Use <code>len(items)</code> to check first."),
        ("Mutating during a for", "Don't <code>append</code> to a list while looping over it — behavior gets weird."),
        ("== vs is for lists", "<code>[1,2] == [1,2]</code> is True. <code>[1,2] is [1,2]</code> is False (different objects)."),
    ]),
    (["dict"], [
        ("KeyError on missing key", "<code>d['x']</code> raises KeyError if 'x' missing. Use <code>d.get('x', default)</code> for safety."),
        ("Keys must hash", "Strings, ints, tuples ok. Lists and dicts can't be keys."),
        ("Insertion order kept", "Since Python 3.7, dicts remember the order you added items in."),
        ("Looping iterates keys", "Default <code>for k in d</code> = keys only. Use <code>.items()</code> for pairs."),
    ]),
    (["function", "def"], [
        ("Mutable default trap", "Never use <code>def f(x=[])</code>. Use <code>x=None</code> + check inside."),
        ("Forgot return?", "No return statement = returns None. Easy to miss when tired."),
        ("self first", "Inside a class method, first param is always <code>self</code> — Python passes it automatically."),
        ("Don't shadow builtins", "Avoid <code>list = [1,2,3]</code> — you just broke <code>list()</code> for the rest of the file."),
    ]),
    (["loop", "for", "while"], [
        ("Off-by-one is everywhere", "<code>range(10)</code> gives 0–9, not 1–10."),
        ("Infinite loop", "Forgot to update the condition in a <code>while</code>? Ctrl-C to exit."),
        ("Don't mutate during for", "Modifying the list you're looping over is a common source of bugs."),
        ("break vs continue", "<code>break</code> exits the loop. <code>continue</code> skips this iteration only."),
    ]),
    (["validate", "validation", "clean"], [
        ("Trust no input", "Users type weird stuff. Always validate before using."),
        ("Catch the right error", "Don't <code>except:</code> blindly — name the exception type."),
        ("Loop until valid", "A while loop with break is the classic pattern for retrying input."),
        ("Strip before compare", "<code>'yes ' == 'yes'</code> is False. Use <code>.strip()</code> first."),
    ]),
    (["random"], [
        ("Pseudo-random", "Same seed = same sequence. Useful for tests, bad for secrets."),
        ("randint includes both ends", "<code>random.randint(1, 6)</code> can return 1 or 6, unlike <code>range</code>."),
        ("Use secrets for security", "For passwords/tokens, use <code>secrets</code>, not <code>random</code>."),
        ("choice() needs non-empty", "<code>random.choice([])</code> raises IndexError."),
    ]),
    (["pygame", "game", "turret", "platform"], [
        ("Frame rate matters", "Without a clock, the game runs as fast as the CPU allows — chaos."),
        ("Coordinates start top-left", "y increases as you go DOWN, not up."),
        ("Always handle QUIT", "Forget pygame.event.QUIT and your window won't close."),
        ("Convert images", "<code>img.convert()</code> or <code>.convert_alpha()</code> — way faster than not."),
    ]),
    (["html", "css"], [
        ("Self-closing void tags", "<code>&lt;img&gt;</code> and <code>&lt;br&gt;</code> have no closing tag in HTML5."),
        ("Specificity wars", "Inline > #id > .class > tag. Stop adding !important."),
        ("Box-sizing default", "Set <code>box-sizing: border-box</code> on everything or padding will lie."),
        ("Flex container ≠ items", "Properties on the container vs the items — easy to mix up."),
    ]),
    (["javascript", "js"], [
        ("== vs ===", "Always use <code>===</code> (strict equality). <code>==</code> does weird type coercion."),
        ("var vs let vs const", "Use <code>const</code> by default, <code>let</code> if you'll reassign. Never <code>var</code>."),
        ("this is weird", "<code>this</code> changes meaning by call site. Arrow functions inherit <code>this</code>."),
        ("Async ≠ parallel", "<code>async/await</code> is concurrent, not multi-core."),
    ]),
    (["prompt", "agent", "ai"], [
        ("Be specific", "Vague prompts get vague code. Name the file, function, inputs, expected output."),
        ("Read the diff", "The AI rewrote your file? Always read what changed before accepting."),
        ("Small steps win", "One feature per prompt > one giant 'build my app' prompt."),
        ("Test what it wrote", "AI-written code looks right and breaks. Always run it."),
    ]),
]

DEFAULT_EDGES = [
    ("Test small", "Run with a tiny input first. If that breaks, big input won't help."),
    ("Read the error", "Python tells you the line and the type. Copy the exact text."),
    ("One change at a time", "If you change three things and it breaks, you don't know which broke it."),
    ("Save often", "Ctrl-S after every change. Or use a real editor that autosaves."),
]


def pick_edges(topic_lc):
    for keywords, edges in GENERIC_EDGES_BY_KEYWORD:
        for kw in keywords:
            if kw in topic_lc:
                return edges
    return DEFAULT_EDGES


GENERIC_DEBUG_BY_KEYWORD = [
    (["dict"], (
        "p = {'name': 'pika', 'hp': 35}\nprint(p['type'])",
        "<b>Bug:</b> The key 'type' was never added to the dict. <code>p['type']</code> raises <code>KeyError</code>. Use <code>p.get('type', 'unknown')</code> for a safe default.",
        "p = {'name': 'pika', 'hp': 35, 'type': 'electric'}\nprint(p.get('type', 'unknown'))",
    )),
    (["list"], (
        "items = ['a', 'b', 'c']\nprint(items[3])",
        "<b>Bug:</b> A 3-item list has indices 0, 1, 2 — there's no index 3. Python raises <code>IndexError: list index out of range</code>.",
        "items = ['a', 'b', 'c']\nprint(items[2])  # last item\n# or: items[-1]",
    )),
    (["loop", "for", "while"], (
        "for i in range(1, 10):\n    if i = 5:\n        print('found')",
        "<b>Bug:</b> <code>=</code> is assignment, <code>==</code> is comparison. Inside an <code>if</code>, you need <code>==</code> or Python raises <code>SyntaxError</code>.",
        "for i in range(1, 10):\n    if i == 5:\n        print('found')",
    )),
    (["function", "def"], (
        "def greet(name):\nprint(f'Hi, {name}')\n\ngreet('Kasim')",
        "<b>Bug:</b> The <code>print</code> line is not indented inside the function. Python raises <code>IndentationError</code>. Function bodies must be indented 4 spaces.",
        "def greet(name):\n    print(f'Hi, {name}')\n\ngreet('Kasim')",
    )),
    (["input", "validate"], (
        "age = input('Age? ')\nif age > 18:\n    print('adult')",
        "<b>Bug:</b> <code>input()</code> always returns a string. Comparing a string to a number with <code>></code> raises <code>TypeError</code>. Cast with <code>int(input(...))</code>.",
        "age = int(input('Age? '))\nif age > 18:\n    print('adult')",
    )),
    (["random"], (
        "import random\nresult = random.choice([])",
        "<b>Bug:</b> <code>random.choice</code> on an empty sequence raises <code>IndexError</code>. Always check the list isn't empty first.",
        "import random\nchoices = ['rock', 'paper', 'scissors']\nresult = random.choice(choices)",
    )),
    (["html"], (
        "<h1>Welcome\n<p>This is my site.</p>",
        "<b>Bug:</b> The <code>&lt;h1&gt;</code> tag is never closed. Browsers will try to recover but the layout will be off.",
        "<h1>Welcome</h1>\n<p>This is my site.</p>",
    )),
    (["css"], (
        ".box {\n  width: 100px;\n  padding: 20px;\n}\n/* expected total width: 100px, actual: 140px */",
        "<b>Bug:</b> By default, <code>padding</code> is added on top of <code>width</code>. Set <code>box-sizing: border-box</code> so width includes padding.",
        ".box {\n  box-sizing: border-box;\n  width: 100px;\n  padding: 20px;\n}",
    )),
    (["javascript", "js"], (
        "const items = ['a', 'b', 'c'];\nfor (var i = 0; i < items.length; i++) {\n  setTimeout(() => console.log(items[i]), 100);\n}",
        "<b>Bug:</b> <code>var</code> isn't block-scoped, so <code>i</code> is shared across timeouts — they all log <code>undefined</code>. Use <code>let</code> instead.",
        "const items = ['a', 'b', 'c'];\nfor (let i = 0; i < items.length; i++) {\n  setTimeout(() => console.log(items[i]), 100);\n}",
    )),
    (["prompt", "agent", "ai"], (
        "Prompt: \"make my game better\"",
        "<b>Bug:</b> Too vague. The AI doesn't know what 'better' means. Be specific: name the file, the function, the problem, and the kind of change you want.",
        "Prompt: \"In game.py, the player can walk off the screen. Add a check in update() so player.x stays between 0 and SCREEN_WIDTH.\"",
    )),
]

# Language-conditional defaults — picked when no specific topic keyword matched.
# Previously a single Python `pirnt` default was injected into every deck,
# producing nonsensical CSS/HTML/JS lessons with Python typos. Audit flagged 30+.
DEFAULT_DEBUG_BY_LANG = {
    "python": (
        "pirnt('Hello, world!')",
        "<b>Bug:</b> <code>pirnt</code> is a typo of <code>print</code>. Python raises <code>NameError: name 'pirnt' is not defined</code>.",
        "print('Hello, world!')",
    ),
    "js": (
        "console.lg('Hello, world!');",
        "<b>Bug:</b> <code>console.lg</code> is a typo of <code>console.log</code>. JavaScript raises <code>TypeError: console.lg is not a function</code>.",
        "console.log('Hello, world!');",
    ),
    "html": (
        "<h1>Welcome\n<p>This is my site.</p>",
        "<b>Bug:</b> The <code>&lt;h1&gt;</code> tag is never closed. The paragraph that follows ends up inside the heading and the rest of the page styles wrong.",
        "<h1>Welcome</h1>\n<p>This is my site.</p>",
    ),
    "css": (
        ".box {\n  width: 100px;\n  padding: 20px;\n}\n/* expected total width: 100px, actual: 140px */",
        "<b>Bug:</b> By default, <code>padding</code> is added on top of <code>width</code>. Set <code>box-sizing: border-box</code> so width includes padding.",
        ".box {\n  box-sizing: border-box;\n  width: 100px;\n  padding: 20px;\n}",
    ),
    "prompt": (
        'Prompt: "make my code better"',
        "<b>Bug:</b> Too vague. The AI doesn't know what 'better' means — performance? readability? layout? Name the file, function, the specific problem, and what 'better' looks like.",
        'Prompt: "In game.py, update() recalculates the level grid every frame. Cache it once on level load instead. Don\'t touch render()."',
    ),
}

# Backwards-compatible alias (some helpers still reference this).
DEFAULT_DEBUG = DEFAULT_DEBUG_BY_LANG["python"]


def pick_debug(topic_lc, lang="python"):
    for keywords, debug in GENERIC_DEBUG_BY_KEYWORD:
        for kw in keywords:
            if kw in topic_lc:
                return debug
    return DEFAULT_DEBUG_BY_LANG.get(lang, DEFAULT_DEBUG_BY_LANG["python"])


def pick_debug_from_corpus(corpus, topic_lc, lang="python"):
    """Take a code block FROM THIS WEEK's slides and introduce a bug in it.
    Bug is one student would realistically hit. Fall back to keyword pick.

    Python-style bug introduction (pirnt typo, indentation drop, dict KeyError)
    is only applied when lang == 'python'. For other languages we skip straight
    to the language-aware keyword pick. This avoids the audit's flagged issue
    of Python typos contaminating CSS/HTML/JS decks."""
    if lang != "python":
        return pick_debug(topic_lc, lang)
    code_blocks = [c for c in corpus.get("code_blocks", []) if 15 < len(c) < 400]
    for code in code_blocks:
        # Case A: dict subscript with a key — change the lookup to a typo'd key
        var_to_kvs = {}
        for dm in DICT_LITERAL_RE.finditer(code):
            var_to_kvs[dm.group(1)] = {k: v for k, v in KEY_VAL_RE.findall(dm.group(2))}
        sub_match = SUBSCRIPT_RE.search(code)
        if sub_match and var_to_kvs:
            v, k = sub_match.group(1), sub_match.group(2)
            if v in var_to_kvs and k in var_to_kvs[v]:
                # Misspell the key (pluralize, or add a letter)
                wrong_k = k + "s" if not k.endswith("s") else k[:-1]
                buggy = code.replace(f"[\"{k}\"]", f"[\"{wrong_k}\"]").replace(f"['{k}']", f"['{wrong_k}']")
                if buggy != code:
                    bug = (
                        f"<b>Bug:</b> The dict has key <code>{repr(k)}</code> but the code asks for "
                        f"<code>{repr(wrong_k)}</code>. Python raises <code>KeyError: {repr(wrong_k)}</code>. "
                        "Either fix the spelling or use <code>.get(key, default)</code> for a safe fallback."
                    )
                    return buggy, bug, code

        # Case B: any `print(` line — introduce typo `pirnt`
        if "print(" in code:
            buggy = code.replace("print(", "pirnt(", 1)
            bug = (
                "<b>Bug:</b> <code>pirnt</code> is a typo of <code>print</code>. "
                "Python raises <code>NameError: name 'pirnt' is not defined</code>. Spell built-ins carefully."
            )
            return buggy, bug, code

        # Case C: assignment like `x = 5` — change `=` inside an if to `=` (already there) — skip
        # Case D: indentation drop — remove leading spaces of any indented line
        lines = code.split("\n")
        for i in range(1, len(lines)):
            if lines[i].startswith("    "):
                buggy_lines = list(lines)
                buggy_lines[i] = lines[i][2:]
                buggy = "\n".join(buggy_lines)
                bug = (
                    "<b>Bug:</b> Inconsistent indentation. Python raises "
                    "<code>IndentationError</code>. The body of a block must use the same number of "
                    "spaces — convention is 4."
                )
                return buggy, bug, code

    # No usable code block — fall back to keyword pick
    return pick_debug(topic_lc, lang)


def generate_mcqs(topic, topic_lc, corpus=None, lang="python"):
    """Build MCQs grounded in this week's slide content (corpus).
    Fall back to generic only if corpus yields nothing usable.

    `lang` only affects fallback distractors + which Python-specific builders
    are allowed to fire (e.g., q_print_literal only matches Python `print()`)."""
    questions = []

    # Try each content-aware builder; collect non-None ones.
    # Python-specific builders are skipped for non-Python decks — they look for
    # Python syntax (dict literals, `from X import Y`) that won't appear in JS/CSS/HTML.
    if corpus:
        active_builders = CONTENT_BUILDERS if lang == "python" else []
        for builder in active_builders:
            q = builder(corpus)
            if q and q not in questions:
                questions.append(q)
                if len(questions) >= 4:
                    break

        # Add a heading-based "what is this lesson about?" if we have headings
        if len(questions) < 4:
            q = q_heading_summary(corpus, topic, lang)
            if q:
                questions.append(q)

        # Always end with a corpus-grounded debug question
        if len(questions) < 5:
            questions.append(q_debug_from_corpus(corpus, topic_lc, lang))

    # Ensure at least 3 questions
    while len(questions) < 3:
        questions.append(q_meta_done(topic))

    return questions[:5]


GENERIC_PRACTICE_BY_KEYWORD = [
    (["dict"], (
        "Build a small dictionary that holds 3 of your favorite things (game, food, song, whatever) and print each one on its own line.",
        "favs = {\n    'game': '___',\n    'food': '___',\n    'song': '___',\n}\n\n# Print each key + value\nfor k, v in favs.items():\n    pass  # print(f'{k}: {v}')",
    )),
    (["list"], (
        "Make a list of 5 things. Print the first, the last, and the middle. Then add one more item and print the full list.",
        "items = ['___', '___', '___', '___', '___']\n\n# print first, last, middle\nprint(items[0])\nprint(items[-1])\nprint(items[len(items) // 2])\n\n# add one\nitems.append('___')\nprint(items)",
    )),
    (["function", "def"], (
        "Write a function that takes a name and returns a greeting. Call it 3 times with different names.",
        "def greet(name):\n    return f'Hello, {name}!'\n\n# Call it with 3 different names\nprint(greet('___'))\nprint(greet('___'))\nprint(greet('___'))",
    )),
    (["loop", "for"], (
        "Print the numbers 1–10. Then print only the even ones.",
        "for i in range(1, 11):\n    print(i)\n\nprint('---')\n\nfor i in range(1, 11):\n    # only print even\n    pass",
    )),
    (["validate", "input"], (
        "Ask the user for a number. Keep asking until they type a valid one. Then print it.",
        "while True:\n    raw = input('Number? ')\n    try:\n        n = int(raw)\n        break\n    except ValueError:\n        print('Not a number — try again.')\n\nprint(f'You typed {n}')",
    )),
    (["random"], (
        "Pick a random Pokémon (or item) from a list and print it. Run the program 5 times to see different picks.",
        "import random\nteam = ['Pikachu', 'Charmander', 'Squirtle', 'Bulbasaur']\nprint(random.choice(team))",
    )),
    (["html"], (
        "Build a tiny HTML page with a heading, two paragraphs, and one image. Open it in your browser.",
        "<!DOCTYPE html>\n<html>\n<head><title>My Page</title></head>\n<body>\n  <h1>Hello</h1>\n  <p>First paragraph.</p>\n  <p>Second paragraph.</p>\n  <img src=\"https://placecats.com/300/200\" alt=\"cat\" />\n</body>\n</html>",
    )),
    (["css"], (
        "Take any HTML page and add a stylesheet that changes the background, font, and one color of your choice.",
        "/* style.css */\nbody {\n  background: #faf6f0;\n  font-family: system-ui, sans-serif;\n}\nh1 {\n  color: #ff7849;\n}",
    )),
    (["javascript", "js"], (
        "Add a button to your HTML page. When clicked, change the text of an element on the page.",
        "<button id='btn'>Click me</button>\n<p id='out'>Before</p>\n<script>\ndocument.getElementById('btn').onclick = () => {\n  document.getElementById('out').textContent = 'After!';\n};\n</script>",
    )),
    (["prompt", "agent", "ai"], (
        "Write a specific, well-scoped prompt that fixes ONE bug in a file. Include the filename, the function, and the expected behavior.",
        "# Example prompt structure:\n# In <filename>, the function <name>() <does X> but should <do Y>.\n# Change just <which line/section> so that <expected behavior>.\n# Don't touch <other functions / files>.",
    )),
]

DEFAULT_PRACTICE = (
    "Take the example code from this week. Type it out from scratch — no copy/paste. Run it. Now change one value or name and predict the output before running again.",
    "# Re-type the example code below. Then experiment.\n",
)


def pick_practice(topic_lc):
    for keywords, p in GENERIC_PRACTICE_BY_KEYWORD:
        for kw in keywords:
            if kw in topic_lc:
                return p
    return DEFAULT_PRACTICE


# ----------------------------------------------------------------------
# Slide HTML rendering
# ----------------------------------------------------------------------

def render_edge_slide(edges):
    cards = "\n".join(
        f'      <div class="edge-card"><div class="ehead">{html_mod.escape(h)}</div>'
        f'<div class="edesc">{d}</div></div>'  # desc may contain HTML
        for h, d in edges
    )
    return (
        '<div class="slide"><div class="pill">⚠ Edge cases</div>'
        '<h2>Gotchas + pitfalls</h2>\n'
        f'<div class="edge-grid">\n{cards}\n</div></div>'
    )


# ----------------------------------------------------------------------
# Pillar slot renderers — Slot 2 (Recap), 3 (Predict), 4 (Vocab), 10 (Code Talk)
# ----------------------------------------------------------------------
# Each renders the slot in the template-conformant shape from TEMPLATE.md so
# instructors and students see the same slot-badge / pill / structure they
# already know from rs001-text-adventure.

def render_recap_slide(recap):
    q, a = recap
    return (
        '<div class="slide">'
        '<span class="slot-badge">SLOT 2</span>'
        '<div class="pill purple">Recap</div>'
        '<h2>Last week you learned…</h2>'
        '<div class="recap-q">'
        '<div class="label">Quick check</div>'
        f'<div class="q">{q}</div>'
        f'<details><summary>Show answer</summary><div class="ans">{a}</div></details>'
        '</div></div>'
    )


def render_predict_slide(predict):
    code, expected, _lang = predict
    return (
        '<div class="slide">'
        '<span class="slot-badge">SLOT 3</span>'
        '<div class="pill">Predict 🤔</div>'
        '<h2>What will this do?</h2>'
        '<div class="predict-card">'
        '<div class="label">Predict first — then click reveal</div>'
        f'<pre>{html_mod.escape(code)}</pre>'
        f'<details><summary>Reveal output</summary><div class="ans">{html_mod.escape(expected)}</div></details>'
        '</div></div>'
    )


def render_vocab_slide(terms):
    rows = "\n".join(
        f'    <span class="term">{html_mod.escape(t)}</span>'
        f'<span class="gloss">{html_mod.escape(eng)}</span>'
        f'<span class="ko">{html_mod.escape(ko)}</span>'
        for t, eng, ko in terms
    )
    return (
        '<div class="slide">'
        '<span class="slot-badge">SLOT 4</span>'
        '<div class="pill">Vocab</div>'
        '<h2>New words today</h2>'
        f'<div class="vocab-table">\n{rows}\n</div></div>'
    )


# Code Talk Frame patterns by language. Each picks the right "X does Y because Z"
# syntactic skeleton for the target language so the sentence frame matches the code.
CODE_TALK_FRAMES = {
    "python": '"This <code>____</code> line does <code>____</code> because <code>____</code>."',
    "js":     '"This <code>____</code> statement does <code>____</code> because <code>____</code>."',
    "html":   '"This <code>&lt;____&gt;</code> tag shows <code>____</code> because <code>____</code>."',
    "css":    '"This <code>____</code> rule changes <code>____</code> because <code>____</code>."',
    "prompt": '"This prompt asks for <code>____</code> in <code>____</code> because <code>____</code>."',
}


def render_modify_slide(modify):
    code, hint = modify
    return (
        '<div class="slide">'
        '<span class="slot-badge">SLOT 9</span>'
        '<div class="pill">Try it</div>'
        '<h2>Fill in the blanks</h2>'
        f'<pre>{html_mod.escape(code)}</pre>'
        f'<p style="margin-top:.6em;font-size:clamp(14px,2.2vmin,18px);opacity:.85"><b>Hint:</b> {hint}</p>'
        '</div>'
    )


def render_code_talk_slide(lang):
    frame = CODE_TALK_FRAMES.get(lang, CODE_TALK_FRAMES["python"])
    return (
        '<div class="slide">'
        '<span class="slot-badge">SLOT 10</span>'
        '<div class="pill purple">Code Talk</div>'
        '<h2>Tell a partner</h2>'
        '<div class="frame-card">'
        '<div class="label">Sentence frame</div>'
        f'<div class="frame">{frame}</div>'
        '<div class="pair-prompt">한국어로 먼저 → 그다음 영어로 / Korean first, then English.</div>'
        '</div></div>'
    )


def render_debug_slides(debug):
    code, bug, fix = debug
    return (
        '<div class="slide"><div class="pill">🐛 Debug</div>'
        '<h2>What\'s wrong with this code?</h2>'
        '<div class="debug-box"><div class="debug-tag">buggy</div>'
        f'<pre style="margin-top:.4em">{html_mod.escape(code)}</pre></div>'
        '<p style="margin-top:.6em;font-size:clamp(14px,2.2vmin,17px);opacity:.85">'
        'Think first — then click next.</p></div>'
        '\n<div class="slide"><div class="pill">🐛 Debug</div>'
        '<h2>The bug</h2>'
        f'<div class="debug-reveal">{bug}</div>'
        '<div class="debug-box" style="margin-top:.7em">'
        '<div class="debug-tag fix">fixed</div>'
        f'<pre style="margin-top:.4em">{html_mod.escape(fix)}</pre></div></div>'
    )


def render_mcq_slides(mcqs):
    out = []
    total = len(mcqs)
    for n, (q, opts, correct, explain) in enumerate(mcqs, 1):
        opts_html = "\n".join(
            f'<button class="opt">{o if "<" in o else html_mod.escape(o)}</button>'
            for o in opts
        )
        explain_attr = html_mod.escape(re.sub(r"<[^>]+>", "", explain))
        out.append(
            f'<div class="slide mcq" data-correct="{correct}" data-explain="{explain_attr}">'
            f'<div class="pill purple">📝 Quiz</div>'
            f'<div class="qmeta">Question {n} of {total}</div>'
            f'<div class="q">{q}</div>'
            f'<div class="opts">{opts_html}</div>'
            f'<div class="qfeedback"></div></div>'
        )
    # Score slide
    out.append(
        '<div class="slide center-all mcq-score">'
        '<div class="pill purple">Quiz</div>'
        '<h2>Your score</h2>'
        f'<div class="score-val">0 / {total}</div>'
        '<p class="score-msg">Answer the questions to see your score.</p>'
        '<button class="quiz-reset">↺ retake</button></div>'
    )
    return "\n".join(out)


def render_practice_slide(practice):
    task, starter = practice
    return (
        '<div class="slide"><div class="pill">💻 Practice</div>'
        '<h2>Coding practice</h2>'
        f'<div class="practice-task">{task}</div>'
        '<div class="debug-box">'
        '<div class="debug-tag fix" style="background:var(--accent-2)">starter</div>'
        f'<pre style="margin-top:.4em">{html_mod.escape(starter)}</pre></div>'
        '<p class="practice-hint">Open your editor. Save as <code>practice.py</code> (or <code>.html</code>). Run it. Iterate.</p></div>'
    )


# ----------------------------------------------------------------------
# Injection
# ----------------------------------------------------------------------

def inject_into_file(path: Path):
    text = path.read_text(encoding="utf-8")

    # Strip any previous injection
    text = INJECTED_BLOCK_RE.sub("", text)

    # Extract title for topic context
    m = TITLE_RE.search(text)
    title = m.group(1).strip() if m else path.stem
    # Normalize: drop the "RSXXX WN —" prefix
    topic = re.sub(r"^[A-Z]+\d+\s+W?\d+\s*[—\-:]\s*", "", title)
    topic_lc = (topic + " " + path.stem).lower()

    stem = path.stem.lower()
    override = OVERRIDES.get(stem, {})
    lang = detect_lang(path)

    # Check which pillar slots the deck author already wrote by hand.
    # rs001 is fully conformant — every slot 1..12 is present — so we skip
    # all pillar injections for that course and just add the Extras block.
    # Decks that wrote slot 2 by hand (e.g. ai001 week-08-final-project) get
    # their hand-authored version preserved.
    already_have = present_slots(text)

    corpus = extract_corpus(text)

    edges = override.get("edges", pick_edges(topic_lc))
    debug = override.get("debug", pick_debug_from_corpus(corpus, topic_lc, lang))
    mcqs = override.get("mcqs", generate_mcqs(topic, topic_lc, corpus, lang))
    practice = override.get("practice", pick_practice(topic_lc))

    # Build the pillar-injection prefix — Slots 2, 3, 4 go BEFORE the existing
    # deck content (they belong at the start of a lesson per TEMPLATE.md).
    pillar_pre_parts = []
    if 2 not in already_have and stem in WEEK_RECAP:
        pillar_pre_parts.append(render_recap_slide(WEEK_RECAP[stem]))
    if 3 not in already_have and stem in WEEK_PREDICT:
        pillar_pre_parts.append(render_predict_slide(WEEK_PREDICT[stem]))
    if 4 not in already_have and stem in WEEK_VOCAB:
        pillar_pre_parts.append(render_vocab_slide(WEEK_VOCAB[stem]))

    # Slots 9 (Modify) + 10 (Code Talk Frame) go near the end, before the Extras block.
    pillar_post_parts = []
    if 9 not in already_have and stem in WEEK_MODIFY:
        pillar_post_parts.append(render_modify_slide(WEEK_MODIFY[stem]))
    if 10 not in already_have:
        pillar_post_parts.append(render_code_talk_slide(lang))

    extras = (
        "\n<!-- INJECTED-EXTRAS-START -->\n"
        + ("\n".join(pillar_pre_parts) + "\n" if pillar_pre_parts else "")
        + ("\n".join(pillar_post_parts) + "\n" if pillar_post_parts else "")
        + render_edge_slide(edges) + "\n"
        + render_debug_slides(debug) + "\n"
        + render_mcq_slides(mcqs) + "\n"
        + render_practice_slide(practice) + "\n"
        + "<!-- INJECTED-EXTRAS-END -->\n"
    )

    # Insert just before <div class="nav">
    if not NAV_OPEN_RE.search(text):
        print(f"  SKIP (no nav block): {path.name}")
        return False

    replacement = extras + '<div class="nav">'
    new_text = NAV_OPEN_RE.sub(lambda _m: replacement, text, count=1)

    # Update counter to reflect new total slide count
    # Count slides post-injection
    slide_count = new_text.count('<div class="slide')
    new_text = SLIDE_COUNT_RE.sub(
        f'<span class="counter" id="counter">1 / {slide_count}</span>',
        new_text,
    )

    path.write_text(new_text, encoding="utf-8")
    return True


def main():
    total = 0
    touched = 0
    for pattern in COURSE_GLOBS:
        for p in sorted(ROOT.glob(pattern)):
            total += 1
            if inject_into_file(p):
                touched += 1
    print(f"injected supplementary slides into {touched} / {total} course-week files")


if __name__ == "__main__":
    main()
