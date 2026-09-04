# Today's decks — 2026-09-05 (Sat)

Seven lessons. **Four are Minecraft BLOCKS (MakeCode), one is IDE Python
(pygame), one is IDE Python (Manim), one is debate.** 08:00 → 20:45 Korea time.

**Kasim gave the topics himself this morning.** His words are the spec. Where
`promised` disagrees with his pick, his pick wins and `promised` is background.

| Time | Student | Track | Topic | Deck |
|---|---|---|---|---|
| 08:00 KST · 06:00 HCMC | YUNGUN | IDE Python (pygame) | a `direction` variable — the snake keeps moving on its own, then food with `random` | `yungun-the-snake-that-keeps-going.html` |
| 09:00 KST · 07:00 HCMC | SUHO | MC **Blocks** | one `repeat` builds every layer of the tower | `suho-one-repeat-every-layer.html` |
| 11:00 KST · 09:00 HCMC | DEBATE [LEO + 1] | **Debate DB001** | Week 1 — AI and homework · claim + reason | `../../debate/db001-tech-ai/week-01.html` (existing, reused — do not rebuild) |
| 13:00 KST · 11:00 HCMC | JOY | MC **Blocks** | Lesson 1 from zero — chat command, agent move, agent place | `joy-lesson-1-the-agent-obeys.html` |
| 18:00 KST · 16:00 HCMC | YURA | MC **Blocks** | a `repeat` around agent move — the loop walks the pattern | `yura-one-repeat-many-steps.html` |
| 19:45 KST · 17:45 HCMC | Dewy | MC **Blocks** | `repeat` + `agent turn` closes the square in one loop | `dewy-the-loop-turns-the-corner.html` |
| 20:45 KST · 18:45 HCMC | ANDY | IDE Python (Manim) | many animations in one `self.play`, `VGroup`, `self.wait` | `andy-many-things-at-once.html` |

**Kasim's exact words this morning:**
> Suho MC BLOCKS, YUNGUN Pyhon, DEBATE class 001 (same as today), Joy Minecraft
> Blocks lesson 1. Yura g5 minecraft blocks, Dewy Minecraft blocks, Andy IDE
> Python (Manim)

Where his words were a track and not a step, the concrete next step was chosen
from that student's own last lesson and is named in their section below.

---

## Report-only drift — nothing here was auto-fixed

- **Dewy** — calendar 19:45 KST, tracker `slot_time` 22:00. Calendar wins today.
- **YUNGUN** — calendar 08:00 KST, tracker `slot_time` 08:10. 10 min.
- **YURA G5** and **DEBATE CLASS [LEO + 1]** have Saturday calendar events but
  **no Saturday row in `tools_students`** (YURA is stored Tue 22:00, the debate
  group is not stored at all). Kasim named both this morning, so both are real.
- **SUHO** is taught under the calendar title `MS001 [화 9시]`, which is his
  `transcript_alias` — it matches, so no rename was proposed. `roster.json` still
  files him under folder `ms001-fri-0900`.
- **SUHO's tracker note** says he agreed on 2026-08-29 to move to text-based
  coding on `app.english-coding.co.uk`. **Kasim's pick this morning is MC BLOCKS**,
  so the move has not happened yet. Background fact, not the plan.
- **`roster.json` slots are stale** for YUNGUN (`sat 20:00`, really 08:00).

## Transcript note — every student today is prep-blind

Gemini notes for Saturday 2026-08-29 hold **one** doc, 17:00 GMT+7 = 19:00 KST,
which is **JADEN [PH]**, not anybody teaching today. Drive has no transcript for
any of these seven. Every fact below comes from `tools_lesson_logs` /
`tools_log_drafts`, which are AI summaries of a recording and were **not**
cross-checked.

**No `ledger/` file exists for any of the seven**, so there is no recorded `gap`
— nothing is known to have been promised to a parent and missed.

---

## Hard rules for every deck

Read first, in this order:
1. `../../TEMPLATE.md` — the slot structure and per-slide rules
2. `../../PEDAGOGY.md` — why each slot exists
3. `../../assets/style.css` — the only styling allowed
4. The reference deck named in that student's section below, for tone

Then:
- Save to `lessons/2026-09-05/<file>.html`. Stylesheet `../../assets/style.css`,
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
- **Every slide carries a visual.** A heading plus a bulleted list is not a
  finished slide.
- **Never gendered pronouns.** No he / she / his / her anywhere in a deck. Use
  the student's name or *they*. The tracker logs below say "herself" and
  "himself" — do not copy that wording onto a slide.

### Shape of the hour
Short recap of last week, then **most of the hour on the new idea**. A deck that
spends half the hour on last week is a failed deck.

### Copy-this-and-it-works contract
The student makes **zero decisions**. If a slide needs the student to infer
anything, it is wrong.

- **One change per slide**, numbered `STEP n / total`.
- Every step carries all five:
  - **the code / the blocks** — full OLD block and full NEW block, never `…`
    inside a changed region
  - **🔍 FIND** — the exact Ctrl+F string (Python track) or the exact block by
    name (block track)
  - **📍 where** — quote the existing line or block it goes under, and the
    indent count
  - **🟣 why** — one line
  - **✅ check** — one line: what running it should show
- **Big builds ramp v1 → v2 → v3 → v4.** Never the finished build first. New
  lines / blocks `.hot`, unchanged ones `.dim`, changed ones get an explicit
  OLD/NEW pair.

---

## BLOCKS TRACK — applies to SUHO, JOY, YURA and Dewy

**All four drag MakeCode blocks. Kasim confirmed this morning by name.**

**Zero Python anywhere.** Not in a code block, not in a debug card, not in a
comment, not in a heading. The tracker logs for these four are written in
Python-ish text (`blocks.fill()`, `agent.move("forward", n)`,
`agent.set_block_or_item()`) because they are AI summaries of a recording —
**that is not what these students see or type.** Redraw every one of those ideas
as a block.

### The `.mcb` component set

Live at the end of `../../assets/style.css`. Worked markup:

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

- `.mcb-c` = a C-shaped block that wraps others (`on chat command`, `repeat`,
  `if`). Its `.hat` is the top bar, its `.mcb-in` holds the blocks inside.
- `.mcb` = a single block. Category class sets the colour: `basic` `player`
  `blocks` `mobs` `agent` `gameplay` `pos` `loops` `logic` `vars` `math`.
- `.dd` = a dropdown hole · `.val` = a white number or text hole · `.ovar` = a
  variable oval · `.swatch` = a colour square for a wool or concrete colour.
- `.mcb-drop` = an empty dashed socket, for "drag the next block in here".
- `.hot` / `.dim` = the block added this step / already there.
- `.mcb-from` names the toolbox drawer. **Every new block gets one.**

### Toolbox drawer colours — use these exact hexes

Pixel-sampled from Kasim's own editor. The `.mcb.<class>` values in `style.css`
already match this table; the `.mcb-from .drawer` inline hex must be typed from
here:

| Drawer | Hex |
|---|---|
| BASIC | `#E89005` |
| PLAYER | `#0078D7` |
| BLOCKS | `#7ABB55` |
| MOBS | `#764BCC` |
| AGENT | `#D83B01` |
| GAMEPLAY | `#8F6D40` |
| POSITIONS | `#69B090` |
| LOOPS | `#569138` |
| LOGIC | `#459197` |
| VARIABLES | `#EA2B1F` |
| MATH | `#6C6EA0` |

**Colour follows the drawer the block came from, never the block it sits
inside.** A green `fill` block nested in a blue `on chat command` hat stays
green. A nested input block is its own drawer colour × 0.85.

**The `~` tilde** is white label text printed inside the position pill, outside
the white number ovals — one `~` before each of the three numbers. It is never
typed into the number field.

**The place-on-move switch is drawn as `agent place on move [ON]`** from the
AGENT drawer. `set_assist(PLACE_ON_MOVE, True)` is the Python-track form and
must never appear.

### Coordinates rule — all four block decks

**y starts at 0. x and z start at 1.** The first free square is `~1 ~0 ~1`.
Never write "coordinates start at 0" as one blanket rule. Counting a range is
unchanged either way: end minus start, then add 1.

### Reference decks for tone (blocks)
- `../2026-09-02/seohoo-pixels-with-a-loop.html`
- `../2026-09-02/ihyeon-maze-first-turn.html`
- `../2026-09-03/jj-the-growing-staircase.html`
- `../2026-09-04/nellie-the-agent-does-the-placing.html`

---

## 08:00 KST · 06:00 HCMC · YUNGUN — `yungun-the-snake-that-keeps-going.html`

**Track:** IDE Python, pygame · **Source:** log + draft 2026-08-29, plus his own
deck `../2026-08-30/yungun-snake-moves.html` shipped for the Sunday lesson
**Topic (Kasim: "YUNGUN Pyhon"):** food with `random`, eating, and the snake
growing — `direction` is recapped, not taught

> **Corrected after reading his live IDE file** (`student_ide`, SELECT only),
> `main.py` last saved 2026-08-30 08:48 KST, during the Sunday lesson.
> **`direction = (1, 0)`, the event-driven key handler that *sets* it,
> `MOVE_INTERVAL`, `clock.tick(60)`, `CELL_SIZE`, `GRID_WIDTH`/`GRID_HEIGHT` and
> a grid-coordinate `snake_body` list are already on his screen.** The snake
> already keeps moving on its own, so the "v1 → v3" plan below was already done
> on 30 Aug. The deck recaps it in 8 slides and spends the hour on food, eating
> and growth.
>
> **The 2026-08-30 deck does not match his live file.** `snake_pos`, `GREEN`,
> `BLACK` and `pygame.key.get_pressed()` appear in that deck and exist nowhere in
> his code. Match the FILE, never that deck.

**Covered last time (log, 2026-08-29)**
- `def` functions called with parameters (`name`, `age`, `favorite_food`)
- f-strings with `{}` to print variables; built lists (foods, animals)
- `for` loop over a list; pygame window + `pygame.draw.rect()`
- Snake position read with `snake_pos[0]` / `snake_pos[1]`; colour constants
- ✓ Fixed a missing-argument error alone by adding `say_hello("James")`
- △ Could not put the meaning of a for-loop variable into a full sentence

**Shipped since (deck `2026-08-30-snake-moves.html`, Sunday lesson)**
Already taught, so **do not re-teach**: what slot 0 and slot 1 hold, adding to a
slot to move, and a key press picking which slot changes. He can already move the
snake **by pressing a key**.

**Promised:** nothing recorded.

**What today teaches**

Right now the snake only moves while a finger is on a key. Today it keeps going
by itself.

Ramp it (as built):

1. **v1** — his file exactly as it stands: `direction` already set, snake already
   sliding. Recap only, 8 slides, including the say-the-sentence work below.
2. **v2** — `import random`, `food = (random.randint(0, GRID_WIDTH - 1),
   random.randint(0, GRID_HEIGHT - 1))`.
3. **v3** — a `food_rect` drawn in `PASTEL_PINK` with a second
   `pygame.draw.rect()`.
4. **v4** — `if new_head == food:` and the food respawns somewhere new.
5. **v5** — `else: snake_body.pop()`. The snake now **grows** when it eats. This
   is the whole lesson.
6. **Then push past it:** a `score` variable · the score in the window caption
   with an f-string · `MOVE_INTERVAL` shrinking as score rises, with a floor
   guard · `%` for wrapping at the window edge · `while food in snake_body:` so
   food never spawns under the snake · self-hit game over.

**Turn the △ into a slot.** He could not say out loud what a loop variable
means. Give him a *say-the-sentence* slide for `direction[0]`: "direction[0] is
how far right the snake moves each step." One sentence, read aloud, then a
fill-the-blank twin. Use `direction[0]` / `direction[1]` — the names in his
file — never `dx`/`dy`, which exist nowhere on his screen.

**Reference deck:** `../2026-08-30/yungun-snake-moves.html` for tone and for the
exact variable names already on his screen — match them, do not rename.
Also `../../python/pygame-starter/` for slot structure.

---

## 09:00 KST · 07:00 HCMC · SUHO — `suho-one-repeat-every-layer.html`

**Track:** Minecraft **BLOCKS** · **Source:** log 2026-08-29 + draft 2026-08-22
**Topic (Kasim: "Suho MC BLOCKS"):** one `repeat` builds every layer of the tower

**Covered last time (2026-08-29)**
- Stacking layers by changing the y number
- A `fill` block per layer, each with its own start and end position
- Loaded an extension program (roller coaster)
- Tree generation with bone meal; a `hollow` option on a structure
- ✓ Worked out the missing layer numbers alone (orange 3–5, yellow 8, blue fixed
  to 14)
- △ Believes the code is not being saved
- △ Waits for guidance instead of typing independently

**The week before (draft, 2026-08-22) — the open promise**
- A `level` variable starting at 0, a `while level < 6` loop
- `if` / `else if` branches inside the loop, a `fill` per branch
- `change level by 1` to step the layer height
- △ **The rainbow tower only ever built layer 1** — the increment or the
  condition was in the wrong place. **`promised`: "bring photo of code, debug
  together why tower stalled on layer 1."** That promise is still open and today
  closes it.

**What today teaches**

Last week he built the tower the slow way: one `fill` block per layer, all the
numbers typed by hand. Today one `repeat` block builds every layer.

Ramp it:

1. **v1** — two `fill` blocks he already knows, drawn as blocks: layer 0 and
   layer 1. Point at the one number that differs.
2. **v2** — a `repeat 4 times` wrapped around **one** `fill`. Run it: four
   identical layers stacked in the same spot, because nothing changes between
   passes. Ask what went wrong *before* the fix.
3. **v3** — make a variable `level`, `set level to 0` **before** the loop, and
   drop the `level` oval into the y hole of both position pills.
4. **v4** — `change level by 1` **inside** the loop, as the **last** block. Now
   each pass builds one layer higher. **This is the layer-1 bug from 22 Aug,
   named out loud:** if `change level by 1` sits outside the loop, every pass
   builds at the same height.
5. **Then push past it:** a colour that changes per pass (rainbow tower) · a
   `repeat` inside a `repeat` for a solid cube · a `width` variable so the tower
   tapers · `if level > 3` to switch block type halfway.

**Turn the △ into slots.** One slide showing where MakeCode saves, so "my code
is not saved" is answered with a picture. One *you drive* slide where he drags
the block and Kasim's hands stay off the keyboard.

**Background fact, not the plan:** his tracker note records an agreement on
2026-08-29 to move to text coding on `app.english-coding.co.uk`. That move has
not happened. Today is blocks.

---

## 11:00 KST · 09:00 HCMC · DEBATE CLASS [LEO + 1] — **no new deck**

**Kasim: "DEBATE class 001 (same as today)".** Reuse the existing deck
`../../debate/db001-tech-ai/week-01.html`, the same one Friday's DB001 group ran
on 2026-09-04. Week 1 — AI and homework, claim + reason.

**Do not rebuild it, do not run `build-debate-decks.py`** — that script wipes
the hand-built debate decks. Link it from the day `index.html` only. There is no
student folder for this group in `roster.json`, so nothing is copied.

The "+1" in the calendar title is not identified anywhere in the tracker or in
`roster.json`. Do not guess a name in any deck, message or report.

---

## 13:00 KST · 11:00 HCMC · JOY — `joy-lesson-1-the-agent-obeys.html`

**Track:** Minecraft **BLOCKS** · **Source:** none — first lesson
**Topic (Kasim: "Joy Minecraft Blocks lesson 1"):** lesson 1 from zero — a chat
command, the agent moves, the agent places

**Covered last time:** nothing. `transcript_alias` is
`JOY [EXPERIENCE LESSON]`, `tools_lesson_logs` is empty, `tools_log_drafts` is
empty, no Drive transcript, no ledger. **Treat as a true first lesson.** Never
imply prior knowledge and never open with a recap of a lesson that did not
happen — replace the Recap slot with a *what we will build today* picture.

**What today teaches**

Absolutely from zero, in this order, each its own ramp version:

1. **v1** — where the MakeCode editor is, what the toolbox drawers are, and how
   a block is dragged out. One slide per drawer that gets used today, painted in
   its real colour.
2. **v2** — the `on chat command "go"` hat from the PLAYER drawer. Type `go` in
   Minecraft chat, something happens. Nothing inside it yet — draw the empty
   `.mcb-drop` socket.
3. **v3** — `agent move forward 1` from the AGENT drawer, dropped inside the
   hat. Run it. The agent takes one step.
4. **v4** — `agent move forward 5`. Same block, one number changed. Count the
   five squares on a drawn grid.
5. **v5** — `agent turn left`, then `agent move forward 5` again. Draw the path
   as an L on a grid, one frame per block.
6. **v6** — `agent place on move [ON]` from the AGENT drawer, above the moves.
   Now walking draws a line of blocks. **Teach the builds-behind rule here with
   a picture**: the agent places the block in the square it just left, not the
   one it stands in.
7. **Then push past it:** a square path (forward, turn, four times, by hand) ·
   what a `repeat` would do to that (preview only, do not teach it fully) ·
   swapping the block in the agent's inventory slot · `agent place on move [OFF]`
   to leave a gap.

Since there is no history, **overshoot harder than usual** — a trial student who
finishes early looks like a short lesson to a watching parent.

**Reference deck:** `../2026-09-04/nellie-the-agent-does-the-placing.html`.

---

## 18:00 KST · 16:00 HCMC · YURA — `yura-one-repeat-many-steps.html`

**Track:** Minecraft **BLOCKS** · **Source:** log 2026-08-25 (stored as Tue
22:00; today is a Saturday slot the tracker does not know about)
**Topic (Kasim: "Yura g5 minecraft blocks"):** a `repeat` around agent move —
the loop walks the pattern

**Covered last time (2026-08-25)**
- `agent place on move` ON / OFF to control when blocks appear
- Agent movement: forward, up, turn left, turn right
- Gaps in a pattern made by switching place-on-move OFF
- A square border (straight moves plus turns); a bridge pattern
  (forward, up, forward)
- The rule that the agent places blocks **behind** itself, not where it stands
- ✓ Counted 6 blocks unaided and typed `forward 6`
- ✓ Switched ON / OFF at the right spots on the border pattern
- ✓ Asked "do I turn it off if I go forward from here?" — checking timing alone
- △ Switched OFF too early on the letter H — two blocks missing, fixed after
  explanation
- △ The builds-behind rule is not solid yet; `forward 2` at the end needed
  several explanations

**Promised (2026-08-25):** "Homework sent: agent on/off worksheet — dotted line,
H rematch, longer bridge, design letter Y. **Next: check homework, then repeat
patterns with loops.**"

Kasim's pick and `promised` agree. The homework check is the way in, then the
loop is the lesson.

**What today teaches**

Right now every step of the border costs a separate block. Four sides means four
copies of the same four blocks. Today one `repeat` does all four.

Ramp it:

1. **Warm-up, short** — the letter-Y / dotted-line homework on screen, with the
   builds-behind rule redrawn as a picture: agent square highlighted, block
   square behind it highlighted a different colour.
2. **v1** — the square border written the long way, drawn as blocks: forward,
   turn, forward, turn, forward, turn, forward, turn. Circle the repeating pair.
3. **v2** — `repeat 4 times` from the LOOPS drawer, wrapped around **one**
   forward + one turn. Same square, four blocks instead of eight.
4. **v3** — change the `4` to `3` and the turn to a different angle. Watch the
   shape change without touching anything else.
5. **v4** — a `side` variable set before the loop, `change side by 1` inside it,
   the oval dropped in the move's number hole. The square becomes a spiral.
6. **Then push past it:** `agent place on move OFF` **inside** the loop for a
   dotted border · a `repeat` inside a `repeat` for a filled square · a staircase
   with `forward` + `up` in one loop · the letter Y drawn with two loops.

**Turn the △ into a Debug slot.** The letter H, place-on-move switched OFF one
step early, two blocks missing. Show the wrong output and the right output side
by side and let Yura find the block to move.

---

## 19:45 KST · 17:45 HCMC · Dewy — `dewy-the-loop-turns-the-corner.html`

**Track:** Minecraft **BLOCKS** · **Source:** log + draft 2026-08-29
**Topic (Kasim: "Dewy Minecraft blocks"):** `repeat` + `agent turn` closes the
square in one loop

**Covered last time (2026-08-29)**
- A `repeat 4 times` loop
- Agent move forward, agent turn left
- Placing fence and flower blocks with the agent
- The `agent place on move` setting
- A custom function that planted 7 different flowers in a row
- Putting items into the agent's inventory by hand
- ✓ Solved the last fence gap alone — worked out that the final `move back 1`
  belongs **outside** the repeat block
- △ **Mixed up which way the agent is facing versus which way it moves**, and
  mixed up turning with moving

**Promised:** nothing recorded.

**What today teaches**

Dewy has already met `repeat`. Today the loop stops being four repeats of a
straight line and becomes a shape: **forward + turn inside the same loop**.

Ramp it:

1. **Warm-up, short** — the fence from last week, and the one block that was
   outside the loop. One slide, then move on.
2. **v1** — the square fence written the long way: forward, turn, forward, turn,
   forward, turn, forward, turn. Drawn as blocks, the repeating pair circled.
3. **v2** — `repeat 4 times` around **forward + turn together**. Four blocks
   become two. Draw one frame per pass on a grid, with an arrow showing which way
   the agent faces after each turn — **this is the △, so it gets the picture.**
4. **v3** — change the repeat count to 3 and the shape opens. Change it to 6.
   The number of turns decides the shape.
5. **v4** — `agent place on move [ON]` above the loop so the square draws itself
   in fence.
6. **Then push past it:** a `size` variable that grows each pass, turning the
   square into a spiral · a `repeat` inside a `repeat` to fill the square ·
   turning right instead of left and predicting the mirror shape · a flower at
   each corner using the block he already knows.

**Facing versus moving is the whole △ and needs a dedicated visual**: a top-down
grid, the agent as an arrow, one frame per block, the arrow rotating on `turn`
and sliding on `move`. A `turn` slide where the agent does not change square at
all is the clearest way to show it.

---

## 20:45 KST · 18:45 HCMC · ANDY — `andy-many-things-at-once.html`

**Track:** IDE Python, **Manim** (the tracker still stores `WD002` /
`JAVASCRIPT` — that is a stale join key, ignore it) · **Source:** log + draft
2026-08-29
**Topic (Kasim: "Andy IDE Python (Manim)"):** several animations in one
`self.play`, grouping with `VGroup`, holding a frame with `self.wait`

**Covered last time (2026-08-29)**
- Manim structure: `Scene`, `construct`, `self.play`
- `Circle()` — colour, radius, `.set_fill()` for fill colour and opacity
- Hex colour codes (`#00FFFF`, `#0A1128`)
- `Square()` and `Transform()` — circle turning into a square
- `Text()`; `.animate.shift()`, `.animate.rotate()`, `.animate.scale()`,
  `.animate.move_to()`
- Chaining animation methods for one compound move
- ✓ Spotted that a circle animation did not close fully, checked it on the
  timeline scrubber
- ✓ Predicted that a negative shift moves text downward, then tested it
- △ Needed repeat guidance on **why `.animate` is required**
- △ `move_to()` uses Manim units, not pixels — kept expecting pixels

**Promised (2026-08-22, older):** "Andy types code first, help only when
needed. Practice autocomplete to build method-name familiarity." Standing
teaching instruction — **keep hands off the keyboard**, not a topic.

**What today teaches**

So far every `self.play` has animated one thing. Today one line moves three.

Ramp it:

1. **v1** — his scene as it stands: one circle, one `self.play`, one `.animate`.
2. **v2** — three mobjects made and placed with `.shift()` (no animation yet), so
   there is something to move together.
3. **v3** — **several animations inside one `self.play(a, b, c)`** — they all run
   at the same time. This is the lesson.
4. **v4** — `VGroup(a, b, c)` and one `.animate` on the group. The whole row
   moves as one object.
5. **v5** — `self.wait(1)` between plays, and `run_time=` on a play, so timing
   becomes something he sets rather than something that happens.
6. **Then push past it:** `LaggedStart` so they start one after another ·
   `FadeIn` / `FadeOut` / `Create` / `Write` as animations that are not
   `.animate` · `.next_to()` for placing relative to another mobject ·
   `.arrange()` on a `VGroup` · `always_redraw` if there is room.

**Turn the △ into slots.**
- **Why `.animate`:** one slide with two lines side by side —
  `self.play(sq.shift(RIGHT))` (jumps, no animation) versus
  `self.play(sq.animate.shift(RIGHT))` (slides). Same picture twice, one arrow.
- **Units, not pixels:** a drawn Manim frame with the axis marked — the frame is
  8 units tall and about 14.2 wide, the centre is `0, 0`. `move_to([3, 0, 0])`
  lands on a marked spot. Never say "pixels".

**Standing instruction from `promised`:** Andy types. Every step slide should be
readable as an instruction to Andy, not a demo for Kasim.

**Reference deck:** `../2026-08-29/andy-manim-first-animation.html` — match its
variable names and its tone.
