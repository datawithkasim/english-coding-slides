# Today's decks — 2026-09-11 (Fri)

Four lessons on the calendar, 16:00 → 19:00 Korea time. **All four are Minecraft
MakeCode Blocks** — Kasim's instruction this morning ("MC BLOCKS" against every
name). Zero Python in any deck today.

Not teaching today, no deck, no message:
- **JIYU** — tracker still says Fri 21:00. Her lesson moved and she is normally a
  Tuesday. No calendar event today. Report only, no tracker edit.
- **DAVID P** — tracker still says Fri 22:00. Moved to Sunday. Report only.

Topic source this morning:
- **IAN's topic is Kasim's own pick** and it overrides the deck carry (see his section).
- The other three use the Idea line, taken from the ledger `gap` / the homework
  just shipped.

| Time | Student | Topic | Deck |
|---|---|---|---|
| 16:00 KST · 14:00 HCMC | JUNWOO | MC **Blocks** — a `row` box + `change row by 1` inside a repeat, on the **ground** (x/z) | `junwoo-the-floor-fills-itself.html` |
| 17:00 KST · 15:00 HCMC | JADEN | MC **Blocks** — a `repeat` **inside his own chat command** | `jaden-one-command-many-flowers.html` |
| 18:00 KST · 16:00 HCMC | NELLIE | MC **Blocks** — `place on move` + `repeat 4` walks the square | `nellie-the-agent-does-the-placing.html` |
| 19:00 KST · 17:00 HCMC | IAN KIM | MC **Blocks** — the box reads itself: `change side by 1` **is** `set side to side + 1` | `ian-the-box-reads-itself.html` |

## Hard rules for every deck

Read first, in this order:
1. `../../TEMPLATE.md` — the slot structure and per-slide rules
2. `../../PEDAGOGY.md` — why each slot exists
3. `../../assets/style.css` — the only styling allowed
4. The reference deck named in that student's section below, for tone

Then:
- Save to `lessons/2026-09-11/<file>.html`. Stylesheet `../../assets/style.css`,
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
- Decks are light cream (palette flipped 2026-09-09). Code boxes and viz chips
  stay dark. Do not reintroduce a dark deck background.

### Shape of the hour
Short recap of last week, then **most of the hour on the new idea**. A deck that
spends half the hour on last week is a failed deck.

### Copy-this-and-it-works contract
The student makes **zero decisions**. If a slide needs the student to infer
anything, it is wrong.

- **One change per slide**, numbered `STEP n / total`. A re-indent is its own step.
- Every code step carries all four:
  - **the code** — full OLD block and full NEW block, never `...` inside a changed region
  - **🔍 FIND** — the exact block to look at (block track: name the block and its drawer)
  - **📍 where** — quote the existing block it goes under, and how deep inside the mouth
  - **🟣 why** — one line
  - **✅ check** — one line: what running it should show
- **Big programs ramp v1 → v2 → v3 → v4.** Never the finished program first. New
  blocks hot, unchanged blocks dim, changed blocks get an explicit OLD/NEW pair.
- **Visuals beat words, and are mandatory for loops, iteration and any maths** —
  one frame per pass with the counter value shown.

### Block track — ALL FOUR decks today
**Zero Python anywhere** — not in a code block, not in a debug card, not in a
comment. Draw the blocks with the `.mcb` / `.mcb-c` / `.mcb-stack` / `.mcb-in` /
`.mcb-drop` / `.mcb-from` components at the end of `assets/style.css`.

Primary reference deck for block drawing: `../2026-09-10/jj-the-spiral-staircase.html`.
Secondary: `../2026-09-04/nellie-the-agent-does-the-placing.html`.

Category classes and their (pixel-sampled) colours:
`basic` `player` `blocks` `mobs` `agent` `gameplay` `pos` `loops` `logic` `vars` `math`.
Every new block gets a `.mcb-from` line naming its toolbox drawer.

Block anatomy: colour follows the **drawer the block came from**, never the block
it sits inside. Nested input = its own drawer colour × 0.85. Number field = white
pill oval. `~` is white label text printed inside the position pill, outside the
white number ovals.

Coordinates, when they appear: **y starts at 0; x and z start at 1.**

---

## 16:00 KST · 14:00 HCMC — JUNWOO · Minecraft **Blocks**

**Last lesson (2026-09-04, from the ledger).** Note: **there is no Drive
transcript for this lesson** — the recording never ran, and the ledger row was
built from a Notion transcript at Kasim's instruction. Facts below are the ledger
`actual`, which is the best record that exists. This is not an error, and the
deck must not pretend to quote a timestamp.

- drawing pixel art on the **ground**, not the wall
- using **x and z only**, with y held at 0
- counting x and z from **1** on the floor grid
- start corner and end corner into one `fill` block
- the letter **J** of his name on the floor, slime block, chat command `f`
- a **creeper face on a 20×20 floor grid**, a different colour block per part
  (pink and magenta glazed terracotta)

**Unmet last week (the gap, and the strongest input today):**
> row 변수와 change row by 1 은 못 했어요. 바닥 격자에서 x와 z를 세는 것과 크리퍼
> 얼굴을 끝까지 완성하는 데 시간을 다 썼어요. 반복은 다음 시간으로 옮겼어요.

The `row` variable and `change row by 1` were promised to the parent and did not
happen. The whole lesson went on counting the floor grid and finishing the face.

**Homework concept just practised:** `ground-plane-xz-fill` — worksheet
`homework-ground-pixel-art-2026-09-04`. It asked him to build, on the ground: the
letter **U**, a **pig face**, and one design of his own. Open the deck by checking
that, not by re-teaching coordinates.

**Where last week's deck stopped**
- Last deck: `../2026-09-04/junwoo-one-repeat-many-rows.html` (91 slides)
- Stop point: from the ledger `actual`. The lesson **diverged** from the deck — the
  deck taught wall pixel art then the repeat; the lesson went to the ground instead.
  He reached roughly **slide 22** (single `fill`, FROM corner, TO corner, one row).
  Everything from **slide 23 ("Wrap it in repeat 4 times") to the end is unreached.**
- **The carry is a REBASE, not a verbatim copy — this is the one exception to the
  verbatim rule today, and it is deliberate.** The unreached arc (repeat → a box
  called `row` → `set` once, `change` every pass → a table of passes → the
  nested-mouth and count-down bonuses) is exactly today's idea and must be reused.
  But every one of those slides puts `row` in the **y** hole and talks about a wall
  climbing. Today it goes in the **z** hole and the rows march away across the
  ground. Port slide by slide, swapping `y` → `z` and "wall / climb / height" →
  "floor / away / depth". Keep the wording, the visuals and the step order.
- **Do not** carry slides 1–22, and do not carry Slot 1 or Slot 2.

**Today's new idea:** one `repeat` fills the whole floor. He hand-placed every row
of the creeper face; today a box called `row` and `change row by 1` inside a
repeat fills a 20×20 floor canvas with one block and one loop.

Ramp: v1 one `fill` = one strip on the ground → v2 wrap it in `repeat 4 times` and
see it print the same strip four times → v3 make a box called `row`, drop it into
both z holes → v4 `change row by 1` inside the mouth, `repeat 20`, the whole
canvas fills.

Visual required: one frame per pass on a top-down floor grid, with the value of
`row` printed beside each frame. Pass 1 = row 1, Pass 2 = row 2, Pass 3 = row 3.
Then the finished 20×20 canvas with the creeper face he already made drawn on top
of it, so he sees what the loop just saved him.

△ from last week and the week before: he needed the coordinate rule re-explained
several times, and he lost a grid square counting the creeper mouth. Both become
Common Mistake slides — one on "the box goes in the hole, not beside it", one on
"`set` once above the mouth, `change` inside it".

Reference deck for tone: `../2026-09-04/junwoo-one-repeat-many-rows.html` (his own
voice) plus `../2026-09-10/jj-the-spiral-staircase.html` for block drawing.

---

## 17:00 KST · 15:00 HCMC — JADEN [PH] · Minecraft **Blocks**

**Slot note:** Jaden's tracker weekday and his folder name `jaden-wed-1800` are
both **stale**. His real slot is **Friday 17:00 KST**, per the calendar (event
updated 2026-09-09). Folder name stays as it is — match on `tracker_name`.

**Last lesson: 2026-08-29 (13 days ago).** He **rested on 09-04**, so there is no
lesson and no card for that date. Read from the Drive transcript
`Meeting started 2026/08/29 17:00 GMT+07:00` (= 19:00 KST). That doc is Gemini's
**prose summary**, not a raw transcript — no timestamps, no code text. Do not
quote a timestamp in this deck.

- the agent builds **while** it moves, with a block type set, to make a fence
- the movement run: forward 7 → turn left → forward 5 → turn left, repeated to
  close the shape
- the agent stopped early because its path was blocked; the fix was **one more
  `move up by 1` added at the END**, the rest of the code untouched
- a **second, separate chat command named `flower`**: set item to flower,
  forward 7, up 1
- more flower types, then Kasim added a waterfall
- growth items on plants; plants need **light and space** or they will not grow
- grouping plants together into a dense forest

**△ what he struggled with:**
- kept typing **`run`** to fire the new command when the name in the oval said
  **`flower`**
- unsure when the agent needs to move up or down at all
- earlier (08-22 and 08-29 logs): mixes up **forward** and **up**

**Unmet last week:** nothing was promised in the doc. No "next time" line exists.

**Homework concept just practised:** worksheet
`homework-fence-and-flower-2026-08-29`. It drilled forward-vs-up, counting the
four fence sides (skip the square the agent stands on), and "type the word in the
white oval, not `run`". Open the deck by checking that sheet.

**Where last week's deck stopped**
- Last deck: `../../../english-coding-students/students/jaden-wed-1800/slides/2026-08-31-my-own-command.html`
  (37 slides). It was built **after** his 08-29 lesson and he rested on 09-04, so
  **it was never taught. Nothing in it is spent.**
- **But it is written in Python** (`def flower():`, `player.on_chat("flower", flower)`,
  `agent.set_block_or_item(...)`). Kasim's instruction this morning is **MC BLOCKS**,
  and his worksheet is blocks too. So **do not carry it verbatim. Port the arc into
  drawn MakeCode blocks.**
- Port this arc, in this order, redrawn as blocks:
  `on chat command "flower"` as a doorbell with a name tag → v1 one flower →
  the chat word fires your command → forward-vs-up → the three bug cards
  (nothing happens / a tower instead of a path / the misspelled name) →
  v2 call it four times → v3 a step between each flower → v4 a whole fence side.
- Keep the bug cards. They are his real mistakes, not invented ones.

**Today's new idea:** a **`repeat` inside his own command**. He already owns two
commands (`fence`, `flower`). Today the `flower` command stops being four copies
of the same two blocks and becomes one `repeat 4 times` mouth with the two blocks
inside it.

Ramp: v1 his `flower` command, one flower → v2 the same two blocks copied four
times, which works but is long → v3 delete three copies and wrap the remaining
pair in `repeat 4 times` → v4 change the one number to 10 and get ten flowers
from one edit.

Visual required: side-by-side — eight stacked blocks on the left, one `repeat`
mouth holding two blocks on the right, an arrow between them, and the same flower
row drawn under both. Then one frame per pass showing which flower gets planted.

Warm-up (short, earns its place, then move on): the white oval holds the word you
type. `run` is not a magic word. One slide, one drawn block with the oval
highlighted, one circle-the-answer card.

Reference deck for tone and block drawing: `../2026-09-10/jj-the-spiral-staircase.html`.

---

## 18:00 KST · 16:00 HCMC — NELLIE · Minecraft **Blocks**

**Last lesson (2026-09-04): nothing was taught.** This is the whole point of her
section. From the ledger:

> 약속한 내용을 하나도 진행하지 못했어요. 초반에 WASD 키가 먹지 않아 마인크래프트를
> 다시 켰고, 그 뒤로는 학생이 많이 피곤해해서 코딩을 시작하지 못했어요. 수업 끝에
> 오늘은 아무것도 못 했다고 학생에게 직접 말했고 숙제도 그 자리에서는 내주지 않았어요.

WASD stopped working, Minecraft was restarted, and she was too tired to start
coding. `actual` is an empty list. Kasim told her at the end that nothing got
done. The worksheet was shipped afterwards, not in the room.

**Last lesson where something WAS taught (2026-08-28), for the Recap slot:**
- `fill` with coordinate ranges (x, y, z)
- a rainbow tower: red, orange, yellow, green, blue, purple, pink wool layers
- the range idea — 0, 1, 2 is three numbers
- layer by layer, working out the start and end coords for each
- `air` blocks to hollow out the inside
- first meeting with the agent: `move forward`, `turn left`, a loop, giving the
  agent items to place
- ✓ she saw the pattern from two demoed layers and wrote the other five herself,
  coordinates correct
- △ she kept placing the agent's blocks **by hand** — picked a fence and placed it
  manually — instead of coding the loop

**Unmet last week:** everything. `place on move` + a repeat block walking a square
wall was promised to the parent and none of it happened.

**Homework concept just practised:** `place-on-move-square` — worksheet
`homework-the-agent-drops-blocks-2026-09-04`. She has had the sheet for a week, so
open by checking it: the switch, `agent set item ... count 64 in slot 1`, five
fences from `move forward by 5`, and the `repeat 4 times` square.

**Where last week's deck stopped**
- Last deck: `../2026-09-04/nellie-the-agent-does-the-placing.html` (59 slides)
- Stop point: **slide 0 of 59.** The ledger `actual` is empty — no coding happened
  at all. Nothing in that deck was taught.
- **Carry the ENTIRE deck verbatim**, slides 3 → 59, unchanged. It was written for
  exactly today's topic, it was reviewed, and it is in her voice. Rebuild only
  Slot 1 (title) and Slot 2 (Recap) — the recap must say last week made no
  progress, warmly and without blame, and point at the homework sheet instead.
- Renumber after carrying: the `counter` span, every `STEP n / total`, the
  `footer-tag` date, the Recap pill date, and the `<!-- N · SLOT -->` comments.

**Today's new idea:** the carried deck **is** the new idea for her — none of it has
been taught. `place on move` switches the agent from her hands to code, and
`repeat 4` walks the square.

**The overshoot rule still applies on top of the carry.** 59 carried slides is not
enough for the hour once she moves fast on a sheet she has already done.

**⚠ Do NOT re-teach what the carry already holds.** The old deck already covers,
around slides 45–55: climbing one block, a second bigger loop, putting the lap
inside it, three laps / three layers, making it a tower, four sides in four
colours, and switching the placer off at the end. Writing any of those again
means the same slide appears twice in one deck.

New tail, genuinely past the end of the carried deck, each with a visual:
- **a doorway** — switch the placer **off** for two steps in the middle of one
  wall, then back **on**, so the square has a gap you can walk through
- **a second storey in a different block** — the tower already exists in the
  carry, so build on it: change the item between storeys, not between walls
- **a `fill` roof** dropped on top of the agent-built walls, joining the `fill`
  block she already knows to the agent work she learns today
- **counting the cost** — how many blocks the whole build used, drawn as a sum,
  and how many clicks it would have been by hand

△ from 08-28 that must become a Common Mistake slide: placing blocks **by hand**
instead of letting the loop do it. That is the exact habit this lesson replaces,
so name it directly — "your hands did nothing" is the win condition.

Reference deck for tone and block drawing: her own
`../2026-09-04/nellie-the-agent-does-the-placing.html`, then
`../2026-09-10/jj-the-spiral-staircase.html`.

---

## 19:00 KST · 17:00 HCMC — IAN KIM (_loha2018) · Minecraft **Blocks**

**⚠ Kasim's own instruction this morning, and it overrides everything else in this
section:**

> "lets keep IAN simple. he still doesnt understand that variables can change when
> we say variable + 1"

So today is **one idea, taught slowly, with a lot of visuals**. It is **not** the
3D / climbing-spiral lesson the ledger pointed at, and **the 40-slide carry from
his last deck is dropped on purpose.** Do not reinstate it. Do not add a tower.

**Last lesson (2026-09-04, from the ledger — i.e. from the transcript):**
- the variable idea: a box called `side` holding one number
- `set side to 10` and `set side to 0`
- `agent move forward by side` — a variable oval in the number hole instead of a
  typed number
- `change side by -1` and `change side by 1`
- `repeat 10 times` holding a move, a turn and a change
- `-1` winds the spiral inwards, `1` winds it outwards
- `agent place on move [on]` to build a wall while walking

**Unmet last week:** nothing. The promise was delivered in full, plus the `-1`
variant. `gap` is null.

**Homework concept just practised:** `sign-of-change-decides-spiral` — worksheet
`homework-the-sign-that-turns-the-spiral-2026-09-04`. It drilled: the box holds
one number, `change side by -1` four times gives 5, 4, 3, 2, `change side by 1`
gives 2, 3, 4, 5, and the sign picks which way the spiral winds.

**So what is left to teach, if he did all that?** The mechanism. He can copy
`change side by 1` and predict the numbers on paper, but he does not believe that
the box **reads its own value, adds one, and puts the answer back in itself.**
That is today, and it is the whole lesson.

**Today's new idea:** `change side by 1` **is** `set side to (side + 1)`. The same
block written the long way. Show that the two are interchangeable, and the
mechanism stops being magic.

Ramp — slow, one idea per version:
- **v1** `set side to 5`, then `agent move forward by side`. The box hands out its
  number. Nothing changes yet.
- **v2** `change side by 1` **once**, outside any loop, then move again. Two walks:
  5, then 6. One block, one change, visible immediately.
- **v3** the same thing written the long way: `set side to (side + 1)` using the
  MATH `+` block with the `side` oval dropped into its left slot. Run it. Same
  result. **This is the slide the whole deck exists for.**
- **v4** put it inside `repeat 4 times` and watch the number climb 5, 6, 7, 8.

Visual required, and it must be the spine of the deck — a three-panel drawing
repeated on every pass:
1. the box `side`, lid open, the number **5** coming out
2. the number sitting next to a `+ 1`, making **6**
3. the **6** going back into the same box, the old 5 crossed out

Draw that panel again for every pass. Never just print a table of numbers.

Also required, because this is the misunderstanding itself: a slide holding the
two blocks **side by side** — `change side by 1` on the left, `set side to (side + 1)`
on the right — with a big `=` between them and both outputs drawn underneath.

Common Mistake slides to include:
- `set side to 1` inside the loop instead of `change side by 1` — the number never
  climbs, it resets every pass. Draw both outcomes.
- reading `side + 1` as "the box is now called side + 1". Draw the box keeping its
  name and only its contents changing.
- putting the `change` block **outside** the mouth — one change, not four.

**Keep it simple.** Do not introduce a second variable, do not introduce height,
do not introduce nesting. If a slide is not about the box reading itself, it does
not belong in the first two thirds of this deck.

**Overshoot tail (tagged OPTIONAL, after the core idea is fully done):** more of
the **same** idea, never a new mechanism — `change side by 2`, `change side by -1`
written the long way as `set side to (side - 1)`, a box that doubles with
`set side to (side + side)`, and reading a second box's value into the first.

**Carry:** none. Last deck `../2026-09-04/ian-kim-the-square-that-grows.html` (94
slides) stopped around **slide 54**, and its unreached tail (climbing spiral →
spiral tower → a second box feeding the step) is real but is **the wrong lesson
for today by Kasim's explicit instruction.** Leave it where it is; it is still
there next week.

Reference deck for tone and block drawing: his own
`../2026-09-04/ian-kim-the-square-that-grows.html`, then
`../2026-09-10/jj-the-spiral-staircase.html`.
