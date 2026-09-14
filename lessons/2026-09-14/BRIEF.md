# Today's decks — 2026-09-14 (Mon)

Times are Korea first, Ho Chi Minh second (KST − 2).

**Calendar is the source of truth for times.** Tracker drift is noted per student.
**EUNWOO is in the tracker on Monday 19:00 but has no Monday calendar event and every
ledger row is a Wednesday — not taught today, no deck, no message.**

**Kasim's instruction this morning, verbatim:** *"Amy is doiing IDE python. Neo IDE python
but we are doing data analysis using pandas and numpy. Jun is doing MC Blocks. Ethan is
doing IDE Python. Yunho is doing MC Python. And then the tech an ddebate class which is
week 3."*

He named **tracks**, and for NEO he named the **topic**. For AMY, ETHAN, YUNHO and JUN no
topic was named, so each takes the Idea line put to him in the walkthrough. Two of his
instructions are **track changes** and both are flagged below.

| Time | Student | Track | Today's topic | File |
|---|---|---|---|---|
| 16:00 KST · 14:00 HCMC | AMY | IDE Python | draw hp as ♥ hearts, then `while hp > 0` — the fight that repeats until game over | `amy-the-fight-that-repeats.html` |
| 17:00 KST · 15:00 HCMC | NEO | IDE Python — **DATA ANALYSIS, new track** | pandas + numpy — a table you can ask questions of | `neo-a-table-that-answers.html` |
| 18:00 KST · 16:00 HCMC | JUN | Minecraft **BLOCKS** — **track change, was Python** | the loop inside a loop, drawn as blocks, then one **variable** resizes the whole build | `jun-one-number-builds-it-all.html` |
| 19:00 KST · 17:00 HCMC | ETHAN | IDE Python | finish the three-way `elif` price fork, then drop the fork **inside** the `for` loop | `ethan-a-gate-on-the-belt.html` |
| 20:00 KST · 18:00 HCMC | YUNHO | Minecraft Python | maths on `i` — gaps, `range(a, b)`, then a loop **inside** a loop | `yunho-maths-on-the-counter.html` |
| 21:00 KST · 19:00 HCMC | LUCY & AMBER | Debate DB001 | Week 3 — Feeds That Choose For You · *They say ___. But ___.* | `../../debate/db001-tech-ai/week-03.html` (**exists already — reuse, do not rebuild**) |

**Not a lesson:** `SnC`, 11:00 KST · 09:00 HCMC. Left alone.

---

## Report-only drift — nothing was auto-fixed, no calendar event was renamed

- **ETHAN** — calendar says Monday **19:00**, `tools_students.slot_time` says **21:00**.
  The calendar is right; last Monday's lesson also ran at 19:00 and the Drive transcript
  confirms it. Tracker not edited.
- **EUNWOO COORDINATES** — `tools_students` has Monday 19:00. There is **no Monday calendar
  event**, and both ledger rows (2026-09-02, 2026-09-09) are Wednesdays. The real slot is
  Wednesday. Tracker not edited. **Separately: the 2026-09-09 homework and feedback are
  built but deliberately unsent, waiting on the mother's reply — do not rebuild, ask
  before sending.**
- **LUCY & AMBER (DB001)** — on the Monday calendar at 21:00, but `tools_students` still
  has this class on Friday and the `roster.json` folders are `lucy-debate-fri-2100` /
  `amber-debate-fri-2100`. The title matches Amber's alias exactly, so it is **not** a
  rename candidate. Left alone.
- **JUN MC** — `roster.json` has no track set, and the last deck was Minecraft **Python**
  (constant form, `agent.move(FORWARD, 5)`). Kasim says **blocks** today. Roster not
  edited; the deck follows Kasim.
- **No ledger file exists for JUN.** `/homework` has never run for him, so the last-lesson
  facts come from the tracker draft of 2026-08-31.
- No calendar renames were needed today — every lesson title already matches.

## Transcripts — what was read for this brief

| Student | Doc (GMT+7 title) | Real date | Days ago |
|---|---|---|---|
| AMY | `2026/09/07 13:59` | Mon 7 Sept | 7 |
| NEO | `2026/09/09 16:00` | Wed 9 Sept | 5 |
| JUN | **none since 31 Aug** | Sun 31 Aug | **14** |
| ETHAN | `2026/09/07 16:59` | Mon 7 Sept | 7 |
| YUNHO | `2026/09/07 18:00` | Mon 7 Sept | 7 |

**JUN had no lesson on 7 Sept** — Kasim cancelled it that morning. The last taught lesson
was 31 Aug, and no Drive transcript exists for that one either.

---

## Hard rules for every deck

Read first, in this order:
1. `../../TEMPLATE.md` — slot structures and per-slide rules
2. `../../PEDAGOGY.md` — why each slot exists
3. `../../assets/style.css` — the only styling allowed
4. The reference deck named in that student's section — tone and markup

Then:
- Save to `lessons/2026-09-14/<file>.html`. Stylesheet `../../assets/style.css`, script
  `../../assets/deck.js`. Slides are `<div class="slide">`, the first is
  `<div class="slide active center-all">`.
- **Copy-this-and-it-works.** The student makes zero decisions. If a slide needs the
  student to infer anything, it is wrong.
- **One change per slide**, numbered `STEP n / total`. A re-indent is its own step.
- Every code step carries all four: full **OLD** block and full **NEW** block (never `...`
  inside a changed region) · **🔍 FIND** the exact Ctrl+F string · **📍 where** (quote the
  existing line it goes under + the indent count) · **🟣 why** in one line · **✅ check** in
  one line (what running it should show).
- **Big programs ramp v1 → v2 → v3 → v4.** Never the finished program first. New lines hot,
  unchanged lines dim, changed lines get an explicit OLD/NEW block.
- **Visuals beat words, and are mandatory for loops, iteration and any maths** — one frame
  per pass with the counter value shown; spacing as boxes on a number line; x positions as
  jumps.
- **Overshoot, hard.** The deck must hold **far more than one lesson can get through**.
  **No slide-count target and no ceiling.** If the teacher could plausibly reach the last
  slide inside the hour, it is too short — go back and add taught ideas. Extra room goes on
  **new concepts with a visual each**, never on more debug cards. Unused slides roll on.
- **As few words as possible.** ≤ 40 English and ≤ 15 Korean words per slide.
- **Every deck teaches at least one new idea** — the one named in the table above. A
  homework check or a revisited mistake is a warm-up that leads into the new idea. It is
  never the whole lesson.
- **The lesson-to-lesson jump can be bigger than the homework's.** Kasim is in the room to
  bridge it. Build for a student being taught, not one working alone.
- **Never a gendered pronoun.** Use the student's name or *they*. No he/she/his/her anywhere.
- Only reuse existing CSS classes. No new inline component styling.
- Update the `counter` span to `1 / <total>` and the `footer-tag` date to 2026-09-14.

### The carry — read this before writing a single slide

Three of today's five students stopped a long way short of last week's deck. **Those
unreached slides are already written, already reviewed and already in that student's
voice. They come across verbatim.** Today's new ideas are built on top of them, not
instead of them. Never carry Slot 1 (title) or Slot 2 (Recap) — both are rebuilt from this
week's facts. Renumber everything after carrying: the `counter` span, every
`STEP n / total`, the `footer-tag` date, the Recap pill date, and the `<!-- N · SLOT -->`
comments.

---

## 16:00 KST · 14:00 HCMC · AMY — IDE Python

**Kasim's instruction: "Amy is doiing IDE python"** — track only, no topic. Concrete pick,
put to him and unchallenged: **draw hp as ♥ hearts, then `while hp > 0` — the fight that
repeats until game over.**

**Last deck:** `../2026-09-07/amy-keep-going-until.html` — 131 slides. Tone and markup
reference. Read it before writing.

### What Amy actually did last week (ledger 2026-09-07, from the Drive transcript)

- indented the fork so it sits **inside** the question
- echoed the typed answer back with an f-string
- read a `red_or_green is not defined` error and fixed it
- added `else` so any answer is caught
- added a second question, `give_or_not`, on the right-hand path
- `hp = 100`
- `hp = hp - 5`, then printed the health that is left

**Unmet last week:** the heart bar and the `while` loop never happened. Amy kept writing
story branches and asked to do health first, so both moved (transcript 00:34:07–00:35:26).
**This is the strongest single input to today's deck — it is the parent's outstanding
promise and it is the front of the carry.**

**Homework concept just practised:** `hp-damage-and-game-over-check`. Open by checking it
landed, in one or two slides, then move.

**Failure modes, from two weeks of records:**
- △ waits for Kasim to type instead of typing → keep at least four
  **"AMY WRITES THIS ONE ALONE"** slides
- △ spelling slips (typed `.title()` as `titile`) → 🔍 FIND strings must be **exact and short**
- ✓ visuals land — `==` vs `in` only clicked after a containment diagram

### The carry — slides that must come across

**Stop point: slide 16 of 131** (`STEP 2 / 40`, "Take a hit" — `hp = hp - 5`). Found from
the ledger `actual`, which is the transcript distilled, and confirmed by the ledger `gap`.
**Slides 17–131 were never reached.** Bring them across verbatim, then build on top:

- **17–23** — turn hp into hearts, how to type ♥, print the hearts, draw the bar, show the
  number, v1 whole file, "one hit is not a fight". **This is today's first new idea,
  already written.**
- **24–49** — the arrow that curls back, watching hp fall, the six rounds walked one frame
  at a time, writing the loop line, the four-space fence, v2 whole file, the three loop
  mistakes, "how many rounds?", changing the damage
- **50–64** — a fork inside a loop, three indent levels, the five step-slides that build
  it, v3 whole file, wrong-order and two-ifs mistakes
- **65–84** — `while` + `input()` keep-asking-until-valid, the `not in` gate, the damage
  box, block vs attack, v4 whole file
- **85–120** — `break`, the round counter, `+=` and `-=`, `randint(10, 25)` damage, monster
  health, `and`, the four endings, the whole battle game
- **121–131** — `or`, `while True`, the blanks, the quiz, "make it yours"

Nothing on that list was taught on 7 Sept, so nothing is dropped.

### Today's new ideas, in order

1. One slide: did the homework hp file run? (`hp-damage-and-game-over-check`)
2. **Hearts** — `"♥" * (hp // 20)`, the bar drawn as a visual first, then the code.
3. **`while hp > 0:`** — the loop that keeps the fight alive. Visual before code: one frame
   per pass with `hp` written on it, the arrow curling back, the exit door opening only
   when `hp` hits 0.
4. The `if` / `elif` / `else` fork moves **inside** the loop. Amy already owns the fork —
   the only new thing is the indent and the repeat.
5. Everything from the carry, in its existing order.

**Then overshoot past slide 131 with new taught ideas, each with its own visual:**
- a **list of monsters** and a `for` loop that fights them one after another
- `while True:` plus `break` as a menu — play again, or quit
- a turn limit: `while hp > 0 and turns < 10`

---

## 17:00 KST · 15:00 HCMC · NEO — IDE Python · DATA ANALYSIS (new track)

**Kasim's instruction: "Neo IDE python but we are doing data analysis using pandas and
numpy."** That is the topic, in his words, and it wins outright.

> **THE CARRY IS DROPPED, DELIBERATELY.** Neo's 2026-09-09 deck
> `../2026-09-09/neo-a-box-that-answers.html` is 106 slides and the lesson only reached
> about slide 8 — the session diverted into rotation instead. That leaves ~98 unreached
> slides on `return`, function defaults and two-value returns. **None of it is used
> today**, because Kasim has moved Neo to data analysis and his topic beats a saving. The
> return deck stays on disk and is still good; it is parked, not spent.

**Reference deck for tone and markup:** `../2026-09-09/neo-a-box-that-answers.html`. Read
it for voice and for the class names only — **not** for content.

### Who Neo is, and why this track fits

Neo is on the **entrance-exam track** (광주 AI 영재고 prep). Data analysis is exactly the
shape of thing that exam rewards, so lean into *asking a table a question* rather than
*typing pandas syntax*. Every step should end in a number Neo can read out loud.

### What Neo actually did last week (ledger 2026-09-09, from the Drive transcript)

- `math.cos` / `math.sin` to rotate coordinates
- `member_pos(f, m)` and the two-line rotation formula
- `spin` added to the formation dictionary, `f['spin'] += SPIN_SPEED` while holding
- found the missing `mx, my = member_pos(f, m)` that stopped the circle turning
- fixed flipped spawn odds, a boss-bullet `vy` sign, and the health-bar parameters
- per-member firing cooldowns with `random.randint`

**Background only.** None of it is today's topic. Use **one** recap slide: *"you already
hand values into a box and catch what comes back — `member_pos` did it. pandas is the same
idea, on a whole table at once."* That is the bridge, and it is honest.

**Unmet last week:** `return` as its own topic never happened (transcript 00:03:25,
00:42:04). It appeared inside `member_pos`. **Say in one line that it is parked, then move
on** — do not turn today into the return lesson.

### ⚠ Hard constraint on every code slide

**Do not assume a CSV file exists, and do not tell Neo to download one.** Build every
DataFrame **from a Python dict written on the slide**, so the code runs in the IDE with
nothing else present:

```python
import pandas as pd
scores = pd.DataFrame({
    "name":   ["Neo", "Amy", "Ethan", "Yunho"],
    "maths":  [92, 78, 85, 64],
    "coding": [88, 95, 71, 90],
})
```

Only once that works, add **one** optional slide showing `pd.read_csv("scores.csv")` and
say plainly it needs a file sitting next to the code. If `import pandas` fails in the IDE,
the whole numpy half still runs — order the deck so numpy sits behind pandas, not in front.

### Today's new ideas, in order — this is a from-zero deck

1. **A table has rows and columns.** Draw it. No code yet.
2. `import pandas as pd` — what the nickname is for.
3. **Build the DataFrame from the dict above.** One column at a time, v1 → v2 → v3.
4. `print(scores)` — read the printed table back, box by box.
5. `.head()`, `.shape`, `.columns` — three ways to look before you leap.
6. **One column is a Series**: `scores["maths"]`. Visual: the column lifted out of the table.
7. `.mean()`, `.max()`, `.min()`, `.sum()` — a whole column becomes one number.
8. **A new column from two old ones**: `scores["total"] = scores["maths"] + scores["coding"]`.
   Visual: the two columns adding row by row, one frame per row.
9. **Filtering** — `scores[scores["maths"] > 80]`. Visual first: a True/False column beside
   the table, then the rows that survive.
10. `.sort_values("total", ascending=False)`.
11. `.describe()` — every number at once.
12. **numpy starts here.** `import numpy as np`, `np.array([1, 2, 3])`.
13. **Vectorised maths** — `arr * 2` does every element with no loop. Visual: the loop Neo
    would have written, beside the one line that replaces it. **This is the idea that pays
    off for the exam — give it the biggest visual on the deck.**
14. `np.mean`, `np.std`, `np.arange`, `np.linspace`.
15. A pandas column *is* a numpy array underneath — `scores["maths"].values`.

**Then overshoot with new taught ideas, each with a visual:**
- `.groupby()` on a table with a repeated column (subject, or class)
- `.apply()` with a small function of Neo's own
- missing values: `None` in the dict, `.isna()`, `.fillna(0)`
- a bar chart with `matplotlib` — **mark this OPTIONAL**, it may not be installed
- `np.random.randint` to make a 100-row table, then ask it a question

**Keep Neo typing.** At least four **"NEO WRITES THIS ONE ALONE"** slides — Neo predicts
values correctly when asked, so put a *what will print?* slide before each run.

---

## 18:00 KST · 16:00 HCMC · JUN — Minecraft BLOCKS (track change)

**Kasim's instruction: "Jun is doing MC Blocks."** Concrete pick: **the loop inside a loop,
drawn as blocks — then one `variable` resizes the whole build.**

> **⚠ TRACK CHANGE. THIS DECK DRAWS BLOCKS. NO PYTHON ANYWHERE.**
> The last deck,
> `../../../english-coding-students/students/jun-mon-1800/slides/2026-08-31-bridge-how-many-blocks.html`,
> is Minecraft **Python** in constant form. **Do not copy its code style.** Every command on
> today's deck is a drawn MakeCode block. A Python line anywhere on this deck is a failed deck.

**Reference deck for block markup — read this one, closely:**
`../2026-09-13/david-p-upside-down-pyramid.html`. Copy its `mcb` markup exactly.

### How a drawn block must look

- Wrapper: `<div class="mcb-c loops">`, hat row `<div class="hat">`, body `<div class="mcb-in">`
- A command: `<div class="mcb agent">agent move <span class="dd">forward</span> <span class="val">1</span></div>`
- New-this-step blocks get `hot`: `<div class="mcb agent hot">`
- Under each group, name the drawer it came from:
  `<p class="mcb-from">from the <span class="drawer" style="background:#D83B01">Agent</span> drawer</p>`
- **A block's colour is its own drawer's colour, never the wrapper's.** Use the `.mcb.<category>`
  class and let `style.css` colour the block; only a `.mcb-from .drawer` chip needs a hex
  typed inline. The pixel-sampled values (style.css lines 2069–2078, fixed 2026-09-08):
  Player `#0078D7`, Agent `#D83B01`, Blocks `#7ABB55`, Loops `#569138`, Logic `#459197`,
  Variables `#EA2B1F`, Math `#6C6EA0`, Positions `#69B090`, Mobs `#764BCC`,
  Gameplay `#8F6D40`, Basic `#E89005`.
  (`#59967A` is **not** the Blocks colour — it is the darkened POSITIONS coordinate pill.)
- Nested inputs sit on a ×0.85 darker shade of the parent. Number and text fields are white
  ovals. A `~` sits **outside** the oval, never inside it.
- **Max four different block types on any one slide.**

### What Jun actually did last lesson (tracker draft, 2026-08-31 — no ledger, no transcript)

- `repeat` loops with a fixed count, and a **loop inside a loop**
- moving and turning the agent
- stacked squares in layers to build a house wall
- debugged the loop structure by comparing against Kasim's version

✓ told `turn right` from `move right` unprompted
△ **the nested loop was hard** — finished only with step-by-step guidance

**Unmet:** nothing recorded. **No lesson on 7 Sept** — Kasim cancelled it that morning, so
there are two weeks between this lesson and the last one. Assume the nested loop needs
rebuilding from the ground up, slowly, in blocks.

**No carry.** The 31 Aug deck taught a Python bridge; the lesson actually taught nested
loops. The deck and the lesson diverged, so nothing from it is reusable. Build fresh.

### Today's new ideas, in order

1. **Warm-up, blocks only:** the four blocks Jun owns — `agent move`, `agent turn`,
   `agent place`, `repeat`. One slide, drawn.
2. **`repeat 4` draws a square.** Visual: four frames, the agent walking one side per frame.
3. **A loop inside a loop**, drawn as a `repeat` block *sitting inside* another `repeat`
   block's mouth. Visual: the outer counter on the left, the inner counter on the right,
   one frame per inner pass. **Slow. This is what beat Jun last time.**
4. Inner ×4, outer ×3 → count the total moves out loud before running.
5. **NEW — the Variables drawer.** `set height to 5`. A drawn `set` block, red, from
   Variables.
6. **Drop the variable into the loop's count slot** — `repeat height`. Visual: OLD block
   with `5` in the oval, NEW block with the `height` variable chip in the oval.
7. **Change one number, change the whole build.** `set height to 3`, then `10`. Three
   pictures side by side, one block changed.
8. `change height by 1` inside the loop — each layer a different size.
9. **`agent place on move ON`** so the walls draw themselves as the agent moves.

**Then overshoot with new taught ideas, each with a visual:**
- a second variable, `width`, so the square becomes a rectangle
- the Math drawer: `height × 2` inside the repeat slot
- a `set` block that a chat command fills — `on chat command size`
- the classic bug: `place on move` left ON after the build, so the walk home draws a line

---

## 19:00 KST · 17:00 HCMC · ETHAN — IDE Python

**Kasim's instruction: "Ethan is doing IDE Python"** — track only, no topic. Concrete pick:
**finish the three-way `elif` price fork, then drop the fork inside the `for` loop.**

**Last deck:** `../2026-09-07/ethan-the-fork.html` — 146 slides. Tone and markup reference.
Read it before writing.

### What Ethan actually did last week (ledger 2026-09-07, from the Drive transcript)

- finished the times-table code and **predicted the output before running it**
- swapped the hard-coded `7` for a user input
- traced which variable the typed value lands in
- comparison operators `>` `<` `==` `!=` `>=` `<=`, and `True` / `False`
- wrote `if` / `else` and ran it
- an age input that prints a different sentence per branch
- `random.randint(1, 18)` to pick the age
- **started** the three-way `elif` price fork — did not finish it

**Unmet last week:** the `elif` price fork was never finished, and the fork never went
inside a loop. The code editor stopped responding near the end of the lesson and Ethan was
refreshing repeatedly until it ended early (transcript 00:36:17–00:38:13). **Both moved to
homework, and both are today's topic.**

**Homework concept just practised:** `if-fork-inside-a-for-loop`. **Open by checking the
homework actually landed** — the editor failure means it may not have saved. One or two
slides, then move.

**Failure modes:**
- △ needed the f-string `{}` explained more than once
- △ **waits for step-by-step guidance instead of reusing a pattern already owned** → put
  **"ETHAN WRITES THIS ONE ALONE"** slides in; the 09-07 deck already uses them well, keep
  at least four
- ✓ recovers from own errors when recounting (fixed `range(13)` → `11` unaided)

### The carry — slides that must come across

**Stop point: slide 71 of 146** (`STEP 7 / 29`, "v3 · The middle question" — the `elif`
line started and not finished). Found from the ledger `actual` and confirmed by the ledger
`gap`. **Slides 72–146 were never reached.** Bring them across verbatim, and re-open 71:

- **72–78** — finish the middle road, v3 with three numbers, why the wide gate goes last,
  the same lines in the wrong order, as many `elif` as you like, which road each age takes
- **79–85** — the six `elif` mistakes (one `=`, no fence, nothing behind the gate, `elif`
  with no `if`, two forks both running, quotes on a number, small-letter `true`)
- **86–95** — `and`, `or`, `not`, with a step slide each
- **96–101** — `%` taught with sweets, leftovers, "a gate on the belt"
- **102–115** — **`loopfork.py`**: the belt, the gate going in, pushing the print inside the
  gate, FIZZ, the other road, v1 → v4 in four moves. **This is the unmet promise. It is the
  heart of today.**
- **116–120** — the gate goes into `tables.py`, then a gate behind a gate
- **121–136** — `guess.py`: the locked box, `randint(1, 10)`, three roads for one guess
- **137–146** — blanks, quiz, the grader, bonus

Nothing on that list was taught on 7 Sept, so nothing is dropped.

### Today's new ideas, in order

1. One or two slides: did the homework file save and run? (`if-fork-inside-a-for-loop`)
2. **Finish the `elif` price fork** — the exact line the editor ate. Show the real
   half-written code as the OLD block.
3. `elif` as a chain read top to bottom, stopping at the first ✓. Visual: the traveller
   walking past each signpost.
4. **Everything from the carry, in its existing order**, with slides 102–115 given the most
   room — that is the promise the parent was given.

**Then overshoot past slide 146 with new taught ideas, each with a visual:**
- `while` — the belt that does not know how long it is
- `break` and `continue` on the belt, one frame per pass
- a list of prices and a `for` loop that grades all of them
- nested `for` — the times-table **grid**, not one row

---

## 20:00 KST · 18:00 HCMC · YUNHO — Minecraft Python

**Kasim's instruction: "Yunho is doing MC Python"** — track only, no topic. Concrete pick:
**maths on `i` — gaps and `range(a, b)` — then a loop inside a loop.**

**Last deck:** `../2026-09-07/yunho-let-the-loop-build.html` — 123 slides. Tone and markup
reference. Read it before writing. This is **Minecraft Education Python**, text code, not
blocks — `blocks.fill()`, `pos()`, constant block names.

### What Yunho actually did last week (ledger 2026-09-07, from the Drive transcript)

- every coordinate question correct — `y` 0–9 is ten slots and is the height, `x` 1–15 is
  fifteen
- discovered the build area is actually **20×20**, not 15×15
- `blocks.fill()` for one layer
- `for i in range(6)` and predicted what it would do before running
- moved the `blocks.fill()` **inside** the loop, with `i` in the height slot
- built a colour list
- `colors[i]` — **proposed the square brackets unprompted**
- `len(colors)` to count the list automatically
- relative coordinates — if you move while the code runs, the origin moves too

**Unmet last week:** nothing. All four promises were kept and `len()` went further than
planned. **Today is a clean forward step, not a repair job.**

**Homework concept just practised:** `arithmetic-on-the-loop-variable` — which is exactly
where the carry resumes. Open by checking it landed, one or two slides, then move.

**Failure modes:**
- △ off-by-one on the height axis (set 10, corrected to 9)
- △ syntax errors from bracket and comma placement — line 42 twice
- ✓ invents own methods (slabs and signs to count coordinates) — leave room for that

**Coordinate rule that must never be got wrong on this deck:** `y` starts at **0**; `x` and
`z` start at **1**. Never write "coordinates start at 0" for all three.

### The carry — slides that must come across

**Stop point: slide 83 of 123** (`STEP 9 / 22`, "The list can count itself" — `len(colors)`).
Found from the ledger `actual`. **Slides 84–123 were never reached.** Bring them across
verbatim:

- **84–87** — one number or two, **maths on `i`**, the step slide, floating layers
- **88–93** — `range` with two numbers, reading a range aloud, walking the list instead of
  the number (`for c in colors`), three step slides
- **94–97** — the counter that never moves, the no-`i` rainbow, number-way vs item-way
- **98–102** — **a loop inside a loop**, three step slides, nine blocks from six lines
- **103–111** — `i` moving `x` as well as `y`, the six stairs, a loop that draws the frame,
  closing the two sides
- **112–123** — three layers three colours, the blanks, the quiz, the colour tower, bonus

Nothing on that list was taught on 7 Sept, so nothing is dropped.

### Today's new ideas, in order

1. One or two slides: did the homework tower run? (`arithmetic-on-the-loop-variable`)
2. **Maths on `i`** — `i * 2` for gaps between layers. Visual: the tower with gaps, one
   frame per pass, the height value written on each frame.
3. **`range(a, b)`** — start somewhere other than zero. Visual: the number line with the
   first and last box marked, and the last box shown as **not** included.
4. **A loop inside a loop** — the outer counter and the inner counter side by side, one
   frame per inner pass, the floor filling in square by square.
5. Everything else from the carry, in its existing order.

**Then overshoot past slide 123 with new taught ideas, each with a visual:**
- `range(a, b, step)` — every second layer
- three nested loops → a solid cube, and the block count that explains why it is slow
- `if i % 2 == 0` inside the loop → stripes
- a list of block names walked with the same `i` that walks the heights

---

## 21:00 KST · 19:00 HCMC · LUCY & AMBER — Debate DB001, Week 3

**Kasim's instruction: "the tech an ddebate class which is week 3."**

**`../../debate/db001-tech-ai/week-03.html` already exists. Reuse it. Do not rebuild it and
do not hand-edit it.** Every DB001 deck is generated by `scripts/build-debate-decks.py`,
which reads its motions and vocabulary from `Desktop/dev/courses/tech_ai_debate` — editing
the HTML by hand puts the deck out of sync with the source of truth. Same handling as week
2 on 7 Sept.

- **Topic:** Feeds That Choose For You — 알고리즘이 고르는 영상
- **Motion:** *Apps that choose your videos make life better.*
- **Skill:** answer what they said, steps 1 and 2 — **They say ___. But ___.**
- **Format:** 60-second showdown. Speaker B must open with *They say*. No restatement, no points.
- One shared Kakao card for both students.
