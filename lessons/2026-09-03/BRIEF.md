# Today's decks — 2026-09-03 (Thu)

Seven lessons on the calendar. **RYAN's 09:00 KST lesson already happened this
morning** (transcript in Drive, ledger row written) — no deck, no message.
Six decks needed, 15:00 → 21:50 Korea time.

**Topics are Kasim's, given this morning. They override `promised`.** Kasim named
five by track; the concrete next step inside each track is named below and was
read back to Kasim. IAN was not named — that one is the Idea line.

| Time | Student | Topic | Deck |
|---|---|---|---|
| 15:00 KST · 13:00 HCMC | ERIC KIM | MC **Python** — function parameters `make_tree(x, z, leaf)` | `eric-trees-that-take-orders.html` |
| 16:20 KST · 14:20 HCMC | JJ (snlovelyb) | MC **Blocks** — change a variable *inside* the loop | `jj-the-growing-staircase.html` |
| 19:00 KST · 17:00 HCMC | DANIEL | Python — `+=` / `-=` reassignment in an input-driven shop | `daniel-money-that-changes.html` |
| 20:00 KST · 18:00 HCMC | SEOHYEON | MC **Blocks** — a loop inside a loop (nested repeat) | `seohyeon-loop-inside-a-loop.html` |
| 21:00 KST · 19:00 HCMC | SERENA | Python — jumping with velocity + landing on the floor | `serena-make-the-cat-jump.html` |
| 21:50 KST · 19:50 HCMC | IAN | Web — one shared `style.css` linked from all 9 pages | `ian-one-file-styles-them-all.html` |

## Hard rules for every deck

Read first, in this order:
1. `../../TEMPLATE.md` — the slot structure and per-slide rules
2. `../../PEDAGOGY.md` — why each slot exists
3. `../../assets/style.css` — the only styling allowed
4. The reference deck named in that student's section below, for tone

Then:
- Save to `lessons/2026-09-03/<file>.html`. Stylesheet `../../assets/style.css`,
  script `../../assets/deck.js`.
- **Overshoot on purpose.** No slide-count target and **no ceiling**. If the
  teacher could plausibly reach the last slide inside the hour, the deck is too
  short — add more taught ideas. Extra room goes to **new concepts with a visual
  each**, never more debug cards. Tag surplus `<span class="activity-tag">OPTIONAL</span>`.
- Update the `counter` span to `1 / <total>`.
- Per-slide caps: **≤ 40 English words, ≤ 15 Korean words**.
- Korean glosses only on Tier-3 vocab, concept hooks and bridges.
- Only reuse existing CSS classes. No new inline component styling.
- Slot 2 (Recap) recalls **that student's own last lesson**, from the facts in
  their section below. Never generic.
- The △ lines are what the student actually got wrong. Turn each into a Common
  Mistake or Debug slot rather than inventing a bug.

### Shape of the hour
Short recap of last week, then **most of the hour on the new idea**. A deck that
spends half the hour on last week is a failed deck.

### Copy-this-and-it-works contract
The student makes **zero decisions**. If a slide needs the student to infer
anything, it is wrong.

- **One change per slide**, numbered `STEP n / total`. A re-indent is its own step.
- Every code step carries all four:
  - **the code** — full OLD block and full NEW block, never `...` inside a changed region
  - **🔍 FIND** — the exact string to search for (block track: the exact block to look at)
  - **📍 where** — quote the existing line it goes under, and the indent count
  - **🟣 why** — one line
  - **✅ check** — one line: what running it should show
- **Big programs ramp v1 → v2 → v3 → v4.** Never the finished program first. New
  lines hot, unchanged lines dim, changed lines get an explicit OLD/NEW block.
- **Visuals beat words, and are mandatory for loops, iteration and any maths** —
  one frame per pass with the counter value shown.

### API form — Minecraft **Python** (ERIC only today)
Constant form, never strings:

```python
agent.move(FORWARD, 5)
blocks.fill(OAK_LOG, pos(0, 0, 0), pos(0, 4, 0))
```

Coordinates: **y starts at 0; x and z start at 1.**

### Block track — JJ and SEOHYEON only
**Zero Python anywhere in their decks** — not in a code block, not in a debug
card, not in a comment. Draw the blocks with the `.mcb` / `.mcb-c` components at
the end of `assets/style.css`. Reference decks:
`../2026-09-02/seohoo-pixels-with-a-loop.html` and `../2026-09-02/ihyeon-maze-first-turn.html`.

Category classes and their (now corrected, pixel-sampled) colours:
`basic` `player` `blocks` `mobs` `agent` `gameplay` `pos` `loops` `logic` `vars` `math`.
Every new block gets a `.mcb-from` line naming its toolbox drawer.

Block anatomy: colour follows the **drawer the block came from**, never the block
it sits inside. Nested input = its own drawer colour × 0.85. Number field = white
pill oval. `~` is white label text printed inside the position pill, outside the
white number ovals.

---

## 15:00 KST · 13:00 HCMC — ERIC KIM [MBS002] · Minecraft **Python**

**Last lesson (2026-08-27, log + draft agree):**
- `def make_tree()` — a function with **no parameters**
- x1, x2, y1, y2, z1, z2 declared inside the function
- `blocks.fill` for trunk and leaves
- `leaves_type = [...]` list of cherry / dark oak / pale oak leaves
- `for leaves in leaves_type` to cycle block types per tree
- `x1 += 10` / `x2 += 10` to space trees apart

✓ Self-checked the for-loop unprompted: "4 types → loops 4 times"
△ List syntax slips — missing commas, mismatched parens; asks before self-debugging
△ Copies code from screen instead of typing independently

**Unmet last week:** nothing missed.
**Said next:** nothing recorded.

**Today's new idea:** give the function **parameters**. `def make_tree(x, z, leaf)`
so one function builds a tree *anywhere*, with *any* leaf, instead of walking a
global x1 forward by 10 each time. Ramp: v1 the function Eric has → v2 one
parameter `x` → v3 add `z` → v4 add `leaf`, then call it four times to plant a
row, then call it from inside a loop to plant a forest.
Visual required: the same `make_tree` box with different values dropping into the
slots, and the resulting tree appearing at a different spot each call.
△ list-syntax slip becomes a Common Mistake slide (missing comma in the argument list).

Reference deck for tone: `../2026-09-01/leo-two-formulas-one-build.html`.

---

## 16:20 KST · 14:20 HCMC — JJ (snlovelyb) · Minecraft **Blocks**

**Last lesson (2026-08-27, log + draft agree):**
- Made a variable `long`, `set long to 5`
- Used the variable as a parameter: `agent move forward by long`
- `repeat 4 times` loop; deciding what goes inside vs outside the loop
- `agent move forward`, `agent turn left`, `agent move up`
- `agent set block`, `agent place on move`
- Chat command `RL` to recall the agent
- Built a square with blocks; placed flowers in a line

✓ Tracked the variable value changing 7→10→5 in `move forward by long`
✓ Self-spotted that `move up` had to move outside the loop
△ Needed repeated help placing `set long to 5` in the right position
△ Could not drop a variable block into a number slot unassisted

**Unmet last week:** nothing missed.
**Said next (2026-08-20 draft):** block-count vs move-count distinction — fold in
as the ✅ check wording, not as the lesson.

**Today's new idea:** **change the variable inside the loop.** Last week `long`
was set once and stayed 5. Today `change long by 1` sits *inside* the repeat, so
every pass draws a longer arm — a growing staircase / spiral instead of a square.
Ramp: v1 the square JJ has → v2 add `change long by 1` inside → v3 turn it into a
spiral → v4 a staircase using `move up` once per pass.
Visual required: one frame per loop pass with the value of `long` printed and the
arm drawn that many blocks long — pass 1 = 5, pass 2 = 6, pass 3 = 7, pass 4 = 8.
△ "can't drop a variable into a number slot" becomes a dedicated slide using
`.mcb-drop` — show the empty oval and the red VARIABLES oval going into it.

Reference deck for tone: `../2026-09-02/ihyeon-maze-first-turn.html`.

---

## 19:00 KST · 17:00 HCMC — DANIEL PYTHON ADVENTURES · Python

**⚠ No log and no draft for 2026-08-27, and no Drive transcript for that date.**
The newest facts are from **2026-08-20**. Write the recap and the parent message
against 08-20, not 08-27.

**Last lesson (2026-08-20 draft):**
- `input()` to receive user input
- Storing input in variables (name, age, food)
- Using variables inside `print()`
- `int()` type conversion
- Basic subtraction on numeric variables
- String vs integer type errors

✓ Wrote the slippers/gecko purchase calculation with `int()` after one explanation
△ Waited for hints on missing capital letters instead of finding them unprompted

**Unmet last week (the promise from 08-20):**
> "Next lesson: variable reassignment, to fix the value-not-updating issue found today"

This is the strongest input today. It was promised and not delivered.

**Today's new idea:** **`+=` and `-=`** — reassignment that actually sticks.
Plain `money = money - 20` was seen on 08-13, so the new thing is the shorthand
and, more importantly, *reassigning in a loop so the value accumulates*.
Ramp: v1 print a fixed balance → v2 `money = money - price` once → v3 `money -= price`
→ v4 ask the price with `input()` + `int()` and subtract it → v5 wrap it in a
`while` so Daniel can buy several things and watch the balance fall.
Visual required: a money box redrawn after each purchase, with the old value
crossed out and the new value beside it, one frame per purchase.
△ missing-capital-letter slip becomes a Common Mistake slide (`Money` vs `money`).

Reference deck for tone: `../2026-08-31/ethan-for-loops-range.html`.

---

## 20:00 KST · 18:00 HCMC — SEOHYEON MS · Minecraft **Blocks**

**Last lesson (2026-08-27, log + draft agree):**
- Opening Code Builder (`C`) and starting a new project
- `on chat command` + `run` to fire the code
- `fill` a glass box 1,1,1 → 15,15,15; water 2,2,2 → 14,14,14
- `agent place` + `agent move` together; moving with keyboard and mouse
- `set side to 15`, `repeat 10 times`, `agent move forward by side`,
  `change side by -2` → a pyramid
- Choosing the block type (sandstone)

✓ Finished both the aquarium and the pyramid
△ Mixed up `right` and `forward` in `agent move`
△ Waited to be asked instead of saying "Teacher, I did it"

**Unmet last week:** nothing missed.
**Said next (2026-08-20 draft):** give Seohyeon time to try before the teacher types —
that is a teaching note, not a topic.

**Today's new idea:** **a loop inside a loop.** Seohyeon has already changed a variable
inside one repeat (the pyramid). The new construct is nesting: an outer
`repeat` that runs a whole inner `repeat` each pass. Build a flat floor
(rows × columns), then stack floors into a solid tower.
Ramp: v1 one `repeat` = one line of blocks → v2 wrap it in a second `repeat` +
turn = a square floor → v3 add `agent move up` between floors = a tower →
v4 shrink each floor with `change side by -1` = a stepped pyramid.
Visual required: a grid filling in one cell at a time, with **both** counters
shown side by side — outer pass 1/3, inner pass 1/5 — so the inner
loop is seen to finish completely before the outer one advances.
△ `right` vs `forward` becomes a Common Mistake slide with a top-down arrow
diagram of the agent's facing.

Reference deck for tone: `../2026-09-02/seohoo-pixels-with-a-loop.html`.

---

## 21:00 KST · 19:00 HCMC — SERENA [PYTHON] · Python (pygame)

**Last lesson (2026-08-27 log):**
- Character position in variables (`cat_x`, `cat_y`)
- Arrow-key handling, four-direction movement
- `if` vs `elif` — simultaneous vs single conditions
- Tidying with variables (`cat_speed`, `WIDTH`, `HEIGHT`, `cat_width`, `cat_height`)
- Gravity and velocity (`cat_vel_y`, `cat_gravity`)
- Y axis: smaller y = higher up
- Wall collision (`if cat_x < 0`, `if cat_x + cat_width > WIDTH`)

✓ Instantly got if-vs-elif: separate ifs allow diagonal movement
✓ Explained gravity unprompted — velocity gains 1 every frame
△ Not solid that (x, y) is the **top-left corner** — confused why collisions need
  `cat_x + cat_width` and `cat_y` minus height

**Unmet last week:** nothing missed.
**Said next:** nothing recorded.

**Today's new idea:** **jumping, and landing.** Gravity already pulls the cat
down forever. Today: SPACE sets `cat_vel_y` to a *negative* number (an upward
kick) and a floor check stops the fall. Then: only allow a jump when standing on
the ground (`on_ground` flag), so the cat cannot fly.
Ramp: v1 gravity as Serena has it → v2 SPACE sets `cat_vel_y = -15` → v3 floor
check `if cat_y + cat_height > HEIGHT` clamps and zeroes velocity → v4 `on_ground`
flag blocks mid-air jumps → v5 a platform to land on.
Visual required: a frame-by-frame strip of the jump arc with `cat_vel_y` printed
each frame (-15, -14, -13 … 0 … +3, +4) beside the cat's height, so the sign flip
at the top is visible.
△ top-left-corner confusion is the **warm-up**: one visual of the cat's box with
the (x, y) dot on the top-left corner and `cat_y + cat_height` marked as the feet.
That warm-up feeds straight into the floor check.

Reference deck for tone: `../2026-09-02/neo-bullets-that-hurt.html`.

---

## 21:50 KST · 19:50 HCMC — IAN WEB DEV · Web development

**Kasim did not name a topic for IAN. This is the Idea line.**

**Last lesson (2026-08-27, log + draft agree):**
- Nav bar with `<nav>` and `<a>`
- CSS `display: flex`, `gap`, `padding`
- `nav a` and `nav a:hover` selectors
- `background-color` on the nav
- `align-items: center`, `justify-content: space-between`
- `flex-wrap` for responsive behaviour
- **Copied the nav code by hand across 9 HTML pages**; debugged missing and
  duplicate home links

✓ Chose own nav background and hover colours; types CSS fast
△ Waits for the teacher to type first
△ Forgets semicolons
△ Missed a duplicate link while copy-pasting

**Unmet last week:** nothing missed.
**Said next:** nothing recorded.

**Today's new idea:** **one external `style.css`, linked from all 9 pages.** Ian
just felt the exact pain this solves — nine copies of the same CSS, and a
copy-paste bug that had to be hunted down. Today: cut the CSS out of the `<style>` block,
paste it into `style.css`, add one `<link>` line per page, then change the nav
colour **once** and watch all nine pages change.
Ramp: v1 the page as it is → v2 create `style.css` and move the nav rules → v3
add `<link rel="stylesheet" href="style.css">` to page 1 and prove it still works
→ v4 add the same line to the other 8 → v5 one edit, nine pages change.
Then push further: a shared `.button` class reused on every page, and CSS
variables (`--brand: #...`) so a colour lives in exactly one place.
Visual required: a fan diagram — one `style.css` file with nine arrows pointing
out to nine pages — shown before any code.
△ forgotten semicolon becomes a Debug slide with the real symptom (the rule after
it silently dies, not an error message).

Reference deck for tone: `../2026-08-31/yunho-pixel-art-bigger.html` for
structure; check `../../webdev/` for a web-track deck if one fits better.
