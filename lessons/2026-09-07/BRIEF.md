# Today's decks — 2026-09-07 (Mon)

Times are Korea first, Ho Chi Minh second (KST − 2).

**Calendar is the source of truth for times.** Tracker drift is noted per student.
JUN MC is on the calendar at 18:00 but **Kasim said NOT TODAY** — no deck, no message.
EUNWOO is in the tracker on Monday 19:00 but has **no calendar event today** — not taught, no deck.

| Time | Student | Track | Today's topic (Kasim's call) | File |
|---|---|---|---|---|
| 16:00 KST · 14:00 HCMC | AMY | Python IDE | `while` — the game loop that keeps asking, and an HP counter that ends it | `amy-keep-going-until.html` |
| 17:00 KST · 15:00 HCMC | NEO | Pygame | `def` — turn the giant file into named functions (after fixing the two homework bugs) | `neo-name-your-own-command.html` |
| 19:00 KST · 17:00 HCMC | ETHAN | Python IDE | `if / elif / else` — the fork, taught **heavy on visuals**, then dropped inside his `for` loop | `ethan-the-fork.html` |
| 20:00 KST · 18:00 HCMC | YUNHO | Minecraft Python | A `for` loop writes the fills — a colour list builds the layers | `yunho-let-the-loop-build.html` |
| 21:00 KST · 19:00 HCMC | LUCY & AMBER | Debate DB001 | Week 2 — AI in the Classroom · evidence, give an example | `../../debate/db001-tech-ai/week-02.html` (existing, **reuse — do not rebuild**) |

---

## Hard rules for every deck

Read first, in this order:
1. `../../TEMPLATE.md` — slot structures and per-slide rules
2. `../../PEDAGOGY.md` — why each slot exists
3. `../../assets/style.css` — the only styling allowed
4. That student's own last deck (named in their section) — tone and markup reference

Then:
- Save to `lessons/2026-09-07/<file>.html`. Stylesheet `../../assets/style.css`,
  script `../../assets/deck.js`. Slides are `<div class="slide">`, the first is
  `<div class="slide active center-all">`.
- **Copy-this-and-it-works.** The student makes zero decisions. If a slide needs
  the student to infer anything, it is wrong.
- **One change per slide**, numbered `STEP n / total`. A re-indent is its own step.
- Every code step carries all four: full **OLD** block and full **NEW** block (never
  `...` inside a changed region) · **🔍 FIND** the exact Ctrl+F string · **📍 where**
  (quote the existing line it goes under + the indent count) · **🟣 why** in one line ·
  **✅ check** in one line (what running it should show).
- **Big programs ramp v1 → v2 → v3 → v4.** Never the finished program first. New lines
  hot, unchanged lines dim, changed lines get an explicit OLD/NEW block.
- **Visuals beat words, and are mandatory for loops, iteration and any maths** — one
  frame per pass with the counter value shown; spacing as boxes on a number line;
  x positions as jumps.
- **Overshoot, hard.** The deck must hold **far more than one lesson can get through**.
  **No slide-count target and no ceiling.** If the teacher could plausibly reach the
  last slide inside the hour, it is too short — go back and add taught ideas. Extra
  room goes on **new concepts with a visual each**, never on more debug cards.
  Unused slides roll to next week.
- **As few words as possible.** ≤ 40 English and ≤ 15 Korean words per slide.
- **Every deck teaches at least one new idea** — the one named in the table above. A
  homework check or a revisited mistake is a warm-up that leads into the new idea. It
  is never the whole lesson.
- **The lesson-to-lesson jump can be bigger than the homework's.** Kasim is in the room
  to bridge it. Build for a student being taught, not one working alone.
- Only reuse existing CSS classes. No new inline component styling.
- Update the `counter` span to `1 / <total>`.

---

## 16:00 KST · 14:00 HCMC · AMY — Python IDE

**Kasim's instruction: "AMY IDE PYTHON".** Concrete pick: **`while` — keep asking until
it is right, and an HP counter that ends the game.**

**Last deck:** `../2026-08-31/amy-player-card-solo.html` — 69 slides. Tone and markup
reference. Read it before writing.

### What she actually did last week (tracker draft, 2026-08-31)

- `if` / `elif` / `else` conditional structure
- `input()` to receive user choices
- the `in` operator to check a substring is contained
- `.lower()` for case-insensitive input
- escape characters (`\`) for special characters in strings
- `print(f"text {variable}")` f-string output

✓ Linked conditionals to Pokemon card HP checks instantly — understood at once
✓ Designed her own difficulty balance; proposed an Easter egg and an elephant-riding mechanic
△ **Waits for Kasim to type instead of typing code herself** — every "AMY WRITES THIS ONE
  ALONE" slide matters, keep several
△ Confused `==` with `in` until she saw a containment diagram — visuals land with her

Week before (2026-08-24): `.lower()`, `.title()`, `.strip()`, `.replace()`, variable
reassignment, method chaining. She once typed `.title()` as `titile` — spelling slips are
her failure mode, so **🔍 FIND strings must be exact and short**.

**Unmet last week:** nothing recorded as promised-and-missed. (Tracker `promised` from
2026-08-24 said "let Amy try the Python card project herself before showing the example" —
background only, and it is honoured by keeping solo-write slides.)

**Transcript:** none. No Drive doc exists for any 2026-08-31 lesson. Facts above come from
the tracker draft.

### The carry — slides that must come across

Last week's deck was built to overshoot and she stopped around slide 36
("This is the player choosing"). **Slides 37–69 were never reached.** Bring these across
verbatim in spirit, then build today on top of them:

- 37–41 — a box that counts down, `take one away`, the visible bar, drawing the hearts,
  "this is the player's health". **This is the direct on-ramp to today's HP counter.**
- 42–50 — build the character screen, Amy builds it with no example first, the tools she
  owns, hints, v1 name only → v2 clean the name → v3 the border → v4 add the game
- 51–62 — the debug and fill-the-blank set
- 63–69 — finish your card, the finished card, type from memory, bonus quests

Also unconfirmed: slides 26–30 (`int()` takes the quotes off, text vs number). **Open with
one fast re-check slide on `int()`** — today's HP maths needs it and there is no record she
has it.

### Today's new idea

**`while` — a loop that repeats until something changes.**

Teach it in this order, one change per slide:

1. Re-check `int()` in one slide (input is text, `int()` makes it a number).
2. The HP counter from the carry: `hp = 100`, `hp = hp - 20`, printed hearts.
3. **New:** `while hp > 0:` — the loop that keeps the game alive. Visual first: one frame
   per pass, `hp` written on each frame, the loop arrow curling back, the exit door opening
   only when `hp` reaches 0.
4. Her `if` / `elif` / `else` fork goes **inside** the loop — she already owns the fork, so
   the only new thing is the indent and the repeat.
5. `while` + `input()` — keep asking until the answer is valid (`while answer not in [...]`).
   She owns `in` and `.lower()`; reuse both.
6. The infinite loop as a taught idea, not a bug card: show the frame counter never
   changing, then the fix.
7. v1 → v2 → v3 → v4 ramp on a small battle game: v1 hp only → v2 the loop → v3 the fork
   inside → v4 the choice that changes the damage.

Overshoot past that with more taught ideas: `break`, a turn counter, `random.randint()` for
damage, a second character. Each with its own visual.

**Keep her typing.** At least four "AMY WRITES THIS ONE ALONE" slides.

---

## 17:00 KST · 15:00 HCMC · NEO — Pygame

**Kasim's instruction: "NEO IDE PYTHON".** Concrete pick: **`def` — give your own commands
a name, after clearing the two homework bugs.**

Neo is twice weekly (Mon + Wed). **His last lesson was Wednesday 2026-09-02, not Monday.**

**Last deck:** `../2026-09-02/neo-bullets-that-hurt.html` — 74 slides. Tone and markup
reference. Read it before writing.

### What he actually did last lesson (ledger, 2026-09-02)

- enemy bullet cooldown timer, random cooldown
- `vx` / `vy`
- bullets built as dictionaries, appended to a list
- bullet-versus-player collision checking
- `lives` → `hp` conversion
- drawing a health bar from a health percentage
- made the screen bigger

Monday 2026-08-31 before that: per-enemy bullet cooldown in `makeEnemy`, decrementing
`enemy["bullet_cooldown"]` each frame, spawn position
`enemy["x"] + enemy["w"] / 2 - bullet_width / 2`, drawing with `pygame.draw.rect()`.
✓ Caught his own bug (code ran, no bullets) — spotted the missing draw code unprompted.
✓ Explained `BY = EY + EH` and the centre formula on his own.

### Unmet last lesson — deal with this FIRST

**Ledger `gap`: "숙제 버그 두 개(타이머 재충전, 보스 처치 순서) 수정 여부가 피드백 기록에 없음."**

The parent was told two homework bugs would be fixed and there is no record they were:

1. **The timer that never recharges** — the reset line sits outside the `if`, so the
   cooldown counts to zero once and stays there.
2. **The boss that will not die** — the death check sits outside the collision block, so
   the door is never opened.

Last week's deck covered these at slides 6–13 ("A timer that never climbs back", "A line
that does nothing", "Reset the timer, inside the if", "Indent 12, not 8", "The boss will
not die", "The door you never open", "Move the death check inside", "Two fixed. One
empty."). **Rebuild that pair as the opening warm-up, tightened to about 8 slides**, then
move to the new idea. It is the way in, not the lesson.

**Transcript:** ledger row carries no transcript link and no Drive doc matched his slot.
Facts above are the ledger `actual`, which is the strongest record available.

### The carry — slides that must come across

He reached roughly slide 55 ("Before you go…"). **Slides 57–74 were never reached.** Bring
them across:

- 57–63 — four more upgrades; a shield counted in frames; make the counter; count it down;
  only hurt when the shield is down; raise the shield on a hit; the shield that never drops
- 64–67 — the bullet sits off-centre; centre the bronze bullet; bronze sparks on a hit;
  gold bar when you are low
- 68–74 — the small `r` bug; the wrong constant; the bar off the top; fill the four blanks;
  make a tank hit hurt more; pick a bonus; save it

### Today's new idea

**`def` — naming a block of code so the file stops growing sideways.**

His main loop is now very long (formations, enemy bullets, player bullets, collisions,
health bar). That is the honest reason for functions, so teach it from his own file.

Order, one change per slide:

1. Visual first: the long `while True:` block drawn as one tall column, then the same
   column with three coloured blocks lifted out and given names.
2. `def draw_health_bar():` — lift the health-bar drawing he wrote last week, verbatim,
   into a function. Nothing else changes. Show the OLD block and the NEW block in full.
3. Calling it: `draw_health_bar()` — one line where seven used to be.
4. **Arguments:** `def draw_health_bar(hp, max_hp):` — the box you hand in. Visual: the
   value travelling into the named slot, one frame per hand-off.
5. `return` — a function that answers instead of drawing: `def hp_percent(hp, max_hp):`
   with `return hp / max_hp`. Visual: the value coming back out.
6. Lift a second real block: `def spawn_formation():`.
7. The bug set that belongs to functions: defined but never called (nothing happens);
   called before it is defined; forgot the `()`; the argument in the wrong order;
   `return` with nothing after it.
8. v1 → v2 → v3 → v4 on his own file: v1 one function → v2 an argument → v3 a return →
   v4 three functions and a short main loop.

Then the carry (shield, i-frames, sparks, gold bar). Overshoot past that too.

**API form is Pygame as he already writes it.** Match his own variable names from his file
— do not rename anything.

---

## 19:00 KST · 17:00 HCMC · ETHAN — Python IDE

**Time note: the calendar says 19:00 KST. The tracker says 21:00.** The calendar is the
truth today; the tracker row is stale. Head the deck 19:00 KST · 17:00 HCMC.

**Kasim's instruction, his exact words: "ETHAN IDE PYTHON (heavy on visuals)".**
Concrete pick: **`if` / `elif` / `else` — the fork — taught heavy on visuals, then dropped
inside the `for` loop he already owns.**

**HEAVY ON VISUALS IS THE INSTRUCTION FOR THIS DECK.** Not decoration — the teaching load
sits on the pictures. Every conditional concept gets a drawn frame before any code:
the fork in the path, the gate that opens or stays shut, the trace table with one row per
pass, the value in a box next to the question being asked of it. If a slide explains a
conditional in words alone, redraw it.

**Last deck:** `../2026-08-31/ethan-for-loops-range.html` — 38 slides. Tone and markup
reference. Read it before writing.

### What he actually did last week (tracker draft, 2026-08-31)

- `input()` for name, age, favourite food
- f-strings and curly braces
- creating lists (a list of countries, a list of foods)
- list indexing — `[0]`, `[1]`, `[2]`
- `for` loops with `range()`, using `i` to index into a list
- using `i` for arithmetic (a multiplication table)

✓ Fixed his own `range(13)` out-of-range error by recounting the elements, corrected to 11
✓ Predicted the list `[1]` value ("England") and the multiplication result **before running**

Week before (2026-08-24): `input()`, variables, `print()`, f-string syntax, a small
interactive story.
△ Needed a repeat explanation of what goes inside the f-string `{}`
△ **Waits for step-by-step guidance instead of applying a prior pattern independently** —
  so keep the "ETHAN WRITES THIS ONE ALONE" slides, and keep them small.

**Unmet last week:** nothing recorded as promised-and-missed.

**Transcript:** none. No Drive doc exists for any 2026-08-31 lesson. Facts above come from
the tracker draft.

### The carry — slides that must come across

He reached roughly slide 22 ("ETHAN WRITES THIS ONE ALONE", after the times table).
**Slides 23–38 were never reached.** Bring them across:

- 23–24 — v4 ask inside the loop; what goes inside the `{ }`
- 25–29 — Bug 1 it won't even start; Bug 2 nothing is inside; Bug 3 wrong five numbers;
  Bug 4 the same letter five times; Bug 5 one row missing
- 30–33 — fill in the blanks; harder, three blanks; 2 fast questions; say it out loud
- 34–37 — build the times-table quiz; pick a bonus; **"toward the guessing game"**;
  before you go

Slide 36 already points at the guessing game. Today's new idea is exactly what unlocks it.

### Today's new idea

**`if` / `elif` / `else` — one question, one road taken.** There is no record he has ever
met a conditional, so build it from zero.

Order, one change per slide, **each with its own drawn frame**:

1. The fork in the path — a picture, no code. One traveller, two roads, a signpost with
   the question on it.
2. `True` and `False` as the only two answers a question can give. Draw the two doors.
3. The comparison operators `==`, `>`, `<`, `>=`, `<=`, `!=` — each as a small picture of
   two boxes being weighed. **`=` puts in, `==` asks** — draw that difference twice.
4. `if` alone: the gate that opens or is skipped. Frame 1 the value, frame 2 the question,
   frame 3 the road taken.
5. The colon and the indent — draw the indented block as the fenced area past the gate.
6. `else`: the second road. Both roads drawn, one highlighted.
7. `elif`: three roads, still exactly one taken. Draw all three, walk the traveller down
   each in three separate frames.
8. **Trace tables** — a table with one row per pass, columns `i`, the question, `True`/`False`,
   what printed. This is the single most valuable visual for him; use it more than once.
9. v1 → v2 → v3 → v4 on a small program: v1 one `if` → v2 add `else` → v3 add `elif` →
   v4 the fork **inside his `for` loop** (his own multiplication table: print `FIZZ` when
   `i` divides evenly). Combining the fork with the loop he already owns is the payoff.
10. The bug set: `=` instead of `==`; the missing colon; the missing indent; `elif` before
    `if`; a second `if` where `elif` was meant (both roads run).

Overshoot past that with more taught ideas, each visual: `and` / `or` drawn as two gates in
series and in parallel; `not`; nested `if`; and the first two steps toward the guessing
game (a secret number, "too high / too low"). Do **not** finish the guessing game — it is
next week's payoff.

---

## 20:00 KST · 18:00 HCMC · YUNHO — Minecraft Python

**Kasim's instruction: "YUNHO MC PYTHON".** Concrete pick: **let a `for` loop write the
fills — a colour list builds the layers.**

### ⚠️ PREP BLIND — read this before anything else

**There is no transcript for Yunho on any recent date, and the tracker contradicts itself.**

- The lesson log for 2026-08-24 says he built 2D pixel art with `blocks.fill()`.
- A second draft, **dated the same day**, says the entire session was lost to an audio
  connection failure and no content was delivered.
- No Drive transcript exists for 2026-08-24 or for 2026-08-31 to settle it.
- There is **no record at all** that last week's deck
  (`../2026-08-31/yunho-pixel-art-bigger.html`) was ever delivered.

**Therefore: treat the whole of last week's deck as unreached carry.** Open with a fast,
respectful re-open of it — if he already has it, the re-open takes five minutes and the
new idea starts early; if he does not, the deck still works. Never assume he has it, and
never spend the lesson on it.

**Last deck:** `../2026-08-31/yunho-pixel-art-bigger.html` — 38 slides. Tone and markup
reference. Read it before writing.

### What he last has on record (lesson log, 2026-08-24)

- `blocks.fill()` to build 2D pixel art
- adjusting and correcting Y values in the 3D coordinate system
- organising several `blocks.fill()` commands in one file
- debugging syntax errors from parenthesis and comma placement
- a coordinate-counting strategy on a 15×15 canvas

✓ Invented his own method with slabs and signs to count coordinates
✓ Fixed a line-42 parenthesis bug straight after it was explained
△ Off-by-one on the Y axis: set 10, had to correct to 9

**Unmet last week:** nothing recorded as promised-and-missed.

### ⚠️ Coordinate rule — never get this wrong

**In Minecraft, `y` starts at 0. `x` and `z` start at 1.** Never write or imply that
"coordinates start at 0" for all three. Any slide teaching counting must say which axis it
is talking about.

### The carry — the whole of last week's deck

- 1–8 — bigger picture, count from 0; the 15×15 canvas; how many blocks; words for today;
  a ruler that starts at 0; standing the ruler up is Y; point or subtract; which number is
  height
- 9–18 — v1 one big rectangle; v1 on the canvas; v2 two eyes; v2 on the canvas; v3 the
  mouth; one creeper, five fills; read the range back; find the end; one row too tall;
  one column too wide
- 19–27 — Bug 1 the body grew; Bug 2 it will not run; Bug 3 line 42 again; Bug 4 the eyes
  vanished; Bug 5 the art turned sideways; Bug 6 the eye shrank; carve the mouth; v4 add
  an outline; check all four edges
- 28–38 — 2 fast questions; say it out loud; your own big sprite; pick a bonus; **mirror it,
  do not retype it; let a loop write the fills; a frame around the whole canvas; make it
  two blocks thick; fill the whole canvas**; before you leave; "0 to 9 is ten"

Slides 32–36 are the direct on-ramp to today's new idea. Compress 1–31 into a brisk
re-open; give 32–36 their full teaching weight.

### Today's new idea

**A `for` loop writes the fills, and a list holds the colours.**

He is currently typing one `blocks.fill()` line per row. That is the honest reason for a
loop, so teach it from his own pain.

Order, one change per slide, **visual before code every time**:

1. His five hand-typed fills drawn as five stacked lines, all nearly identical. Circle the
   one number that changes. That number is what the loop will supply.
2. `for i in range(5):` — one drawn frame per pass with `i` written on it: `i = 0`,
   `i = 1`, `i = 2`, `i = 3`, `i = 4`. Five frames, five pictures of the world after each.
3. `range(5)` gives 0, 1, 2, 3, 4 — five numbers, last one is 4. Draw them as boxes on a
   number line. **Tie it to his own off-by-one: "0 to 9 is ten."**
4. The colon and the indent — draw the indented body as the part that repeats.
5. `i` inside a coordinate: `blocks.fill(..., pos(1, i, 1), pos(15, i, 15), ...)`.
   Show the OLD five lines and the NEW two lines in full.
6. **A list:** `colors = [RED_WOOL, ORANGE_WOOL, YELLOW_WOOL, LIME_WOOL, LIGHT_BLUE_WOOL,
   PURPLE_WOOL]`. Draw it as six numbered slots. **Spell it `colors`, no `u`.**
7. `colors[i]` — the loop number picks the slot. Draw the arrow from `i` into the slot,
   one frame per pass.
8. Put them together — a six-layer rainbow tower from one loop.
9. v1 → v2 → v3 → v4: v1 five hand fills → v2 the loop with a fixed colour → v3 the colour
   list → v4 `colors[i]` inside the loop.
10. The bug set: forgetting the colon; no indent so only the last line loops; `range(6)`
    against a five-item list (`IndexError`); the loop variable never used, so every layer
    lands on the same Y; using a string `"red_wool"` instead of the constant.

**API form is constant form** — `RED_WOOL`, `pos(...)`, `REPLACE`, `blocks.fill(...)`.
Never string names like `"red_wool"`.

Overshoot with more taught ideas: `range(start, stop)`; a nested loop for a solid cube;
`for` over the list directly (`for c in colors:`); a frame around the canvas built by a
loop. Each with a visual.

---

## 21:00 KST · 19:00 HCMC · LUCY & AMBER — Debate DB001

**Not a new deck. No deck agent. Reuse `../../debate/db001-tech-ai/week-02.html` exactly as
it is.** Debate decks are generated by `scripts/build-debate-decks.py` from
`dev/courses/tech_ai_debate` and must never be hand-edited.

- They ran **Week 1 — AI and Homework · claim + reason** on Friday 2026-09-04.
- Today is **Week 2 — AI in the Classroom · evidence, give an example**.
- Motion: *A computer could teach a class better than a person.*
- Skill: **Evidence — give an example.** Frame: `For example, ___.`
- Format: **Pair debate** — 45 seconds each, two rounds. Round 2 adds one more example
  only, no new reasons.
- The usual mistake to name in class: *"AI teachers are good because they help you."* —
  nothing was shown. A reason needs an example.

Link it from `index.html` at 21:00. One shared Kakao card for both students.
