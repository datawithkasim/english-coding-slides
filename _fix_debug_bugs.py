# One-off: replace the repetitive print->pirnt debug slides across all
# injected decks with a varied, language-appropriate bug bank, and make
# every buggy/fixed code block use real line breaks.
import re, sys, hashlib, pathlib

ROOT = pathlib.Path(__file__).parent

def esc(s):
    return (s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
             .replace('"', '&quot;').replace("'", '&#x27;'))

def attr(s):
    return (s.replace('&', '&amp;').replace('"', '&quot;')
             .replace('<', '&lt;').replace('>', '&gt;'))

def opt(s):
    # button label: plain text, minimal escaping (no inline HTML)
    return '<button class="opt">' + s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;') + '</button>'

# Each bug: (buggy, fixed, reveal_html, explain_plain, correct_opt, [d1,d2,d3])
PY = [
 ("message = \"Hello!\"\npirnt(message)",
  "message = \"Hello!\"\nprint(message)",
  "<code>pirnt</code> is a typo. Python only knows <code>print</code>, so it raises <code>NameError: name 'pirnt' is not defined</code>.",
  "Typo: pirnt should be print (NameError).",
  "pirnt is a typo of print, so Python raises NameError.",
  ["Strings can't be stored in variables.", "You must write print() before assigning the variable.", "It needs an import for print."]),
 ("age = 12\nif age >= 10\n    print(\"Old enough\")",
  "age = 12\nif age >= 10:\n    print(\"Old enough\")",
  "The <code>if</code> header is missing its colon. Python raises <code>SyntaxError: expected ':'</code>. Every <code>if</code>/<code>for</code>/<code>while</code>/<code>def</code> line ends in <code>:</code>.",
  "Missing colon after the if condition (SyntaxError).",
  "The if line needs a colon at the end (SyntaxError).",
  [">= is not a real operator.", "age must be a string here.", "print must be indented less."]),
 ("def greet():\nprint(\"Hi!\")\ngreet()",
  "def greet():\n    print(\"Hi!\")\ngreet()",
  "The body of <code>greet()</code> is not indented. Python raises <code>IndentationError: expected an indented block</code>. Code inside a function must be indented.",
  "Function body not indented (IndentationError).",
  "The line inside greet() must be indented (IndentationError).",
  ["greet() can't be called before it's defined.", "Functions must return a value.", "print() can't be used inside a function."]),
 ("score = 5\nif score = 10:\n    print(\"Win!\")",
  "score = 5\nif score == 10:\n    print(\"Win!\")",
  "<code>=</code> assigns a value; <code>==</code> compares. Using <code>=</code> in an <code>if</code> raises <code>SyntaxError</code>. Comparisons need <code>==</code>.",
  "= assigns; comparison needs == (SyntaxError).",
  "Comparison needs == , not = (SyntaxError).",
  ["score is not defined.", "if statements can't test numbers.", "It is missing an else branch."]),
 ("age = 12\nprint(\"I am \" + age + \" years old\")",
  "age = 12\nprint(\"I am \" + str(age) + \" years old\")",
  "You can't join a number to a string with <code>+</code>. Python raises <code>TypeError: can only concatenate str (not \"int\") to str</code>. Wrap it in <code>str()</code>.",
  "Can't concatenate str and int — use str(age).",
  "age is a number; wrap it in str() to join it to text.",
  ["age must be quoted everywhere.", "print() only takes one argument.", "+ is not allowed inside print()."]),
 ("colors = [\"red\", \"green\", \"blue\"]\nprint(colors[3])",
  "colors = [\"red\", \"green\", \"blue\"]\nprint(colors[2])",
  "A 3-item list has indexes 0, 1, 2. <code>colors[3]</code> raises <code>IndexError: list index out of range</code>. The last index is <code>len - 1</code>.",
  "Index 3 is out of range — last index is 2.",
  "Index 3 is out of range; the last index is 2 (IndexError).",
  ["Lists can't hold strings.", "You must use colors.get(3).", "List indexes start at 1."]),
 ("count = 0\nwhile count < 5:\n    print(count)",
  "count = 0\nwhile count < 5:\n    print(count)\n    count += 1",
  "<code>count</code> never changes, so <code>count &lt; 5</code> is always true — an infinite loop. Add <code>count += 1</code> inside the loop.",
  "count never increments — infinite loop.",
  "count never changes, so the while loop runs forever.",
  ["while can't use the < operator.", "print(count) should be print(count + 1).", "Missing a colon after while."]),
 ("def total():\n    return 2 + 3\nprint(total)",
  "def total():\n    return 2 + 3\nprint(total())",
  "<code>total</code> with no <code>()</code> prints the function object, not its result. Call it with <code>total()</code>.",
  "Missing () — total() actually calls the function.",
  "total needs () to call it; without () it prints the function itself.",
  ["return can't add two numbers.", "Functions can never be printed (crash).", "def must be capitalised."]),
 ("name = \"Kasim'\nprint(name)",
  "name = \"Kasim\"\nprint(name)",
  "The string opens with <code>\"</code> but closes with <code>'</code>. Python raises <code>SyntaxError: unterminated string literal</code>. Quotes must match.",
  "Mismatched quotes — unterminated string (SyntaxError).",
  "The quotes don't match, so the string is never closed (SyntaxError).",
  ["name is a reserved word.", "Strings must go inside [ ].", "print() can't take a variable."]),
 ("age = input(\"Age? \")\nif age > 18:\n    print(\"Adult\")",
  "age = int(input(\"Age? \"))\nif age > 18:\n    print(\"Adult\")",
  "<code>input()</code> always returns a string. Comparing a string with a number raises <code>TypeError</code>. Convert with <code>int()</code>.",
  "input() returns a string — wrap it in int().",
  "input() gives text; convert with int() before comparing to a number.",
  ["input() takes no prompt text.", "if can't compare with >.", "age must be printed first."]),
 ("nums = [1, 2, 3]\nnums = nums.append(4)\nprint(nums)",
  "nums = [1, 2, 3]\nnums.append(4)\nprint(nums)",
  "<code>.append()</code> changes the list in place and returns <code>None</code>. Reassigning makes <code>nums</code> become <code>None</code>. Just call <code>nums.append(4)</code>.",
  ".append() returns None — don't reassign.",
  "append() returns None, so reassigning makes nums None.",
  ["Lists can't grow after they're made.", "append() needs two arguments.", "You must write nums + 4 instead."]),
 ("first_name = \"Kasim\"\nprint(firstname)",
  "first_name = \"Kasim\"\nprint(first_name)",
  "<code>firstname</code> was never defined — the variable is <code>first_name</code> (with an underscore). Python raises <code>NameError</code>. Names must match exactly.",
  "Name mismatch: first_name vs firstname (NameError).",
  "firstname doesn't match first_name, so Python raises NameError.",
  ["Underscores aren't allowed in names.", "print() needs quotes around variables.", "Variables can't hold strings."]),
]

JS = [
 ("console.lg(\"Hello!\");",
  "console.log(\"Hello!\");",
  "<code>console.lg</code> is a typo of <code>console.log</code>. The browser throws <code>TypeError: console.lg is not a function</code>.",
  "Typo: console.lg should be console.log.",
  "console.lg is a typo of console.log (TypeError).",
  ["A missing semicolon crashes it.", "Strings need single quotes in JS.", "console must be capitalised."]),
 ("let score = 5;\nif (score = 10) {\n  console.log(\"Win\");\n}",
  "let score = 5;\nif (score === 10) {\n  console.log(\"Win\");\n}",
  "<code>=</code> assigns; <code>===</code> compares. <code>if (score = 10)</code> sets score to 10 and is always truthy. Use <code>===</code>.",
  "= assigns; use === to compare.",
  "= assigns a value; comparison needs ===.",
  ["let can't be reassigned.", "if doesn't need braces.", "console.log can't go inside if."]),
 ("const count = 1;\ncount = count + 1;\nconsole.log(count);",
  "let count = 1;\ncount = count + 1;\nconsole.log(count);",
  "A <code>const</code> can't be reassigned. <code>count = count + 1</code> throws <code>TypeError: Assignment to constant variable</code>. Use <code>let</code> for values that change.",
  "const can't be reassigned — use let.",
  "const can't be reassigned; use let for changing values.",
  ["count + 1 is invalid math.", "A semicolon is missing.", "console.log needs a string."]),
 ("const btn = document.getElementById(\"submit\");\nbtn.addEventListener(\"click\", run);",
  "// the button's id in the HTML is \"submitBtn\"\nconst btn = document.getElementById(\"submitBtn\");\nbtn.addEventListener(\"click\", run);",
  "If no element has <code>id=\"submit\"</code>, <code>getElementById</code> returns <code>null</code> and <code>null.addEventListener</code> throws <code>Cannot read properties of null</code>. The id must match the HTML exactly.",
  "getElementById returned null — the id must match the HTML.",
  "No element has that id, so getElementById returns null.",
  ["addEventListener needs 3 arguments.", "'click' should be 'onclick'.", "const can't hold an element."]),
 ("const colors = [\"red\", \"green\", \"blue\"];\nconsole.log(colors[3]);",
  "const colors = [\"red\", \"green\", \"blue\"];\nconsole.log(colors[2]);",
  "A 3-item array has indexes 0–2. <code>colors[3]</code> is <code>undefined</code>, not the last item. The last index is <code>length - 1</code>.",
  "Index 3 is undefined — last index is 2.",
  "colors[3] is undefined; the last index is 2.",
  ["Arrays start counting at 1.", "Use colors.get(3) instead.", "Arrays can't store strings."]),
 ("let total = \"5\";\ntotal = total + 1;\nconsole.log(total);",
  "let total = 5;\ntotal = total + 1;\nconsole.log(total);",
  "<code>\"5\" + 1</code> is the string <code>\"51\"</code>, not <code>6</code> — JS concatenates when one side is a string. Use a number, or <code>Number()</code>.",
  "\"5\" + 1 gives \"51\" — use a number / Number().",
  "\"5\" is text, so \"5\" + 1 becomes \"51\", not 6.",
  ["You can't add to a string at all (crash).", "let should be const.", "Missing semicolons break it."]),
 ("function double(n) {\n  n * 2;\n}\nconsole.log(double(4));",
  "function double(n) {\n  return n * 2;\n}\nconsole.log(double(4));",
  "<code>double()</code> never <code>return</code>s, so it gives <code>undefined</code>. Add <code>return n * 2;</code>.",
  "No return — the function gives undefined.",
  "double() has no return, so it gives undefined.",
  ["n * 2 is invalid syntax.", "The function must be an arrow function.", "console.log can't call a function."]),
 ("function greet() {\n  return \"Hi!\";\n}\nconsole.log(greet);",
  "function greet() {\n  return \"Hi!\";\n}\nconsole.log(greet());",
  "<code>greet</code> with no <code>()</code> logs the function itself, not its result. Call it: <code>greet()</code>.",
  "Missing () — greet() actually calls it.",
  "greet needs () to run; without it you log the function.",
  ["Functions can't return strings.", "greet must be capitalised.", "console.log only takes numbers."]),
]

WEB = [
 ("<h1>Welcome\n<p>My site</p>",
  "<h1>Welcome</h1>\n<p>My site</p>",
  "The <code>&lt;h1&gt;</code> is never closed. Without <code>&lt;/h1&gt;</code> the browser pulls the <code>&lt;p&gt;</code> into the heading. Every tag needs a closing tag.",
  "Missing </h1> — close every tag.",
  "The <h1> has no closing </h1> tag.",
  ["h1 must be lowercase only.", "p can't come after h1.", "Headings need a class."]),
 (".card {\n  color: red\n  padding: 8px;",
  ".card {\n  color: red;\n  padding: 8px;\n}",
  "<code>color: red</code> has no semicolon, so the browser reads it as one broken value and drops both rules. End every declaration with <code>;</code> and close the block with <code>}</code>.",
  "Missing semicolon (and closing }) breaks the rule.",
  "color: red is missing its semicolon, so the rule breaks.",
  ["red is not a valid colour.", "padding can't be 8px.", "Class names can't start with a dot."]),
 (".box {\n  width: 200;\n}",
  ".box {\n  width: 200px;\n}",
  "<code>width: 200</code> has no unit, so the browser ignores it. Lengths need a unit like <code>px</code>, <code>%</code>, or <code>rem</code>.",
  "width: 200 has no unit — use 200px.",
  "width needs a unit, e.g. 200px.",
  ["width can't be a number.", "A semicolon is missing.", ".box must be #box."]),
 ("<div class=\"hero\"></div>\n\n#hero {\n  background: navy;\n}",
  "<div class=\"hero\"></div>\n\n.hero {\n  background: navy;\n}",
  "<code>#hero</code> selects <code>id=\"hero\"</code>, but the element uses <code>class=\"hero\"</code>. Use a class selector: <code>.hero</code>.",
  "#hero targets an id; the element has a class — use .hero.",
  "The element has a class, so the selector must be .hero not #hero.",
  ["div can't have a background.", "navy is not a colour.", "Missing semicolon after navy."]),
 ("<a href=\"about.html>About</a>",
  "<a href=\"about.html\">About</a>",
  "The <code>href</code> value is missing its closing quote, so the browser treats <code>&gt;About&lt;/a&gt;</code> as part of the URL and the link breaks. Quotes must be closed.",
  "Unclosed quote in href — the link breaks.",
  "The href is missing its closing quote, so the link breaks.",
  ["<a> can't link to .html files.", "About must go in a <span>.", "href should be src."]),
 (".row {\n  justify-content: center;\n}",
  ".row {\n  display: flex;\n  justify-content: center;\n}",
  "<code>justify-content</code> only works on a flex (or grid) container. Without <code>display: flex;</code> it does nothing.",
  "justify-content needs display: flex on the parent.",
  "justify-content does nothing without display: flex.",
  ["center is not a valid value.", "A semicolon is missing.", ".row must be a <table>."]),
 ("p {\n  color = blue;\n}",
  "p {\n  color: blue;\n}",
  "CSS uses <code>:</code> between a property and its value, not <code>=</code>. <code>color = blue</code> is invalid and ignored. Write <code>color: blue;</code>.",
  "CSS uses a colon, not = (color: blue;).",
  "CSS separates property and value with : not =.",
  ["blue must be written #blue.", "p can't be styled.", "It is missing a class."]),
 ("<img src=\"cat.jpg\">\n</img>",
  "<img src=\"cat.jpg\" alt=\"a cat\">",
  "<code>&lt;img&gt;</code> is a void element — it has no closing tag, so <code>&lt;/img&gt;</code> is invalid. Add <code>alt</code> text for accessibility.",
  "img has no closing tag; add alt text instead.",
  "<img> is self-closing — there is no </img>.",
  ["img needs a width.", "src should be href.", "img must sit inside a div."]),
]

AI = [
 ('Prompt: "make my app better"',
  'Prompt: "On the login page, make the Submit button blue and 16px, and show an error message under the field when the password is empty."',
  "\"Make it better\" gives the AI no target. A good prompt names <b>what</b>, <b>where</b>, and what <b>done</b> looks like. Be specific.",
  "Too vague — say what, where, and what 'done' looks like.",
  "It is too vague: name what to change, where, and what done looks like.",
  ["Prompts must be a single word.", "AI can't change buttons.", "You must paste all your code first."]),
 ('Prompt: "Fix the bug."',
  'Prompt: "The cart total shows 0 after I add items. Expected: it sums each item\'s price. Here is the addItem function: ..."',
  "\"Fix the bug\" with no error, no expected behaviour, and no code leaves the AI guessing. Give it the symptom, the goal, and the relevant code.",
  "No context — give the symptom, expected result, and code.",
  "It gives no symptom, expected result, or code for the AI to use.",
  ["You can never ask AI to fix bugs.", "Bugs must be fixed by hand only.", "Prompts can't mention functions."]),
 ('Prompt: "Build me a full social network with chat, payments, and AI."',
  'Prompt: "Step 1: build a sign-up form with email and password. We will add chat after this works."',
  "Huge all-at-once prompts produce messy, broken output. Break the build into small steps and verify each one.",
  "Too much at once — break it into small steps.",
  "It asks for everything at once instead of small, checked steps.",
  ["AI can only build games.", "You must name only the language.", "Longer prompts are always better."]),
 ('Prompt: "Format the date nicely."',
  'Prompt: "Format the date as \'17 May 2026\' (day month year). Right now it shows 2026-05-17."',
  "\"Nicely\" is subjective. Show a concrete before/after example so the AI knows the exact format you want.",
  "Show a concrete before/after example of the output.",
  "\"Nicely\" is subjective; show the exact format with an example.",
  ["AI can't format dates.", "Dates must be numbers.", "You can't show examples to an AI."]),
 ('Prompt: "Add a database."',
  'Prompt: "Add a SQLite database with a \'users\' table (id, email, created_at). We use Python and Flask."',
  "Without the language, framework, or schema, the AI picks something that may not fit. State the stack and the constraints.",
  "State the stack and constraints, not just 'add a database'.",
  "It doesn't say the stack or the table schema the AI should use.",
  ["AI can't add databases.", "You must build the database first.", "SQLite is the only option."]),
 ('Prompt: "Your code is broken, fix it."',
  'Prompt: "Clicking Save does nothing; the console shows \'saveNote is not defined\'. Here is the button and the function."',
  "Blame gives no information. Describe what you did, what you expected, what actually happened, and the exact error text.",
  "Describe steps, expected vs actual, and the error text.",
  "Blame carries no information: give steps, expected vs actual, and the error.",
  ["You must restart the AI each time.", "Errors can't be pasted into prompts.", "AI ignores polite prompts."]),
 ('Prompt: "Add login."',
  'Prompt: "Add email/password login. Done = a wrong password shows \'Incorrect password\'; a correct one goes to /dashboard."',
  "With no \"done looks like\" check, you can't tell whether the AI succeeded. Put the acceptance test in the prompt.",
  "Add a 'done looks like' acceptance check to the prompt.",
  "It gives no acceptance check, so you can't tell if it worked.",
  ["Login can't be tested.", "Prompts can't include conditions.", "AI decides when it's done, not you."]),
 ('Prompt: "make it faster and prettier and add dark mode and fix the bug and deploy it"',
  'Prompt: "First, fix the blank-page-on-reload bug. We will do dark mode and deploy after that works."',
  "Bundling unrelated asks in one line means none get done well. Pick the single highest-priority change and verify it first.",
  "Don't bundle unrelated asks — do the top priority first.",
  "It bundles many unrelated asks; do the top priority first and verify.",
  ["You can only ever ask one thing.", "Deploying must always come first.", "AI can't prioritise at all."]),
]

def family(rel):
    if rel.startswith("webdev/web002-javascript/"): return "js", JS
    if rel.startswith("webdev/web001-css/") or rel.startswith("webdev/web003-portfolio/"): return "web", WEB
    if rel.startswith("ai-coding/"): return "ai", AI
    return "py", PY

RE_BUGGY  = re.compile(r'(<div class="debug-tag">buggy</div>\s*<pre[^>]*>).*?(</pre>)', re.DOTALL)
RE_REVEAL = re.compile(r'(<div class="debug-reveal"><b>Bug:</b> ).*?(</div>)', re.DOTALL)
RE_FIXED  = re.compile(r'(<div class="debug-tag fix">fixed</div>\s*<pre[^>]*>).*?(</pre>)', re.DOTALL)
RE_QUIZ = re.compile(
    r'(<div class="slide mcq"[^>]*\bdata-correct=")[^"]*("\s+data-explain=")[^"]*("[^>]*>)'
    r'(.*?)<div class="q">(?:What(?:&#39;|&#x27;|\'|’)s wrong with this code\?)<br>'
    r'(<pre[^>]*>).*?</pre>\s*</div>\s*<div class="opts">.*?</div>\s*<div class="qfeedback">',
    re.DOTALL)

def process(path):
    rel = path.relative_to(ROOT).as_posix()
    fam, bank = family(rel)
    h = int(hashlib.md5(rel.encode()).hexdigest(), 16)
    buggy, fixed, reveal_html, explain, correct, distractors = bank[h % len(bank)]
    txt = path.read_text(encoding="utf-8")
    if 'debug-reveal' not in txt:
        return None
    n = [0, 0, 0, 0]
    txt, n[0] = RE_BUGGY.subn(lambda m: m.group(1) + esc(buggy) + m.group(2), txt)
    txt, n[1] = RE_REVEAL.subn(lambda m: m.group(1) + reveal_html + m.group(2), txt)
    txt, n[2] = RE_FIXED.subn(lambda m: m.group(1) + esc(fixed) + m.group(2), txt)
    buttons = opt(correct) + ''.join(opt(d) for d in distractors)
    def quiz_sub(m):
        return (m.group(1) + "0" + m.group(2) + attr(explain) + m.group(3) + m.group(4)
                + '<div class="q">What\'s wrong with this code?<br>' + m.group(5)
                + esc(buggy) + '</pre></div><div class="opts">' + buttons
                + '</div><div class="qfeedback">')
    txt, n[3] = RE_QUIZ.subn(quiz_sub, txt)
    path.write_text(txt, encoding="utf-8")
    return rel, fam, h % len(bank), n

def main():
    files = sorted(p for p in ROOT.rglob("*.html")
                   if 'debug-reveal' in p.read_text(encoding="utf-8"))
    dry = "--apply" not in sys.argv
    if dry:
        print(f"DRY RUN — {len(files)} candidate files\n")
    miss = []
    for p in files:
        rel, fam, idx, n = (process(p) if not dry else _preview(p))
        flag = "" if (n and all(n)) else "  <-- INCOMPLETE"
        if not (n and all(n)): miss.append((rel, n))
        print(f"{fam:3} #{idx:<2} buggy={n[0]} reveal={n[1]} fixed={n[2]} quiz={n[3]}  {rel}{flag}")
    print(f"\n{'APPLIED' if not dry else 'DRY'} — {len(files)} files, {len(miss)} incomplete")
    for rel, n in miss:
        print("  INCOMPLETE", n, rel)

def _preview(path):
    rel = path.relative_to(ROOT).as_posix()
    fam, bank = family(rel)
    h = int(hashlib.md5(rel.encode()).hexdigest(), 16)
    buggy, fixed, reveal_html, explain, correct, distractors = bank[h % len(bank)]
    txt = path.read_text(encoding="utf-8")
    n = [len(RE_BUGGY.findall(txt)), len(RE_REVEAL.findall(txt)),
         len(RE_FIXED.findall(txt)), len(RE_QUIZ.findall(txt))]
    return rel, fam, h % len(bank), n

if __name__ == "__main__":
    main()
