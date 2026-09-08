# Today's decks — 2026-09-09 (Wed)

Times are Korea first, Ho Chi Minh second (KST − 2).

**Calendar is the source of truth for times.** Tracker drift is noted, never fixed here.

Six lessons today. Kasim confirmed the list and the platform for each, and chose
"based on their last lesson" for every topic — each deck carries straight on from
what the ledger says actually happened.

| KST | HCMC | Student | Platform |
|---|---|---|---|
| 15:00 | 13:00 | SEOHOO | Minecraft **BLOCKS** (MakeCode) |
| 17:00 | 15:00 | EUNWOO | Minecraft **Python** |
| 18:00 | 16:00 | NEO | Python / Pygame |
| 19:00 | 17:00 | YUNA | Python (app IDE) |
| 20:00 | 18:00 | YOOJUN | Minecraft **BLOCKS** — trial, 40 min |
| 21:00 | 19:00 | 이현 (LEE HYEON) | Minecraft **BLOCKS** (MakeCode) |

**Not today, do not build:** RIHAN · JADEN · DANIEL LEE. The tracker still lists all
three on Wednesday. Jaden moved to Friday 17:15, Daniel stopped lessons, Rihan has no
calendar event for two weeks. Report only, change nothing.

**Tracker drift, report only:** EUNWOO is stored as Monday 19:00 (really Wed 17:00) ·
NEO is stored as 17:00 (really 18:00) · YOOJUN has no tracker row at all.

## Hard rules for every deck

Read first, in this order:
1. `../../TEMPLATE.md` — slot structures and per-slide rules
2. `../../PEDAGOGY.md` — why each slot exists
3. `../../assets/style.css` — the only styling allowed
4. That student's own most recent deck, named in their section — tone and markup reference

Then:
- Save to `lessons/2026-09-09/<file>.html`. Stylesheet `../../assets/style.css`,
  script `../../assets/deck.js`.
- **Overshoot hard.** The deck must hold far more than one lesson can get through.
  No slide ceiling, no slide target. If the teacher could plausibly reach the last
  slide inside the hour, it is too short — go back and add taught ideas. Extra room
  goes on **new concepts with a visual each**, never on more debug cards.
- Per-slide caps: **≤ 40 English words, ≤ 15 Korean words.**
- **One change per slide**, numbered `STEP n / total`. A re-indent is its own step.
- Every code step carries all five:
  **the code** (full OLD block and full NEW block, never `...` inside a changed region) ·
  **🔍 FIND** the exact Ctrl+F string, or on the block track the exact block to look at ·
  **📍 where** — quote the existing line it goes under, and the indent count ·
  **🟣 why**, one line ·
  **✅ check**, one line (what running it should show).
- Big programs ramp **v1 → v2 → v3 → v4**. Never the finished program first. New
  lines hot, unchanged lines dim, changed lines get an explicit OLD/NEW block.
- **Visuals are mandatory for loops, iteration and any maths** — one frame per pass
  with the counter value shown; spacing as boxes on a number line; x positions as jumps.
- Only reuse existing CSS classes (`.var-fill`, `.viz-reassign`, `.viz-if`, `.viz-3`,
  `.mcb` and friends). No new inline component styling.
- Update the `counter` span to `1 / <total>`.
- **Every deck teaches at least one new idea** — the one named in its section. A
  homework check or a revisited mistake is the warm-up that leads into it, never the
  whole lesson.
- **Carry slides listed in a section come across verbatim.** Today's deck is built on
  top of them, not instead of them.

### Block track — SEOHOO, YOOJUN and 이현

**Their slides DRAW THE BLOCKS.** These three drag blocks in MakeCode and do not read
Python. A slide must be a picture of the thing on their screen, using the words printed
on the real block. **Zero Python anywhere in their decks** — not in a code block, not in
a debug card, not in a comment. `agent.move(FORWARD, 5)` in a block deck is a bug.

Use the existing components, do not invent markup:

```html
<div class="mcb-c player">
  <div class="hat">on chat command <span class="val">"go"</span></div>
  <div class="mcb-in">
    <div class="mcb agent">agent move <span class="dd">forward</span> <span class="val">5</span></div>
    <div class="mcb agent">agent turn <span class="dd">left</span></div>
  </div>
</div>
<p class="mcb-from">from the <span class="drawer" style="background:#D83B01">Agent</span> drawer</p>
```

- `.mcb-c` = a C-shaped block that wraps others (`on chat command`, `repeat`, `if`).
  Its `.hat` is the top bar, its `.mcb-in` holds the blocks inside.
- `.mcb` = a single block. Category class sets the colour: `basic` `player` `blocks`
  `mobs` `agent` `gameplay` `pos` `loops` `logic` `vars` `math`.
- `.dd` = dropdown hole · `.val` = white number or text hole · `.ovar` = variable oval ·
  `.swatch` = colour square · `.mcb-drop` = empty dashed socket ("drag it in here").
- `.hot` / `.dim` mean what they mean in text decks: hot = added this step, dim = already there.
- `.mcb-from` names the toolbox drawer. **Every new block gets one.**

**Drawer colours — these are pixel-sampled from Kasim's own editor. The `.mcb.<class>`
values in `style.css` already match this table exactly, so use the class and let the CSS
colour it. Only `.mcb-from .drawer` needs the hex typed inline:**

| Drawer | Hex | | Drawer | Hex |
|---|---|---|---|---|
| BASIC | `#E89005` | | POSITIONS | `#69B090` |
| PLAYER | `#0078D7` | | LOOPS | `#569138` |
| BLOCKS | `#7ABB55` | | LOGIC | `#459197` |
| MOBS | `#764BCC` | | VARIABLES | `#EA2B1F` |
| AGENT | `#D83B01` | | MATH | `#6C6EA0` |
| GAMEPLAY | `#8F6D40` | | | |

Do not copy the drawer hex out of `../2026-09-02/BRIEF.md` — its Agent chip says
`#5c2d91`, which is wrong. Agent is `#D83B01`.

**Block anatomy — a drawn block that differs from the screen is a bug:**
- Colour follows the drawer the block **came from**, never the block it sits inside. An
  `on chat command` hat is PLAYER blue with a BLOCKS-green `fill` nested inside it.
- A nested input block is its own drawer colour × 0.85.
- Number field = white pill oval, dark slate text. String field = white rounded rect with
  dark-red `"` marks. Plain dropdown = same fill as parent, darker border, white `▾`.
- The `~` tilde is white label text **outside** the white number oval, one before each number.
- The place-on-move switch is written `agent place on move [ON]`. Never `set_assist(...)`.

### API form — Minecraft Python (EUNWOO only today)

```python
blocks.fill(QUARTZ_BLOCK, pos(2, 0, 0), pos(4, 6, 0))
agent.move(FORWARD, 5)
```

Bare CAPS constants. No quotes. `agent.move("forward", 5)` is wrong and will not run.
Never copy API form from `../2026-08-29/dewy-agent-loops.html` — that deck is string form.

### Coordinates rule — every Minecraft deck today

`pos(x, y, z)` — x across, y up, z forward. **y counts from 0. x and z count from 1.**
First free square is `pos(1, 0, 1)`. Never write "coordinates start at 0" as one blanket
rule for all three axes. Any counting visual labels x and z from 1 and y from 0.

### World files

Kasim hosts the world, the student joins. **Never open a deck with a world-import slide.**
`.mcworld` files are for homework only.

---

## 15:00 KST · 13:00 HCMC · SEOHOO — `seohoo-two-numbers-one-tower.html`

**Track:** MS001, Minecraft **BLOCKS** (MakeCode) · **Source:** ledger 2026-09-02, from transcript
**Topic Kasim gave:** carry on from last lesson — a second variable alongside HEIGHT
**Reference deck:** `../2026-09-02/seohoo-pixels-with-a-loop.html` — his own, same markup and tone

**What actually happened last time**
- Counted the x range 6→11 out loud
- `on chat command "face"`
- Filled one row with a fill block
- Wrapped it in `repeat 15`
- Made a `HEIGHT` variable
- `change HEIGHT by 1` to climb
- `if HEIGHT = 4` / `if HEIGHT = 14` condition blocks
- Narrowed the x range to cut the creeper's mouth

**Unmet promise:** none. Nothing was left owed.

**Carry:** none worth having — the deck reached about slide 58 of 64 and the tail is
bonus and wrap-up, not content. Build fresh.

**△ Known weak spot, use it as the warm-up hook:** y starting at 0. He has started ranges
at 1 and miscounted the end more than once. Open with one counting check that settles it,
then move on. Do not spend the lesson there.

**The new idea:** **two variables changing at the same time.** Last week one variable
(`HEIGHT`) went up. Today a second one (`WIDTH`) comes down on the same pass, so the shape
narrows as it climbs — a pyramid instead of a wall.

Build it as a ramp:
- v1 — the wall he already has, `HEIGHT` only, dim
- v2 — add a `WIDTH` variable, set it once, use it in the fill so the row length is no
  longer typed in by hand
- v3 — `change WIDTH by -2` inside the same repeat, next to `change HEIGHT by 1`
- v4 — the pyramid runs; add `if WIDTH < 1` to stop it going inside out

**Visuals are mandatory here.** One frame per pass of the repeat, showing both boxes side
by side: `HEIGHT` counting 0,1,2,3… and `WIDTH` counting 15,13,11,9… Then the row drawn
underneath each frame so he sees the shape appear. `.var-fill` and `.viz-3` exist for this.

---

## 17:00 KST · 15:00 HCMC · EUNWOO — `eunwoo-one-loop-two-lists.html`

**Track:** MS002, Minecraft **Python** · **Source:** ledger 2026-09-02, from transcript
**Topic Kasim gave:** carry on from last lesson — one counter driving two lists
**Reference deck:** `../2026-09-02/eunwoo-see-the-numbers.html` — own deck, same tone

**What actually happened last time**
- Remainder `%`
- How dividing by 4 gives 0, 1, 2, 3 over and over
- Counting positions from 0
- `XS[2]` to pull one value out of a list
- That the slot number and the value in it are different things
- Reading two coordinate lists
- A `for` loop running 24 times
- A diamond shape on the floor

**Unmet promise:** none.

**Carry:** none worth having — reached about slide 33 of 39, tail is bonus. Build fresh.

**The new idea:** **one counter reading two lists at once.** She can already pull `XS[2]`
out by hand. Today `i` goes into both lists on the same pass — `XS[i]` and `ZS[i]` — so a
single loop walks a path instead of a straight line.

Build it as a ramp:
- v1 — the loop she has, one list, dim
- v2 — `for i in range(24)` with `XS[i]` in place of the typed number
- v3 — `ZS[i]` added to the same line, both lists read by the same `i`
- v4 — the spiral or path appears; then change one value in `ZS` and watch only that
  block move

**Visual, mandatory:** two rows of boxes stacked — `XS` on top, `ZS` underneath, with one
arrow labelled `i` pointing down through both. Advance the arrow one box per frame and show
the block that lands. This is the whole lesson in one picture.

**Coordinates:** y from 0, x and z from 1. Her `XS`/`ZS` values are player-relative offsets,
not a grid drill, so do not turn this into an origin lecture — state it once, correctly.

---

## 18:00 KST · 16:00 HCMC · NEO — `neo-a-box-that-answers.html`

**Track:** RS003, Python / Pygame · **Source:** ledger 2026-09-07, from transcript
**Topic Kasim gave:** carry on from last lesson — pick up exactly where it stopped
**Reference deck:** `../2026-09-07/neo-name-your-own-command.html` — **this is the carry source**

**What actually happened last time**
- Found why the formation had vanished: `start_x` was sitting in `vx`
- Wrapped the drawing lines into `def draw_health_bar`
- Gave it parameters `hp` and `max_hp`
- Made `def draw_boss_bar(boss)`
- Spawned a boss every 250 points with `next_boss` / `boss_number`
- Scaled boss health by boss number
- Read and fixed `NoneType` and unexpected-indent errors

**Unmet promise:** `return`. The parent was told it was coming. The formation-speed bug and
the health-bar errors ate the time. This week's homework already practises `return`, so he
arrives able to do it.

**THE CARRY — read this before writing anything.**
Open `../2026-09-07/neo-name-your-own-command.html`. It has 118 slides and the lesson
stopped at roughly **slide 48**, immediately before the slide titled **"A box that answers"**
(marked `STEP 6 / 17`), which is the `return` slide. **Slides ~49 to ~118 were never seen.**

- Copy slides ~49 onward **verbatim** — same markup, same step text, same visuals. They are
  good slides and re-teaching around them wastes the lesson.
- Renumber the `STEP n / total` chain across the whole new deck so it is continuous.
- Put a short warm-up in front: check the homework `return` sheet, and re-open the
  `NoneType` error from last week, because that error is what a missing `return` looks like.
  That is the bridge into the carried slides, and it is the only new material at the front.
- Then **extend past slide 118.** The old deck ends at "Save it. Five new names." Add new
  taught ideas on top: a function that returns a value used in a condition
  (`if take_damage(hp, 10) <= 0:`), and returning two values at once for a position.
  Each new idea gets its own visual.

**Do not rebuild from scratch.** A fresh deck here throws away 70 finished slides and risks
re-teaching a step he already did.

---

## 19:00 KST · 17:00 HCMC · YUNA — `yuna-number-the-players.html`

**Track:** Python, app IDE · **Source:** ledger 2026-09-02, from transcript
**Topic Kasim gave:** carry on from last lesson — the nested loop that was promised
**Reference deck:** `../2026-09-02/yuna-every-team-at-once.html` — **this is the carry source**

**What actually happened last time**
- `for` loops
- `for team in hockey` to pull the keys out
- `input()`
- `hockey[team]` to pull a card out
- Using two sets of brackets
- That dictionary keys are case sensitive
- Built her own dictionary from scratch (a McDonald's menu)

**Unmet promise:** numbering the player names with a nested loop. The parent was told this
would happen and the record does not show it. **This is today's lesson.**

**THE CARRY — read this before writing anything.**
Open `../2026-09-02/yuna-every-team-at-once.html`. It has 55 slides and the lesson stopped
at roughly **slide 34**, immediately before the slide titled **"v4b — number the players"**
(marked `STEP 6 / 6`), which is the nested loop. **Slides ~35 to ~55 were never seen.**

- Copy slides ~35 onward **verbatim**, renumber the step chain continuously.
- Warm-up in front: re-open her own McDonald's dictionary, not the hockey one, and pull one
  value out of it. Same skill, her own data, thirty seconds. Then into the carried slides.
- Then **extend past slide 55.** Add: a nested loop over her own menu with `enumerate` so the
  number comes for free, and a count of how many items each category holds.

**File state, checked in the live IDE 2026-09-08 — this changed the deck:**
Her workspace `main.py` is 274 bytes: the menu homework starter, JOB comments stripped, and
**the three missing commas still missing**. JOB 2, 3 and 4 are not done. The hockey program she
wrote on 2 Sept is **gone** — the IDE was reseeded with the menu homework and nothing in
`student_ide` holds it. So "open the Project tab" was a dead end and the deck now opens with a
**paste block** (slide 6) that restores the hockey dict plus the `for team in hockey:` loop she
typed herself, so the 15 carried hockey slides have a file to work on. STEP 1 is the three commas.

**Visual, mandatory for the nested loop:** the outer loop's key highlighted in one colour,
the inner loop's counter ticking 1, 2, 3 underneath it, one frame per inner pass, and the
outer key changing only when the inner list runs out. This is the exact thing that is hard.

---

## 20:00 KST · 18:00 HCMC · YOOJUN — `yoojun-first-square.html`

**Track:** none yet · Minecraft **BLOCKS** · **Source:** none — first ever lesson
**Topic Kasim gave:** trial lesson, Grade 1, Minecraft blocks

**TRIAL LESSON. 40 minutes, not 60. Grade 1 — the youngest student on the list today.**
There is no previous lesson, no transcript, no homework and no ledger. Nothing to carry and
nothing to check.

**No tracker row and no student folder.** Build the deck in `lessons/2026-09-09/` and stop
there — there is no folder to copy it into and one must not be invented.

**The shape of the lesson:**
- Something visible on screen inside the first five minutes. A Grade 1 student who has not
  seen a result in five minutes is lost.
- **Steps must be tiny** — smaller than any other deck today. One block dragged per slide.
- Still overshoot: build far past 40 minutes of material so it cannot run out. The tail
  becomes lesson two if the trial converts.

**The lesson:**
- v1 — `on chat command "go"` with one `agent move forward 1`. Type `go`, the agent moves.
  That is the first win.
- v2 — more moves, so it walks a line
- v3 — `agent turn left`, so it turns a corner
- v4 — four moves and four turns, so it walks a square
- v5 — `agent place on move [ON]`, so the square becomes a drawn shape left in the world
- v6 — `repeat 4` wrapped around one move and one turn, so the same square comes from four
  blocks instead of eight. **This is the idea worth showing a parent.**

**Visual, mandatory:** a top-down grid with the agent as an arrow, one frame per block run,
showing the trail it leaves. A Grade 1 student reads the picture, not the words.

**Never** open with a world file. Kasim hosts, Yoojun joins, and the join clicks are spoken.

---

## 21:00 KST · 19:00 HCMC · 이현 (LEE HYEON) — `ihyeon-agent-feels-the-wall.html`

**Track:** MS000, Minecraft **BLOCKS** (MakeCode) · **Source:** ledger 2026-09-02, from transcript
**Topic Kasim gave:** carry on from last lesson — the real wall detection
**Reference deck:** `../2026-09-02/ihyeon-maze-first-turn.html` — own deck, same markup and tone

**What actually happened last time**
- Loop blocks, and true/false
- `if` blocks
- `agent detect` — front, left, right, down
- Redstone used as the signal
- Making rules (right side clear → turn left)
- Three helper commands: R, L and TP
- Why a pile of `if` blocks gets slow
- Solved 8 mazes

**Unmet promise:** the promise was **wall detection**, and the lesson used **redstone blocks
laid on the floor** as the signal instead. The parent was told the agent would look at walls.
**That is today.**

**Carry:** none worth having — reached about slide 59 of 62 and the tail is wrap-up.
Build fresh.

**The new idea:** **the agent detects the wall itself, with no redstone laid down.** Last
week the maze had to be marked out for the agent. Today the maze is bare and the agent still
gets through, because `agent detect block forward` answers true or false on its own.

Build it as a ramp:
- v1 — last week's redstone rule, dim, one slide, to name what is being replaced
- v2 — swap the redstone check for `agent detect block forward`, same maze, same result,
  **no redstone placed** — this is the whole point, show the two side by side
- v3 — `if / else`: wall in front → turn, no wall → move forward
- v4 — wrap it in a `repeat until` so the agent solves the maze without being told the shape
- v5 — the right-hand rule: always try right first, then forward, then left. One rule that
  solves any maze.

**Visual, mandatory:** a top-down maze grid, agent as an arrow, and a true/false flag drawn
at the square in front of it on every frame. The flag is the block's answer. Show it flipping
as the agent turns.

**△ Known habit:** moves to the next step before the agent has finished. Build one slide that
makes the wait visible — the agent still walking while the next block is already highlighted.
