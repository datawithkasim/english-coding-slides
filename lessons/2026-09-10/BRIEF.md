# Today's decks — 2026-09-10 (Thu)

Eight events on the calendar. **RYAN's 09:00 KST lesson already happened this
morning** (transcript in Drive, ledger row written, homework shipped) — no deck,
no message. **ERIC KIM 15:00 KST is cancelled this week** (Kasim, this morning) —
no deck, no message. **JIYU 23:00 KST is Tuesday's lesson moved to tonight.**

Six decks needed, 16:20 → 23:00 Korea time.

**Topics come from last week's transcripts** — Kasim's instruction this morning.
In practice that means each student's `ledger/<folder>.json` newest row: its
`actual` is the Drive transcript distilled by `/homework`, and its `gap` is what
was promised to the parent and not delivered. The gap wins where there is one.

**IAN is the one exception.** No transcript exists for him at all — Drive's Meet
Recordings folder holds nothing before 2026-08-26, and there is no doc at his
21:50 KST slot on either 08-27 or 09-03. His 09-03 lesson did not happen. His
section is built from his **live IDE project** instead, read this morning.

| Time | Student | Topic | Deck |
|---|---|---|---|
| 16:20 KST · 14:20 HCMC | JJ (snlovelyb) | MC **Blocks** — `move up` inside the loop: the spiral staircase | `jj-the-spiral-staircase.html` |
| 19:00 KST · 17:00 HCMC | DANIEL | Python — `while` loop shop: buy until the money runs out | `daniel-the-shop-that-keeps-going.html` |
| 20:00 KST · 18:00 HCMC | SEOHYEON | MC **Blocks** — a loop inside a loop (nested repeat) | `seohyeon-loop-inside-a-loop.html` |
| 21:00 KST · 19:00 HCMC | SERENA | Python — three ledges from one list, drawn in a loop | `serena-three-ledges-one-list.html` |
| 21:50 KST · 19:50 HCMC | IAN | Web — CSS variables, one `.button` rule, grouped selectors | `ian-name-the-colour-once.html` |
| 23:00 KST · 21:00 HCMC | JIYU | MC **Python** — a `for` loop that repeats one `fill` along a row | `jiyu-one-fill-many-times.html` |

## Hard rules for every deck

Read first, in this order:
1. `../../TEMPLATE.md` — the slot structure and per-slide rules
2. `../../PEDAGOGY.md` — why each slot exists
3. `../../assets/style.css` — the only styling allowed
4. The reference deck named in that student's section below, for tone

Then:
- Save to `lessons/2026-09-10/<file>.html`. Stylesheet `../../assets/style.css`,
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
- Decks are light cream now (palette flipped 2026-09-09). Code boxes and viz
  chips stay dark. Do not reintroduce a dark deck background.

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

### The carry
Most of these students have a large unreached tail from last week. **Carry those
slides across verbatim** — they were already reviewed and are already in that
student's voice. Never carry Slot 1 (title) or Slot 2 (Recap); both are rebuilt
from this week's facts. Renumber everything after carrying: the `counter` span,
every `STEP n / total`, the `footer-tag` date, the Recap pill date, and the
`<!-- N · SLOT -->` comments.

### API form — Minecraft **Python** (JIYU only today)
Constant form, never strings:

```python
blocks.fill(PINK_CONCRETE, pos(5, 0, 0), pos(7, 7, 0))
agent.move(FORWARD, 5)
```

Coordinates: **y starts at 0; x and z start at 1.**

### Block track — JJ and SEOHYEON only
**Zero Python anywhere in their decks** — not in a code block, not in a debug
card, not in a comment. Draw the blocks with the `.mcb` / `.mcb-c` components at
the end of `assets/style.css`. Reference decks:
`../2026-09-02/seohoo-pixels-with-a-loop.html` and `../2026-09-02/ihyeon-maze-first-turn.html`.

Category classes and their (pixel-sampled) colours:
`basic` `player` `blocks` `mobs` `agent` `gameplay` `pos` `loops` `logic` `vars` `math`.
Every new block gets a `.mcb-from` line naming its toolbox drawer.

Block anatomy: colour follows the **drawer the block came from**, never the block
it sits inside. Nested input = its own drawer colour × 0.85. Number field = white
pill oval. `~` is white label text printed inside the position pill, outside the
white number ovals.

---

## 16:20 KST · 14:20 HCMC — JJ (snlovelyb) · Minecraft **Blocks**

**Last lesson (2026-09-03, from the ledger — i.e. from the transcript):**
- `repeat 4 times`
- `set long to 6`, then `set long to 5`
- `change long by 1` **inside** the repeat → a spiral that grows
- `set long to 10` + `change long by 2` → a bigger spiral
- `change long by -1` → a spiral that shrinks
- typing the minus sign on a tablet keyboard

**Unmet last week (the gap, and the strongest input today):**
> 계단(move up)은 못 했어요. 나선을 키우는 것과 줄이는 것을 둘 다 하고, 더하기 빼기를
> 소리 내어 함께 계산하는 데 (00:41:06, 00:43:15) 시간을 썼어요.

The staircase was promised to the parent and did not happen. Both spirals did.

**Homework concept just practised:** `variable-grows-each-step`.

**Where last week's deck stopped**
- Last deck: `../2026-09-03/jj-the-growing-staircase.html` (91 slides, 38 steps)
- Stop point: found from the ledger `actual`. He reached the shrinking-spiral
  steps, roughly **STEP 14 of 38, slide ~60 of 91**.
- **Important:** he did *not* go through the deck in order. The `move up` /
  climb slides (**STEP 12, "Climb once every pass"**, "Longer and higher, every
  pass", "v4 — a spiral staircase", around slides 44–48) were **skipped, not
  reached**. They are the single most valuable carry in the deck.
- Carry: the STEP 12 climb block **verbatim**, plus every slide after the
  shrinking-spiral steps. Do not carry slides 1–43 — those were taught.

**Today's new idea:** `move up` inside the same repeat, so `long` grows **and**
the agent climbs — the spiral becomes a staircase. Ramp: v1 the growing spiral
JJ already has → v2 add `agent move up by 1` inside the loop → v3 tune the climb
so the steps look right → v4 a shrinking staircase using `change long by -1`
with the climb still in.

Visual required: one frame per pass showing **both** numbers — the value of
`long` and the height so far. Pass 1 = long 5, height 1. Pass 2 = long 6,
height 2. Pass 3 = long 7, height 3. Pass 4 = long 8, height 4.

△ from last week: he needed help putting `set long to 5` in the right place, and
could not drop a variable oval into a number slot alone. Both become dedicated
`.mcb-drop` slides — show the empty white oval and the red VARIABLES oval going
into it.

Reference deck for tone: `../2026-09-02/ihyeon-maze-first-turn.html`.

---

## 19:00 KST · 17:00 HCMC — DANIEL PYTHON ADVENTURES · Python

**Last lesson (2026-09-03, from the ledger — i.e. from the transcript):**
- explained his own code out loud
- `input()` for name, age, food, then f-string output
- `int(input())` for an amount
- a price variable and `money` subtraction (35, 7.50)
- line 13: letters printing instead of the calculation
- line 15: the subtraction not being saved — **he found this himself off one hint**
- the short forms `-=` and `+=`
- adding the 36.30 his mother gave him to `money`

**Unmet last week (the gap, and the strongest input today):**
> while 반복으로 여러 개 사는 상점은 못 했어요. 13번 줄과 15번 줄 오류를 직접 찾아
> 고치는 데 (00:26:51, 00:29:32) 시간을 썼고, 마지막에 어머니 돈을 더하기가 아니라
> 빼기로 쓴 것을 바로잡느라 (00:37:09) 남은 시간을 썼어요.

**Homework concept just practised:** `second-box-adds-up-while-first-goes-down`.

**Where last week's deck stopped**
- Last deck: `../2026-09-03/daniel-money-that-changes.html` (90 slides, 31 steps)
- Stop point: from the ledger `actual` — he reached `-=` / `+=` and the typed
  price, i.e. roughly **STEP 8 of 31, slide ~39 of 90**.
- Carry: everything from **"Keep shopping until the box is empty"** (the slide
  just before STEP 9) to the end. That is the entire `while` block, ~50 slides,
  including "Pass 1 / Pass 2 / Pass 3" tables, "It never stops 😱", "Left outside
  the loop", and the DANIEL TYPES THIS ONE ALONE cards. Carry it verbatim.
- Do not carry slides 1–38.

**Today's new idea:** the `while` shop — keep buying until the money runs out.
Ramp: v1 the single purchase he has → v2 wrap it in `while money > 0` → v3 pull
the three lines inside the loop → v4 stop cleanly when the money is gone, and
print the final balance.

Visual required: the money box redrawn once per pass, old value crossed out, new
value beside it, and the loop condition shown as `True` / `False` on each pass so
the last pass visibly ends the loop.

△ from last week: the line-15 slip (subtraction not saved) is worth one Common
Mistake slide — `money - price` vs `money = money - price` — because inside a
loop it now fails silently forever instead of once.

Reference deck for tone: `../2026-08-31/ethan-for-loops-range.html`.

---

## 20:00 KST · 18:00 HCMC — SEOHYEON MS · Minecraft **Blocks**

**Last lesson (2026-09-03, from the ledger — i.e. from the transcript):**
- `RL` chat command to call the agent to her own position
- typing the command name in chat to run it
- standing out of the way of the build
- `agent move forward by 8` + `agent move up by 1` → a row of flowers
- five kinds of flower, starting with tulips
- a pond with `fill` and coordinates
- a stone wall so the water does not spill, plus a waterfall
- planting saplings and growing them with bone meal
- a `forever` loop that keeps placing saplings

**Unmet last week (the gap, and the strongest input today):**
> 반복 안의 반복(중첩 repeat)은 못 했어요. 꽃밭(00:12:47), 연못과 돌담(00:21:04),
> 묘목(00:26:24)을 손으로 짓는 데 수업 시간을 다 썼어요.

She spent the whole hour hand-building. The nested loop never started. **This is
the second week running that nested repeat has been promised and missed** — it
was also the topic of last week's deck.

**Homework concept just practised:** `later-fill-replaces-earlier-where-they-overlap`.

**Where last week's deck stopped**
- Last deck: `../2026-09-03/seohyeon-loop-inside-a-loop.html` (87 slides)
- Stop point: from the ledger `actual` — she barely entered the deck. Nothing
  after the opening recap and vocabulary slides was reached.
- Carry: **almost the whole deck**, roughly slides 13 → 87, verbatim. That
  includes the whole nested-repeat ramp, `side` shrinking each floor, the stepped
  pyramid, Bug 5 and Bug 6, the questions, the hollow-vs-solid tower, the snake
  fill, the cube as three counters, and the alternating block floors.
- Rebuild only: Slot 1 title, Slot 2 recap (from this week's facts above), and
  the vocabulary slides if they name things she has now already met.

**Today's new idea:** the same one, reached this time — **a repeat inside a
repeat**. Because so much carries, spend the extra room on getting her *into* the
first nested loop faster: fewer hand-build slides, straight to one row loop
inside one floor loop.

Ramp: v1 one `repeat` drawing a single row → v2 wrap it in a second `repeat` to
stack rows into a floor → v3 add `change side by -2` so each floor shrinks →
v4 the stepped pyramid.

Visual required: two counters on screen at once, outer and inner, with the inner
one resetting every time the outer one ticks. One frame per inner pass.

△ from last week: she waited to be asked rather than saying she had finished.
That is behaviour, not a skill — **do not put it in the deck.** The skill △ is
mixing up `right` and `forward`, which does belong on a Common Mistake slide.

Reference deck for tone: `../2026-09-02/seohoo-pixels-with-a-loop.html`.

---

## 21:00 KST · 19:00 HCMC — SERENA [PYTHON] · Python (pygame)

**Last lesson (2026-09-03, from the ledger — i.e. from the transcript):**
- the screen coordinate system with 0 at the top
- the cat's feet = `cat_y + cat_height`
- adding gravity to `cat_vel_y` every frame
- negative velocity goes up, positive goes down
- following one jump frame by frame in a table
- `print` to check the spacebar was being read at all
- spacebar sets `cat_vel_y = -15`
- a landing check so the feet never pass 480
- `on_ground` to stop her jumping again in mid-air

**Unmet last week:** nothing missed. `gap` is `null`.
**Said next:** jump and landing, then platforms if there was time.

**Homework concept just practised:** `one-platform-is-four-numbers-used-twice`.
She has already done a single platform on paper and in code for homework.

**Where last week's deck stopped**
- Last deck: `../2026-09-03/serena-make-the-cat-jump.html` (101 slides)
- Stop point: from the ledger `actual` — she finished the jump, the landing and
  `on_ground`, i.e. about **slide 66 of 101** ("One line, before the bonuses").
- Carry: slides ~67 → 96, the whole bonus run, verbatim. In deck order they are:
  jump height as a named variable, tuning it, a jump counter refilled by landing,
  **three ledges as a list** (the "Three ledges, one list" → "Only land while
  falling" → "Close the window" run), coyote time, terminal velocity, and the
  three bug cards.
- Today's topic **is** part of that carry, so reorder rather than rewrite: bring
  the three-ledges run to the front of the new material and leave the rest after it.

**Today's new idea:** **three ledges from one list, drawn in a loop.** She can do
one platform. Today one list holds several, a `for` loop draws them all, and the
same landing check runs against each one in turn.

Ramp: v1 the one hard-coded ledge from her homework → v2 the same four numbers
moved into a list → v3 a `for` loop that draws every ledge in the list → v4 the
landing check inside that loop, so she can land on any of them → v5 land only
while falling, so she can jump up through a ledge from underneath.

Visual required: the list drawn as four boxes, and the loop pointer moving along
it one ledge per frame, with the ledge appearing on the game screen as the
pointer reaches it.

△ from last week: she was not solid that `(x, y)` is the **top-left corner**, and
was confused about why collisions need `cat_x + cat_width`. That is exactly what
"four numbers used twice" leans on, so open with one visual slide on it —
a rectangle with all four of its edges labelled from just `x`, `y`, `w`, `h`.

Reference deck for tone: `../2026-09-03/serena-make-the-cat-jump.html` (her own).

---

## 21:50 KST · 19:50 HCMC — IAN WEB DEV · Web (HTML / CSS)

**⚠ There is no transcript for IAN, and there never has been.** Drive's Meet
Recordings folder holds no document earlier than 2026-08-26, and there is no doc
at his 21:50 KST slot on 08-27 or on 09-03. There is also no file activity in his
project on 09-03. **His 09-03 lesson did not happen.** He has no ledger file.

**What is true, read from his live IDE project this morning** (`iancheon`,
workspace `61f3b5e6-170b-46e2-8aea-c372b996a7d9`):

Working and finished:
- ten pages, all linking one shared `styles.css` — `index`, `about_me`,
  `aspiration`, `contacts`, `current_focus`, `hobbies`, `projects`,
  `qualifications`, `skills`, `values`
- a `nav` flex bar on every page: `display:flex`, `gap:14px`,
  `background-color:#cec7c4`, `padding:20px`, `align-items:center`,
  `justify-content:space-between`, `flex-wrap:wrap`
- `nav a` white, `nav a:hover` blue `rgb(17, 40, 141)`
- `index.html` is a 3×3 picture grid — `.vertical-grid` and three
  `.horizontal-grid` rows, `grid-template-columns: 1fr 1fr 1fr`, `gap: 10px`
- `.horizontal-grid img` with `aspect-ratio: 1/1.2`, `object-fit: contain`,
  and a `transition: transform 300ms ease` with `a:hover img { scale(1.1) }`

He worked **alone** on Wed 2026-09-09, 16:42–17:39 KST — about 57 minutes. He
edited all nine content pages plus `index.html`, and added
`img/current_focus.jpg`, fixing the old filename that had a space in it.
`styles.css` has not been touched since 27 August.

Three real problems in the live files, all verified this morning:
1. **Every page loads `<script src="scripts.js"></script>` and that file does not
   exist.** Ten silent 404s.
2. `current_focus.html` has `<li>` items with no `<ul>` around them, and an
   `<h2>` used as a sentence.
3. The nine content pages have **no styling at all below the nav** — no body
   font, no width limit, no colour. Only the nav and the home grid are styled.

**Where last week's deck stopped**
- Last deck: `../2026-09-03/ian-one-file-styles-them-all.html` (67 slides). It
  was built and **never used** — that lesson did not happen.
- Its opening premise is now stale: it teaches "make one shared style.css and
  link it from all nine pages", and he already has exactly that.
- Carry: slides ~35 → 61 verbatim — "Words for the next part", the `.button`
  rule, "Wear it anywhere", CSS variables ("Give the colour a name" → "Type one
  word. Watch." → the font name), `class` vs `id`, "A comma means and also",
  grouped selectors, "The last rule wins", "Your whole style.css", "Page 10 costs
  one line".
- Drop slides 1–34: they teach the shared stylesheet he already has, plus a
  find-the-broken-link drill that no longer applies.

**Today's new idea:** **name a value once and use it everywhere** — CSS custom
properties for the colour and the font, one `.button` class reused across pages,
and grouped selectors with a comma. The point he should leave with: change one
line at the top, and all ten pages change.

Ramp: v1 the `styles.css` he has → v2 `:root { --ink: #11288d; }` and use
`var(--ink)` in `nav a:hover` → v3 add `--paper` and `--font` and apply them to
`body` → v4 one `.button` rule, put on the "Back to home" link that already
exists on his pages → v5 group `h1, h2` with a comma so both get the same font.

Visual required: the top-of-file variable block with arrows fanning out to every
rule that uses it, and a before/after of the whole site when one hex value
changes.

Warm-up, both from his own live files, both one slide each:
- the missing `scripts.js` — show the console 404, then delete the one line (or
  create an empty file). Name the file, quote the exact line.
- the `<li>` with no `<ul>` in `current_focus.html` — show his real lines and the
  fix.

Do not invent a bug. These two are real and are in his files right now.

Reference deck for tone: `../2026-09-03/ian-one-file-styles-them-all.html` (his own).

---

## 23:00 KST · 21:00 HCMC — JIYU [TASHKENT_LAMU] · Minecraft **Python**

**⚠ This is Tuesday's lesson moved to tonight.** The tracker carries JIYU on two
slots — Tue 23:00 and Fri 21:00 — and today's calendar event is the Tuesday one
rescheduled from 2026-09-08. She has **no ledger file**.

**Last transcript:** 2026-09-04, her Friday slot, 6 days ago. No deck was built
for that lesson, so there is nothing to carry.

**Last lesson log (2026-08-25):**
- `blocks.fill()` with coordinate ranges — start pos, end pos, block type
- the X / Y / Z system, with Z fixed at 0 for flat pixel art
- counting coordinates right to left
- creeper pixel art: legs, body and head as one rectangle, eyes
- Python form: `blocks.fill(PINK_CONCRETE, pos(5, 0, 0), pos(7, 7, 0))`, run with `r`

✓ first leg (5–7, 0–7) straight after the coordinate explanation
✓ counted backwards from 15 to get 10–12 for the second leg herself, keeping Y the same
✓ body and head as one rectangle in one attempt, both eye coordinates right
△ confused overwriting the numbers in an old line with adding a **new** `fill` line
△ block-name spelling stopped the run several times
△ comma slips — typed `770` and `1012` instead of `7,1,0` and `10,12,0`

**Said next (from the log):** check the pixel-art homework, then bigger art with
loops or a new scene.

**Where last week's deck stopped:** no deck exists. Build fresh, no carry.

**Today's new idea:** **a `for` loop that repeats one `fill`.** She writes one
`fill` line per shape today; one loop can draw a row of them. Ramp: v1 the one
`fill` she knows → v2 the same `fill` written out three times with the x moving
by 4 each time → v3 a `for i in range(3)` that does it → v4 the loop variable
doing the arithmetic, `pos(1 + i * 4, ...)`.

Visual required: one frame per pass with `i` printed and the block appearing at
its computed x — pass 0 draws at x 1, pass 1 at x 5, pass 2 at x 9.

△ the comma slips become a dedicated Common Mistake slide: `pos(770)` next to
`pos(7, 1, 0)`, with the error message the game actually shows.
△ "overwrite the old line vs add a new line" becomes one slide with two panels,
because a loop makes it matter far more.

**Parent message for JIYU is English only** — no Korean, no translation column.

Reference deck for tone: `../2026-09-02/seohoo-pixels-with-a-loop.html`
(structure only — that one is the block track, JIYU is Python).
