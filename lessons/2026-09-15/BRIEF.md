# Today's decks — 2026-09-15 (Tue)

Times are Korea first, Ho Chi Minh second (KST − 2).

**Calendar is the source of truth for times.** Tracker drift is noted per student.
**DAVID G8 and JIYU are in the tracker on Tuesday but have no Tuesday calendar event —
not taught today, no deck, no message.**

**Kasim's instruction this morning, verbatim:** *"yeah whatever the idea is."*

He named no topics, so every student takes the Idea line put to him in the walkthrough.
One of those is a **track change** (RIO → pure Python) and it is flagged below.

| Time | Student | Track | Today's topic | File |
|---|---|---|---|---|
| 16:00 KST · 14:00 HCMC | RIO | **IDE Python — track change, was Minecraft Python** | first pure-Python lesson: a variable, then `for` + `range()` printing a growing tower | `rio-your-first-python-file.html` |
| 18:00 KST · 16:00 HCMC | HWON | IDE Python (pygame) | `colliderect` — Dario touches the bread, the bread disappears, the score goes up | `hwon-eat-the-bread.html` |
| 19:00 KST · 17:00 HCMC | JASON | IDE Python (pygame) | finish the landing check, then platforms into a **list** and one loop checks them all | `jason-a-list-of-platforms.html` |
| 20:00 KST · 18:00 HCMC | LEO | Minecraft Python | a **loop inside a loop** — one counter per row, one per column, a 5 × 5 floor | `leo-a-loop-inside-a-loop.html` |
| 21:00 KST · 19:00 HCMC | YURA | Minecraft **blocks** | the **spiral** — `side` grows inside the repeat, so the walls never close | `yura-the-square-unrolls.html` |

**Not a lesson:** `MUAY THAI`, 11:00 KST · 09:00 HCMC. Left alone.

---

## Report-only drift — nothing was auto-fixed, no calendar event was renamed

- **No calendar renames were needed today** — every lesson title already matches a tracker
  `name` exactly (`YURA G5 ` matches on whitespace-insensitive compare).
- **JASON** — calendar says Tuesday **19:00**, `tools_students.slot_time` says **17:00**. The
  calendar is right; the 2026-09-08 Drive transcript is the `16:59 GMT+7` doc, which is
  19:00 KST. Tracker not edited. Folder name `jason-tue-1700` left alone (join key).
- **YURA** — calendar says Tuesday **21:00** today, `tools_students.slot_time` says **22:00**,
  and `roster.json` says `yura-tue-2200`. Her recurring slot is actually **Saturday 18:00
  KST**; today's event is that Saturday instance moved. The 2026-09-12 lesson was postponed
  to today. Tracker and roster not edited.
- **DAVID G8** — `tools_students` has Tuesday 21:00. There is **no Tuesday calendar event**,
  and the last two decks built for him are `2026-09-06` and `2026-09-13`, both **Sundays**.
  The Tuesday slot looks dead. Tracker not edited — fix by hand.
- **JIYU** — `tools_students` has Tuesday 23:00. There is **no Tuesday calendar event today**.
  Taught Tue 2026-09-01, skipped Tue 2026-09-08, last lesson 2026-09-10 (`21:00 GMT+7` doc =
  23:00 KST). Tuesday slot is unconfirmed. Tracker not edited.
- **HWON has no ledger file.** `/homework` has never run for him, so his last-lesson facts in
  this brief come **straight from the Drive transcript**, not from a ledger row. There is no
  homework concept on record for 2026-09-08 and no worksheet was shipped.
- **RIO's parent may not know about the Python switch.** The 2026-09-08 ledger note says the
  announcement was deliberately kept out of the parent text for Kasim to send himself. Today's
  parent message names pure Python, so check that before pasting.

## Transcripts — what was read for this brief

| Student | Doc (GMT+7 title) | Real date | Days ago |
|---|---|---|---|
| RIO | `2026/09/08 14:00` | Tue 8 Sept | 7 |
| HWON | `2026/09/08 16:00` | Tue 8 Sept | 7 |
| JASON | `2026/09/08 16:59` | Tue 8 Sept | 7 |
| LEO | `2026/09/08 18:00` | Tue 8 Sept | 7 |
| YURA | `2026/09/05 16:00` | Sat 5 Sept | **10** |

**LEO's Sunday 2026-09-13 lesson did not run.** A 99-slide deck was built for it
(`2026-09-13/leo-one-loop-fills-the-floor.html`) but there is **no Drive transcript for
13 Sept 16:00 GMT+7** and **no worksheet or feedback** in `leo-kim-sun-1800` newer than
2026-09-06. That whole deck is unspent and carries into today.

**YURA's 2026-09-12 lesson did not run either** — the calendar event was moved to today
before the slot. Her 98-slide deck from that day is completely unspent.

---

## Hard rules for every deck

Read first, in this order:
1. `../../TEMPLATE.md` — slot structures and per-slide rules
2. `../../PEDAGOGY.md` — why each slot exists
3. `../../assets/style.css` — the only styling allowed
4. The reference deck named in that student's section — tone and markup

Then:
- Save to `lessons/2026-09-15/<file>.html`. Stylesheet `../../assets/style.css`, script
  `../../assets/deck.js`. Slides are `<div class="slide">`, the first is
  `<div class="slide active center-all">`.
- **Copy-this-and-it-works.** The student makes zero decisions. If a slide needs the
  student to infer anything, it is wrong.
- **One change per slide**, numbered `STEP n / total`. A re-indent is its own step.
- Every code step carries all four: **the code** (full OLD block and full NEW block, never
  `...` inside a changed region) · **🔍 FIND** the exact Ctrl+F string · **📍 where** — quote
  the existing line it goes under, and the indent count · **🟣 why**, one line · **✅ check**,
  one line (what running it should show).
- **Big programs ramp v1 → v2 → v3 → v4.** Never the finished program first. New lines hot,
  unchanged lines dim, changed lines get an explicit OLD/NEW block.
- **Visuals beat words, and are mandatory for loops, iteration and any maths** — one frame per
  pass with the counter value shown; spacing as boxes on a number line; x positions as jumps.
  Reuse the `style.css` animation components (`.var-fill` / `.viz-reassign` / `.viz-if` /
  `.viz-3`), never new inline styling.
- **Overshoot, hard.** The deck must hold **WAAAY more than one lesson can get through**. **No
  slide-count target and no ceiling.** If the teacher could plausibly reach the last slide
  inside the hour, go back and add taught ideas. Extra room goes to **new concepts with a
  visual each**, never more debug cards.
- **As few words as possible.** ≤ 40 English and ≤ 15 Korean words per slide.
- **Every deck teaches at least one new idea** — the one named in the table above. A homework
  check or a revisited mistake is a warm-up that leads into it, never the whole lesson.
- **The lesson-to-lesson jump can be bigger than the homework's.** Kasim is in the room to
  bridge it. That is not licence to skip a step.
- **Carry rules:** carried slides come across **verbatim**. Never carry slot 1 (title) or
  slot 2 (recap) — both are rebuilt from this brief. Renumber after carrying: the `counter`
  span, every `STEP n / total`, the `footer-tag` date, the recap pill date, and the
  `<!-- N · SLOT -->` comments.
- **Minecraft decks use constant form** — `agent.move(FORWARD, 5)`, never a string.
- **Minecraft coordinate origins:** `y` starts at 0; `x` and `z` start at 1. Never say
  "coordinates start at 0" for all three.
- **Never gendered pronouns.** Use the name, or they.

---

## 16:00 KST · 14:00 HCMC — RIO

**Topic today: his first pure-Python lesson.** A variable, then `for i in range(n)` printing a
tower that grows. Same loop idea he already owns from Minecraft, now in a `.py` file he runs
himself.

- **Track change.** He has been on Minecraft Python. Kasim announced on 2026-09-08 (at
  `00:14:35` of the transcript) that he moves to pure Python this week. Today is that week.
- **He has an IDE account** (`app_user_id 130d706b-6438-432c-9b10-fecf21fd81be`), so the
  student app is the vehicle. He also demoed a self-made solar-system game on GitHub, and
  Kasim showed him a terminal workflow, so he is not starting from nothing.
- **Last lesson (ledger 2026-09-08) — what he actually did:**
  - presented his own solar-system game (NPCs, missions, GitHub hosting)
  - saw a terminal-based workflow
  - revised coordinates: `y` starts at 0, `x` and `z` start at 1
  - `for i in range(6)` — the pass count
  - put variables `x`, `y` inside `pos()`
  - `y = y + 1` inside the loop to stack floors
  - `x = x + 1` inside the loop to spread sideways
  - syntax errors: the colon on the `range` line, tab indentation, initialising `x = 0` /
    `y = 0`
- **Unmet last week:** nothing missed — `gap` is null.
- **Homework concept just practised:** `two-variables-grow-inside-one-loop`
  (`worksheets/homework-staircase-two-variables-2026-09-08.md`).
- **Last deck:** `STUDENTS/students/rio-tue-1600/slides/2026-09-08-loops-do-the-counting.html`
  (= `SLIDES/lessons/2026-09-08/rio-loops-do-the-counting.html`), 64 slides.
- **Stop point: reached ~slide 36 of 41 taught steps.** Found from the **ledger `actual`** — its
  last bullets are both `x` and `y` growing inside one loop, which is deck step "Two boxes,
  two speeds".
- **Slides to carry: NONE.** Kasim's topic is a track change, and every unreached slide is
  Minecraft `blocks.fill`. **The carry is dropped on purpose** — build fresh. Say nothing about
  Minecraft in the deck except one bridge slide: the loop he already knows, now in Python text.

**Deck shape:**
1. Recap: his staircase loop, in Minecraft, from last week.
2. Bridge: same loop, no Minecraft — a file, a run button, text output.
3. `print()` first. One line, run it, see it.
4. A variable holds a number. Print the variable.
5. `for i in range(5)` — the counter, one frame per pass, `i` shown each time.
6. Print `i` — five lines of output.
7. `"#" * i` — a row that grows. This is the tower.
8. Then overshoot: `input()` to name the tower, `range(a, b)`, `range` with a step, a second
   variable growing at a different speed (his two-variable homework, now in text), nested loop
   printing a square of `#`, and a triangle that counts down.

**Reference deck for tone:** `SLIDES/python/rs001-text-adventure/` (first-Python voice), plus
`SLIDES/lessons/2026-09-14/amy-the-fight-that-repeats.html` for the IDE-Python markup.

---

## 18:00 KST · 16:00 HCMC — HWON

**Topic today: `colliderect`.** Dario touches the bread, the bread disappears, the score goes
up. This is the unmet promise from last week.

- **Language: English only.** No Korean glosses in this deck.
- **No ledger row.** These facts come from the Drive transcript of 2026-09-08
  (`16:00 GMT+7` doc), read directly.
- **Last lesson (transcript 2026-09-08) — what he actually did:**
  - found the bug: the character could not move down, because there was no bottom barrier
  - `y = 0` is the TOP; bigger `y` moves down, smaller `y` moves up
  - why the floor is `760` and not `800` — the player is 40 tall
  - wrote the bottom-barrier `if` on lines 73–74, using the height logic, not copy-paste
  - replaced the hardcoded `40` on line 74 with the existing `Super_Dario_H` from line 30
  - typed the `Dario_rect` line on line 77 — the collision rectangle, **started only**
- **Unmet last week:** eating the bread never happened. Only the `Dario_rect` line was typed.
  Bread respawn never started.
- **Said next:** collision, then bread respawn.
- **Watch out:** that lesson was rough. He was distracted the whole hour, the transcript ends at
  33 minutes, and he had lost his old project code off his own computer. Build the warm-up so
  it works even if his file is not exactly where it was left — the first code slide must show
  the full current state of the relevant lines, not just a diff.
- **No homework was shipped for 2026-09-08**, so he has practised nothing since. The deck must
  re-establish the `Dario_rect` line itself before using it.
- **Last deck:** `STUDENTS/students/hwon-tue-1800/slides/2026-09-08-walls-then-the-bread.html`
  (= `SLIDES/lessons/2026-09-08/hwon-walls-then-the-bread.html`), 77 slides, 25 taught steps.
- **Stop point: reached ~step 6 of 25.** Found from the **Drive transcript** (no ledger). The
  last deck idea named out loud is the down wall doing nothing, plus the `Dario_rect` line.
- **Slides to carry:** everything from taught step **8 ("yum before you move")** to the end —
  the collision check, the bread that will not sit still (respawn), the score, `(10, 10)` is the
  top, the score vanishing, one pass one bread, the invisible bread, the every-frame timer.
  Carry them **verbatim**. Steps 1–7 (down wall, `y = 0` is the TOP, right wall) are spent —
  drop them, except a one-slide recap.
- **New on top of the carry:** the bread **list** — three breads, one loop checks them all, and
  a `for` loop drawing them. Then a bread that is worth more points than the others.

**Reference deck for tone:** the last deck above, and
`SLIDES/python/rs003-pygame-shooter/` for collision markup.

---

## 19:00 KST · 17:00 HCMC — JASON

**Topic today: finish the landing check, then a list of platforms and one loop that checks them
all.** This is the unmet promise from last week, word for word.

- **Last lesson (ledger 2026-09-08) — what he actually did:**
  - why the jump value is negative (the top of the screen is 0)
  - `ground_y + player height` to place the floor platform
  - fixed indentation so the arrow keys sit outside the event loop
  - added `platform_1` / `platform_2` (`x`, `y`, `w`, `h`)
  - found why the platforms were not drawn — a `ground_platform` reference
  - screen edges: `x < 0`, `x > WIDTH - player w`
  - used the `width` variable instead of `640`
  - started the landing check on line 98, **left commented out at the end of the lesson**
- **Unmet last week:** *"발판 리스트 + 반복문 검사는 못 나갔어요"* — the platform list and the
  loop check never happened. The landing check was started and pushed to homework.
- **Homework concept just practised:** `landing-on-a-platform-colliderect`
  (`worksheets/homework-platformer-landing-2026-09-08.md`). **The deck starts from what he can
  now do** — assume the landing check exists in some form and check it, do not re-teach
  `colliderect` from zero.
- **Last deck:** `STUDENTS/students/jason-tue-1700/slides/2026-09-08-land-on-the-platform.html`
  (= `SLIDES/lessons/2026-09-08/jason-land-on-the-platform.html`), 54 slides, 48 taught steps.
- **Stop point: reached ~step 18 of 48.** Found from the **ledger `actual`** — its last bullet
  is the landing check started on line 98 and commented out, which is deck step "Landing asks
  four questions at once".
- **Slides to carry:** everything from taught step **19 ("Has he reached the left edge?")** to
  the end — the four landing questions one at a time, `==` vs `=`, only-while-falling, say the
  landing rule, one platform → a list of them, make it a list and loop the check, three
  platforms and a gap, one pass per platform, the check falling out of the loop, tap-vs-hold
  jump, coyote time, the patrolling platform, falling off and restarting. Carry them
  **verbatim**. Steps 1–18 are spent.
- **New on top of the carry:** after the list works, a platform that **disappears** when he
  lands on it, and a counter of how many platforms he has touched.

**Reference deck for tone:** the last deck above, and `SLIDES/python/rs004-platformer/`.

---

## 20:00 KST · 18:00 HCMC — LEO

**Topic today: a loop inside a loop.** One counter walks the row, one walks the column, and a
5 × 5 floor comes out of one `blocks.fill` line.

- **Same student as `leo-kim-sun-1800`.** Check both folders before writing. His Sunday slot
  runs the same arc — a repeat across the two folders is the failure mode here.
- **Last lesson (ledger 2026-09-08, Tuesday) — what he actually did:**
  - revised the remainder operator `%` (`1%3`, `2%3`, `3%3`)
  - `range(6)` is 0 to 5
  - `=` vs `==`
  - `height = 5` as the default inside the loop
  - `if i % 3 == 0: height = 9`
  - `x = x + 1` to space the towers — he missed the update twice and debugged it
  - a wool colour list + `i % 6` to cycle the colours
  - `elif i % 5 == 0: height = 7`
  - declared `z` and `z = z + 1`
- **Unmet last week:** the table showing which towers both rules hit. Debugging the missing `x`
  update, plus colours and the z axis, ate the time. It went to homework.
- **Homework concept just practised:** `elif-chain-first-match-wins`
  (`worksheets/homework-first-rule-wins-2026-09-08.md`).
- **Last deck (Tuesday):**
  `STUDENTS/students/leo-kim-tue-2000/slides/2026-09-08-one-loop-two-jobs.html`, 78 slides,
  36 taught steps. **Reached ~step 32 of 36** — found from the ledger `actual`, whose last
  bullets are the `elif` and the `z` variable ("Same symbol, different variable").
- **The big carry — the unused Sunday deck:**
  `STUDENTS/students/leo-kim-sun-1800/slides/2026-09-13-one-loop-fills-the-floor.html`
  (= `SLIDES/lessons/2026-09-13/leo-one-loop-fills-the-floor.html`), 99 slides, 40 taught steps.
  **Reached 0 of 40.** That lesson **did not run**: no Drive transcript for 13 Sept 16:00 GMT+7,
  and no worksheet or feedback in `leo-kim-sun-1800` newer than 2026-09-06.
- **What to do with it:** that deck already teaches exactly today's topic — integer division
  `//`, the strip folding into a floor, one loop vs a loop inside a loop, the 5 × 5 floor, rows
  vs columns picking the colour, `//` vs `%`. **Carry its whole body verbatim.** Rebuild only
  slot 1 (title) and slot 2 (recap) from the Tuesday facts above, then append the Tuesday tail's
  four unreached steps (steps 33–36: "A 5 × 5 floor, turned sideways", "A loop inside a loop",
  "Find square 12", "Your skyline") only where they are **not already in** the Sunday deck —
  drop any duplicate rather than teaching it twice.
- **New on top of the carry:** a **third** nested loop — `x`, `z` and now `y`, so the floor
  becomes a solid cube; then one `if` inside the inner loop so the floor comes out as a
  checkerboard.

**Reference deck for tone:** the Sunday deck above (it is the spine of today's deck).

---

## 21:00 KST · 19:00 HCMC — YURA

**Topic today: the spiral.** `side` grows inside the repeat, so the four walls never close.

- **Minecraft BLOCKS, not Python.** Every code step is a **drawn MakeCode block**, never a
  Python line. Block colour comes from the source drawer, not the wrapper; nested inputs are
  ×0.85 darker; fields are white ovals; `~` sits outside the oval.
- **Last lesson (ledger 2026-09-05) — what she actually did:**
  - `repeat 4` to make a square
  - that the repeat count decides the shape (6 instead of 4 fills the inside in)
  - read the code out loud to find the wrong block
  - made a variable `side`
  - `agent move forward by side`
  - changed `side` to 4, 10, 8 to see the size change
  - started stacking one more level on top of the square (**not finished**)
- **Unmet last week:** the spiral. Time ran out while stacking a second level on the square, so
  the spiral moved to this lesson. That lesson also opened about 6 minutes late.
- **Homework concept just practised:** `move-up-between-two-squares`
  (`worksheets/homework-the-second-square-2026-09-05.md`).
- **Last deck:** `STUDENTS/students/yura-tue-2200/slides/2026-09-12-the-square-unrolls.html`
  (= `SLIDES/lessons/2026-09-12/yura-the-square-unrolls.html`), 98 slides, 50 taught steps.
- **Stop point: reached 0 of 50.** That deck was built for Friday 2026-09-12, and the lesson was
  **moved to today before the slot** — no Drive transcript exists for it. **The entire deck is
  unspent.**
- **Slides to carry: the whole body, verbatim.** It already teaches exactly today's topic —
  the second square, the level number is `y`, `repeat`, one wall per pass, `side` growing
  mid-loop, the square becoming a spiral, growing by 2, the fat spiral, the odd-number table.
  Rebuild **only** slot 1 (title) and slot 2 (recap) from the 2026-09-05 facts above, and fix
  every date stamp. Do **not** rewrite the body.
- **New on top of the carry:** `side` **shrinking** each pass so the spiral winds inward, and a
  second variable so the height grows as the spiral turns — a spiral staircase.

**Reference deck for tone:** the 2026-09-12 deck above (it is the spine of today's deck).
