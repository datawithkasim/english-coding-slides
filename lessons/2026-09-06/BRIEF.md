# Today's decks — 2026-09-06 (Sun)

Yungun excluded on Kasim's instruction. Remaining Sunday slots below.
Times are Korea first, Ho Chi Minh second (KST − 2).

Calendar is the source of truth for times this week. Tracker drift is noted where it exists.

## Hard rules for every deck

Read first, in this order:
1. `../../TEMPLATE.md` — slot structures and per-slide rules
2. `../../PEDAGOGY.md` — why each slot exists
3. `../../assets/style.css` — the only styling allowed
4. `../2026-08-30/<that student's deck>.html` — tone and markup reference

Then:
- Save to `lessons/2026-09-06/<file>.html`. Stylesheet `../../assets/style.css`,
  script `../../assets/deck.js`.
- **Overshoot hard.** The deck must hold far more than one lesson. No slide ceiling.
  Extra room goes on new taught ideas with a visual each, never on more debug cards.
- Per-slide caps: **≤ 40 English words, ≤ 15 Korean words**.
- One change per slide, numbered. Every code step carries: full OLD block and full
  NEW block, 🔍 FIND string, 📍 where (quote the line it goes under + indent count),
  🟣 why in one line, ✅ check in one line.
- Big programs ramp v1 → v2 → v3 → v4. New lines hot, old lines dim, OLD/NEW on
  changed lines.
- Only reuse existing CSS classes. No new inline component styling.
- Update the `counter` span to `1 / <total>`.

---

## 10:00 KST · 08:00 HCMC · DIS — GROUP PREP CLASS, 3 STUDENTS, 50 MINUTES

**Students: Cian, Leah, Danny.** Spell them exactly like that. The tracker
misspells two of them (Shian / Leia) — ignore the tracker.

**Source:** Notion lesson report + full transcript, 2026-08-30. No Drive
transcript exists for that date; Notion is the only record and it is complete.

### What they actually built last week

Working code at the end of the lesson:

```python
colors = [RED_WOOL, ORANGE_WOOL, YELLOW_WOOL, LIME_WOOL, LIGHT_BLUE_WOOL, PURPLE_WOOL]
y = 0
for i in range(6):
    blocks.fill(colors[i], pos(3, y, 3), pos(12, y, 12), REPLACE)
    y = y + 1
```

**API form is constant form** — `RED_WOOL`, `pos(...)`, `REPLACE`. Never string
names like `"red_wool"`. Spell the list `colors`, no `u` — Kasim said in class
that his own code has no `u`, and last week's deck spelled it `colours`, which is
part of why they hit name errors. Fix that here.

Concepts they now own: X/Y/Z axes, `blocks.fill` with a coordinate range,
`REPLACE`, a variable inside a coordinate, `for i in range(6)`, indentation inside
a loop, a list, `colors[i]`, `y = y + 1`.

### Wins
- **Danny** finished the loop + variable code first, then did the extension alone:
  four more materials and `range(10)` for a ten-layer tower.
- **Leah** fixed her own `y = y + 1` indentation error, then moved the whole tower
  by changing the coordinate numbers. Later added pink, white and black herself.
- **Cian** spotted that `REPLACE` was needed before Kasim said it, and fixed
  `for index in range` → `for i in range` immediately once explained.

### Mistakes — turn each into a slide, name no one
- `colors` list written **inside** the `for` loop instead of above it.
- `for index in range(6)` with `colors[i]` inside → `name 'i' is not defined`.
- `y` typed as a literal number in the coordinates instead of the letter `y`.
- `y = y + 1` indented to the wrong level, so the tower builds flat on one layer.
- A missing comma between two items in the list.
- Code deleted by accident, then retyped from scratch — **Ctrl+Z exists**. This
  cost one student most of the lesson. It earns its own slide.
- Moving in-world while the code runs, so blocks land in the wrong place.

### Today — the new ideas, in teach → build cycles

Kasim teaches a part, they build it, then the next part. Mark the cycles so he can
see at a glance where to stop talking. STAGE divider before each block, a
"Now you build it" slide closing each one.

| Stage | New idea | They build |
|---|---|---|
| **0** warm-up | rebuild last week's tower from memory | the rainbow tower |
| **1** | **`i` is already the counter** — delete `y` entirely, put `i` straight in the coordinate | same tower, three lines shorter |
| **2** | **a loop inside a loop** — the outer one moves along X, the inner one builds up | a row of rainbow towers |
| **3** | **`range(start, stop, step)`** — spacing without arithmetic | towers spaced 4 apart |
| **stretch** | `i % 3` to cycle colours; a pyramid that shrinks each layer | free build |

Stage 1 is the one that must land: it removes `y = y + 1`, which is the line that
broke two of the three last week. The whole of Stage 1 is "the counter you already
have can do the job of the variable you kept forgetting to indent."

Stage 2 is the real new concept — a loop inside a loop. It needs a visual with one
frame per pass: outer counter on the left, inner counter ticking through its full
range inside each outer step.

**Undo slide goes near the front**, before Stage 1, not buried in stretch.

---

## 18:00 KST · 16:00 HCMC · LEO KIM — `leo-remainder-patterns.html`

**Kasim confirmed: the 30 Aug Sunday lesson did not happen.** His most recent
lesson is Tuesday 1 Sept, and today continues from there. At the end of that
lesson Kasim told him "I'll see you on Sunday this week."

**Fibonacci is DONE. Do not teach it again.** Kasim's instruction: expand into a
new algorithm, using the remainder operator `%`.

### What he has already been taught — check against these, never repeat them

- `lessons/2026-08-25/leo-algorithms-nested-loops.html` — the staircase algorithm,
  two changing variables, start and end moving together.
- `lessons/2026-09-01/leo-two-formulas-one-build.html` — Fibonacci towers, the
  `h1 = h2` / `h2 = y` hand-over, a linear accumulator beside a Fibonacci one,
  spacing, starting the chain at 2 and 3. **30 slides, all of it landed.**

Neither deck uses `%` anywhere. The remainder operator is genuinely new to him.

### Where he actually is

Working code from 1 Sept:

```python
def towers():
    x = 2
    spacing = 2
    h1 = 1
    h2 = 1
    for i in range(6):
        y = h1 + h2
        blocks.fill(QUARTZ_BLOCK, pos(x, 0, 0), pos(x, y, 0), REPLACE)
        x = x + spacing
        h1 = h2
        h2 = y

player.on_chat("towers", towers)
```

The `pos` numbers are reconstructed — they were never read out. Keep them
consistent but do not build a slide whose point depends on them.

Concepts he owns: `for i in range(n)`, accumulators, reassignment order inside a
loop, defining vs calling a function, `player.on_chat`, `blocks.fill` with a
variable, lists, two changing variables at once.

### Wins from 1 Sept
- Counted the towers and **corrected Kasim** — he was right, there were seven.
- Diagnosed the real bug himself: "we didn't put the H1 and H2 in the fill code."
- Extended the sequence past the screen, unprompted, to 144.
- Explained the rule in his own words after a thinking countdown.

### Mistakes to design around
- Says only "I don't know" when stuck. The 1 Sept deck gave him three sentence
  frames for this. **Carry them forward into this deck**, early and late.
- Waits for the teacher to type first. Every Make slide needs a type-first marker.
- Confused by reassignment mid-trace: "does h2 change or does y change, both?"
- Ran the wrong chat command word and thought the code was broken.
- He was tired and said so twice. Short slides, pictures doing the work.

### ⚠ One thing to fix, not repeat

On 1 Sept `range(6)` was described as "the first time i is 1, until it hits 6."
Python's `range(6)` gives **0, 1, 2, 3, 4, 5**. This deck depends on `i` starting
at 0, because `i % 6` only lines up if it does. Show the six true values on a
counter strip early. Do not restate the wrong version and do not call it out.

### Today — the remainder, and the patterns it makes

**The hook, and it is a real bug.** He has six colours. Ask for twenty towers and
`colors[i]` dies on tower seven with `IndexError: list index out of range`. That
is the problem `%` exists to solve. Open there.

**New idea 1: `%` is what is left over.** 7 ÷ 3 is 2 remainder 1, so `7 % 3` is 1.
Draw it as sweets shared into bags: how many are left in your hand. No code yet.

**New idea 2: `%` wraps a counter round.** A counter strip with `i` on the top row
running 0 to 11 and `i % 6` on the bottom row running 0 1 2 3 4 5 0 1 2 3 4 5.
Point at the moment it snaps back to zero. This is the whole idea in one picture.

**New idea 3: `colors[i % 6]` — twenty towers, six colours, no crash.**

```python
colors = [RED_WOOL, ORANGE_WOOL, YELLOW_WOOL, LIME_WOOL, LIGHT_BLUE_WOOL, PURPLE_WOOL]
for i in range(20):
    blocks.fill(colors[i % 6], pos(x, 0, 0), pos(x, 5, 0), REPLACE)
    x = x + spacing
```

**New idea 4: `i % 2` splits everything into two.** `if i % 2 == 0:` build stone,
`else:` build gold. Alternating stripes. Show the counter strip again with only
0 and 1 on the bottom row.

**New idea 5 — the payoff: one loop can fill a square.**

```python
for i in range(25):
    x = i % 5
    z = i // 5
    blocks.fill(STONE, pos(x, 0, z), pos(x, 0, z), REPLACE)
```

`%` gives the column, `//` gives the row. Twenty-five blocks in a 5×5 grid from a
single loop. Put this side by side with the nested-loop version he already knows
from 25 Aug, so he sees two routes to the same build. Draw the grid filling in,
one frame per pass, with `i`, `x` and `z` written under each square.

**Stretch:** `(x + z) % 2` for a checkerboard floor; `if i % 3 == 0` for a special
block every third tower; `i % 6` driving height as well as colour.

Sentence frames for being stuck go in early, not just at the end.

---

## 19:00 KST · 17:00 HCMC · DAVID G8 — `david-g8-ask-until-valid.html`

**Tracker says Tuesday 21:00. The calendar says Sunday 19:00.** He is on the
calendar today. Report the drift, do not fix the tracker.

**He is an IDE student.** Username `hcseo31`, David Seo. He writes Python in the
app IDE, not Minecraft. His project is a **text dungeon crawler** called the
Abandoned Amusement Park.

**Source: his live IDE code**, project `Workspace`, `main.py`, last saved
2026-08-25. This is the truth about where he is. The 1 Sept 21:00 Drive recording
in his old Tuesday slot is a **different student on a Minecraft track** — ignore
it completely, it is not him.

### What his code actually looks like right now

Top of file:

```python
inventory = ['park map', 'pocket knife', 'camera', 'flashlight']

chapter_one = None
chapter_two = None
chapter_four = None
game_over = None

poisoned = None
burned = None
drunk = None
ripped = None
```

Then a `strike / leave` opening choice which sets `chapter_one = True`, followed by
three separate top-level chapter loops: `while chapter_one:`, `while chapter_two:`,
`while chapter_four:`, each ending by setting its own flag to `False`. There is a
`while game_over:` loop at the very bottom.

Concepts he already uses: `input().lower()`, `if` / `elif` / `else`, `==` for
comparison, `while` loops as chapter switches, `True` / `False` / `None` flags,
`inventory.append()`, `in` to test membership, `break`, `
` inside a string,
escaped apostrophes.

### The six real bugs in his own file — these are the deck's debug slides

Do not invent anything. All six are in his code right now.

1. **The crash from last lesson is still there, unfixed.**
   ```python
   print('You sees three areas infornt of you. ... [mansion/bumper cars/street]?').lower()
   ```
   `print()` gives back `None`, and `None.lower()` raises
   `AttributeError: 'NoneType' object has no attribute 'lower'`. It should be
   `input(...)`, and the answer should be stored in a variable. He was set this as
   homework on 25 Aug and it has not been done.
2. **Chapters 2 and 4 can never run.** `chapter_two` and `chapter_four` start as
   `None` and nothing ever sets them `True`, so both `while` loops are skipped.
3. **Nothing ever gives the railway valley key** in this version, so even if
   chapter 2 ran, its first `if` would be false.
4. **An answer thrown away**:
   `input('Should you deactivate with your wrench [yes/no]').lower()` is not
   stored in any variable, so nothing can be done with it.
5. **A missing `.lower()`**: `open_chest = input('...[red/blue/green]')` has no
   `.lower()`, unlike every other input in the file, so typing `Red` falls to the
   `else` and kills the player.
6. **`while game_over:` is an infinite loop.** If it ever becomes `True` it prints
   "You died..." forever. Needs a `break`.

### Wins from his last lesson
- Fixed `=` to `==` himself once questioned.
- Found the right line numbers to place code from guidance alone.
- Explained `break` in his own words: "breaking the loop".
- The writing itself is genuinely good and he clearly enjoys it. Say so.

### Mistakes to design around
- Mixes up `=` and `==` repeatedly.
- Could not see why setting every chapter flag `True` at the start breaks the flow.
- Nested conditionals and indentation still shaky — he needs to be told which
  block a line belongs in, every time.

### Today — ask again until the answer is valid

Promised next lesson, in the tracker: check the homework, then **input validation
loops**. That is the spine.

Warm-up: run his game, hit the crash on purpose, read the error out loud. Then:

**New idea 1: the ask-again loop.**
```python
answer = ''
while answer not in ['strike', 'leave']:
    answer = input('strike or leave? ').lower()
```
Draw it as a gate: a wrong answer sends you back round, a right answer lets you
through. One frame per attempt.

**New idea 2: `not in` and a list of allowed answers.** He already uses `in` for
the inventory, so this is the same idea pointed at a different list. Show both
lines side by side.

**New idea 3: one function, used everywhere.**
```python
def ask(question, options):
    answer = ''
    while answer not in options:
        answer = input(question).lower()
    return answer
```
Then every choice in the game becomes one line. This is the payoff: he replaces
five hand-written blocks with five calls. Show the before-and-after wall of code.

**New idea 4: flags that switch the next chapter on.** `chapter_two = True` at the
end of chapter one, so the chapters actually connect. Draw the three chapters as
boxes with an arrow that only appears when the flag flips.

**Stretch:** a `yes_no()` wrapper that only accepts yes or no; a retry counter that
gives up after three wrong answers; using the `poisoned` flag he already declared
but never uses.

---

## 20:00 KST · 18:00 HCMC · LOGAN — `logan-keyboard-control.html`

**Calendar and Notion both say 20:00.** The tracker's 19:00 is stale. Do not
change the tracker.

**Source:** Notion lesson report 2026-08-30, which matches the tracker log exactly.

### What they actually built last week — first Pygame lesson

```python
import pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Logan's Game")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
RED = (255, 0, 0)

x = 200
y = 200

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, (x, y, 100, 100))
    pygame.display.flip()
    clock.tick(60)
```

Concepts he now owns: `pygame.init()`, `set_mode((500, 500))`, `set_caption()`,
`draw.rect(screen, colour, (x, y, w, h))`, `screen.fill()`, RGB tuples in
variables, the `while running` game loop, `event.get()` / `pygame.QUIT`,
`Clock()` and `clock.tick(60)`, and moving a shape by adding to a variable once
per frame.

### Wins
- Worked out on his own that the first number moves the shape left-right and the
  second moves it up-down.
- Did the centring maths himself after one hint: "width divided by 2 is 50."
- Understood per-frame movement immediately after one practice run.

### Mistakes — these are the deck's debug slides
- That `(0, 0)` is the **top-left** and that y grows **downward** needed
  explaining several times. This is the single weakest thing he has.
- That a rect is drawn from its **top-left corner**, so putting it at the top
  right means subtracting the rect's width from the screen width — only landed
  after a visual.

### Today — `pygame.key.get_pressed()`

**New idea 1: the keyboard changes the variables.** Read the keys once per frame
and add to `x` and `y`, so he drives the rectangle instead of watching it drift.

```python
keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT]:
    x = x - 5
```

**New idea 2: stopping at the edges.** `if x < 0: x = 0` and
`if x > 500 - 100: x = 500 - 100`. This is the slide that finally forces the
top-left-corner rule to make sense, because the right-hand limit is only correct
if you subtract the rect's width. Draw it.

**New idea 3 (stretch):** a `speed` variable so one number changes how fast he
moves, then a second rect he cannot walk through.

Slot 5 must be a picture of the screen with `(0, 0)` in the top-left corner, y
arrows pointing **down**, and the rect's anchor dot on its top-left corner. Every
coordinate visual in this deck uses that same picture.

---

## 21:00 KST · 19:00 HCMC · CLAIRE — `claire-hp-bar.html`

**Source:** Notion lesson report 2026-08-30, which matches the tracker log exactly.

### What she actually built last week — the boss

- Added `HP` to each enemy type: how many hits before it dies.
- Added `HP`, `maxHP` and `is_boss` keys inside `make_enemy`.
- Wrote a `BOSS_TYPE` dictionary: colour, size, speed, points, HP.
- Set `BOSS_SCORE_TRIGGER` and `BOSS_STOP_Y` constants.
- Wrote `make_boss()`: spawns from the centre, stops at a Y limit.
- Gated spawning with a `boss_active` boolean.
- Used `.get()` and `if enemy.get("is_boss"):` to split boss from normal enemies.
- Alt+click multi-cursor editing.

### Wins
- Remembered by herself to paste her homework code into the project before testing.
- Asked whether missiles and bullets should do different damage — her own question.
- Caught the edge case first: "what happens if it's equal?" on the boss Y limit.

### Mistakes — the deck's debug slides
- **`[]` vs `()` when reading a dictionary key.** Repeatedly. This is the one.
- `.get()` returning `None` was explained and still did not hold in real use.
- Alt+click multi-cursor failed after several demonstrations. Do not build the
  lesson on it; if it appears, it is one optional slide.

### ⚠ Corrected from her live IDE code (read 2026-09-06)

The tracker log and the Notion report both write the keys in camelCase. **Her real
code does not.** Confirmed by reading `student_ide` directly:

- `enemy["hp"]` and `enemy["max_hp"]` — lowercase, snake_case.
- Other keys as expected: `"rect"`, `"color"`, `"points"`, `"speed"`, `"w"`, `"h"`,
  `"is_boss"`.

She works in the **Homework** project, which is newer than Workspace. It carries
numbered worksheet markers that make exact FIND anchors, for example:
`# --- WORKSHEET STEP 5 : the boss health bar goes under this line ---`

**Her homework is only part done.** Step 2, the boss stopping at `BOSS_STOP_Y`,
she wrote herself. Steps 3, 4 and 5 are untouched: a bullet and a missile still
delete an enemy on the first hit and nothing ever subtracts from `"hp"`.

**So damage has to be built before the bar.** A health bar drawn today would sit
permanently full and then vanish. Teach `enemy["hp"] -= 1` and `-= 3` first, with
removal moved inside an `if enemy["hp"] <= 0:` branch — and note that the score
and spark lines must move into that branch too, or she scores on every bullet.

### Today — draw the boss's health

**New idea 1: a bar whose width is a fraction.**
`bar_width = (enemy["HP"] / enemy["maxHP"]) * 200`. Every symbol in that line is
a square bracket, so the line she keeps getting wrong is now the line she cannot
avoid. Show the maths as a picture: full bar, half bar, empty bar, with the
fraction written under each.

**New idea 2: two rects stacked** — a dark background bar drawn first, the green
bar drawn on top of it, so an empty bar still has an outline.

**New idea 3: colour that changes with health.** `if` / `elif` on the fraction:
green above 0.5, orange above 0.25, red below. Ties conditionals to the number
she just computed.

**Stretch:** the same bar over every enemy, not just the boss; a bar that shrinks
smoothly instead of jumping.

Slot 5 = a drawer you open with `["HP"]` beside a machine you name with
`.centerx`, the same picture as last time so it is recognised, then a third panel
showing `.get("is_boss")` as "look in the drawer, and don't crash if it's empty."

Put a visible **WAIT** marker on every Make slide. Kasim's own note: leave more
wait time before hinting.

---

## 22:00 KST · 20:00 HCMC · DAVID P — `david-p-inverted-pyramid.html`

**Tracker says Friday 22:00. Both the calendar and the 30 Aug Notion report say
Sunday 22:00.** He is a Sunday student. Report the drift, do not fix the tracker.

**Source:** Notion lesson report 2026-08-30.

**API form is constant form**: `agent.move(FORWARD, 5)`, `agent.turn(LEFT)`.
The Notion report writes `agent.move("forward")` and "change side by" because it
paraphrases speech. Never use those forms in the deck.

### What he actually built last week
- Rewrote the regular pyramid code start to finish **by himself**.
- Chose 9 repeats himself, reasoning about how slow the agent is.
- Tried a negative size step on his own to make the pyramid shrink.
- Started, but did not finish, the inverted pyramid.

### Mistakes — the deck's debug slides
- Cannot yet work out **where the agent must start** for an inverted pyramid.
- Needed help every time counting how many `agent.move(BACK, n)` and
  `agent.move(RIGHT, n)` steps reach the next layer.
- **Runs the whole program at once instead of testing a piece at a time**, so when
  it breaks he cannot find where. This is a habit, and it gets its own slide.

### Today — the pyramid that shrinks

Warm-up: his own regular pyramid, one run, to prove it still works. Then:

**New idea 1: one variable decides the direction.** `step = -2` instead of
`step = 2`, and `side = side + step` inside the loop. One number flips the whole
build. He already reached for a negative number himself, so this names what he
did.

**New idea 2: work out the start from the finish.** A widest-layer-first pyramid
starts where the last layer of the old one ended. Draw both pyramids side by side
with the agent's start marked on each, and count the offset on the picture before
any code.

**New idea 3: run it one layer at a time.** Build the loop with `range(1)` first,
check the layer, then change the 1 to 9. This is the fix for his real habit, and
it is taught as a technique with its own slide, not as advice.

**Stretch:** a hollow pyramid; a variable for the start height so one number
lifts the whole thing off the ground.
