# Today's decks — 2026-09-01 (Tue)

Six lessons, 16:00 → 23:00 Korea time. One deck per student, built from what the
tracker says they last did and what was promised for next time.

**Roster source of truth today is the calendar, not `tools_students`.** The
tracker is stale in three places (see the drift note at the bottom). Kasim
confirmed the six students by name this morning.

## Hard rules for every deck

Read first, in this order:
1. `../../TEMPLATE.md` — the 20-slot structure and the per-slide rules
2. `../../PEDAGOGY.md` — why each slot exists
3. `../../assets/style.css` — the only styling allowed; the BC-track section holds
   `.trace-grid`, `.debug-card`, `.err`, `.quiz-card`, `.stretch-list`, `.exit`,
   `.activity-tag`
4. One finished deck in the matching course folder, as the reference for tone
   (Minecraft Python: `../2026-08-31/eunwoo-see-the-numbers.html` and
   `../2026-08-30/leo-loop-that-changes.html` · Pygame:
   `../2026-08-25/jason-finish-the-game.html` and
   `../2026-08-25/hwon-drive-super-dario.html`)

Then:
- Save to `lessons/2026-09-01/<file>.html`. Stylesheet path is
  `../../assets/style.css` and the script is `../../assets/deck.js` — this folder
  sits two levels deep, same as every course folder.
- **Overshoot on purpose.** Base is the 20-slot structure, then add 4–8 extra
  slots: more debug cards, a harder modify, extra stretch challenges. Target
  **26–30 slides**. A lesson must never run out of material. Mark the overflow
  slots with `<span class="activity-tag">OPTIONAL</span>` so the ones that must
  be taught stay obvious.
- Update the `counter` span to `1 / <total>` and check `deck.js` for how it
  counts, so navigation and the counter agree.
- Per-slide caps hold everywhere: **≤ 40 English words, ≤ 15 Korean words**.
- Korean glosses only on Tier-3 vocab, concept hooks, and bridges.
- Only reuse existing CSS classes. No new inline component styling.
- Slot 2 (Recap) must recall **that student's own last lesson**, using the facts
  in their brief below — not a generic recap.
- The △ lines in a brief are what the student actually got wrong. Turn each into
  a Common Mistake or Debug slot rather than inventing a bug.

### Copy-this-and-it-works contract

The student makes **zero decisions**. If a slide needs the student to infer
anything, it is wrong.

- **One change per slide**, numbered `STEP n / total`. A re-indent is its own step.
- Every code step carries all four:
  - **the code** — full OLD block and full NEW block, never `...` inside a
    changed region
  - **🔍 FIND** — the exact Ctrl+F string
  - **📍 where** — quote the existing line it goes under, and the indent count
  - **🟣 why** — one line
  - **✅ check** — one line: what running it should show
- **Big programs ramp v1 → v2 → v3 → v4.** Never the finished program first. New
  lines hot, unchanged lines dim, changed lines get an explicit OLD/NEW block.
- **Visuals beat words, and are mandatory for loops, iteration and any maths** —
  one frame per pass with the counter value shown; spacing as boxes on a number
  line; x positions as jumps.

### API form — Minecraft Python

Write it the way the decks write it, never the way a tracker draft paraphrases it:

```python
blocks.fill(QUARTZ_BLOCK, pos(2, 0, 0), pos(4, 6, 0))
agent.move(FORWARD, 5)
```

Block names are **bare CAPS constants** — no quotes, no strings. Same for
directions. A message or slide that writes `"quartz_block"` or `agent.move("forward", 5)`
is wrong and will not run.

---

## 16:00 KST · 14:00 HCMC · RIO — `rio-x-before-y.html`

**Track:** MS002, Minecraft Python · **Source:** log, 2026-08-25

**Covered last time**
- `blocks.fill` structure — block type, start `pos`, end `pos`
- Counting an X range and a Y range on the grid
- Coordinates start at **0**, not 1
- Underscores in block names (`MOSS_BLOCK`)
- Splitting the two `pos()` calls onto separate lines to read them

**✓ Wins** — entered the 7→11 / 3→3 range correctly, then worked out the next
block (6→12) himself. Fixed the moss-block name the instant the underscore was
explained. Late in the lesson he started calculating ranges (8→10, 9→9) before
getting hints.

**△ Mistakes — the deck exists because of these two**
- **Mixed up the X and Y axes several times.** Needed a screen-share example
  before the order settled.
- **Zero-start not internalised.** Entered `3,3` where `2,2` was needed.

**Today (Kasim's pick):** warm up on the two shaky ideas, then **learn `z` — the
third number in `pos()`, the one he has always typed `0` into.** Depth/forward.
By the end he builds a path running out of the gate and a roof over both, using
a z *range*, and knows z counts from 0 exactly like x and y.

**Every lesson teaches something new.** The drill is the way in, not the whole
lesson. Build it as a ladder of tiny identical-shaped tasks (one `blocks.fill`
line each), and the last two rungs are the new z idea.

- Slot 5 model: the grid as **two rulers**, X along the bottom, Y up the side.
  Always read the bottom one first. Say the sentence "**X first, then Y**" on
  every code slide.
- **Off-by-one visual is mandatory.** Draw a strip of boxes labelled
  0 1 2 3 4 5 and mark that 6 boxes end at **5**. Repeat that strip whenever a
  range appears.
- Ramp: v1 one flat bar · v2 a rectangle (X range + Y range) · v3 two rectangles
  side by side · v4 a small shape made of three fills · **v5 the new idea — z**:
  a path at `pos(0,0,1)`→`pos(5,0,4)`, then a roof at `pos(0,9,0)`→`pos(5,9,4)`.
- **z semantics, confirmed against the other Minecraft decks:** `pos(x, y, z)` =
  x across, y up, z forward. Never paraphrase it the other way round.

**Debug slides (3+)** — (1) X and Y swapped, so the wall builds sideways;
(2) `pos(3,3,0)` where `pos(2,2,0)` was meant — his real 08-25 mistake, show the
block landing one square off; (3) `MOSS BLOCK` with a space instead of
`MOSS_BLOCK`; (4) OPTIONAL: end `pos` smaller than start `pos`.

**Code Talk Frame** — "X goes from ___ to ___, Y goes from ___ to ___, so the
fill is `pos(___,___,0)` to `pos(___,___,0)`." Make him read it aloud on every
build, not once.

---

## NOT TODAY · EUNWOO — Wed 17:00 KST · 15:00 HCMC — `eunwoo-see-the-numbers.html`

⚠ **Corrected by Kasim 2026-09-01: EUNWOO teaches Wednesday 17:00 KST, not Tuesday.**
The deck below is built and correct. It is tomorrow's (09-02) lesson, not today's.
No parent message goes out for her today.

**Track:** MS002, Coordinates, Minecraft Python · **Source:** log, 2026-08-24

⚠ **Corrected mid-run on 2026-09-01.** The 08-31 lesson never happened. Three
independent checks agree: Notion full-text search returns nothing for Eunwoo
after 2026-08-24, there is no `tools_log_drafts` or `tools_lesson_logs` row for
08-31, and **Monday 2026-08-31 had no EUNWOO calendar event at all** (that day
was AMY, NEO, JUN, ETHAN, YUNHO). He had already moved off Monday onto this
Tuesday 17:00 slot.

So `../2026-08-31/eunwoo-see-the-numbers.html` was built for a slot that no
longer existed and was never delivered. **That deck is today's deck** — it was
written from the 08-24 draft, so its Recap slot already recaps the right lesson.
It has been copied into this folder unchanged and re-verified (38 slides,
counter matches, asset paths correct, no quoted-string API bug).

`eunwoo-two-strands.html` stays in this folder **unlinked from `index.html`**.
It is the correct next lesson, queued for whenever he finishes the number
reading. Do not teach it today — its Recap assumes a lesson that did not happen.

**Covered last time (08-24 log)**
- Coordinate values stored in lists (`XS`, `ZS`)
- A `for` loop running 24 iterations
- The **modulo operator** `%` for index calculation (`i % 8`, `i % 4`)
- Calculated coordinates in variables `ax`, `az`, `bx`, `bz`, `k`, `j`
- Gold and emerald blocks placed with `blocks.fill()` and `pos()`
- A DNA-spiral structure

**✓ Wins** — worked out on her own that the DNA spiral needed obsidian; noticed
her code ran clean where the teacher's did not.

**△ Mistakes — still open**
- **Fixed a bug but could not explain what changed** — *"it just got fixed."*
- **Does not understand how `ax`, `az`, `bx`, `bz` are calculated.** The algebra
  idea is new to her.

**Today (Kasim's pick):** read the numbers first, then **use them to build the
second strand** — `j = (i + 2) % 4`, `bx`/`bz` from the same lists, emerald
placed opposite the gold. The tracing is the way in; strand B is the new idea,
and it is the payoff for being able to read `i % 4` at all.

The trace half stays **trace-heavy** and uses `.trace-grid` far more than usual.
The v3 slides are no longer OPTIONAL — they are the lesson's new idea.

Step 1 — `%` on its own, with no Minecraft in sight. A row of 12 numbers and what
`i % 4` gives for each. Slot 5 model: a **clock with 4 hours**; counting past 3
lands back on 0. The wrap-around arrow is drawn.

| `i` | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|---|
| `i % 4` | 0 | 1 | 2 | 3 | 0 | 1 | 2 | 3 | 0 |

Step 2 — `XS[i % 4]`: the index picks a slot in the list, the list gives back a
coordinate. The list is drawn as four labelled boxes with an arrow landing in one.

Step 3 — the coordinate table she was promised on 07-21 (*"build a coordinate
table so Eunwoo finds the pattern rule herself"*). She fills in `i`, `i % 4`,
`ax`, `az` for `i = 0…7`, and states the rule.

Ramp: v1 four blocks from a list · v2 the loop with `%` wrapping · **v3 the
second strand `bx`, `bz` offset from the first — today's new idea, core not
optional** · v4 the full spiral with height (still OPTIONAL).

**Debug slides** — (1) `XS[i]` without `%` → `IndexError` once `i` passes the
list length; (2) `i % 8` where `i % 4` was meant → the pattern repeats too
slowly; (3) the index used as the coordinate directly, so blocks land at 0,1,2,3
instead of the list values; (4) OPTIONAL: `blocks.fill` vs `blocks.place` mixed
up — her real 07-21 mistake.

**Code Talk Frame** — force the sentence she could not produce:
"`i % 4` gives ___, so `XS[i % 4]` picks ___, which puts the block at ___."
This directly answers the *"it just got fixed"* problem. She says it twice.

**Next lesson:** `eunwoo-two-strands.html` in this folder covers strand B plus
the rungs between the strands. Strand B is taught today, so that deck needs its
opening rebuilt around the rungs before it is used.

---

## 18:00 KST · 16:00 HCMC · HWON — `hwon-four-walls-and-the-bread.html`

**Track:** RS003, Python / Pygame · **Source:** log, 2026-08-25

**Covered last time**
- The event loop and the quit button (`pygame.event.get()`, `pygame.QUIT`)
- `pygame.key.get_pressed()` with `K_RIGHT` / `K_LEFT` / `K_UP` / `K_DOWN`
- Four-direction movement: `x` / `y` plus or minus `speed` every frame
- Boundary conditionals; **y counts DOWN from the top**; the right wall needs
  `WIDTH - width`
- Screen resized to 800 × 800

**✓ Wins** — explained x/y = position and w/h = size the moment he was asked.
Wrote the UP/DOWN key blocks himself after seeing the LEFT/RIGHT pattern.

**△ Mistakes — the deck exists because of these three**
- **The y-axis direction (0 at the top) is still shaky** after several
  explanations.
- **First wrote the right boundary as `x > 800`** — forgot that `x` is the left
  edge. Fixed only after a diagram.
- **The down wall was left as a copy of the up wall** at the end of the lesson —
  that was his homework.

**Homework he was sent:** walls worksheet — find and fix the down wall, make the
right wall use `super_dario['w']`.

**Today (promised):** **finish all four walls, then bread collision (eat the
bread).** Homework check first, then the new idea.

- Slot 2 recap is the homework: put his down-wall bug on screen and let him say
  what he changed.
- **The y-axis visual is mandatory and goes early.** Draw the 800×800 screen with
  `y = 0` at the TOP and an arrow pointing DOWN labelled "y gets bigger". Reuse
  it on every wall slide.
- **Each edge is its own step.** Left wall, right wall, top wall, bottom wall —
  four separate STEP slides, each with the diagram beside it showing which edge
  the number belongs to.
- The right wall step must spell out: `x` is the **left** edge, so the right edge
  is `x + width`, so the limit is `WIDTH - width`.
- Then collision: `pygame.Rect` for Dario and for the bread, `colliderect`, and
  moving the bread to a new random spot when it is eaten.
- Ramp: v1 all four walls working · v2 the bread drawn · v3 the two rects and
  `colliderect` printing "yum" · v4 the bread respawns and the score goes up.

**Debug slides (3+)** — (1) `x > 800` instead of `x > WIDTH - width`, so half of
Dario leaves the screen; (2) the down wall still checking `y < 0` (his exact
homework bug); (3) `colliderect` written without `()` so it never fires;
(4) OPTIONAL: the bread respawn placed outside the `if`, so it teleports every
frame.

**Code Talk Frame** — "`y = 0` is the ___ of the screen, so bigger `y` means
___." And: "`x` is the ___ edge, so the right edge is `x` plus ___."

---

## 19:00 KST · 17:00 HCMC · JASON — `jason-pick-the-next-project.html`

**Track:** RS003, Python / Pygame · **Source:** log, 2026-08-25

⚠ **Calendar time 19:00 KST is correct. The tracker's 17:00 is stale** — his
Notion notes have been at 19:00 since 08-18.

**Covered last time**
- `boss_level` as a global, reset to 1 in `reset_game()`
- Level scaling: `boss_hp = BOSS_MAX_HP + (boss_level - 1) * 10` and
  `boss_speed = BOSS_SPEED + (boss_level - 1)`
- Feeding `boss_hp` / `boss_speed` into the boss dict (`hp`, `max_hp`, `vx`)
- `abs()` for the wall bounce (left wall done in the lesson)
- The 5-bullet spread: `for vx in [-4, -2, 0, 2, 4]` then append with `"vx"`
- Win condition: `BOSSES_TO_WIN`, `game_won`, the YOU WIN screen
- Balancing enemy and boss sizes, sprite rotation

**✓ Wins** — completed the `(boss_level - 1)` formula himself. Spotted dead code
at line 439 unprompted and said to remove it. Applied the CAPS-for-constants rule
without being reminded.

**△ Mistakes**
- **`abs()` needed a full explanation** before it clicked.
- **Missed the colon after `if`** several times.
- **Needed a walkthrough of `boss_x + boss_w // 2`** centering.

**Homework he was sent:** bug hunt worksheet — fix the spread spawn `/(2 - 8)`,
fix the right wall `-BOSS_SPEED` with `-abs()`, add a Boss x/5 counter UI, add
boss rage (`cooldown - boss_level * 5`).

**Today (promised):** **check the homework, celebrate the finished game, pick the
next project.**

This deck has an unusual shape. It is **one third review, one third celebration,
one third a choice.** Build it that way.

- **Part 1 — homework marking (slots 2, 10–12).** One debug card per worksheet
  task, in the worksheet's own order. He reads out what he changed; the card
  shows the fix.
- **Part 2 — the finished game (slots 5–7).** A single slide showing the whole
  architecture of what he built: the boss loop, the level formula, the spread,
  the win screen. Label the parts he wrote himself. This is the celebration —
  make it visual, a map of the program, not a wall of code.
- **Part 3 — the choice (slots 17–18).** Three next projects as three cards, each
  with a one-line hook, one screenshot-style mock, and the first thing he would
  build. He picks one at the end of the lesson.
  - **A — enemies that think:** simple chase AI, a state machine (patrol / chase
    / flee). Builds on his boss dict.
  - **B — a platformer:** gravity, jumping, ground collision. New physics, same
    Pygame.
  - **C — a level editor:** draw a level in a grid, save it to a file, load it
    back. New idea: files.
- Make the pick a real decision with a real slide, not a throwaway question.

**Debug slides (3+)** — all four homework tasks become debug cards:
(1) the spread spawn `/(2 - 8)`; (2) the right wall needing `-abs()`;
(3) the Boss x/5 counter drawn before `pygame.display.flip()`;
(4) the rage cooldown going negative when `boss_level` gets big.
Then his own △: (5) OPTIONAL — a missing colon after `if`, and
(6) OPTIONAL — `boss_x + boss_w // 2` traced with real numbers.

**Code Talk Frame** — "`abs()` turns ___ into ___, so the boss always moves
___." And, for the pick: "I want to build ___ because ___."

---

## 20:00 KST · 18:00 HCMC · LEO KIM — `leo-two-formulas-one-build.html`

**Track:** MS002, Minecraft Python · **Source:** log 2026-08-25 +
`../2026-08-30/leo-loop-that-changes.html`

**Covered last time (08-25)**
- Patterns: how a variable changes on each turn of a loop
- The Fibonacci rule (add the previous two numbers)
- `for` with `range()`
- `blocks.fill()` 3D shapes; managing six corner variables
  (`x1`, `x2`, `y1`, `y2`, `z1`, `z2`)
- Update lines go **INSIDE** the loop (indentation)
- Colour-coding shapes to debug

**Also covered 08-30:** one loop, many structures — a row of pillars whose
spacing comes from a multiplier.

**✓ Wins** — found the Fibonacci rule himself. Read the staircase deltas off the
pattern unprompted ("x +2, z +2, y +1"). Strategic: picked the easiest pattern
first, on purpose.

**△ Mistakes**
- **Put update lines on the same line as / outside the `for` loop** — an
  indentation error that needed several passes.
- **Unsure whether to reuse or re-create `y`** when the delta differs between
  patterns.
- (08-30) **Says only "I don't know" when stuck**, and **waits for the teacher to
  type first.**

**Homework he was sent:** growing shapes worksheet — staircase, pyramid,
Fibonacci towers (no lists, plain `h1`/`h2` hand-over), flat-staircase bug hunt,
variable-reuse question.

**Today (promised):** **check the homework, then combine two formulas in one
build.** One loop, two variables changing by two different rules at the same
time — e.g. `x` grows by a fixed step while `y` grows by the Fibonacci rule.

Two things this deck must keep doing from 08-30:
- **Sentence frames for being stuck.** Three to read aloud instead of "I don't
  know": "It breaks on line ___.", "I expected ___ but I got ___.", "I don't know
  what ___ means." Put them early **and** late.
- **Type-first prompts.** Every Make slide starts with him typing one line before
  any demo. Mark them so Kasim waits.

- **Two-column trace is mandatory.** `.trace-grid` with `i`, `x`, `y` — one row
  per turn, so he sees two rules running in the same loop.
- The reuse-vs-recreate △ gets its own slide: one `y` that keeps its value across
  turns, next to a fresh `y` made each turn, and what each one builds.
- Ramp: v1 one formula (his 08-30 pillars) · v2 the second formula on its own ·
  v3 both in one loop · v4 both plus the shape's height.

**Debug slides (3+)** — (1) the update line dedented out of the loop, so nothing
grows (his exact △); (2) the two updates in the wrong order, so `y` uses last
turn's `x`; (3) `y` re-created inside the loop, so the Fibonacci chain resets
every turn; (4) OPTIONAL: `range(5)` where six shapes were wanted.

**Code Talk Frame** — "`x` changes by ___ each turn and `y` changes by ___, so
after turn 3 they are ___ and ___."

---

## 23:00 KST · 21:00 HCMC · JIYU — `jiyu-pixel-art-with-loops.html`


⚠ **Coordinate origins (Kasim, 2026-09-01):** `x` and `z` start at **1**, `y`
starts at **0**. The student stands on the grid's `0,0,0`, so `x 0` / `z 0` are
the lines under their feet and `y 0` is the floor. Flat pixel art sits at `z 1`,
not `z 0`. First free square is `pos(1, 0, 1)`.
**Track:** MS001, Minecraft Python · **Source:** log, 2026-08-25

**Covered last time**
- `blocks.fill()` with coordinate ranges — start `pos`, end `pos`, block type
- The X / Y / Z coordinate system; **Z fixed at 0** for flat pixel art
- Counting coordinates right to left
- Creeper pixel art: legs, body + head as one rectangle, eyes
- Python form: `blocks.fill(PINK_CONCRETE, pos(5,0,0), pos(7,7,0))`; run with `r`

**✓ Wins** — first leg (5→7, 0→7) done straight after the coordinate explanation.
Counted backwards from 15 to get 10→12 for the second leg herself, and kept Y the
same. Body + head as one rectangle in one attempt. Both eye coordinates right.

**△ Mistakes — the deck exists because of these three**
- **Confused overwriting numbers in an old line with adding a NEW fill line.**
- **Block-name spelling stopped the run** several times (found via the grass swap
  test).
- **Comma slips** — typed `770` and `1012` instead of `7,1,0` and `10,12,0`.

**Homework she was sent:** pixel art architect worksheet — comma drill,
block-name drill, mushroom build (one fill per shape), own 4-fill design.

**Today (promised):** **check the homework, then bigger art with loops.**

- Slot 2 recap is the homework: her own 4-fill design on screen, and the comma
  drill answers.
- **The comma △ is a formatting habit, not a concept.** Give it a permanent
  visual: `pos(` **7** `,` **1** `,` **0** `)` with the three numbers in three
  coloured boxes and the commas oversized between them. Repeat the boxes on every
  code slide in the deck.
- **New-line-vs-edit gets its own STEP slide.** Show the old line unchanged and a
  brand-new line added underneath, with 📍 quoting the line it goes under.
- Then the loop: the same shape repeated down the wall, with `i` from `range()`
  feeding one of the coordinates.
- **Loop visual is mandatory** — one frame per pass, `i` shown, the block landing
  in a different place each time.
- Ramp: v1 one shape by hand · v2 the same shape written with `i` fixed at 0 ·
  v3 the `for` loop repeating it · v4 a second colour offset from the first.

**Debug slides (3+)** — (1) `pos(770)` instead of `pos(7,7,0)` — her exact comma
slip, show the error message; (2) `PINK CONCRETE` with a space, so the run stops;
(3) an old line edited when a new line was wanted, so the first shape vanishes;
(4) OPTIONAL: `i` used in the loop but the coordinate never changing, so all
shapes stack in one spot.

**Code Talk Frame** — "`pos` takes ___ numbers with a comma between each, so 7, 1
and 0 is written ___." And: "This turn `i` is ___, so the shape lands at ___."

---

## Carried over, not teaching today

**Ryan** — `ryan-enemy-name-tags.html` was pre-built on 2026-08-27 for this
folder from his live IDE code and the 08-20 draft. His 09:00 KST slot did not run
today. **The deck is now stale**: his 08-27 log shows enemy dictionaries and
`stats = enemies[enemy[2]]` were already covered, which is what that deck
teaches. Rebuild from the 08-27 log before it is used — the bridge named in the
old brief was "enemies shoot back".

## Tracker drift — reported, never auto-fixed

`tools_students` disagrees with the calendar and with Notion in five places.
Nothing here was written to the database.

| Student | Tracker says | Reality |
|---|---|---|
| JASON [PH] PYGAMER | Tue 17:00 KST | Tue **19:00** KST — calendar and every Notion note since 08-18 |
| EUNWOO COORDINATES | Mon 19:00 KST | **Wed 17:00** KST (confirmed by Kasim 2026-09-01) |
| DAVID G8 | Tue 21:00 KST | **Sun 19:00** KST (17:00 HCMC) |
| YURA G5 | Tue 22:00 KST | **Sat 18:00** KST (16:00 HCMC) |
| Ryan | Tue 09:00 KST | Last two lessons were **Thursday** 09:00 KST |

**SUHO** — resolved by Kasim 2026-09-01: **Sat 09:00 KST · 07:00 HCMC**.

| Source | Says | Verdict |
|---|---|---|
| `tools_students` | Sat 09:00 KST | correct |
| Google Calendar | Sat 09:00 KST, title `MS001 [화 9시]` | correct |
| Notion (newest note 08-29) | Sat 09:00 KST | correct |
| `english-coding-students/roster.json` | `weekday_en: "fri"`, folder `ms001-fri-0900` | **WRONG** |

`roster.json` is the file `/slides-today` step 2 reads to decide who teaches. As
it stands, SUHO would be built into Friday's deck run and missed on Saturday.
The fix is one line: `"fri"` → `"sat"`, `"금"` → `"토"`. The folder name can stay
as it is, since matching is on `tracker_name`. Not changed by this run —
`roster.json` is outside what `/morning` may write.
