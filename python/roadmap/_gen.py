"""
Generates a topic-per-file slide deck covering roadmap.sh/python.
Run: python _gen.py
"""
from pathlib import Path
import html
import re

HERE = Path(__file__).parent

CATEGORY_EMOJI = {
    "01-basics": "🐣",
    "02-control-flow": "🚦",
    "03-data-structures": "📦",
    "04-functions": "🧰",
    "05-modules-packages": "📚",
    "06-stdlib": "🧪",
    "07-file-io": "📁",
    "08-error-handling": "⚠️",
    "09-oop": "🏗️",
    "10-advanced": "🧙",
    "11-dsa": "🌳",
    "12-testing": "✅",
    "13-quality": "✨",
    "14-concurrency": "⚡",
    "15-web": "🌐",
    "16-data-ml": "🤖",
    "17-gui-games": "🎮",
    "18-automation-cv": "🔧",
    "19-cli": "💻",
}

# ----------------------------------------------------------------------
# MANIFEST — every roadmap.sh/python topic, grouped by category
# Each topic: (slug, title, summary, code, bullets[6], related[3])
# ----------------------------------------------------------------------

CATEGORIES = [
    ("01-basics", "Stage 1 · Basics", [
        ("what-is-python", "What is Python?",
         "Python is a high-level, interpreted, dynamically-typed language created by Guido van Rossum in 1991. Famous for readability.",
         "# Python looks like English\nname = 'Kasim'\nprint(f'Hello, {name}!')",
         [("readable", "indentation = structure"), ("interpreted", "no compile step"),
          ("dynamic", "types at runtime"), ("batteries", "huge stdlib"),
          ("free", "open source"), ("everywhere", "web, AI, scripts")],
         ["installation", "hello-world", "repl"]),

        ("installation", "Install Python",
         "Get Python 3.12+ from python.org, or use pyenv to manage many versions. Verify with python --version.",
         "$ python --version\nPython 3.12.2\n\n$ pyenv install 3.12.2\n$ pyenv global 3.12.2",
         [("python.org", "official installer"), ("pyenv", "many versions"),
          ("homebrew", "mac · brew install python"), ("apt", "ubuntu · apt install python3"),
          ("Microsoft Store", "windows easy"), ("uv python", "uv installs python too")],
         ["what-is-python", "hello-world", "virtual-envs"]),

        ("hello-world", "Hello, World!",
         "Save as hello.py, run with python hello.py. Your first Python program is one line.",
         "# hello.py\nprint('Hello, world!')",
         [("print()", "outputs to console"), ("strings", "wrap in '' or \"\""),
          ("save .py", "Python file extension"), ("run", "python hello.py"),
          ("REPL", "or paste into python shell"), ("no semicolon", "newline ends statement")],
         ["repl", "syntax-indentation", "input-output"]),

        ("repl", "The REPL — interactive Python",
         "REPL = Read-Eval-Print-Loop. Type python in your terminal and you get a live Python shell. Perfect for trying ideas.",
         "$ python\n>>> 2 + 2\n4\n>>> name = 'Mina'\n>>> name.upper()\n'MINA'",
         [(">>>", "primary prompt"), ("...", "continuation prompt"),
          ("exit()", "leave the REPL"), ("up arrow", "previous command"),
          ("IPython", "nicer REPL with colors"), ("Jupyter", "notebook-style REPL")],
         ["hello-world", "input-output", "variables"]),

        ("syntax-indentation", "Syntax + Indentation",
         "Python uses indentation (4 spaces) to define code blocks instead of braces. Indentation is mandatory, not cosmetic.",
         "if hp > 0:\n    print('alive')\n    if hp < 10:\n        print('low!')\nelse:\n    print('game over')",
         [("4 spaces", "PEP 8 standard"), ("never mix", "tabs + spaces breaks"),
          ("colon", "starts a block"), ("dedent", "ends a block"),
          ("readable", "indent = structure"), ("IndentationError", "common beginner bug")],
         ["comments", "control-flow", "variables"]),

        ("comments", "Comments",
         "Comments document why code exists. Python ignores them at runtime. Use them sparingly — code should explain itself.",
         "# single line comment\nx = 5  # inline comment\n\n'''\nmulti-line string\noften used as docstring\n'''",
         [("#", "single line"), ("triple quotes", "docstrings"),
          ("explain why", "not what"), ("avoid noise", "don't restate code"),
          ("TODO:", "common marker"), ("FIXME:", "known issue")],
         ["syntax-indentation", "docstrings", "pep8"]),

        ("variables", "Variables",
         "A variable is a labelled box for a value. Python infers the type from the value — no declaration needed.",
         "hp = 100\nname = 'Pikachu'\nis_shiny = True\nlevel = 5.5\n\n# reassign freely\nhp = hp - 10",
         [("snake_case", "naming convention"), ("no type", "inferred"),
          ("case-sensitive", "Hp ≠ hp"), ("reserved words", "if, for, def, etc"),
          ("unicode ok", "한국어 = '안녕'"), ("multi-assign", "a, b = 1, 2")],
         ("numbers", "strings", "operators")),

        ("numbers", "Numbers — int + float",
         "Python has int (whole numbers, unlimited size) and float (decimals, 64-bit). Arithmetic works as expected.",
         "n = 42          # int\nx = 3.14        # float\ngiant = 2 ** 100  # arbitrarily big!\n\nresult = (10 + 5) / 3   # 5.0",
         [("int", "no overflow"), ("float", "IEEE 754"),
          ("//", "integer division"), ("%", "modulo (remainder)"),
          ("**", "exponentiation"), ("complex", "3+4j supported")],
         ["operators", "math-module", "type-casting"]),

        ("strings", "Strings",
         "Strings are immutable sequences of characters. Use single, double, or triple quotes. Concatenate with +.",
         "name = 'Pikachu'\nshout = name.upper() + '!'\nlength = len(name)         # 7\nfirst = name[0]            # 'P'\nslice_ = name[1:4]         # 'ika'",
         [("immutable", "can't change in place"), ("indexing", "0-based"),
          ("slicing", "[start:stop:step]"), ("concat", "with +"),
          ("repeat", "with *"), ("f-string", "f'{var}'")],
         ["string-methods", "fstrings", "slicing"]),

        ("booleans", "Booleans + None",
         "bool has two values: True and False (capital T/F). None is Python's null — the absence of a value.",
         "alive = True\ndefeated = False\n\nresult = None  # not yet set\n\n# from comparisons:\nis_low = hp < 10",
         [("True / False", "capitalized"), ("None", "Python's null"),
          ("truthy", "non-empty, non-zero"), ("falsy", "0, '', [], {}, None"),
          ("is None", "preferred over == None"), ("bool(x)", "cast to True/False")],
         ["operators", "truthy-falsy", "type-casting"]),

        ("operators", "Operators",
         "Math (+, -, *, /), comparison (==, !=, <, >), logical (and, or, not), membership (in), identity (is).",
         "# math\n5 + 3   # 8\n5 // 2  # 2  (int div)\n5 % 2   # 1  (mod)\n5 ** 2  # 25\n\n# logic\nTrue and False  # False\n'a' in 'cat'    # True",
         [("+ - * /", "arithmetic"), ("// % **", "int div, mod, power"),
          ("== != < >", "comparison"), ("and or not", "logic"),
          ("in", "membership"), ("is", "identity")],
         ["numbers", "comparisons", "booleans"]),

        ("type-casting", "Type Casting",
         "Convert between types: int(), float(), str(), bool(), list(), dict(). input() always returns str — cast to use as a number.",
         "age = int(input('Age? '))\nprice = float('9.99')\nbig = str(1_000_000)\nflag = bool(0)   # False",
         [("int(x)", "to integer"), ("float(x)", "to decimal"),
          ("str(x)", "to text"), ("bool(x)", "to True/False"),
          ("list(x)", "to list"), ("ValueError", "on bad input")],
         ["numbers", "strings", "input-output"]),

        ("input-output", "Input + print",
         "input() reads a line of text from the user. print() writes to the console. Both are standard library, no import.",
         "name = input('Your name? ')\nprint(f'Hello, {name}')\nprint('a', 'b', sep='-')\nprint('loading', end='...')",
         [("input(prompt)", "always returns str"), ("print(*args)", "auto-separates with space"),
          ("end=''", "no newline"), ("sep='-'", "join with -"),
          ("file=", "redirect output"), ("flush=True", "force write")],
         ["fstrings", "type-casting", "logging"]),

        ("fstrings", "f-strings",
         "f-strings (formatted string literals, Python 3.6+) embed values inside strings using {expr}. The cleanest way to format text.",
         "name = 'Kasim'\nhp = 73\nprint(f'{name} has {hp} HP')\nprint(f'{hp / 100:.2%}')   # 73.00%\nprint(f'{name:>10}')        # right-align width 10",
         [("f'{x}'", "embed any expr"), (":.2f", "2 decimals"),
          (":,", "thousands sep"), (":%", "percent"),
          (":>10 :<10 :^10", "alignment"), ("=", "self-doc: f'{x=}'")],
         ["strings", "string-methods", "input-output"]),

        ("string-methods", "Common string methods",
         "Strings come with dozens of built-in methods. Memorize the top six and you can do 90% of text work.",
         "s = '  Hello, World!  '\ns.strip()         # 'Hello, World!'\ns.upper()         # '  HELLO, WORLD!  '\ns.lower()\ns.replace('o', '0')\ns.split(',')      # ['  Hello', ' World!  ']\ns.startswith('  H')",
         [("strip()", "trim whitespace"), ("upper/lower", "change case"),
          ("split()", "to list"), ("join()", "from list"),
          ("replace()", "swap parts"), ("startswith/endswith", "check edge")],
         ["strings", "fstrings", "regex"]),
    ]),

    ("02-control-flow", "Stage 2 · Control Flow", [
        ("if-elif-else", "if / elif / else",
         "Branch on conditions. elif chains additional checks. else catches everything left.",
         "if hp > 50:\n    print('healthy')\nelif hp > 10:\n    print('hurt')\nelse:\n    print('critical')",
         [("if", "first check"), ("elif", "additional"),
          ("else", "fallback"), ("ternary", "x if cond else y"),
          ("nested ok", "but flat is better"), ("no switch", "use match/case")],
         ["truthy-falsy", "operators", "match-case"]),

        ("truthy-falsy", "Truthy + Falsy",
         "Any value can be tested in an if. Empty collections, 0, None, and '' are falsy. Everything else is truthy.",
         "if []:    print('never runs')\nif [0]:   print('runs!')   # non-empty\nif None:  print('never')\nif 'no':  print('runs!')",
         [("False", "0, 0.0, '', [], {}, set(), None"), ("True", "everything else"),
          ("bool(x)", "explicit cast"), ("if x:", "implicit cast"),
          ("len(x) == 0", "explicit empty check"), ("is None", "for None check")],
         ["if-elif-else", "booleans", "operators"]),

        ("for-loops", "for loops",
         "for iterates over any iterable: list, tuple, string, dict, range, generator, file, anything with __iter__.",
         "for x in [1, 2, 3]:\n    print(x)\n\nfor i, name in enumerate(['a','b']):\n    print(i, name)\n\nfor k, v in d.items():\n    ...",
         [("any iterable", "list, str, dict, ..."), ("enumerate()", "with index"),
          ("zip()", "two lists in parallel"), ("range()", "n times"),
          ("for-else", "else runs if no break"), ("break/continue", "control"),],
         ["while-loops", "range", "iterators"]),

        ("while-loops", "while loops",
         "while loops until a condition becomes false. Useful when iteration count is unknown.",
         "hp = 100\nwhile hp > 0:\n    hp -= attack()\n    if hp < 0:\n        break\n\nwhile True:\n    cmd = input('> ')\n    if cmd == 'quit': break",
         [("condition checked first", "may run 0 times"),
          ("infinite loop", "while True:"),
          ("break", "exit loop"),
          ("else", "runs if no break"),
          ("careful", "easy infinite loop"),
          ("prefer for", "when count known")],
         ["for-loops", "break-continue", "pass"]),

        ("range", "range()",
         "range(stop), range(start, stop), range(start, stop, step) — lazy sequence of integers. Cheap, doesn't build a list.",
         "range(5)         # 0 1 2 3 4\nrange(2, 8)      # 2 3 4 5 6 7\nrange(0, 10, 2)  # 0 2 4 6 8\nrange(10, 0, -1) # countdown",
         [("0-indexed", "default start"), ("stop excluded", "like slicing"),
          ("negative step", "countdown"), ("lazy", "doesn't store all"),
          ("list(range(5))", "force materialize"), ("len(range)", "O(1)")],
         ["for-loops", "lists", "iterators"]),

        ("break-continue", "break + continue",
         "break exits the loop entirely. continue skips to the next iteration. Use both sparingly.",
         "for n in range(100):\n    if n == 7:\n        break       # exits\n    if n % 2:\n        continue    # skip odd\n    print(n)",
         [("break", "exit nearest loop"), ("continue", "skip to next iter"),
          ("only innermost", "for nested loops"), ("no goto", "Python has none"),
          ("for-else", "else skipped on break"), ("readability", "avoid deep nesting")],
         ["for-loops", "while-loops", "pass"]),

        ("pass", "pass — do nothing",
         "pass is a no-op. Useful as a placeholder when syntax requires a statement but you have nothing to do yet.",
         "def todo():\n    pass    # implement later\n\nclass Empty:\n    pass\n\nif x: pass\nelse:  do_thing()",
         [("placeholder", "syntax filler"), ("vs continue", "pass = nothing, continue = next iter"),
          ("vs return", "return exits function"), ("dev habit", "stub then fill"),
          ("class Empty: pass", "minimal class"), ("if cond: pass", "skip a branch")],
         ["if-elif-else", "for-loops", "functions"]),

        ("match-case", "match / case (3.10+)",
         "Structural pattern matching. Like switch in other languages, but with destructuring of lists, tuples, dicts, and classes.",
         "match command.split():\n    case ['go', direction]:\n        move(direction)\n    case ['take', *items]:\n        pickup(items)\n    case _:\n        print('???')",
         [("3.10+", "newish feature"), ("|", "match multiple"),
          ("[*x]", "rest pattern"), ("case _", "default"),
          ("class patterns", "Point(x=0, y=y)"), ("guards", "case x if x > 0:")],
         ["if-elif-else", "tuples", "classes"]),
    ]),

    ("03-data-structures", "Stage 3 · Data Structures", [
        ("lists", "Lists",
         "Ordered, mutable sequence. The workhorse collection. Indexing, slicing, appending all built in.",
         "items = ['sword', 'shield', 'potion']\nitems.append('bow')\nitems[0]            # 'sword'\nitems[-1]           # 'bow'\nlen(items)          # 4",
         [("[ ]", "literal"), ("ordered", "preserves insert order"),
          ("mutable", "change in place"), ("indexable", "items[0]"),
          ("slicable", "items[1:3]"), ("nestable", "lists of lists")],
         ["list-methods", "tuples", "slicing"]),

        ("list-methods", "List methods",
         "append, extend, insert, pop, remove, sort, reverse, index, count. Most mutate in place — be careful.",
         "x = [3, 1, 2]\nx.append(4)     # [3,1,2,4]\nx.sort()        # [1,2,3,4]\nx.pop()         # returns 4\nx.reverse()     # in place\nx.index(2)      # 1",
         [("append(x)", "add one"), ("extend(iter)", "add many"),
          ("insert(i, x)", "at position"), ("pop(i=-1)", "remove + return"),
          ("sort()", "in place"), ("sorted(x)", "new list")],
         ["lists", "comprehensions", "sorting-algorithms"]),

        ("tuples", "Tuples",
         "Ordered, immutable sequence. Like a frozen list. Useful for fixed records and dict keys.",
         "point = (3, 5)\nrgb = (255, 0, 128)\nx, y = point     # unpacking\nsingle = (5,)    # trailing comma!",
         [("( )", "literal"), ("immutable", "can't change"),
          ("hashable", "if items are"), ("unpacking", "a, b = tup"),
          ("named", "via namedtuple"), ("returns", "common for multi-return")],
         ["lists", "namedtuple", "dataclasses"]),

        ("sets", "Sets",
         "Unordered collection of unique items. Fast membership tests. Math-set operations supported.",
         "a = {1, 2, 3, 2}    # {1, 2, 3}\nb = {3, 4, 5}\na | b              # union\na & b              # intersection\na - b              # difference\n4 in b             # True",
         [("{ }", "literal (not empty!)"), ("set()", "empty set"),
          ("unique", "duplicates removed"), ("unordered", "no indexing"),
          ("O(1) lookup", "hash table"), ("set ops", "| & - ^")],
         ["lists", "frozensets", "hash-table"]),

        ("frozensets", "Frozensets",
         "Immutable version of set. Hashable, so usable as dict key or member of another set.",
         "fs = frozenset([1, 2, 3])\nfs.add(4)   # AttributeError!\n\nlookup = {fs: 'first three'}",
         [("immutable", "can't add/remove"), ("hashable", "use as dict key"),
          ("from iterable", "frozenset([...])"), ("set methods", "without mutation"),
          ("ops still work", "| & -"), ("perf same", "O(1) lookup")],
         ["sets", "tuples", "hash-table"]),

        ("dictionaries", "Dictionaries",
         "Unordered (insertion-ordered since 3.7) key-value pairs. Fast lookup by key. The most used Python collection.",
         "p = {'name': 'pikachu', 'hp': 35}\np['hp']              # 35\np.get('type', '?')   # 'electric' or '?'\np['lvl'] = 12        # add\n'name' in p          # True",
         [("{k: v}", "literal"), ("keys", "unique + hashable"),
          ("values", "anything"), ("get(k, default)", "safe lookup"),
          ("O(1) lookup", "hash table"), ("ordered", "insertion order")],
         ["dict-methods", "sets", "json"]),

        ("dict-methods", "Dict methods",
         "keys, values, items for iteration. update for merging. setdefault for lazy init. pop for remove+return.",
         "d = {'a': 1, 'b': 2}\nfor k, v in d.items():\n    print(k, v)\n\nd.update({'c': 3})\nd.setdefault('d', []).append(1)\nd.pop('a')",
         [("keys()", "view of keys"), ("values()", "view of values"),
          ("items()", "view of pairs"), ("update()", "merge another dict"),
          ("setdefault()", "get or init"), ("pop(k)", "remove + return")],
         ["dictionaries", "collections-module", "for-loops"]),

        ("enumerate-zip", "enumerate + zip",
         "enumerate adds an index. zip pairs items from multiple iterables. Both are lazy iterators.",
         "for i, name in enumerate(names):\n    print(i, name)\n\nfor name, hp in zip(names, hps):\n    print(name, hp)\n\nlist(zip([1,2], ['a','b']))",
         [("enumerate(it)", "(index, value)"), ("zip(a, b)", "(a[i], b[i])"),
          ("zip stops", "at shortest"), ("zip_longest", "fills with None"),
          ("itertools", "more options"), ("lazy", "iterator not list")],
         ["for-loops", "iterators", "itertools"]),

        ("bytes-bytearray", "bytes + bytearray",
         "bytes is an immutable sequence of integers 0-255. bytearray is mutable. Used for binary data: files, network, encoding.",
         "data = b'hello'\ndata[0]              # 104 ('h')\nba = bytearray(data)\nba[0] = 72           # mutable\n\n'café'.encode('utf-8')  # bytes",
         [("b''", "bytes literal"), ("immutable", "bytes"),
          ("mutable", "bytearray"), ("encode/decode", "str ↔ bytes"),
          ("UTF-8 default", "for text"), ("binary files", "open(..., 'rb')")],
         ["strings", "file-io", "encoding"]),

        ("comprehensions", "List / Dict / Set comprehensions",
         "Build collections in one expression. Pythonic, readable, fast. Always preferred over for-loop + append for simple cases.",
         "squares = [x*x for x in range(10)]\nevens = [x for x in nums if x % 2 == 0]\nsqd = {x: x*x for x in range(5)}\nset_ = {c.lower() for c in text}",
         [("[x for x in it]", "list"), ("{k: v for ...}", "dict"),
          ("{x for x in it}", "set"), ("(x for x in it)", "generator!"),
          ("if filter", "conditional include"), ("nested", "for in for")],
         ["lists", "generators", "for-loops"]),

        ("slicing", "Slicing",
         "Access a sub-section of any sequence with [start:stop:step]. Negative indices count from end. Step can be negative.",
         "s = 'abcdefg'\ns[1:4]    # 'bcd'\ns[:3]     # 'abc'\ns[-3:]    # 'efg'\ns[::2]    # 'aceg' (every 2nd)\ns[::-1]   # 'gfedcba' (reverse)",
         [("[start:stop]", "stop excluded"), ("[::step]", "every step-th"),
          ("[-1]", "last item"), ("[::-1]", "reverse"),
          ("works on", "str list tuple bytes"), ("no error", "out of range ok")],
         ["lists", "strings", "tuples"]),

        ("collections-module", "collections module",
         "Bonus data structures: Counter (frequency map), defaultdict (auto-init), deque (fast both ends), OrderedDict, namedtuple.",
         "from collections import Counter, defaultdict, deque\n\nCounter('banana')          # {'a': 3, 'n': 2, 'b': 1}\ndd = defaultdict(list)\ndd['fav'].append('pika')\nq = deque(maxlen=10)",
         [("Counter", "frequency"), ("defaultdict", "auto-init missing"),
          ("deque", "fast appendleft + popleft"), ("OrderedDict", "less needed now"),
          ("namedtuple", "tuple with fields"), ("ChainMap", "stack of dicts")],
         ["dictionaries", "lists", "stdlib"]),
    ]),

    ("04-functions", "Stage 4 · Functions", [
        ("def", "Defining functions",
         "Functions are defined with def, take parameters, return values. First-class objects — pass them around like data.",
         "def greet(name):\n    return f'Hi, {name}!'\n\nprint(greet('Mina'))\n\n# functions are objects:\nf = greet\nprint(f('Kasim'))",
         [("def", "keyword"), ("return", "exit + value"),
          ("None return", "if no return statement"), ("first-class", "pass as arg"),
          ("snake_case", "naming"), ("one job", "each function")],
         ["arguments", "return", "scope-legb"]),

        ("arguments", "Positional + keyword args",
         "Positional args match by position. Keyword args match by name. Mix is allowed, positional must come first.",
         "def attack(target, power, crit=False):\n    ...\n\nattack(enemy, 50)\nattack(enemy, power=50, crit=True)\nattack(target=enemy, power=50)",
         [("positional", "by order"), ("keyword", "by name"),
          ("default", "name=value"), ("/", "positional-only"),
          ("*", "keyword-only"), ("clarity", "kwargs at call site")],
         ["default-args", "args-kwargs", "def"]),

        ("default-args", "Default arguments",
         "Default values are evaluated once at def time. Never use mutable defaults — they persist across calls.",
         "def greet(name='friend'):\n    return f'Hi, {name}'\n\n# DANGER:\ndef bad(items=[]):     # shared mutable!\n    items.append(1)\n    return items\n\n# FIX:\ndef good(items=None):\n    items = items or []",
         [("name=value", "in def line"), ("evaluated once", "at def"),
          ("no mutable default", "[] {} set() etc"), ("use None", "+ check inside"),
          ("immutable ok", "int str tuple"), ("call-site override", "any time")],
         ["arguments", "args-kwargs", "common-mistakes"]),

        ("args-kwargs", "*args + **kwargs",
         "*args collects extra positional args into a tuple. **kwargs collects extra keyword args into a dict. Unpacking in calls works the same.",
         "def total(*nums):\n    return sum(nums)\n\ntotal(1, 2, 3)       # 6\n\ndef make(**opts):\n    return opts\n\nmake(name='pika', hp=35)",
         [("*args", "extra positional"), ("**kwargs", "extra keyword"),
          ("names", "args, kwargs by convention"), ("unpack at call", "f(*lst, **d)"),
          ("any name", "*a / **k works"), ("flexible APIs", "common in libs")],
         ["arguments", "decorators", "default-args"]),

        ("return", "return",
         "return exits a function and returns a value. No return statement = returns None. Can return multiple values as tuple.",
         "def divmod_(a, b):\n    return a // b, a % b   # tuple\n\nq, r = divmod_(17, 5)\n\n# early return:\ndef safe(x):\n    if x is None:\n        return 'missing'\n    return x.upper()",
         [("return value", "exits + returns"), ("no return", "returns None"),
          ("multi-return", "comma = tuple"), ("early return", "guard clauses"),
          ("return None", "explicit"), ("can't return outside", "SyntaxError")],
         ["def", "tuples", "args-kwargs"]),

        ("lambda", "Lambda — anonymous functions",
         "Single-expression unnamed functions. Useful as throwaway callbacks for sort, map, filter, etc. Don't overuse.",
         "double = lambda x: x * 2\n\nnames.sort(key=lambda p: p.hp)\nlist(map(lambda x: x*x, range(5)))\nlist(filter(lambda x: x > 0, nums))",
         [("lambda args: expr", "single expression"), ("no statements", "expr only"),
          ("anonymous", "no name needed"), ("callback use", "sort, map, filter"),
          ("often overused", "def is clearer"), ("no docstring", "less debuggable")],
         ["def", "functional-programming", "decorators"]),

        ("scope-legb", "Scope — LEGB",
         "Python resolves names in order: Local, Enclosing, Global, Builtin. nonlocal modifies enclosing. global modifies module-level.",
         "x = 'global'\n\ndef outer():\n    x = 'enclosing'\n    def inner():\n        nonlocal x\n        x = 'local'\n    inner()\n    print(x)   # 'local'",
         [("L", "local · inside function"), ("E", "enclosing · outer function"),
          ("G", "global · module-level"), ("B", "builtin · print, len, etc"),
          ("nonlocal", "modify enclosing"), ("global", "modify module-level")],
         ["closures", "def", "modules"]),

        ("closures", "Closures",
         "An inner function that remembers variables from its enclosing scope, even after the outer function returns.",
         "def counter():\n    n = 0\n    def tick():\n        nonlocal n\n        n += 1\n        return n\n    return tick\n\nc = counter()\nc(); c(); c()   # 1 2 3",
         [("inner fn", "captures outer vars"), ("survives", "outer return"),
          ("nonlocal", "to modify"), ("alternative", "to classes for state"),
          ("decorator basis", "decorators use closures"), ("functional style", "common pattern")],
         ["scope-legb", "decorators", "lambda"]),
    ]),

    ("05-modules-packages", "Stage 5 · Modules + Packages", [
        ("import", "import",
         "Bring code from another module into the current namespace. One .py file = one module. Standard imports go at top.",
         "import math\nmath.sqrt(16)         # 4.0\n\nimport pokedex\npokedex.POKEMON[7]\n\nimport very.long.name as short",
         [("import x", "whole module"), ("as", "rename"),
          ("at top", "PEP 8"), ("relative", "from . import sibling"),
          ("absolute preferred", "over relative"), ("sys.path", "search path")],
         ["from-import", "custom-modules", "init-py"]),

        ("from-import", "from ... import",
         "Pull specific names directly into current namespace. Avoid * imports — they hide where names came from.",
         "from math import sqrt, pi\nsqrt(16)        # no math. prefix\n\nfrom .utils import helper   # relative\nfrom typing import (\n    Optional, List, Dict,\n)",
         [("from x import y", "selective"), ("import *", "avoid"),
          ("multi-line", "parens for grouping"), ("rename", "from x import y as z"),
          ("relative", "from .module import"), ("avoid clashes", "be specific")],
         ["import", "custom-modules", "namespaces"]),

        ("custom-modules", "Custom modules",
         "Any .py file you can import is a module. Group related code together, expose a clean API at the top.",
         "# pokemon.py\ndef create(name, hp):\n    return {'name': name, 'hp': hp}\n\n# main.py\nimport pokemon\np = pokemon.create('Pika', 35)",
         [("any .py", "is a module"), ("filename", "becomes module name"),
          ("same folder", "or on sys.path"), ("__name__", "lets you check"),
          ("entry point", "if __name__ == '__main__'"), ("API design", "decide public vs private")],
         ["import", "init-py", "main-guard"]),

        ("init-py", "__init__.py",
         "Marks a directory as a package. Code in it runs on import. Use it to set up the package's public API.",
         "# mypkg/__init__.py\nfrom .core import main\nfrom .utils import helper\n\n__version__ = '0.1.0'\n__all__ = ['main', 'helper']",
         [("makes a package", "vs plain folder"), ("runs on import", "of the package"),
          ("__all__", "controls from x import *"), ("__version__", "common convention"),
          ("empty ok", "even empty file works"), ("namespace pkgs", "no __init__.py since 3.3")],
         ["custom-modules", "import", "package-managers"]),

        ("main-guard", "__main__ guard",
         "if __name__ == '__main__' lets code run when called as a script but skip on import. Crucial for testable modules.",
         "def main():\n    print('run!')\n\nif __name__ == '__main__':\n    main()",
         [("script vs module", "two modes"), ("on import", "skipped"),
          ("on direct run", "executed"), ("python -m pkg", "runs __main__.py"),
          ("test friendly", "no side effects on import"), ("CLI entry", "common pattern")],
         ["custom-modules", "import", "argparse"]),

        ("pip", "pip",
         "Python's default package installer. Pulls packages from PyPI (or a local index). Comes with every modern Python.",
         "$ pip install requests\n$ pip install 'fastapi>=0.110'\n$ pip install -r requirements.txt\n$ pip uninstall requests\n$ pip list",
         [("install", "pip install x"), ("uninstall", "pip uninstall x"),
          ("upgrade", "pip install -U x"), ("freeze", "pip freeze > req.txt"),
          ("from file", "pip install -r req.txt"), ("python -m pip", "explicit version")],
         ["pypi", "virtual-envs", "requirements-txt"]),

        ("pypi", "PyPI",
         "The Python Package Index — 500,000+ open source libraries. Check downloads, last release, and maintainers before trusting one.",
         "# search: pypi.org/search\n# package page: pypi.org/project/requests\n# publish your own with twine + pyproject.toml",
         [("pypi.org", "central index"), ("search", "by name or tag"),
          ("trust signals", "downloads · maintainers"), ("license", "always check"),
          ("publish", "twine upload dist/*"), ("private indexes", "internal companies")],
         ["pip", "poetry", "uv"]),

        ("virtual-envs", "Virtual environments",
         "Isolated Python installs per project. Avoids 'works on my machine' hell. Always use one.",
         "$ python -m venv .venv\n$ source .venv/bin/activate   # mac/linux\n$ .venv\\Scripts\\activate     # windows\n$ pip install requests\n$ deactivate",
         [("venv module", "stdlib · always works"), ("one per project", "isolated deps"),
          ("activate", "shell-specific"), (".venv folder", "common convention"),
          ("gitignore", "don't commit"), ("uv venv", "faster alternative")],
         ["pip", "pyenv", "requirements-txt"]),

        ("requirements-txt", "requirements.txt",
         "Plain-text list of packages your project needs. Anyone can pip install -r requirements.txt to match.",
         "# requirements.txt\nrequests==2.31.0\nfastapi>=0.110\nnumpy~=1.26\n\n# pin everything in lockfile:\npip freeze > requirements.txt",
         [("pin versions", "for reproducibility"), ("==", "exact"),
          (">=", "minimum"), ("~=", "compatible"),
          ("freeze", "pip freeze > req.txt"), ("dev vs prod", "separate files")],
         ["pip", "poetry", "uv"]),

        ("poetry", "Poetry",
         "Modern Python project manager. Handles deps, venvs, building, publishing — all from pyproject.toml.",
         "$ poetry new myapp\n$ poetry add requests\n$ poetry install\n$ poetry run python main.py\n$ poetry build && poetry publish",
         [("pyproject.toml", "single config"), ("poetry.lock", "exact versions"),
          ("manages venv", "automatically"), ("publishes", "to PyPI"),
          ("groups", "dev / test / prod"), ("alternatives", "uv, pdm, hatch")],
         ["pyproject-toml", "uv", "pdm"]),

        ("uv", "uv",
         "Astral's ultra-fast Python package + project manager (Rust-based, 2024). Drop-in replacement for pip + venv + poetry, but 10-100x faster.",
         "$ uv venv\n$ uv pip install requests\n$ uv add fastapi\n$ uv run python main.py\n$ uv python install 3.12",
         [("Rust-based", "extremely fast"), ("compat", "pip-compatible"),
          ("uv pip", "drop-in for pip"), ("uv add", "project mode"),
          ("manages Python", "uv python install"), ("rising default", "2024+ choice")],
         ["pip", "poetry", "virtual-envs"]),

        ("conda", "Conda",
         "Package manager from Anaconda. Strong in data science — handles non-Python deps (CUDA, BLAS, etc) that pip can't.",
         "$ conda create -n ml python=3.12\n$ conda activate ml\n$ conda install numpy pandas\n$ conda env export > env.yml",
         [("non-Python deps", "C libs · CUDA · MKL"), ("mini vs full", "miniconda is small"),
          ("channels", "conda-forge etc"), ("env.yml", "share environment"),
          ("slow", "vs pip · use mamba"), ("data science", "common in science")],
         ["pip", "virtual-envs", "uv"]),
    ]),

    ("06-stdlib", "Stage 6 · Standard Library", [
        ("os", "os",
         "Interact with the operating system: env vars, processes, paths. Use pathlib for file paths instead, in modern code.",
         "import os\nos.getcwd()\nos.environ['HOME']\nos.makedirs('a/b/c', exist_ok=True)\nos.remove('file.txt')\nos.system('ls')",
         [("getcwd", "current dir"), ("environ", "env vars"),
          ("makedirs", "mkdir -p"), ("remove", "delete file"),
          ("os.path", "old path API"), ("use pathlib", "modern alternative")],
         ["sys", "pathlib", "subprocess"]),

        ("sys", "sys",
         "Talk to the Python interpreter: command-line args, stdout/stderr, path, version, exit.",
         "import sys\nsys.argv             # ['script.py', 'arg1']\nsys.exit(1)\nsys.path             # import search path\nsys.stdout.write('hi\\n')\nsys.version",
         [("argv", "cli args"), ("exit", "with code"),
          ("path", "module search"), ("stdout / stderr", "streams"),
          ("version", "Python version"), ("platform", "windows/linux/darwin")],
         ["os", "argparse", "main-guard"]),

        ("pathlib", "pathlib",
         "Object-oriented file paths. Replaces most of os.path. Use this in new code — it's much cleaner.",
         "from pathlib import Path\np = Path('data/file.txt')\np.exists()\np.read_text()\np.write_text('hello')\np.parent\np.suffix\np.with_suffix('.bak')",
         [("Path()", "construct"), ("/", "join: Path('a') / 'b'"),
          ("read_text / write_text", "simple I/O"), ("exists / is_file / is_dir", "checks"),
          ("glob / rglob", "find files"), (".parent .name .suffix", "parts")],
         ["os", "file-io", "glob"]),

        ("json", "json",
         "Read and write JSON. Most common interchange format. Built-in, no install.",
         "import json\nd = {'name': 'pika', 'hp': 35}\ns = json.dumps(d)\njson.loads(s)\n\nwith open('data.json') as f:\n    data = json.load(f)",
         [("dumps", "dict → str"), ("loads", "str → dict"),
          ("dump", "dict → file"), ("load", "file → dict"),
          ("indent=2", "pretty print"), ("default=", "custom serializer")],
         ["pydantic", "file-io", "yaml"]),

        ("csv", "csv",
         "Read and write CSV. Handle quoting and dialects. For anything complex, use pandas instead.",
         "import csv\nwith open('data.csv') as f:\n    for row in csv.DictReader(f):\n        print(row['name'])\n\nwith open('out.csv', 'w') as f:\n    w = csv.writer(f)\n    w.writerow(['a','b','c'])",
         [("reader / writer", "list-based"), ("DictReader / DictWriter", "dict-based"),
          ("newline=''", "open with this"), ("delimiter", "default ','"),
          ("dialect", "excel · unix · custom"), ("for big data", "use pandas")],
         ["pandas", "json", "file-io"]),

        ("datetime", "datetime",
         "Dates and times with timezone support. Always store UTC. Convert to local only for display.",
         "from datetime import datetime, timedelta, timezone\nnow = datetime.now(timezone.utc)\ntomorrow = now + timedelta(days=1)\nnow.isoformat()\ndatetime.fromisoformat('2025-01-01T00:00:00+00:00')",
         [("datetime", "date + time"), ("date / time", "separate"),
          ("timedelta", "difference"), ("timezone", "tz-aware always"),
          ("strftime / strptime", "format / parse"), ("ISO 8601", "preferred format")],
         ["time", "calendar", "zoneinfo"]),

        ("time", "time",
         "Lower-level timing: sleep, perf_counter for benchmarks, timestamps. For real dates, use datetime.",
         "import time\ntime.sleep(0.5)\nstart = time.perf_counter()\ndo_work()\nelapsed = time.perf_counter() - start\nts = time.time()      # epoch seconds",
         [("sleep(s)", "pause"), ("time()", "epoch seconds"),
          ("perf_counter", "high-res benchmark"), ("monotonic", "never goes back"),
          ("ctime / strftime", "format"), ("vs datetime", "lower level")],
         ["datetime", "asyncio", "logging"]),

        ("math", "math",
         "Common math functions: sqrt, pi, sin, log, factorial. For arrays of numbers use NumPy.",
         "import math\nmath.sqrt(2)\nmath.pi\nmath.sin(math.pi / 2)\nmath.factorial(10)\nmath.log(100, 10)\nmath.inf",
         [("sqrt pow exp", "powers"), ("pi e tau", "constants"),
          ("sin cos tan", "trig (radians!)"), ("log log10 log2", "logs"),
          ("isnan isinf", "checks"), ("floor ceil trunc", "rounding")],
         ["numbers", "random", "numpy"]),

        ("random", "random",
         "Pseudo-random numbers and choices. For cryptography use secrets instead.",
         "import random\nrandom.random()              # [0.0, 1.0)\nrandom.randint(1, 10)         # 1-10 inclusive\nrandom.choice(['a','b','c'])\nrandom.shuffle(my_list)\nrandom.seed(42)",
         [("random()", "float 0-1"), ("randint(a, b)", "int incl"),
          ("choice / choices", "pick one or N"), ("sample", "pick without replacement"),
          ("shuffle", "in place"), ("seed", "reproducible")],
         ["math", "secrets", "numpy"]),

        ("re-regex", "re — regex",
         "Pattern matching for text. Powerful but cryptic. Use raw strings (r'...') to avoid backslash hell.",
         "import re\nre.search(r'\\d+', 'abc123def')   # match obj\nre.findall(r'\\w+', text)\nre.sub(r'\\s+', ' ', text)\np = re.compile(r'^(\\w+)@(.+)$')",
         [("r'...'", "raw string"), ("\\d \\w \\s", "digit · word · space"),
          ("+ * ?", "1+ · 0+ · 0-1"), ("( )", "capture group"),
          ("search / match / findall", "common"), ("compile", "reuse pattern")],
         ["strings", "string-methods", "validation"]),

        ("collections-stdlib", "collections (stdlib)",
         "Specialized container types: Counter, defaultdict, deque, namedtuple, OrderedDict, ChainMap.",
         "from collections import Counter, defaultdict, deque\n\nCounter('mississippi')\ndd = defaultdict(int)\ndd['x'] += 1\nq = deque(maxlen=100)",
         [("Counter", "frequency map"), ("defaultdict", "auto-init"),
          ("deque", "fast both ends"), ("namedtuple", "tuple with fields"),
          ("OrderedDict", "rarely needed now"), ("ChainMap", "stacked dicts")],
         ["dictionaries", "data-structures", "tuples"]),

        ("itertools", "itertools",
         "Lazy iterator combinators: chain, cycle, repeat, product, permutations, combinations, groupby, islice.",
         "from itertools import chain, product, groupby\n\nlist(chain([1,2], [3,4]))     # [1,2,3,4]\nlist(product('AB', '12'))      # all pairs\n[(k, list(g)) for k, g in groupby(sorted(data))]",
         [("chain", "stitch iterables"), ("product", "cartesian"),
          ("permutations", "all orderings"), ("combinations", "without order"),
          ("groupby", "cluster runs"), ("islice", "lazy slicing")],
         ["functools", "iterators", "for-loops"]),
    ]),

    ("07-file-io", "Stage 7 · Files + I/O", [
        ("open-read", "Reading files",
         "open() returns a file object. read(), readline(), or iterate line-by-line. Always close (or use with).",
         "with open('data.txt') as f:\n    text = f.read()\n\nwith open('data.txt') as f:\n    for line in f:\n        print(line.rstrip())",
         [("'r'", "default · read text"), ("'rb'", "read binary"),
          ("read()", "whole file"), ("readline()", "one line"),
          ("for line in f", "line by line · memory-cheap"), ("encoding='utf-8'", "be explicit")],
         ["with-statement", "open-write", "pathlib"]),

        ("open-write", "Writing files",
         "Open with 'w' to write (overwrites), 'a' to append. Always use with to auto-close.",
         "with open('out.txt', 'w') as f:\n    f.write('hello\\n')\n    f.writelines(['a\\n', 'b\\n'])\n\nwith open('log.txt', 'a') as f:\n    f.write('new line\\n')",
         [("'w'", "write · overwrites"), ("'a'", "append"),
          ("'x'", "exclusive create · fails if exists"), ("write()", "one chunk"),
          ("writelines()", "iterable"), ("encoding='utf-8'", "be explicit")],
         ["open-read", "with-statement", "pathlib"]),

        ("with-statement", "with statement",
         "Context managers handle setup + teardown. with open(...) auto-closes file even if exceptions happen.",
         "with open('data.txt') as f:\n    text = f.read()\n# file closed here, even on error\n\nwith open('a') as a, open('b') as b:\n    ...",
         [("with x as y:", "syntax"), ("auto cleanup", "even on exceptions"),
          ("multi-context", "with a, b:"), ("not just files", "locks, connections, etc"),
          ("contextlib", "make your own"), ("@contextmanager", "decorator style")],
         ["context-managers", "open-read", "exceptions"]),

        ("binary-files", "Binary files",
         "Open with 'rb' / 'wb' to read/write bytes (images, archives, audio). No automatic encoding.",
         "with open('img.png', 'rb') as f:\n    data = f.read()\n\nwith open('copy.png', 'wb') as f:\n    f.write(data)",
         [("'rb'", "read bytes"), ("'wb'", "write bytes"),
          ("no encoding", "raw bytes"), ("bytes type", "vs str"),
          ("seek / tell", "move within file"), ("for media", "images, audio, archives")],
         ["bytes-bytearray", "open-read", "pathlib"]),
    ]),

    ("08-error-handling", "Stage 8 · Errors + Exceptions", [
        ("try-except", "try / except",
         "Catch errors before they crash your program. Be specific about which exception types you handle.",
         "try:\n    age = int(input('Age? '))\nexcept ValueError:\n    print('Need a number!')\nexcept Exception as e:\n    print(f'Unexpected: {e}')",
         [("try:", "wrap risky code"), ("except X:", "catch one type"),
          ("except (A, B):", "multiple"), ("as e", "bind to name"),
          ("be specific", "avoid bare except"), ("don't silence", "log it at least")],
         ["finally", "raise", "custom-exceptions"]),

        ("finally", "finally + else",
         "finally always runs (success or failure). else runs only if no exception. Use finally for cleanup.",
         "try:\n    f = open('x.txt')\nexcept FileNotFoundError:\n    print('missing')\nelse:\n    print('opened')\nfinally:\n    print('done')",
         [("finally", "always runs"), ("else", "only on success"),
          ("for cleanup", "close files, connections"), ("with stmt", "often better"),
          ("return in finally", "wins over try return"), ("exception in finally", "suppresses original")],
         ["try-except", "with-statement", "context-managers"]),

        ("raise", "raise",
         "Throw an exception explicitly. Use raise ... from to chain. Re-raise inside except with bare raise.",
         "if age < 0:\n    raise ValueError('age must be positive')\n\ntry:\n    do_thing()\nexcept LookupError as e:\n    raise RuntimeError('init failed') from e",
         [("raise X(msg)", "throw"), ("raise", "re-raise current"),
          ("raise ... from e", "chain causes"), ("from None", "suppress chain"),
          ("typical types", "ValueError, TypeError, RuntimeError"), ("don't raise Exception", "too broad")],
         ["try-except", "custom-exceptions", "logging"]),

        ("custom-exceptions", "Custom exceptions",
         "Subclass Exception (or a more specific one) for your library's errors. Gives callers a clean catch target.",
         "class GameError(Exception):\n    pass\n\nclass OutOfMana(GameError):\n    def __init__(self, needed, have):\n        super().__init__(f'need {needed}, have {have}')\n        self.needed = needed",
         [("subclass Exception", "or specific"), ("hierarchy", "your own tree"),
          ("__init__", "add context fields"), ("from None", "if chain unhelpful"),
          ("library convention", "BaseError per package"), ("doc them", "in API docs")],
         ["raise", "classes", "inheritance"]),
    ]),

    ("09-oop", "Stage 9 · Object-Oriented Programming", [
        ("classes", "Classes",
         "Blueprints for objects. Define attributes and behavior. Instantiate with ClassName(args).",
         "class Pokemon:\n    def __init__(self, name, hp):\n        self.name = name\n        self.hp = hp\n\npika = Pokemon('Pikachu', 35)\npika.name      # 'Pikachu'",
         [("class Name:", "PascalCase"), ("def __init__", "constructor"),
          ("self", "first arg of methods"), ("instances", "ClassName(...)"),
          ("attributes", "self.x = y"), ("methods", "functions on the class")],
         ["instances", "methods", "dunder-init"]),

        ("instances", "Instances + Attributes",
         "Class attributes are shared. Instance attributes are per-object. Be careful with mutable class attrs.",
         "class Dog:\n    species = 'Canis lupus'   # class attr\n    def __init__(self, name):\n        self.name = name      # instance attr\n\nDog.species\nDog('Rex').name",
         [("class attr", "shared by all"), ("instance attr", "per object"),
          ("self.x = y", "instance"), ("ClassName.x = y", "class"),
          ("mutable class attr", "danger! shared mutation"), ("__dict__", "all attrs of instance")],
         ["classes", "methods", "dunder-init"]),

        ("methods", "Methods",
         "Functions defined inside a class. First arg is self (the instance). Bound methods know their object.",
         "class Counter:\n    def __init__(self):\n        self.n = 0\n    def tick(self):\n        self.n += 1\n    def value(self):\n        return self.n\n\nc = Counter()\nc.tick(); c.tick()\nc.value()  # 2",
         [("self", "first arg always"), ("bound method", "obj.method"),
          ("staticmethod", "@staticmethod"), ("classmethod", "@classmethod cls arg"),
          ("instance method", "default kind"), ("method resolution", "MRO for inheritance")],
         ["classes", "static-class-methods", "inheritance"]),

        ("dunder-init", "__init__ — constructor",
         "Special method called when you instantiate. Set up initial state here. self is the new instance.",
         "class Battle:\n    def __init__(self, p1, p2, weather='clear'):\n        self.p1 = p1\n        self.p2 = p2\n        self.weather = weather\n        self.turn = 1",
         [("called on creation", "ClassName(...) → __init__"),
          ("set up state", "all instance attrs"),
          ("self", "the new instance"),
          ("can take args + defaults", "like normal funcs"),
          ("returns None", "implicit"),
          ("vs __new__", "rare · __new__ for immutable")],
         ["classes", "dunder-methods", "dataclasses"]),

        ("dunder-methods", "Dunder (__magic__) methods",
         "Python calls these automatically: __str__ for print, __eq__ for ==, __len__ for len(), __iter__ for for-loops.",
         "class Pokemon:\n    def __init__(self, name): self.name = name\n    def __str__(self):  return self.name\n    def __eq__(self, o): return self.name == o.name\n    def __repr__(self): return f'Pokemon({self.name!r})'",
         [("__str__", "user-facing print"), ("__repr__", "debug print"),
          ("__eq__", "=="), ("__lt__", "<"),
          ("__len__", "len()"), ("__iter__ __next__", "for loops")],
         ["dunder-init", "operators", "classes"]),

        ("inheritance", "Inheritance",
         "Subclasses inherit from parents. super() calls the parent's method. Prefer composition over deep hierarchies.",
         "class Animal:\n    def speak(self): return 'noise'\n\nclass Dog(Animal):\n    def speak(self): return 'woof'\n    def fetch(self): ...\n\nDog().speak()    # 'woof'\nDog().fetch()    # ok",
         [("class Child(Parent)", "syntax"), ("super()", "parent method"),
          ("override", "redefine method"), ("is-a relationship", "Dog IS Animal"),
          ("isinstance(obj, Cls)", "check"), ("issubclass", "type check")],
         ["multiple-inheritance", "polymorphism", "composition"]),

        ("multiple-inheritance", "Multiple Inheritance + MRO",
         "Python supports multiple parents. Order matters — MRO (Method Resolution Order) decides which method wins.",
         "class A:\n    def hi(self): return 'A'\nclass B(A):\n    def hi(self): return 'B'\nclass C(A):\n    def hi(self): return 'C'\nclass D(B, C): pass\n\nD().hi()       # 'B'\nD.__mro__",
         [("class D(B, C)", "syntax"), ("MRO", "Method Resolution Order"),
          ("__mro__", "see the order"), ("C3 linearization", "the algorithm"),
          ("mixins", "common pattern"), ("diamond problem", "avoided by MRO")],
         ["inheritance", "abstract-classes", "composition"]),

        ("polymorphism", "Polymorphism + Duck Typing",
         "Different types respond to the same method name. Python doesn't care about types as long as the method exists.",
         "class Dog:\n    def speak(self): return 'woof'\nclass Cat:\n    def speak(self): return 'meow'\n\nfor a in [Dog(), Cat()]:\n    print(a.speak())",
         [("same method", "different types"), ("duck typing", "if it quacks like a duck..."),
          ("no inheritance needed", "in Python"), ("protocols", "typed duck typing"),
          ("formal alternative", "abstract base classes"), ("Pythonic", "core idea")],
         ["inheritance", "protocols", "abstract-classes"]),

        ("encapsulation", "Encapsulation",
         "Hide internal details. Python uses naming convention (_private, __mangled) — no real private. Trust + community.",
         "class Account:\n    def __init__(self, balance):\n        self._balance = balance    # convention: private\n        self.__secret = 'xyz'      # name-mangled\n    def get(self):\n        return self._balance",
         [("_name", "convention: don't touch"), ("__name", "name-mangled (rare)"),
          ("@property", "read-only attrs"), ("getter/setter", "via @property"),
          ("we are adults", "Python's philosophy"), ("__dict__", "shows everything anyway")],
         ["properties", "classes", "abstraction"]),

        ("abstract-classes", "Abstract base classes (ABC)",
         "Force subclasses to implement methods. Use abc.ABC + @abstractmethod when you need to declare an interface.",
         "from abc import ABC, abstractmethod\n\nclass Shape(ABC):\n    @abstractmethod\n    def area(self): ...\n\nclass Circle(Shape):\n    def __init__(self, r): self.r = r\n    def area(self): return 3.14 * self.r**2",
         [("from abc import", "ABC, abstractmethod"), ("can't instantiate ABC", "must subclass"),
          ("@abstractmethod", "must override"), ("vs Protocols", "stricter, less flexible"),
          ("interface-like", "design contracts"), ("nominal typing", "vs duck typing")],
         ["protocols", "inheritance", "polymorphism"]),

        ("properties", "@property",
         "Looks like an attribute, runs as a method. Use for computed values or validated access.",
         "class Circle:\n    def __init__(self, r): self._r = r\n    @property\n    def area(self): return 3.14 * self._r**2\n    @area.setter\n    def area(self, val):\n        raise AttributeError('read-only')",
         [("@property", "getter"), ("@x.setter", "setter"),
          ("@x.deleter", "deleter"), ("no parens", "at call site"),
          ("computed attrs", "cache if expensive"), ("validated input", "in setter")],
         ["classes", "encapsulation", "dataclasses"]),

        ("dataclasses", "@dataclass",
         "Auto-generate __init__, __repr__, __eq__ from class annotations. Less boilerplate, same power.",
         "from dataclasses import dataclass, field\n\n@dataclass\nclass Pokemon:\n    name: str\n    hp: int = 100\n    moves: list = field(default_factory=list)",
         [("@dataclass", "decorator"), ("annotations", "name: type"),
          ("auto __init__", "generated"), ("auto __repr__", "useful for debug"),
          ("field(default_factory=...)", "mutable defaults"), ("frozen=True", "immutable")],
         ["classes", "type-hints", "dunder-init"]),
    ]),

    ("10-advanced", "Stage 10 · Advanced Python", [
        ("iterators", "Iterators",
         "Anything with __iter__ + __next__. for loops use them under the hood. Roll your own for custom traversal.",
         "class Count:\n    def __init__(self, stop): self.i, self.stop = 0, stop\n    def __iter__(self): return self\n    def __next__(self):\n        if self.i >= self.stop: raise StopIteration\n        self.i += 1\n        return self.i - 1",
         [("__iter__", "returns self typically"),
          ("__next__", "returns next value"),
          ("StopIteration", "signals end"),
          ("for-loops use these", "implicitly"),
          ("iter() / next()", "manual control"),
          ("generators easier", "yield keyword")],
         ["generators", "for-loops", "dunder-methods"]),

        ("generators", "Generators",
         "Functions with yield. Pause + resume, producing values lazily. Memory-cheap alternative to lists.",
         "def count(n):\n    i = 0\n    while i < n:\n        yield i\n        i += 1\n\nfor x in count(5):\n    print(x)",
         [("yield", "pause + emit"), ("lazy", "computed on demand"),
          ("memory-cheap", "one value at a time"), ("send / throw", "advanced control"),
          ("generator expression", "(x for x in ...)"), ("from yield", "delegate to sub-gen")],
         ["iterators", "comprehensions", "asyncio"]),

        ("decorators", "Decorators",
         "Functions that wrap functions. @name above def applies a decorator. Used for caching, logging, auth, retries.",
         "def log(fn):\n    def wrapper(*args, **kw):\n        print(f'calling {fn.__name__}')\n        return fn(*args, **kw)\n    return wrapper\n\n@log\ndef attack(target): ...",
         [("@name", "syntax"), ("function in, function out", "concept"),
          ("functools.wraps", "preserve metadata"),
          ("with args", "extra wrapper layer"),
          ("class decorators", "also possible"),
          ("examples: @cache @property", "common")],
         ["closures", "functools", "args-kwargs"]),

        ("context-managers", "Context managers",
         "Objects with __enter__ + __exit__. Used with with statement. Handle setup + teardown safely.",
         "from contextlib import contextmanager\n\n@contextmanager\ndef timer():\n    start = time.perf_counter()\n    yield\n    print(time.perf_counter() - start)\n\nwith timer():\n    slow_work()",
         [("__enter__", "setup"),
          ("__exit__", "teardown · runs even on errors"),
          ("with stmt", "uses them"),
          ("@contextmanager", "decorator helper"),
          ("nested", "with a, b:"),
          ("examples", "open · locks · transactions")],
         ["with-statement", "decorators", "exceptions"]),

        ("functools", "functools",
         "Higher-order utilities: cache, lru_cache, partial, reduce, wraps, singledispatch.",
         "from functools import cache, partial, reduce\n\n@cache\ndef fib(n):\n    if n < 2: return n\n    return fib(n-1) + fib(n-2)\n\nadd5 = partial(operator.add, 5)\nreduce(operator.mul, [1,2,3,4])",
         [("@cache", "memoize (no limit)"), ("@lru_cache(maxsize=N)", "bounded cache"),
          ("partial(fn, x)", "fix args"), ("reduce", "fold a list"),
          ("@wraps", "preserve metadata"), ("singledispatch", "type-based dispatch")],
         ["decorators", "lambda", "itertools"]),

        ("walrus", "Walrus := (3.8+)",
         "Assign inside an expression. Useful in while loops and comprehensions. Don't overuse — can hurt readability.",
         "while (chunk := f.read(1024)):\n    process(chunk)\n\nif (n := len(items)) > 10:\n    print(f'too big: {n}')",
         [(":=", "assign + return"), ("3.8+", "newish"),
          ("inside expressions", "if · while · listcomp"),
          ("avoid overuse", "can be unclear"),
          ("common pattern", "while-read loops"),
          ("scoping", "leaks into outer scope")],
         ["operators", "if-elif-else", "while-loops"]),

        ("type-hints", "Type hints",
         "Optional annotations that describe types. Python itself ignores them — tools (mypy, pyright, IDEs) use them.",
         "def greet(name: str, age: int = 0) -> str:\n    return f'{name} is {age}'\n\nfrom typing import Optional, List, Dict\nx: List[int] = [1, 2, 3]\ny: Optional[str] = None",
         [("name: type", "param hints"), ("-> type", "return hint"),
          ("Optional[X]", "X or None"), ("List Dict Tuple", "from typing"),
          ("3.9+", "list dict directly"), ("Union[A,B] or A|B", "either type")],
         ["mypy", "protocols", "dataclasses"]),

        ("protocols", "Protocols — structural typing",
         "Define an interface by methods/attrs, not inheritance. Like duck typing, but checked by mypy.",
         "from typing import Protocol\n\nclass Speakable(Protocol):\n    def speak(self) -> str: ...\n\ndef shout(s: Speakable):\n    print(s.speak().upper())",
         [("Protocol", "structural typing"), ("no inheritance", "needed"),
          ("duck-typed but checked", "by mypy"), ("@runtime_checkable", "for isinstance"),
          ("vs ABC", "more flexible"), ("3.8+", "in typing")],
         ["type-hints", "abstract-classes", "polymorphism"]),

        ("pattern-matching", "Pattern matching (match/case)",
         "Like switch in other languages, but with destructuring. Match lists, tuples, dicts, classes, all in one syntax.",
         "match cmd.split():\n    case ['quit'] | ['exit']:\n        bye()\n    case ['go', direction]:\n        move(direction)\n    case ['take', *items] if items:\n        pickup(items)",
         [("match x:", "switch"), ("case pat:", "branch"),
          ("|", "OR patterns"), ("*rest", "rest pattern"),
          ("if guard", "extra condition"), ("3.10+", "newer feature")],
         ["if-elif-else", "tuples", "classes"]),

        ("metaclasses", "Metaclasses",
         "Classes whose instances are other classes. Rare — usually frameworks. type() is the default metaclass.",
         "class Meta(type):\n    def __new__(mcs, name, bases, ns):\n        ns['hello'] = lambda self: 'hi'\n        return super().__new__(mcs, name, bases, ns)\n\nclass MyClass(metaclass=Meta): pass",
         [("classes are objects", "of type 'type'"),
          ("metaclass=Meta", "class declaration"),
          ("__new__", "create the class"),
          ("frameworks use these", "Django ORM, ABC, etc"),
          ("rare in app code", "almost always overkill"),
          ("alternatives", "decorators · __init_subclass__")],
         ["classes", "decorators", "inheritance"]),
    ]),

    ("11-dsa", "Stage 11 · Data Structures + Algorithms", [
        ("big-o", "Big-O notation",
         "How runtime grows with input size. O(1) constant, O(log n) halving, O(n) linear, O(n²) quadratic.",
         "# O(1) — hash lookup\nd[key]\n\n# O(n) — scan\nfor x in list_: ...\n\n# O(n²) — nested\nfor a in list_:\n    for b in list_: ...",
         [("O(1)", "instant · dict lookup"), ("O(log n)", "binary search"),
          ("O(n)", "scan a list"), ("O(n log n)", "good sort"),
          ("O(n²)", "nested loops"), ("O(2^n)", "brute recursion")],
         ["sorting-algorithms", "hash-table", "recursion-dp"]),

        ("stack", "Stack — LIFO",
         "Last-In First-Out. Python lists work as stacks: append + pop. Used for undo, parsing, function calls.",
         "stack = []\nstack.append(1)\nstack.append(2)\nstack.pop()   # 2\nstack.pop()   # 1",
         [("LIFO", "last in, first out"), ("append + pop", "O(1) both"),
          ("undo / redo", "classic use"), ("expression parsing", "balanced parens"),
          ("function calls", "the call stack"), ("alt: deque", "or LifoQueue")],
         ["queue", "lists", "recursion-dp"]),

        ("queue", "Queue — FIFO",
         "First-In First-Out. Use collections.deque (lists are slow at the front). BFS uses queues.",
         "from collections import deque\nq = deque()\nq.append('a')\nq.append('b')\nq.popleft()   # 'a'",
         [("FIFO", "first in, first out"),
          ("deque", "fast popleft"),
          ("avoid list.pop(0)", "O(n)!"),
          ("BFS uses queue", "graph traversal"),
          ("queue.Queue", "thread-safe"),
          ("asyncio.Queue", "for async")],
         ["stack", "bfs-dfs", "collections-stdlib"]),

        ("linked-list", "Linked list",
         "Sequence of nodes, each pointing to the next. O(1) insert/remove at head, O(n) random access. Python lists are arrays, not linked.",
         "class Node:\n    def __init__(self, val):\n        self.val = val\n        self.next = None\n\nhead = Node(1)\nhead.next = Node(2)\nhead.next.next = Node(3)",
         [("nodes", "val + next pointer"),
          ("singly / doubly", "next only · or prev too"),
          ("O(1) insert head", "fast"),
          ("O(n) lookup", "slow"),
          ("Python list ≠ linked", "list is dynamic array"),
          ("interview-favorite", "study it")],
         ["lists", "stack", "queue"]),

        ("hash-table", "Hash table",
         "Map keys to values using a hash function. O(1) average lookup. Python dict and set are hash tables.",
         "users = {'kasim': 12, 'Mina': 10}\nusers['kasim']           # O(1)\n'Mina' in users           # O(1)\n\n# behind the scenes:\n# hash(key) % capacity",
         [("O(1) avg lookup", "hash function"),
          ("Python dict / set", "implementation"),
          ("collisions", "open addressing in CPython"),
          ("keys must hash", "be hashable"),
          ("memory cost", "vs list"),
          ("rehashing", "auto-grows")],
         ["dictionaries", "sets", "big-o"]),

        ("binary-tree", "Binary tree + BST",
         "Each node has 0, 1, or 2 children. BST = sorted (left < node < right). Used in search, indexing.",
         "class Node:\n    def __init__(self, val):\n        self.val = val\n        self.left = self.right = None\n\ndef insert(root, val):\n    if root is None: return Node(val)\n    if val < root.val: root.left  = insert(root.left, val)\n    else:               root.right = insert(root.right, val)\n    return root",
         [("binary", "≤ 2 children"),
          ("BST", "sorted property"),
          ("O(log n) balanced", "worst O(n)"),
          ("traversals", "in/pre/post-order"),
          ("balanced trees", "AVL, RB"),
          ("heapq", "stdlib heap")],
         ["graph", "recursion-dp", "bfs-dfs"]),

        ("graph", "Graphs",
         "Nodes + edges. Directed or undirected. Represented as adjacency list (dict of lists) or matrix.",
         "graph = {\n    'A': ['B', 'C'],\n    'B': ['A', 'D'],\n    'C': ['A'],\n    'D': ['B'],\n}",
         [("nodes + edges", "the structure"),
          ("directed / undirected", "edges with/without arrows"),
          ("weighted", "edges have cost"),
          ("adjacency list", "dict of neighbours"),
          ("adjacency matrix", "2D array"),
          ("cyclic / acyclic", "DAG = no cycles")],
         ["bfs-dfs", "binary-tree", "hash-table"]),

        ("bfs-dfs", "BFS + DFS",
         "Graph traversal. BFS (queue) finds shortest path. DFS (stack/recursion) goes deep first.",
         "from collections import deque\ndef bfs(g, start):\n    seen = {start}\n    q = deque([start])\n    while q:\n        n = q.popleft()\n        for nb in g[n]:\n            if nb not in seen:\n                seen.add(nb)\n                q.append(nb)",
         [("BFS", "queue · level-by-level"),
          ("DFS", "stack/recursion · deep first"),
          ("shortest path", "BFS in unweighted"),
          ("Dijkstra", "weighted shortest"),
          ("A*", "heuristic search"),
          ("seen set", "avoid cycles")],
         ["graph", "queue", "stack"]),

        ("sorting-algorithms", "Sorting",
         "Bubble (slow O(n²)), Merge + Quick (O(n log n)), Python's sorted() uses TimSort (also O(n log n), real-world fast).",
         "nums = [5, 2, 8, 1, 9]\nsorted(nums)      # [1, 2, 5, 8, 9]\nnums.sort()       # in place\nsorted(items, key=lambda x: x.hp, reverse=True)",
         [("bubble", "O(n²) · simple"),
          ("merge", "O(n log n) · stable"),
          ("quick", "O(n log n) avg"),
          ("TimSort", "Python's default"),
          ("sorted(it)", "new list"),
          ("list.sort()", "in place")],
         ["big-o", "lists", "recursion-dp"]),

        ("recursion-dp", "Recursion + Dynamic Programming",
         "Recursion = function calls itself. DP = recursion + memoization. Solves big problems by combining small answers.",
         "from functools import cache\n\n@cache\ndef fib(n):\n    if n < 2: return n\n    return fib(n-1) + fib(n-2)\n\nfib(100)   # instant",
         [("base case", "stops the recursion"),
          ("recursive case", "smaller subproblem"),
          ("call stack", "Python limit ~1000"),
          ("memoization", "@cache solves it"),
          ("tabulation", "bottom-up DP"),
          ("classics", "fib · knapsack · LCS")],
         ["functools", "stack", "big-o"]),
    ]),

    ("12-testing", "Stage 12 · Testing", [
        ("unittest", "unittest (stdlib)",
         "Python's built-in test framework. Class-based, xUnit-style. Works everywhere — no install.",
         "import unittest\n\nclass TestBattle(unittest.TestCase):\n    def test_attack(self):\n        p = Pokemon('a', 100)\n        p.take_damage(10)\n        self.assertEqual(p.hp, 90)\n\nif __name__ == '__main__':\n    unittest.main()",
         [("stdlib", "no install"), ("class-based", "TestCase subclass"),
          ("test_* methods", "auto-discovered"), ("assertEqual / assertRaises / ...", "asserts"),
          ("setUp / tearDown", "per test"), ("verbose", "than pytest")],
         ["pytest", "doctest", "mocking"]),

        ("pytest", "pytest — the modern default",
         "Minimal syntax, powerful plugins, great error reports. The de-facto Python test framework.",
         "# test_battle.py\ndef test_attack_reduces_hp():\n    p = Pokemon('a', 100)\n    p.take_damage(10)\n    assert p.hp == 90\n\n# $ pytest -v",
         [("functions not classes", "just def test_x"),
          ("plain assert", "auto-introspected"),
          ("pytest -v", "verbose"),
          ("pytest -k name", "filter tests"),
          ("plugins", "cov · xdist · mock"),
          ("conftest.py", "shared setup")],
         ["fixtures", "unittest", "coverage"]),

        ("fixtures", "pytest fixtures",
         "Reusable test setup. Define once with @fixture, request by name as a test arg. Scopes: function, class, module, session.",
         "import pytest\n\n@pytest.fixture\ndef battle():\n    return Battle(create_p1(), create_p2())\n\ndef test_p1_wins(battle):\n    battle.run()\n    assert battle.winner is battle.p1",
         [("@pytest.fixture", "decorator"),
          ("scope=", "function · class · module · session"),
          ("yield in fixture", "for teardown"),
          ("autouse=True", "applied automatically"),
          ("parametrize", "data-driven tests"),
          ("conftest.py", "share across files")],
         ["pytest", "mocking", "coverage"]),

        ("mocking", "Mocking",
         "Replace real objects with fakes in tests. unittest.mock has MagicMock + patch. Use to isolate units from I/O.",
         "from unittest.mock import patch, MagicMock\n\ndef test_calls_api():\n    with patch('mymod.api_call') as m:\n        m.return_value = {'ok': True}\n        result = do_thing()\n        m.assert_called_once()",
         [("MagicMock", "fake any object"),
          ("@patch", "swap during test"),
          ("return_value", "fake response"),
          ("side_effect", "raise / sequence"),
          ("assert_called_with", "check usage"),
          ("pytest-mock", "nicer API")],
         ["pytest", "fixtures", "unittest"]),

        ("doctest", "doctest",
         "Tests inside docstrings. The example is the test. Great for quick API examples that double as docs.",
         "def add(a, b):\n    '''\n    >>> add(2, 3)\n    5\n    >>> add(-1, 1)\n    0\n    '''\n    return a + b\n\n# $ python -m doctest mod.py",
         [("inside docstrings", "examples = tests"),
          (">>>", "expected"),
          ("python -m doctest", "run them"),
          ("pytest --doctest-modules", "run with pytest"),
          ("good for examples", "small APIs"),
          ("not for big suites", "use pytest")],
         ["unittest", "pytest", "docstrings"]),

        ("coverage", "Coverage",
         "Measure which lines tests actually hit. coverage.py is the tool. Aim for high coverage but don't chase 100% blindly.",
         "$ pip install coverage\n$ coverage run -m pytest\n$ coverage report\n$ coverage html   # browseable HTML",
         [("coverage run", "executes + tracks"),
          ("coverage report", "text summary"),
          ("coverage html", "visual report"),
          ("pytest-cov", "integrated"),
          ("100% means little", "untested logic may exist"),
          ("CI gate", "fail under threshold")],
         ["pytest", "ci", "quality"]),
    ]),

    ("13-quality", "Stage 13 · Code Quality", [
        ("pep8", "PEP 8 — style guide",
         "Python's official style. 4-space indent, snake_case, 79-char lines (soft). Don't memorize — use a formatter.",
         "# bad\ndef MyFunction (X,Y):\n    return  X+Y\n\n# good\ndef my_function(x, y):\n    return x + y",
         [("4 spaces indent", "not tabs"),
          ("snake_case", "functions + vars"),
          ("PascalCase", "classes"),
          ("UPPER_CASE", "constants"),
          ("79 chars line", "or 88 with black"),
          ("auto-format", "just use black/ruff")],
         ["black-ruff", "pylint-flake8", "mypy"]),

        ("black-ruff", "black + ruff",
         "black: opinionated formatter, no config. ruff: fast linter + formatter (Rust). Run both on save.",
         "$ pip install black ruff\n$ black .\n$ ruff check .\n$ ruff check --fix .\n$ ruff format .",
         [("black", "no-arg formatter"),
          ("ruff format", "black-compatible"),
          ("ruff check", "fast linter"),
          ("ruff --fix", "auto-fix"),
          ("editor integrations", "format on save"),
          ("pre-commit hook", "auto-run")],
         ["pep8", "pylint-flake8", "pre-commit"]),

        ("mypy", "mypy — static type checker",
         "Reads your type hints and finds bugs without running code. Run in CI to catch errors before tests.",
         "$ pip install mypy\n$ mypy myapp/\n\n# myapp/x.py\ndef greet(name: str) -> str:\n    return f'Hi, {name}'\n\ngreet(42)   # mypy: error",
         [("--strict", "all checks"),
          ("Optional[X]", "X or None"),
          ("# type: ignore", "skip line"),
          ("mypy.ini", "config"),
          ("pyright alt", "Microsoft · faster"),
          ("gradual typing", "add hints over time")],
         ["type-hints", "protocols", "pylint-flake8"]),

        ("pylint-flake8", "pylint + flake8",
         "Older linters. pylint is thorough but slow. flake8 = pycodestyle + pyflakes + mccabe. Mostly replaced by ruff.",
         "$ pip install pylint flake8\n$ pylint myapp/\n$ flake8 myapp/",
         [("pylint", "thorough · slow"),
          ("flake8", "fast classic"),
          ("ruff replaces both", "100x faster"),
          ("legacy projects", "still common"),
          ("config files", ".pylintrc · setup.cfg"),
          ("plugins", "many for both")],
         ["black-ruff", "pep8", "mypy"]),

        ("pre-commit", "pre-commit",
         "Run hooks (lint, format, type-check) before every commit. Single config across team, all tools.",
         "# .pre-commit-config.yaml\nrepos:\n  - repo: https://github.com/astral-sh/ruff-pre-commit\n    rev: v0.4.0\n    hooks:\n      - id: ruff\n      - id: ruff-format",
         [("YAML config", ".pre-commit-config.yaml"),
          ("pre-commit install", "set up the hook"),
          ("auto-run on commit", "blocks bad commits"),
          ("manual", "pre-commit run --all-files"),
          ("update", "pre-commit autoupdate"),
          ("CI too", "run on PRs")],
         ["black-ruff", "mypy", "ci"]),

        ("logging", "logging",
         "Levels (debug, info, warning, error, critical), destinations (stdout, file, syslog), filters. Never use print in real apps.",
         "import logging\nlogging.basicConfig(level=logging.INFO)\nlog = logging.getLogger(__name__)\n\nlog.info('player joined: %s', name)\nlog.error('out of mana')",
         [("levels", "DEBUG < INFO < WARNING < ERROR < CRITICAL"),
          ("getLogger(__name__)", "module logger"),
          ("%s formatting", "lazy interpolation"),
          ("handlers", "file · stream · http"),
          ("formatters", "control output"),
          ("structlog / loguru", "modern alternatives")],
         ["debugging", "exceptions", "input-output"]),
    ]),

    ("14-concurrency", "Stage 14 · Concurrency + Async", [
        ("threading", "threading",
         "Light-weight threads, share memory. Good for I/O wait (network, disk). Bad for CPU work (GIL).",
         "import threading\ndef work(n):\n    print(n)\n\nts = [threading.Thread(target=work, args=(i,)) for i in range(5)]\nfor t in ts: t.start()\nfor t in ts: t.join()",
         [("Thread(target=fn)", "create"),
          ("start()", "run"),
          ("join()", "wait for finish"),
          ("Lock / RLock", "mutual exclusion"),
          ("GIL", "limits CPU parallelism"),
          ("good for I/O", "not CPU")],
         ["multiprocessing", "gil", "concurrent-futures"]),

        ("multiprocessing", "multiprocessing",
         "Real parallel processes, separate memory. Good for CPU-heavy work — escapes the GIL by running multiple interpreters.",
         "from multiprocessing import Pool\n\ndef square(n): return n * n\n\nwith Pool(4) as p:\n    print(p.map(square, range(10)))",
         [("Pool", "worker processes"),
          ("Process(target=fn)", "single"),
          ("Queue / Pipe", "IPC"),
          ("CPU parallel", "real cores"),
          ("overhead", "fork or spawn"),
          ("pickle data", "for IPC")],
         ["threading", "gil", "concurrent-futures"]),

        ("gil", "The GIL",
         "Global Interpreter Lock — only one thread runs Python bytecode at a time. Why threading doesn't help CPU work.",
         "# 8 threads doing math = 1 thread effectively\n# 8 threads waiting on network = 8x speedup\n\n# Workarounds:\n# - multiprocessing\n# - C extensions (release the GIL)\n# - PEP 703 no-GIL build (3.13+)",
         [("one thread at a time", "Python bytecode"),
          ("why?", "memory safety · C ext compat"),
          ("workarounds", "multiproc · C ext · async"),
          ("PEP 703", "free-threaded build (3.13+)"),
          ("affects threading only", "asyncio works fine"),
          ("don't fear it", "many real bottlenecks are I/O")],
         ["threading", "multiprocessing", "asyncio"]),

        ("asyncio", "asyncio",
         "Single-threaded concurrency via cooperative multitasking. async/await syntax. Best for many simultaneous network calls.",
         "import asyncio\n\nasync def fetch(url):\n    ...\n    return data\n\nasync def main():\n    results = await asyncio.gather(\n        fetch('a'), fetch('b'),\n    )\n\nasyncio.run(main())",
         [("async def", "coroutine"),
          ("await", "yield + resume"),
          ("asyncio.run(main())", "entry point"),
          ("asyncio.gather", "many in parallel"),
          ("event loop", "cooperative scheduler"),
          ("not for CPU", "use multiproc")],
         ["async-patterns", "concurrent-futures", "threading"]),

        ("concurrent-futures", "concurrent.futures",
         "Pool of workers, swap Thread / Process with one word. Map work over inputs, get futures back.",
         "from concurrent.futures import ThreadPoolExecutor\n\nwith ThreadPoolExecutor() as ex:\n    futures = [ex.submit(fetch, u) for u in urls]\n    results = [f.result() for f in futures]\n\n# or:\n    results = list(ex.map(fetch, urls))",
         [("ThreadPoolExecutor", "I/O bound"),
          ("ProcessPoolExecutor", "CPU bound"),
          ("submit()", "schedule one · returns Future"),
          ("map()", "schedule many"),
          ("as_completed", "iterate as they finish"),
          ("future.result()", "blocks until done")],
         ["threading", "multiprocessing", "asyncio"]),

        ("async-patterns", "Async patterns",
         "gather (parallel), Queue (producer/consumer), Semaphore (rate limit), TaskGroup (structured concurrency, 3.11+).",
         "sem = asyncio.Semaphore(10)\n\nasync def fetch(url):\n    async with sem:        # rate limit\n        ...\n\nasync with asyncio.TaskGroup() as tg:\n    for u in urls:\n        tg.create_task(fetch(u))",
         [("gather", "run many · wait all"),
          ("TaskGroup", "structured · 3.11+"),
          ("Queue", "async producer/consumer"),
          ("Semaphore", "limit concurrency"),
          ("wait_for", "timeout"),
          ("shield", "protect from cancel")],
         ["asyncio", "concurrent-futures", "threading"]),
    ]),

    ("15-web", "Stage 15 · Web Development", [
        ("django", "Django",
         "Full-stack web framework. ORM, admin, auth, templates included. Best for big, traditional sites.",
         "# views.py\nfrom django.shortcuts import render\n\ndef index(req):\n    return render(req, 'index.html', {'name': 'Kasim'})\n\n# urls.py\nfrom django.urls import path\nurlpatterns = [path('', index)]",
         [("batteries included", "everything built in"),
          ("ORM", "models + migrations"),
          ("admin panel", "free CRUD UI"),
          ("templating", "DTL"),
          ("DRF", "Django REST Framework"),
          ("convention-heavy", "the Django way")],
         ["flask", "fastapi", "sqlalchemy"]),

        ("flask", "Flask",
         "Minimal microframework. You bring the libs (DB, auth, etc). Great for small APIs and prototypes.",
         "from flask import Flask\napp = Flask(__name__)\n\n@app.route('/')\ndef hello():\n    return 'Hello!'\n\n# $ flask run",
         [("microframework", "minimal core"),
          ("decorator routes", "@app.route"),
          ("flexible", "bring your own everything"),
          ("Jinja2", "default templates"),
          ("extensions", "Flask-SQLAlchemy etc"),
          ("good for prototypes", "and small APIs")],
         ["django", "fastapi", "jinja"]),

        ("fastapi", "FastAPI",
         "Modern async framework built on Starlette + Pydantic. Auto docs (OpenAPI), type-driven. Best for APIs.",
         "from fastapi import FastAPI\nfrom pydantic import BaseModel\n\napp = FastAPI()\n\nclass Item(BaseModel):\n    name: str\n    price: float\n\n@app.post('/items')\nasync def create(item: Item):\n    return item",
         [("async first", "fast"),
          ("Pydantic", "auto validation"),
          ("auto docs", "/docs · /redoc"),
          ("type-driven", "params from hints"),
          ("Starlette under it", "ASGI"),
          ("popular for APIs", "modern default")],
         ["pydantic", "django", "flask"]),

        ("requests-httpx", "requests + httpx",
         "HTTP clients. requests is sync, classic, easy. httpx is requests-compatible + async.",
         "import requests\nr = requests.get('https://api.x/users', timeout=5)\nr.raise_for_status()\nr.json()\n\n# async (httpx):\nimport httpx\nasync with httpx.AsyncClient() as c:\n    r = await c.get(url)",
         [("requests", "sync · classic"),
          ("httpx", "sync + async"),
          ("timeout", "always set one!"),
          ("raise_for_status", "throw on 4xx/5xx"),
          (".json()", "parse response"),
          ("Session / AsyncClient", "reuse connections")],
         ["fastapi", "asyncio", "json"]),

        ("pydantic", "Pydantic",
         "Data validation via type hints. Convert dirty JSON into typed Python objects. Foundation of FastAPI.",
         "from pydantic import BaseModel, Field\n\nclass User(BaseModel):\n    name: str = Field(min_length=1)\n    age: int = Field(ge=0)\n    email: str | None = None\n\nUser(name='Kasim', age=27)",
         [("BaseModel", "subclass for schemas"),
          ("type hints", "drive validation"),
          ("Field()", "extra constraints"),
          ("model_validate", "from dict / JSON"),
          ("model_dump", "to dict / JSON"),
          ("v2 fast", "Rust-based core")],
         ["type-hints", "fastapi", "dataclasses"]),

        ("jinja", "Jinja2 templates",
         "Templating engine for HTML (and anything else). Used by Flask, Django can use it too.",
         "# templates/page.html\n<h1>Hello, {{ name }}!</h1>\n<ul>\n{% for item in items %}\n  <li>{{ item }}</li>\n{% endfor %}\n</ul>",
         [("{{ var }}", "interpolate"),
          ("{% block %}", "logic"),
          ("inheritance", "{% extends %}"),
          ("filters", "{{ name|upper }}"),
          ("escape by default", "XSS-safe"),
          ("Flask default", "Django optional")],
         ["flask", "django", "fastapi"]),

        ("sqlalchemy", "SQLAlchemy",
         "SQL toolkit and ORM. Core (SQL expression) + ORM (Python classes). Most popular DB lib outside Django.",
         "from sqlalchemy import create_engine\nfrom sqlalchemy.orm import sessionmaker\n\nengine = create_engine('postgresql://...')\nSession = sessionmaker(bind=engine)\n\nwith Session() as s:\n    users = s.query(User).all()",
         [("Core", "SQL expression language"),
          ("ORM", "objects ↔ rows"),
          ("engine", "DB connection"),
          ("session", "unit of work"),
          ("alembic", "migrations"),
          ("any RDBMS", "postgres · mysql · sqlite")],
         ["django", "fastapi", "pydantic"]),

        ("deployment", "Deployment basics",
         "Run a Python web app in production: gunicorn / uvicorn behind nginx, on a VPS / PaaS / container.",
         "# gunicorn (sync WSGI)\n$ gunicorn app:app\n\n# uvicorn (async ASGI)\n$ uvicorn app:app --host 0.0.0.0 --port 8000\n\n# Dockerfile FROM python:3.12-slim ...",
         [("gunicorn", "WSGI · sync"),
          ("uvicorn", "ASGI · async (FastAPI)"),
          ("nginx", "reverse proxy"),
          ("Docker", "containerize"),
          ("VPS · PaaS · K8s", "host options"),
          ("env vars", "for secrets · DB URL")],
         ["fastapi", "django", "ci"]),
    ]),

    ("16-data-ml", "Stage 16 · Data + ML", [
        ("numpy", "NumPy",
         "Fast multi-dim arrays + linear algebra. The base of the whole scientific Python stack.",
         "import numpy as np\na = np.array([1, 2, 3])\nb = a * 2          # [2, 4, 6]\na.mean()           # 2.0\nmat = np.zeros((3, 3))\nmat @ mat          # matrix multiply",
         [("ndarray", "core type"),
          ("vectorized ops", "no for-loops"),
          ("broadcasting", "shape rules"),
          ("dtype", "int32 · float64 etc"),
          ("slicing", "powerful indexing"),
          ("fast (C/SIMD)", "100x list speed")],
         ["pandas", "matplotlib", "scikit-learn"]),

        ("pandas", "Pandas",
         "Spreadsheets in code. DataFrames, groupby, joins, time series, I/O for csv/json/parquet/sql.",
         "import pandas as pd\ndf = pd.read_csv('data.csv')\ndf.head()\ndf[df['age'] > 18]\ndf.groupby('country')['rev'].sum()\ndf.to_parquet('out.parquet')",
         [("DataFrame", "core type"),
          ("read_csv / to_csv", "I/O"),
          ("groupby", "split-apply-combine"),
          ("merge / join", "SQL-style"),
          ("indexing", "loc · iloc"),
          ("alt: polars", "faster modern option")],
         ["numpy", "matplotlib", "csv"]),

        ("matplotlib", "Matplotlib",
         "Classic plotting library. Powerful but verbose. Most other plot libs build on it.",
         "import matplotlib.pyplot as plt\nplt.plot([1,2,3], [1,4,9])\nplt.xlabel('x')\nplt.title('Squares')\nplt.savefig('plot.png')\nplt.show()",
         [("plt", "pyplot interface"),
          ("plot / scatter / bar / hist", "plot types"),
          ("subplots", "multiple axes"),
          ("savefig", "to file"),
          ("verbose but flexible", "fine control"),
          ("seaborn, plotly", "higher-level wrappers")],
         ["pandas", "seaborn", "plotly"]),

        ("seaborn", "Seaborn",
         "Statistical plots built on matplotlib. Beautiful defaults. Great for exploratory data analysis.",
         "import seaborn as sns\nimport matplotlib.pyplot as plt\nsns.scatterplot(data=df, x='age', y='income', hue='sex')\nsns.heatmap(df.corr(), annot=True)\nplt.show()",
         [("statistical viz", "regression · distributions"),
          ("works on DataFrame", "tidy data"),
          ("nice defaults", "no styling needed"),
          ("hue · style · size", "encode dimensions"),
          ("facet grids", "small multiples"),
          ("uses matplotlib", "still need plt.show")],
         ["matplotlib", "pandas", "plotly"]),

        ("scikit-learn", "scikit-learn",
         "Classical ML: regression, classification, clustering, preprocessing. Consistent fit/predict API across all models.",
         "from sklearn.ensemble import RandomForestClassifier\nfrom sklearn.model_selection import train_test_split\n\nX_train, X_test, y_train, y_test = train_test_split(X, y)\nm = RandomForestClassifier().fit(X_train, y_train)\nm.score(X_test, y_test)",
         [("fit / predict", "consistent API"),
          ("classifiers", "RF · SVM · LR"),
          ("regressors", "Linear · GBR"),
          ("Pipeline", "preprocess + model"),
          ("train_test_split", "evaluation"),
          ("cross_val_score", "robust eval")],
         ["pytorch", "tensorflow", "numpy"]),

        ("pytorch", "PyTorch",
         "Deep learning framework. Dynamic graphs, Pythonic, dominant in research. Backed by Meta.",
         "import torch\nimport torch.nn as nn\n\nclass Net(nn.Module):\n    def __init__(self):\n        super().__init__()\n        self.fc = nn.Linear(10, 2)\n    def forward(self, x):\n        return self.fc(x)",
         [("tensors", "GPU-aware arrays"),
          ("autograd", "automatic gradients"),
          ("nn.Module", "your models"),
          ("dynamic graphs", "Python control flow"),
          ("research default", "papers use it"),
          ("HF Transformers", "built on PyTorch")],
         ["tensorflow", "scikit-learn", "langchain"]),

        ("tensorflow", "TensorFlow + Keras",
         "Google's deep learning framework. Strong production tooling (TFX, TFLite). Keras is the high-level API.",
         "import tensorflow as tf\nfrom tensorflow import keras\n\nm = keras.Sequential([\n    keras.layers.Dense(64, activation='relu'),\n    keras.layers.Dense(10, activation='softmax'),\n])\nm.compile(optimizer='adam', loss='ce')\nm.fit(X, y)",
         [("Keras API", "high-level"),
          ("tf.data", "pipeline"),
          ("static + dynamic", "graphs (since 2.0)"),
          ("TFLite", "mobile + edge"),
          ("TF Serving", "production"),
          ("vs PyTorch", "both valid choices")],
         ["pytorch", "scikit-learn", "numpy"]),

        ("langchain", "LangChain",
         "Framework for LLM-powered apps: chains, agents, memory, retrieval. Talk to OpenAI / Anthropic / local models.",
         "from langchain_anthropic import ChatAnthropic\nfrom langchain.prompts import ChatPromptTemplate\n\nllm = ChatAnthropic(model='claude-3-5-sonnet')\nprompt = ChatPromptTemplate.from_messages([('user', '{q}')])\nchain = prompt | llm\nchain.invoke({'q': 'hi'})",
         [("chains", "compose LLM calls"),
          ("agents", "tool-using LLMs"),
          ("memory", "conversation history"),
          ("retrievers", "RAG over docs"),
          ("vector stores", "Chroma · Pinecone"),
          ("LangGraph", "stateful agents")],
         ["pytorch", "fastapi", "json"]),

        ("streamlit", "Streamlit",
         "Build data apps in pure Python. No frontend needed. One file → an interactive web UI.",
         "import streamlit as st\nimport pandas as pd\n\nst.title('My App')\nname = st.text_input('Name')\ndf = pd.read_csv('data.csv')\nst.dataframe(df)\nst.line_chart(df['rev'])",
         [("pure Python", "no JS needed"),
          ("st.*", "widget functions"),
          ("auto re-run", "on any change"),
          ("st.dataframe / chart", "data-aware"),
          ("free hosting", "streamlit.app"),
          ("alt: gradio · dash", "similar tools")],
         ["pandas", "matplotlib", "fastapi"]),

        ("jupyter", "Jupyter notebooks",
         "Interactive notebooks (.ipynb). Mix code, output, markdown, plots. Standard for data exploration + teaching.",
         "$ pip install jupyterlab\n$ jupyter lab\n\n# .ipynb files mix:\n#   - code cells\n#   - markdown cells\n#   - rich outputs (plots, tables)",
         [("JupyterLab", "modern UI"),
          (".ipynb", "JSON file format"),
          ("cells", "code + markdown"),
          ("kernel", "Python (or many others)"),
          ("Colab", "free Google version"),
          ("nbconvert", "to PDF · HTML")],
         ["pandas", "matplotlib", "scikit-learn"]),
    ]),

    ("17-gui-games", "Stage 17 · GUI + Games", [
        ("tkinter", "Tkinter",
         "Python's stdlib GUI toolkit. Built into every Python. Looks dated but works everywhere.",
         "import tkinter as tk\nroot = tk.Tk()\ntk.Label(root, text='Hello').pack()\ntk.Button(root, text='Click', command=root.quit).pack()\nroot.mainloop()",
         [("stdlib", "no install"),
          ("Tk widgets", "Label · Button · Entry"),
          ("pack / grid / place", "layout"),
          ("mainloop", "event loop"),
          ("ttk", "themed widgets"),
          ("dated look", "see customtkinter")],
         ["customtkinter", "pyqt", "kivy"]),

        ("customtkinter", "CustomTkinter",
         "Modern-looking widgets on top of Tkinter. Dark mode, rounded corners, themes. Drop-in upgrade.",
         "import customtkinter as ctk\nctk.set_appearance_mode('dark')\napp = ctk.CTk()\nctk.CTkLabel(app, text='Hello').pack(pady=10)\nctk.CTkButton(app, text='Go').pack()\napp.mainloop()",
         [("install", "pip install customtkinter"),
          ("ctk widgets", "modern look"),
          ("dark mode", "set_appearance_mode"),
          ("themes", "blue / green / dark-blue"),
          ("Tk-compatible", "API is similar"),
          ("free", "MIT license")],
         ["tkinter", "pyqt", "kivy"]),

        ("pyqt", "PyQt / PySide",
         "Bindings to the Qt C++ toolkit. Native look-and-feel. PySide is the free LGPL version.",
         "from PySide6.QtWidgets import QApplication, QPushButton\napp = QApplication([])\nbutton = QPushButton('Click me')\nbutton.clicked.connect(lambda: print('hi'))\nbutton.show()\napp.exec()",
         [("Qt under the hood", "C++ powerhouse"),
          ("PySide", "LGPL · use this"),
          ("PyQt", "GPL or commercial"),
          ("Qt Designer", "GUI builder"),
          ("signals / slots", "event model"),
          ("native look", "OS-style widgets")],
         ["tkinter", "kivy", "wxpython"]),

        ("kivy", "Kivy",
         "Cross-platform UI, multi-touch, custom rendered (OpenGL). Targets desktop + mobile.",
         "from kivy.app import App\nfrom kivy.uix.button import Button\n\nclass MyApp(App):\n    def build(self):\n        return Button(text='Hello')\n\nMyApp().run()",
         [("OpenGL-rendered", "consistent look"),
          ("mobile", "Android + iOS"),
          ("KV lang", "declarative UI"),
          ("touch-first", "gestures built in"),
          ("Python only", "no Java/Swift needed"),
          ("alt: BeeWare · Toga", "native widgets")],
         ["pygame", "tkinter", "pyqt"]),

        ("pygame", "Pygame",
         "Classic 2D game library. Sprites, sound, input. Bedrock for many beginner game projects.",
         "import pygame\npygame.init()\nscreen = pygame.display.set_mode((640, 480))\nrunning = True\nwhile running:\n    for e in pygame.event.get():\n        if e.type == pygame.QUIT: running = False\n    screen.fill((0, 0, 0))\n    pygame.display.flip()",
         [("Surface", "drawable buffer"),
          ("event loop", "QUIT · KEYDOWN · etc"),
          ("Sprite + Group", "game objects"),
          ("Clock", "frame rate"),
          ("mixer", "sound"),
          ("rs003 + rs004", "our courses use it")],
         ["arcade", "kivy", "panda3d"]),

        ("arcade", "Arcade",
         "Modern Python game library. Cleaner API than Pygame. Built-in physics, sprites, animations.",
         "import arcade\n\nclass Game(arcade.Window):\n    def __init__(self):\n        super().__init__(640, 480, 'Game')\n    def on_draw(self):\n        self.clear()\n        arcade.draw_circle_filled(100, 100, 30, arcade.color.RED)\n\nGame()\narcade.run()",
         [("object-oriented", "subclass Window"),
          ("modern API", "cleaner than pygame"),
          ("physics built in", "Pymunk wrapper"),
          ("hardware accelerated", "OpenGL"),
          ("good docs", "tutorials"),
          ("Python 3.10+", "modern Python only")],
         ["pygame", "kivy", "panda3d"]),
    ]),

    ("18-automation-cv", "Stage 18 · Automation + Scraping + CV", [
        ("pyautogui", "PyAutoGUI",
         "Cross-platform mouse + keyboard automation. Move cursor, click, type, take screenshots, find images on screen.",
         "import pyautogui as p\np.moveTo(100, 200)\np.click()\np.write('hello', interval=0.1)\np.screenshot('screen.png')\nx, y = p.locateCenterOnScreen('button.png')",
         [("moveTo / click / drag", "mouse"),
          ("write / press / hotkey", "keyboard"),
          ("screenshot", "save image"),
          ("locateOnScreen", "find image"),
          ("FAILSAFE", "top-left corner aborts"),
          ("cross-platform", "win · mac · linux")],
         ["selenium", "schedule", "pillow"]),

        ("selenium", "Selenium",
         "Browser automation. Classic for testing web apps + scraping JS-heavy sites. Drives real browsers.",
         "from selenium import webdriver\nfrom selenium.webdriver.common.by import By\n\nd = webdriver.Chrome()\nd.get('https://example.com')\nd.find_element(By.NAME, 'q').send_keys('hi')\nd.quit()",
         [("WebDriver", "controls real browser"),
          ("find_element", "by id / xpath / css"),
          ("click / send_keys", "interact"),
          ("waits", "explicit / implicit"),
          ("headless mode", "no window"),
          ("alt: Playwright", "modern alternative")],
         ["playwright", "beautifulsoup", "scrapy"]),

        ("playwright", "Playwright",
         "Modern browser automation from Microsoft. Faster + cleaner API than Selenium. Auto-waits.",
         "from playwright.sync_api import sync_playwright\n\nwith sync_playwright() as p:\n    browser = p.chromium.launch()\n    page = browser.new_page()\n    page.goto('https://example.com')\n    page.fill('input[name=q]', 'hi')\n    browser.close()",
         [("auto-wait", "no flaky timing"),
          ("multi-browser", "Chromium · Firefox · WebKit"),
          ("sync + async", "API"),
          ("codegen", "record actions"),
          ("trace viewer", "debug visually"),
          ("headless or not", "your choice")],
         ["selenium", "beautifulsoup", "asyncio"]),

        ("beautifulsoup", "BeautifulSoup",
         "Parse HTML / XML. CSS-like selectors. Great with requests for static-page scraping.",
         "import requests\nfrom bs4 import BeautifulSoup\n\nhtml = requests.get(url).text\nsoup = BeautifulSoup(html, 'html.parser')\ntitles = [h.text for h in soup.select('h2.title')]",
         [("BeautifulSoup(html, parser)", "init"),
          ("select / select_one", "CSS selectors"),
          ("find / find_all", "by tag / class / id"),
          ("text · attrs", "content access"),
          ("lxml parser", "fastest backend"),
          ("static HTML only", "use playwright for JS")],
         ["scrapy", "playwright", "requests-httpx"]),

        ("scrapy", "Scrapy",
         "Full web-scraping framework. Concurrent, robust, with pipelines and exporters. For serious scraping.",
         "import scrapy\n\nclass QuoteSpider(scrapy.Spider):\n    name = 'quotes'\n    start_urls = ['http://quotes.toscrape.com']\n\n    def parse(self, response):\n        for q in response.css('div.quote'):\n            yield {'text': q.css('span.text::text').get()}",
         [("Spider class", "your scraper"),
          ("start_urls", "where to begin"),
          ("parse()", "yield items + follow links"),
          ("Item pipelines", "clean + save"),
          ("concurrent", "async by design"),
          ("scrapy crawl", "run it")],
         ["beautifulsoup", "playwright", "selenium"]),

        ("pillow", "Pillow (PIL)",
         "Image manipulation: open, save, resize, crop, rotate, filter, draw text. The standard image lib.",
         "from PIL import Image, ImageFilter\nimg = Image.open('a.png')\nimg = img.resize((100, 100))\nimg = img.filter(ImageFilter.BLUR)\nimg.save('b.png')",
         [("Image.open", "load any format"),
          ("resize / crop / rotate", "transform"),
          ("ImageFilter", "blur · sharpen · edge"),
          ("ImageDraw", "shapes + text"),
          ("convert", "RGB · L · RGBA"),
          ("EXIF", "metadata access")],
         ["opencv", "matplotlib", "file-io"]),

        ("opencv", "OpenCV",
         "Computer vision powerhouse: detection, tracking, transforms, video I/O. Python bindings to a huge C++ library.",
         "import cv2\nimg = cv2.imread('photo.jpg')\ngray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)\nedges = cv2.Canny(gray, 100, 200)\ncv2.imwrite('edges.jpg', edges)",
         [("cv2.imread / imwrite", "I/O"),
          ("BGR not RGB!", "OpenCV's default"),
          ("Canny · threshold", "edge / binary"),
          ("haar cascades", "face detection"),
          ("VideoCapture", "webcam · file"),
          ("DNN module", "load deep models")],
         ["pillow", "numpy", "pytorch"]),

        ("schedule", "schedule + cron",
         "Run jobs on a schedule. schedule lib is simple Python. For production: APScheduler or system cron.",
         "import schedule, time\n\ndef job():\n    print('running')\n\nschedule.every(10).minutes.do(job)\nschedule.every().day.at('09:00').do(job)\n\nwhile True:\n    schedule.run_pending()\n    time.sleep(1)",
         [("simple cron-like", "in Python"),
          ("every(n).minutes / hours / days", "DSL"),
          ("at('HH:MM')", "specific time"),
          ("run_pending", "in your loop"),
          ("APScheduler", "production-grade"),
          ("system cron", "if outside Python")],
         ["asyncio", "logging", "ci"]),
    ]),

    ("19-cli", "Stage 19 · CLI Tools", [
        ("argparse", "argparse (stdlib)",
         "Parse command-line arguments. Verbose but built-in. Auto-generates --help.",
         "import argparse\np = argparse.ArgumentParser()\np.add_argument('name')\np.add_argument('--age', type=int, default=0)\nargs = p.parse_args()\nprint(args.name, args.age)",
         [("ArgumentParser", "the main object"),
          ("add_argument", "positional or --flag"),
          ("type=int / float", "auto-cast"),
          ("default=", "if not given"),
          ("--help", "auto-generated"),
          ("subparsers", "for git-style subcommands")],
         ["click", "typer", "main-guard"]),

        ("click", "Click",
         "Decorator-based CLI library. Composable, supports subcommands, prompts, colors. Used by Flask itself.",
         "import click\n\n@click.command()\n@click.argument('name')\n@click.option('--age', default=0, type=int)\ndef hello(name, age):\n    click.echo(f'Hi {name}, {age}')\n\nif __name__ == '__main__':\n    hello()",
         [("@click.command", "decorator-based"),
          ("@click.argument", "positional"),
          ("@click.option", "flag"),
          ("@click.group", "subcommands"),
          ("click.echo", "print with color"),
          ("click.prompt", "interactive input")],
         ["argparse", "typer", "rich"]),

        ("typer", "Typer",
         "CLI from type hints. Built on Click, same author as FastAPI. Cleanest modern option.",
         "import typer\n\napp = typer.Typer()\n\n@app.command()\ndef hello(name: str, age: int = 0):\n    print(f'Hi {name}, {age}')\n\nif __name__ == '__main__':\n    app()",
         [("type-driven", "args from hints"),
          ("FastAPI-style DX", "same author"),
          ("Click underneath", "compatibility"),
          ("Annotated[..., typer.Option(...)]", "rich options"),
          ("auto --help", "from docstrings"),
          ("Rich integration", "pretty output")],
         ["click", "argparse", "rich"]),

        ("rich", "Rich + Textual",
         "Rich: beautiful terminal output (colors, tables, progress bars, syntax highlighting). Textual: full TUI apps.",
         "from rich.console import Console\nfrom rich.table import Table\nconsole = Console()\nt = Table('Name', 'HP')\nt.add_row('Pika', '35')\nconsole.print(t)\nconsole.log('[bold red]error[/]')",
         [("Console", "smart print"),
          ("Table · Tree · Panel", "structured output"),
          ("Progress", "progress bars"),
          ("Syntax", "code highlighting"),
          ("[bold red]markup[/]", "inline styles"),
          ("Textual", "full TUI framework")],
         ["typer", "click", "logging"]),
    ]),
]


# ----------------------------------------------------------------------
# Template
# ----------------------------------------------------------------------

TOPIC_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} — Python Roadmap</title>
<link rel="stylesheet" href="../../../assets/style.css">
</head>
<body>
<div class="stage">
  <div class="footer-tag">{cat_label} · {title}</div>

  <!-- 1: Title -->
  <div class="slide active center-all">
    <div class="pill {pill_class}">{badge}</div>
    <div class="emoji">{emoji}</div>
    <h1>{title}</h1>
    <p class="big" style="margin-top:.6em;color:var(--accent-2);">{cat_label}</p>
  </div>

  <!-- 2: Why care -->
  <div class="slide">
    <div class="pill">Why</div>
    <h2>Why this matters</h2>
    <p class="big" style="margin-top:.4em">{summary}</p>
  </div>

  <!-- 3: Concept -->
  <div class="slide">
    <div class="pill">Concept</div>
    <h2>What is it?</h2>
    <div class="topic-grid" style="margin-top:.4em">
      <div class="topic-chip"><div class="head">{first_head}</div><div class="desc">{first_desc}</div></div>
      <div class="topic-chip"><div class="head">{second_head}</div><div class="desc">{second_desc}</div></div>
    </div>
    <p style="margin-top:.8em;font-size:clamp(14px,2.2vmin,17px);opacity:.85">{summary}</p>
  </div>

  <!-- 4: Code -->
  <div class="slide">
    <div class="pill">Code</div>
    <h2>Example</h2>
<pre>{code}</pre>
  </div>

  <!-- 5: Core points -->
  <div class="slide">
    <div class="pill">Core</div>
    <h2>Core points</h2>
    <div class="topic-grid three" style="margin-top:.4em">
{bullets_core}
    </div>
  </div>

  <!-- 6: More -->
  <div class="slide">
    <div class="pill">More</div>
    <h2>Going deeper</h2>
    <div class="topic-grid three" style="margin-top:.4em">
{bullets_more}
    </div>
  </div>

  <!-- 7: Edge cases -->
  <div class="slide">
    <div class="pill">⚠ Edge cases</div>
    <h2>Gotchas + pitfalls</h2>
    <div class="edge-grid">
{edge_cards}
    </div>
  </div>

  <!-- 8: Debug — buggy code -->
  <div class="slide">
    <div class="pill">🐛 Debug</div>
    <h2>What's wrong with this code?</h2>
    <div class="debug-box">
      <div class="debug-tag">buggy</div>
<pre style="margin-top:.4em">{debug_code}</pre>
    </div>
    <p style="margin-top:.6em;font-size:clamp(14px,2.2vmin,17px);opacity:.85">Think first — then click next.</p>
  </div>

  <!-- 9: Debug reveal -->
  <div class="slide">
    <div class="pill">🐛 Debug</div>
    <h2>The bug</h2>
    <div class="debug-reveal">{debug_bug}</div>
    <div class="debug-box" style="margin-top:.7em">
      <div class="debug-tag fix">fixed</div>
<pre style="margin-top:.4em">{debug_fix}</pre>
    </div>
  </div>

{mcq_slides}

  <!-- MCQ score -->
  <div class="slide center-all mcq-score">
    <div class="pill purple">Quiz</div>
    <h2>Your score</h2>
    <div class="score-val">0 / {mcq_count}</div>
    <p class="score-msg">Answer the questions to see your score.</p>
    <button class="quiz-reset">↺ retake</button>
  </div>

  <!-- Related -->
  <div class="slide">
    <div class="pill purple">Related</div>
    <h2>What next?</h2>
    <p style="margin-top:.6em;font-size:clamp(15px,2.5vmin,19px);line-height:1.7">
      {related}
    </p>
    <p style="margin-top:1em;font-size:clamp(13px,2vmin,16px);opacity:.7">
      <a href="../index.html" style="color:var(--accent);text-decoration:none">← all topics</a>
      &nbsp;·&nbsp;
      <a href="../../../all-slides.html" style="color:var(--accent);text-decoration:none">🗂 master library</a>
      &nbsp;·&nbsp;
      <a href="../../roadmap-mega.html" style="color:var(--accent);text-decoration:none">overview deck →</a>
    </p>
  </div>

  <!-- Coding practice (LAST per request) -->
  <div class="slide">
    <div class="pill">💻 Practice</div>
    <h2>Coding practice</h2>
    <div class="practice-task">{practice_task}</div>
    <div class="debug-box">
      <div class="debug-tag fix" style="background:var(--accent-2)">starter</div>
<pre style="margin-top:.4em">{practice_starter}</pre>
    </div>
    <p class="practice-hint">Open your editor. Save as <code>practice.py</code>. Run it. Iterate.</p>
  </div>

  <!-- Close -->
  <div class="slide center-all">
    <div class="emoji">{emoji}</div>
    <h1 style="font-size:clamp(34px,5.5vmin,52px)">{title}</h1>
    <p class="big" style="margin-top:.5em;color:var(--accent-2);">Done. Next topic →</p>
  </div>

  <div class="nav">
    <button id="prev" aria-label="prev">‹</button>
    <span class="counter" id="counter">1 / N</span>
    <button id="next" aria-label="next">›</button>
  </div>
</div>
<script src="../../../assets/deck.js"></script>
</body>
</html>
"""

MCQ_SLIDE = """  <!-- MCQ {n} -->
  <div class="slide mcq" data-correct="{correct}" data-explain="{explain}">
    <div class="pill purple">📝 Quiz</div>
    <div class="qmeta">Question {n} of {total}</div>
    <div class="q">{question}</div>
    <div class="opts">
{options}
    </div>
    <div class="qfeedback"></div>
  </div>"""

INDEX_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Python Roadmap — All Topics</title>
<link rel="stylesheet" href="../../assets/style.css">
<style>
  html, body {{ overflow: auto; display: block; height: auto; }}
  .stage {{ position: static; width: min(96vw, 1100px); aspect-ratio: auto; height: auto; min-height: 100vh; margin: 0 auto; padding: 2em 0; }}
  .slide {{ position: static; opacity: 1; transform: none; padding: 5vmin; display: block !important; }}
  .cat-block {{ margin-top: 1.8em; }}
  .cat-head {{ display:flex; align-items:center; gap:.6em; margin-bottom:.4em; }}
  .cat-head h3 {{ margin: 0; font-size: clamp(20px, 3.4vmin, 28px); }}
  .topic-list {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); gap: .4em .8em; }}
  .topic-list a {{
    display: block; padding: .6em .8em; border: 1px solid var(--border, #444);
    border-radius: 8px; text-decoration: none; color: inherit;
    background: var(--card-bg, rgba(255,255,255,.02));
    transition: all .15s;
  }}
  .topic-list a:hover {{
    border-color: var(--accent); background: rgba(255,255,255,.05);
  }}
  .topic-list a .num {{ opacity: .5; font-size: .85em; margin-right: .4em; }}
  .toplinks {{ display:flex; gap:1em; margin-top: .8em; font-size: clamp(13px,2vmin,16px); }}
  .toplinks a {{ color: var(--accent); }}
</style>
</head>
<body>
<div class="stage">
  <div class="slide active">
    <div class="pill purple">All Topics</div>
    <h1 style="font-size:clamp(34px,5vmin,48px);">Python Roadmap</h1>
    <p style="font-size:clamp(15px,2.5vmin,18px);opacity:.85;max-width:60ch;">
      {n_topics} topics across 19 stages, based on roadmap.sh/python.
      Each topic is one page with a summary, code, key points, and links to related topics.
    </p>
    <div class="toplinks">
      <a href="../roadmap-mega.html">📊 Overview deck →</a>
      <a href="../index.html">🗂 Course slides →</a>
      <a href="https://roadmap.sh/python" target="_blank" rel="noopener">🌐 roadmap.sh/python →</a>
    </div>

{category_blocks}

    <p style="margin-top:2em;opacity:.6;font-size:clamp(12px,1.8vmin,14px)">
      Source: <a href="https://roadmap.sh/python" style="color:var(--accent)">roadmap.sh/python</a>
    </p>
  </div>
</div>
</body>
</html>
"""


# ----------------------------------------------------------------------
# Generator
# ----------------------------------------------------------------------

def make_bullets(bullets):
    """N bullets in topic-chip format."""
    lines = []
    for head, desc in bullets:
        lines.append(
            f'      <div class="topic-chip"><div class="head">{html.escape(head)}</div>'
            f'<div class="desc">{html.escape(desc)}</div></div>'
        )
    return "\n".join(lines)


# ----------------------------------------------------------------------
# Auto-derivation for new fields
# ----------------------------------------------------------------------

WARNING_RE = re.compile(
    r"\b(never|avoid|careful|always|must|danger|don.?t|raises?|error|gotcha|"
    r"pitfall|beware|note|caution|warning|crash|break|fail|wrong|forget)\b",
    re.IGNORECASE,
)


def derive_edge_cases(bullets, title):
    """Pull warning-flavored bullets first; pad with rest. Returns 4-5."""
    warnings = []
    rest = []
    for head, desc in bullets:
        text = f"{head} {desc}"
        if WARNING_RE.search(text):
            warnings.append((head, desc))
        else:
            rest.append((head, desc))
    edges = warnings + rest
    if len(edges) < 4:
        # Add generic edges
        edges = edges + [
            ("Read the error", f"When {title} fails, the traceback names the line + type."),
            ("Small test first", "Try a tiny example before applying to a big project."),
        ]
    return edges[:5]


# Per-category "introduce a typo" patterns (preserved order matters)
GENERIC_BUGS = [
    # (find, replace_with, explanation)
    ("print(", "pirnt(", "Typo: <code>pirnt</code> is not defined. Python raises <code>NameError</code>. Spell built-in functions exactly."),
    ("len(", "lenght(", "Typo: <code>lenght</code> is not a real function — the built-in is <code>len()</code> (no 'gh')."),
    ("range(", "rage(", "Typo: <code>rage</code> is not defined. Python's loop helper is <code>range()</code>."),
    (".append(", ".apend(", "Typo: list method is <code>append</code> (two p's). <code>.apend()</code> raises <code>AttributeError</code>."),
    (".strip(", ".stip(", "Typo: string method is <code>.strip()</code>, not <code>.stip()</code> — AttributeError."),
    ("import ", "improt ", "Typo: keyword is <code>import</code>, not <code>improt</code>. Python raises <code>SyntaxError</code>."),
    ("return ", "retrun ", "Typo: keyword is <code>return</code>. <code>retrun</code> is treated as a variable name → NameError."),
    ("True", "true", "Python booleans are <code>True</code> / <code>False</code> (capitalized). Lowercase <code>true</code> is undefined → NameError."),
    ("None", "none", "Python's null is <code>None</code> (capital N). Lowercase <code>none</code> is undefined → NameError."),
    (" == ", " = ", "Used <code>=</code> (assignment) instead of <code>==</code> (comparison). Inside an <code>if</code>, this is a <code>SyntaxError</code>."),
    ("for ", "fore ", "Typo: keyword is <code>for</code>, not <code>fore</code>. SyntaxError."),
    ("def ", "dfe ", "Typo: keyword is <code>def</code>, not <code>dfe</code>. SyntaxError."),
]


def derive_debug(code, title):
    """Return (buggy_code, bug_html, fix_code)."""
    for find, repl, expl in GENERIC_BUGS:
        if find in code:
            buggy = code.replace(find, repl, 1)
            return buggy, f"<b>Bug:</b> {expl}", code
    # Fallback: drop the last line's indentation
    lines = code.split("\n")
    for i in range(1, len(lines)):
        if lines[i].startswith("    "):
            buggy_lines = list(lines)
            buggy_lines[i] = lines[i][2:]  # remove 2 spaces (wrong indent)
            return (
                "\n".join(buggy_lines),
                "<b>Bug:</b> <code>IndentationError</code>. The indented line uses 2 spaces instead of 4. "
                "Python is strict — keep indentation consistent (PEP 8 says 4 spaces).",
                code,
            )
    # Final fallback: trailing colon issue
    return (
        code.replace(":", "", 1) if ":" in code else code + "  # missing newline?",
        "<b>Bug:</b> a required <code>:</code> after a block statement is missing. Python raises <code>SyntaxError</code>.",
        code,
    )


def gen_mcq_definition(title, summary, bullets):
    """Q: which describes {title}?"""
    correct = summary if len(summary) < 130 else summary.split(".")[0] + "."
    distractors = [
        f"A deprecated alias for the {bullets[0][0]} statement, removed in Python 3.",
        f"A Python 2-only feature; modern code uses something else.",
        f"A built-in keyword reserved for class definitions only.",
    ]
    return (
        f"Which best describes <b>{html.escape(title)}</b>?",
        [correct] + distractors,
        0,
        "Definition straight from the topic summary.",
    )


def gen_mcq_truth(title, bullets):
    """Q: which of these is TRUE about {title}?"""
    head, desc = bullets[0]
    correct = f"{head} — {desc}"
    distractors = [
        f"It only works on Python 2.7 and earlier.",
        f"It cannot be combined with any other feature.",
        f"It must be declared at the top of every file.",
    ]
    return (
        f"Which is TRUE about <b>{html.escape(title)}</b>?",
        [correct] + distractors,
        0,
        f"Key fact: {head}.",
    )


def gen_mcq_spotbug(buggy_code, bug_explanation):
    """Q: what's wrong with this code?"""
    short_expl = re.sub(r"<[^>]+>", "", bug_explanation).replace("Bug: ", "")
    return (
        f"What's wrong with this code?<br><pre style=\"font-size:.85em;margin-top:.5em\">{html.escape(buggy_code)}</pre>",
        [
            short_expl,
            "Nothing — the code is correct as-is.",
            "Missing <code>import sys</code> at the top.",
            "The variable was never declared with <code>let</code>.",
        ],
        0,
        "Spot the typo / mistake.",
    )


def gen_mcq_bullet(title, bullets, idx):
    """Q derived from bullet idx — which detail is correct?"""
    head, desc = bullets[idx]
    correct = f"{head} → {desc}"
    others = [
        f"{head} → something completely unrelated",
        f"{head} is reserved and cannot be used in user code",
        f"{head} works only in async functions",
    ]
    return (
        f"Which is the correct description of <code>{html.escape(head)}</code> in {html.escape(title)}?",
        [correct] + others,
        0,
        f"{head}: {desc}",
    )


def derive_mcqs(topic, complexity):
    """Generate 3-8 MCQs based on complexity (1-3 -> 3 questions, 4 -> 5, 5+ -> 7)."""
    slug, title, summary, code, bullets, related = topic[:6]

    target = 3
    if complexity >= 5:
        target = 7
    elif complexity >= 4:
        target = 5

    mcqs = []
    mcqs.append(gen_mcq_definition(title, summary, bullets))
    mcqs.append(gen_mcq_truth(title, bullets))

    buggy, expl, _fix = derive_debug(code, title)
    mcqs.append(gen_mcq_spotbug(buggy, expl))

    # Extra questions from remaining bullets
    for i in range(1, min(len(bullets), target - 3 + 1)):
        if len(mcqs) >= target:
            break
        mcqs.append(gen_mcq_bullet(title, bullets, i))

    return mcqs[:target]


def derive_practice(code, title, category):
    """Return (task_text, starter_code)."""
    task_templates = [
        f"Extend the example: add one more case that uses <b>{html.escape(title)}</b> in a different way. Print the result.",
        f"Take the example and turn it into a small function. Call the function with two different inputs.",
        f"Combine this with a feature from a previous topic (lists, dicts, or loops). Build something tiny that prints something useful.",
        f"Reproduce the example by typing — no copy/paste. Then change one thing and predict the output before running.",
    ]
    # Pick deterministically by title hash
    idx = sum(ord(c) for c in title) % len(task_templates)
    task = task_templates[idx]
    starter = code + "\n\n# Your turn: extend the example below this line.\n"
    return task, starter


def make_mcq_options(opts):
    """HTML buttons for MCQ options."""
    lines = []
    for o in opts:
        # Allow code/HTML in options; escape only if no tags
        if "<" not in o:
            o = html.escape(o)
        lines.append(f'      <button class="opt">{o}</button>')
    return "\n".join(lines)


def make_mcq_slides(mcqs):
    """Render all MCQ slides."""
    slides = []
    total = len(mcqs)
    for n, (q, opts, correct, explain) in enumerate(mcqs, start=1):
        slides.append(MCQ_SLIDE.format(
            n=n,
            total=total,
            correct=correct,
            explain=html.escape(explain).replace("\n", " "),
            question=q,
            options=make_mcq_options(opts),
        ))
    return "\n".join(slides)


def make_edge_cards(edges):
    cards = []
    for head, desc in edges:
        cards.append(
            f'      <div class="edge-card"><div class="ehead">{html.escape(head)}</div>'
            f'<div class="edesc">{html.escape(desc)}</div></div>'
        )
    return "\n".join(cards)


def slugify(s):
    return re.sub(r"[^a-z0-9-]", "-", s.lower())


def make_related(category_dir, all_slugs, related_slugs):
    links = []
    for s in related_slugs:
        # try same category first, then any
        target = all_slugs.get(s)
        if target:
            rel_cat, rel_file = target
            if rel_cat == category_dir:
                href = f"{rel_file}.html"
            else:
                href = f"../{rel_cat}/{rel_file}.html"
            label = rel_file.replace("-", " ")
            links.append(f'<a href="{href}">{label}</a>')
        else:
            # placeholder — keep so we see what's missing
            links.append(f'<span style="opacity:.5">{s}</span>')
    return " · ".join(links)


def generate():
    # First pass: build slug → (category, file) map
    all_slugs = {}
    total = 0
    for cat_dir, cat_label, topics in CATEGORIES:
        for slug, *_ in topics:
            all_slugs[slug] = (cat_dir, slug)
            total += 1

    # Second pass: write files
    written = 0
    for cat_idx, (cat_dir, cat_label, topics) in enumerate(CATEGORIES, start=1):
        outdir = HERE / cat_dir
        outdir.mkdir(parents=True, exist_ok=True)

        for topic_idx, topic in enumerate(topics, start=1):
            slug, title, summary, code, bullets, related = topic

            # Normalize related (may be tuple by mistake)
            if isinstance(related, tuple):
                related = list(related)

            badge = f"{cat_idx}.{topic_idx}"
            pill_class = "purple" if cat_idx > 14 else ""
            emoji = CATEGORY_EMOJI.get(cat_dir, "🐍")

            # Split bullets in half: core (first half) + more (second half)
            mid = (len(bullets) + 1) // 2
            bullets_core = bullets[:mid]
            bullets_more = bullets[mid:]

            # First two bullets used as concept-slide chips
            first_head, first_desc = bullets[0]
            second_head, second_desc = bullets[1] if len(bullets) > 1 else bullets[0]

            # Complexity = rough heuristic for # of MCQs
            complexity = 3
            if cat_idx in (9, 10, 11, 14):   # OOP, advanced, DSA, concurrency
                complexity = 5
            elif cat_idx in (15, 16):         # web, data/ml
                complexity = 4

            edge_cases = derive_edge_cases(bullets, title)
            buggy_code, bug_html, fix_code = derive_debug(code, title)
            mcqs = derive_mcqs(topic, complexity)
            practice_task, practice_starter = derive_practice(code, title, cat_label)

            mcq_slides_html = make_mcq_slides(mcqs)

            html_out = TOPIC_HTML.format(
                title=html.escape(title),
                cat_label=html.escape(cat_label),
                pill_class=pill_class,
                badge=badge,
                emoji=emoji,
                summary=html.escape(summary),
                code=html.escape(code),
                first_head=html.escape(first_head),
                first_desc=html.escape(first_desc),
                second_head=html.escape(second_head),
                second_desc=html.escape(second_desc),
                bullets_core=make_bullets(bullets_core),
                bullets_more=make_bullets(bullets_more),
                edge_cards=make_edge_cards(edge_cases),
                debug_code=html.escape(buggy_code),
                debug_bug=bug_html,
                debug_fix=html.escape(fix_code),
                mcq_slides=mcq_slides_html,
                mcq_count=len(mcqs),
                practice_task=practice_task,
                practice_starter=html.escape(practice_starter),
                related=make_related(cat_dir, all_slugs, related),
            )

            (outdir / f"{slug}.html").write_text(html_out, encoding="utf-8")
            written += 1

    # Build index
    blocks = []
    for cat_idx, (cat_dir, cat_label, topics) in enumerate(CATEGORIES, start=1):
        items = []
        for topic_idx, (slug, title, *_) in enumerate(topics, start=1):
            items.append(
                f'        <a href="{cat_dir}/{slug}.html">'
                f'<span class="num">{cat_idx}.{topic_idx}</span>{html.escape(title)}</a>'
            )
        block = (
            f'    <div class="cat-block">\n'
            f'      <div class="cat-head"><h3>{html.escape(cat_label)}</h3>'
            f'<span style="opacity:.5">· {len(topics)} topics</span></div>\n'
            f'      <div class="topic-list">\n'
            f'{chr(10).join(items)}\n'
            f'      </div>\n'
            f'    </div>'
        )
        blocks.append(block)

    index_out = INDEX_HTML.format(
        n_topics=total,
        category_blocks="\n".join(blocks),
    )
    (HERE / "index.html").write_text(index_out, encoding="utf-8")
    written += 1

    print(f"wrote {written} files ({total} topics + 1 index) under {HERE}")

    # Build master hub
    n_master = generate_master_hub()
    print(f"wrote master hub with {n_master} slides indexed")


# ----------------------------------------------------------------------
# Master Hub — scans ALL .html slides in repo + emits filterable index
# ----------------------------------------------------------------------

# english-coding-slides root (two levels up from roadmap/)
ROOT = HERE.parent.parent

TITLE_RE = re.compile(r"<title>(.*?)</title>", re.IGNORECASE | re.DOTALL)

# Mapping from roadmap category dir -> human stage label + emoji
ROADMAP_CAT_LABEL = {cd: lbl for cd, lbl, _ in CATEGORIES}


def extract_title(path: Path) -> str:
    try:
        txt = path.read_text(encoding="utf-8", errors="ignore")
        m = TITLE_RE.search(txt)
        if m:
            t = m.group(1).strip()
            # strip common suffixes like " — Python Roadmap"
            t = re.sub(r"\s*[—\-·|]\s*Python\s*Roadmap.*$", "", t)
            return t
    except Exception:
        pass
    return path.stem.replace("-", " ").title()


def classify(rel_path: str):
    """Return (track, course, week, stage, domain, tags[]) for a file path
    relative to english-coding-slides root."""
    p = rel_path.replace("\\", "/")
    tags = []
    track = course = week = stage = domain = None

    # Python curriculum courses
    m = re.match(r"python/rs(\d+)-([^/]+)/week-(\d+)", p)
    if m:
        n = m.group(1)
        course = f"RS{n}"
        week = f"W{int(m.group(3))}"
        track = "Curriculum"
        domain = "Python"
        tags += [course, week, domain, track]
        return track, course, week, None, domain, tags

    # Web courses
    m = re.match(r"webdev/web(\d+)-([^/]+)/week-(\d+)", p)
    if m:
        n = m.group(1)
        course = f"WEB{n}"
        week = f"W{int(m.group(3))}"
        track = "Curriculum"
        domain = "Web"
        tags += [course, week, domain, track]
        return track, course, week, None, domain, tags

    # AI courses
    m = re.match(r"ai-coding/ai(\d+)-([^/]+)/week-(\d+)", p)
    if m:
        n = m.group(1)
        course = f"AI{n}"
        week = f"W{int(m.group(3))}"
        track = "Curriculum"
        domain = "AI"
        tags += [course, week, domain, track]
        return track, course, week, None, domain, tags

    # Roadmap topic pages
    m = re.match(r"python/roadmap/(\d{2}-[^/]+)/([^/]+)\.html$", p)
    if m:
        cat_dir = m.group(1)
        cat_label = ROADMAP_CAT_LABEL.get(cat_dir, cat_dir)
        # Stage X · Name → "Stage X"
        sm = re.match(r"Stage\s+(\d+)", cat_label)
        if sm:
            stage = f"Stage {sm.group(1)}"
        track = "Roadmap"
        domain = "Python"
        # category short name
        cat_short = cat_label.split("·", 1)[-1].strip() if "·" in cat_label else cat_label
        tags += [track, domain, stage or cat_short, cat_short]
        return track, None, None, stage, domain, tags

    # Roadmap mega deck
    if p == "python/roadmap-mega.html":
        return "Roadmap", None, None, None, "Python", ["Roadmap", "Python", "Overview"]

    # Roadmap index
    if p == "python/roadmap/index.html":
        return "Roadmap", None, None, None, "Python", ["Roadmap", "Python", "Index"]

    # Glossary / root index
    if p == "glossary.html":
        return "Reference", None, None, None, "Mixed", ["Reference", "Glossary"]
    if p == "index.html":
        return "Reference", None, None, None, "Mixed", ["Reference", "Hub"]

    return "Other", None, None, None, None, ["Other"]


COURSE_EMOJI = {
    "RS001": "📖", "RS002": "📦", "RS003": "🎯", "RS004": "🕹",
    "WEB001": "🎨", "WEB002": "⚡", "WEB003": "🌐",
    "AI001": "🤖",
}


def scan_slides():
    """Walk english-coding-slides for every .html, return list of dicts."""
    entries = []
    for html_path in sorted(ROOT.rglob("*.html")):
        rel = html_path.relative_to(ROOT)
        rel_str = str(rel).replace("\\", "/")
        # skip generator script's own output we don't want to surface
        if rel_str == "all-slides.html":
            continue
        track, course, week, stage, domain, tags = classify(rel_str)
        title = extract_title(html_path)
        # build pill emoji
        if course:
            emoji = COURSE_EMOJI.get(course, "📑")
        elif track == "Roadmap":
            # try to find category emoji
            m = re.match(r"python/roadmap/(\d{2}-[^/]+)/", rel_str)
            emoji = CATEGORY_EMOJI.get(m.group(1), "🐍") if m else "🐍"
        else:
            emoji = "📑"

        entries.append({
            "path": rel_str,
            "title": title,
            "track": track,
            "course": course,
            "week": week,
            "stage": stage,
            "domain": domain,
            "tags": [t for t in tags if t],
            "emoji": emoji,
        })
    return entries


MASTER_HUB_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>English Coding · Slide Library</title>
<link rel="stylesheet" href="assets/style.css">
<style>
  html, body { overflow: auto; display: block; height: auto; background: #1f1f2e; }
  body { font-family: "Inter", -apple-system, "Segoe UI", system-ui, sans-serif; color: #f4f0e8; padding: 0; margin: 0; }
  .wrap { max-width: 1280px; margin: 0 auto; padding: 2em 1.5em 4em; }
  header { display:flex; align-items:baseline; justify-content:space-between; gap:1em; flex-wrap:wrap; }
  header h1 { font-size: clamp(28px, 4vmin, 42px); margin: 0; }
  header .sub { opacity: .7; font-size: clamp(13px, 2vmin, 16px); }
  .count { opacity: .65; font-size: clamp(13px, 2vmin, 16px); margin-top:.3em; }

  .search {
    width: 100%; max-width: 380px; padding: .55em .9em;
    border-radius: 999px; border: 1px solid #444;
    background: rgba(255,255,255,.06); color: inherit;
    font-size: 15px; outline: none;
  }
  .search:focus { border-color: #ff7849; }

  .tag-section { margin-top: 1.4em; }
  .tag-section h3 {
    margin: 0 0 .35em; font-size: 12px; letter-spacing: .12em;
    text-transform: uppercase; opacity: .55; font-weight: 600;
  }
  .tag-row { display: flex; flex-wrap: wrap; gap: .35em .4em; }
  .tag {
    cursor: pointer; user-select: none;
    padding: .35em .8em; border-radius: 999px;
    border: 1px solid #444; background: rgba(255,255,255,.04);
    font-size: 13px; color: inherit;
    transition: all .12s;
  }
  .tag:hover { border-color: #ff7849; }
  .tag.active {
    background: #ff7849; color: #1a1a2e; border-color: #ff7849; font-weight: 600;
  }
  .tag .n { opacity: .55; margin-left: .3em; font-size: 11px; }
  .tag.active .n { opacity: .8; color: #1a1a2e; }

  .reset {
    margin-top: .8em; cursor: pointer;
    font-size: 13px; color: #ff7849; background: none; border: none;
    padding: 0;
  }
  .reset:hover { text-decoration: underline; }

  .grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
    gap: .8em;
    margin-top: 1.6em;
  }
  .card {
    display: block; padding: 1em; border-radius: 14px;
    background: rgba(255,255,255,.04);
    border: 1px solid #444;
    text-decoration: none; color: inherit;
    transition: all .12s;
  }
  .card:hover {
    border-color: #ff7849; background: rgba(255,120,73,.08);
    transform: translateY(-1px);
  }
  .card .ico { font-size: 22px; }
  .card .pill {
    display: inline-block; background: #6b4ee6; color: #fff;
    padding: .15em .55em; border-radius: 999px; font-size: 11px;
    font-weight: 600; letter-spacing: .04em; margin-right: .3em;
  }
  .card .pill.orange { background: #ff7849; }
  .card .pill.gray { background: #444; }
  .card h4 {
    margin: .4em 0 .25em; font-size: 16px; line-height: 1.25;
  }
  .card .tags { font-size: 11px; opacity: .55; margin-top: .35em; }
  .card .tags span { margin-right: .4em; }

  .empty { padding: 3em; text-align: center; opacity: .55; font-style: italic; }
</style>
</head>
<body>
<div class="wrap">
  <header>
    <div>
      <h1>📚 English Coding · Slide Library</h1>
      <div class="sub">Every slide deck in one place. Click a tag to filter.</div>
    </div>
    <input class="search" id="search" placeholder="🔎  search title..." />
  </header>
  <div class="count" id="count"></div>

__TAGSECTIONS__

  <button class="reset" id="reset">↺ clear filters</button>

  <div class="grid" id="grid">
__CARDS__
  </div>

  <div class="empty" id="empty" style="display:none">no slides match</div>
</div>

<script>
const cards = document.querySelectorAll('.card');
const tags = document.querySelectorAll('.tag');
const search = document.getElementById('search');
const count = document.getElementById('count');
const empty = document.getElementById('empty');
const grid = document.getElementById('grid');
const resetBtn = document.getElementById('reset');

const activeFilters = new Set();
const filterGroups = {};  // group -> Set of active tags

tags.forEach(t => {
  t.addEventListener('click', () => {
    const tag = t.dataset.tag;
    const group = t.dataset.group;
    if (!filterGroups[group]) filterGroups[group] = new Set();
    if (filterGroups[group].has(tag)) {
      filterGroups[group].delete(tag);
      t.classList.remove('active');
    } else {
      filterGroups[group].add(tag);
      t.classList.add('active');
    }
    applyFilters();
  });
});

resetBtn.addEventListener('click', () => {
  Object.values(filterGroups).forEach(s => s.clear());
  tags.forEach(t => t.classList.remove('active'));
  search.value = '';
  applyFilters();
});

search.addEventListener('input', applyFilters);

function applyFilters() {
  const q = search.value.trim().toLowerCase();
  let shown = 0;
  cards.forEach(c => {
    const cardTags = (c.dataset.tags || '').split(',').filter(Boolean);
    const cardTitle = (c.dataset.title || '').toLowerCase();

    let match = true;
    // each filter group: card must match AT LEAST ONE tag in group (OR within group)
    // across groups: AND
    for (const [group, set] of Object.entries(filterGroups)) {
      if (set.size === 0) continue;
      const has = [...set].some(t => cardTags.includes(t));
      if (!has) { match = false; break; }
    }
    if (match && q) {
      match = cardTitle.includes(q);
    }
    c.style.display = match ? '' : 'none';
    if (match) shown++;
  });
  count.textContent = `${shown} of ${cards.length} slides`;
  empty.style.display = shown === 0 ? '' : 'none';
}

applyFilters();
</script>
</body>
</html>
"""


def render_tag_sections(entries):
    """Build tag chip sections grouped by Track / Course / Week / Stage / Domain."""
    groups = {
        "Track": [],
        "Domain": [],
        "Course": [],
        "Week": [],
        "Stage": [],
    }
    counters = {g: {} for g in groups}
    for e in entries:
        if e["track"]:    counters["Track"][e["track"]] = counters["Track"].get(e["track"], 0) + 1
        if e["domain"]:   counters["Domain"][e["domain"]] = counters["Domain"].get(e["domain"], 0) + 1
        if e["course"]:   counters["Course"][e["course"]] = counters["Course"].get(e["course"], 0) + 1
        if e["week"]:     counters["Week"][e["week"]] = counters["Week"].get(e["week"], 0) + 1
        if e["stage"]:    counters["Stage"][e["stage"]] = counters["Stage"].get(e["stage"], 0) + 1

    def sort_key(group, tag):
        if group == "Week":
            return int(tag[1:])
        if group == "Stage":
            return int(tag.split()[1])
        if group == "Course":
            # RS first, then WEB, then AI; within each, by number
            order = {"R": 0, "W": 1, "A": 2}
            return (order.get(tag[0], 3), int(re.sub(r"\D", "", tag) or 0))
        return tag

    sections = []
    for group, _ in groups.items():
        items = sorted(counters[group].items(), key=lambda kv: sort_key(group, kv[0]))
        if not items:
            continue
        chips = "\n".join(
            f'      <button class="tag" data-group="{group}" data-tag="{html.escape(t)}">'
            f'{html.escape(t)}<span class="n">{n}</span></button>'
            for t, n in items
        )
        sections.append(
            f'  <div class="tag-section">\n'
            f'    <h3>{group}</h3>\n'
            f'    <div class="tag-row">\n{chips}\n    </div>\n'
            f'  </div>'
        )
    return "\n".join(sections)


def render_card(entry):
    course_pill = ""
    if entry["course"]:
        course_pill = f'<span class="pill orange">{html.escape(entry["course"])}</span>'
    elif entry["track"] == "Roadmap":
        course_pill = '<span class="pill">Roadmap</span>'
    elif entry["track"] == "Reference":
        course_pill = '<span class="pill gray">Ref</span>'
    else:
        course_pill = '<span class="pill gray">Slide</span>'

    week_pill = f'<span class="pill gray">{html.escape(entry["week"])}</span>' if entry["week"] else ""
    stage_pill = f'<span class="pill gray">{html.escape(entry["stage"])}</span>' if entry["stage"] else ""

    tags_attr = ",".join(entry["tags"])
    tag_str = " ".join(f"<span>#{html.escape(t)}</span>" for t in entry["tags"][:4])

    return (
        f'    <a class="card" href="{html.escape(entry["path"])}" target="_blank" '
        f'data-tags="{html.escape(tags_attr)}" data-title="{html.escape(entry["title"])}">\n'
        f'      <div class="ico">{entry["emoji"]}</div>\n'
        f'      <div>{course_pill}{week_pill}{stage_pill}</div>\n'
        f'      <h4>{html.escape(entry["title"])}</h4>\n'
        f'      <div class="tags">{tag_str}</div>\n'
        f'    </a>'
    )


def generate_master_hub():
    entries = scan_slides()
    cards = "\n".join(render_card(e) for e in entries)
    tag_sections = render_tag_sections(entries)
    out = (MASTER_HUB_HTML
           .replace("__TAGSECTIONS__", tag_sections)
           .replace("__CARDS__", cards))
    (ROOT / "all-slides.html").write_text(out, encoding="utf-8")
    return len(entries)


if __name__ == "__main__":
    generate()
