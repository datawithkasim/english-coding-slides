"""
Injects supplementary slides (edge cases, debug, MCQ quiz, coding practice)
into the existing hand-authored course-week HTML decks (rs001-4, web001-3, ai001).

Insertion point: just before <div class="nav">.
Order added: edge → debug-buggy → debug-reveal → MCQ × N → score → practice.
The existing course-week close slide stays as the narrative wrap-up;
the new practice slide becomes the final slide (per request).

Idempotent: re-running first strips previously injected blocks (marked with
<!-- INJECTED-EXTRAS-START --> / <!-- INJECTED-EXTRAS-END -->), then re-adds.

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


def strip_tags(s: str) -> str:
    s = TAG_RE.sub("", s)
    s = s.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&").replace("&quot;", '"').replace("&#39;", "'").replace("&#x27;", "'")
    return s.strip()


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


def q_heading_summary(corpus, topic):
    """Ask what the lesson is about — answer references the actual <h1>/<h2>."""
    headings = [h for h in corpus["headings"] if 4 < len(h) < 60]
    if not headings:
        return None
    h = headings[0]
    return (
        f"Looking at the slide titles, what is this lesson mainly about?",
        [h, "List comprehensions", "Decorators and metaclasses", "Multi-threaded I/O"],
        0,
        f"The lesson title says it: {h}",
    )


# Generic fallbacks — only used when corpus yields nothing useful
def q_debug_from_corpus(corpus, topic_lc):
    debug = pick_debug(topic_lc)
    code, bug, _ = debug
    short_bug = strip_tags(bug).replace("Bug: ", "")
    return (
        "What's wrong with this code?<br>"
        f'<pre style="font-size:.8em;margin-top:.4em">{html_mod.escape(code)}</pre>',
        [short_bug, "Nothing — works as written.", "Missing <code>import sys</code>.", "Variable not declared with <code>let</code>."],
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

DEFAULT_DEBUG = (
    "pirnt('Hello, world!')",
    "<b>Bug:</b> <code>pirnt</code> is a typo of <code>print</code>. Python raises <code>NameError: name 'pirnt' is not defined</code>.",
    "print('Hello, world!')",
)


def pick_debug(topic_lc):
    for keywords, debug in GENERIC_DEBUG_BY_KEYWORD:
        for kw in keywords:
            if kw in topic_lc:
                return debug
    return DEFAULT_DEBUG


def pick_debug_from_corpus(corpus, topic_lc):
    """Take a code block FROM THIS WEEK's slides and introduce a bug in it.
    Bug is one student would realistically hit. Fall back to keyword pick."""
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
    return pick_debug(topic_lc)


def generate_mcqs(topic, topic_lc, corpus=None):
    """Build MCQs grounded in this week's slide content (corpus).
    Fall back to generic only if corpus yields nothing usable."""
    questions = []

    # Try each content-aware builder; collect non-None ones
    if corpus:
        for builder in CONTENT_BUILDERS:
            q = builder(corpus)
            if q and q not in questions:
                questions.append(q)
                if len(questions) >= 4:
                    break

        # Add a heading-based "what is this lesson about?" if we have headings
        if len(questions) < 4:
            q = q_heading_summary(corpus, topic)
            if q:
                questions.append(q)

        # Always end with a corpus-grounded debug question
        if len(questions) < 5:
            questions.append(q_debug_from_corpus(corpus, topic_lc))

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

    corpus = extract_corpus(text)

    edges = override.get("edges", pick_edges(topic_lc))
    debug = override.get("debug", pick_debug_from_corpus(corpus, topic_lc))
    mcqs = override.get("mcqs", generate_mcqs(topic, topic_lc, corpus))
    practice = override.get("practice", pick_practice(topic_lc))

    extras = (
        "\n<!-- INJECTED-EXTRAS-START -->\n"
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
