# Today's decks — 2026-09-04 (Fri)

Four lessons. **Three are Minecraft BLOCKS (MakeCode), one is the first ever
debate class.** 16:00 → 21:00 Korea time.

**Kasim gave no topic overrides this morning, so every topic below is the Idea
line read back to him and not objected to.** `promised` is empty for all three
coders, so there is nothing it could override.

| Time | Student | Track | Topic | Deck |
|---|---|---|---|---|
| 16:00 KST · 14:00 HCMC | JUNWOO | MC **Blocks** | a `repeat` around `fill` — one block draws row after row | `junwoo-one-repeat-many-rows.html` |
| 18:00 KST · 16:00 HCMC | NELLIE | MC **Blocks** | agent `place on move` inside a `repeat` — the loop places, not her hands | `nellie-the-agent-does-the-placing.html` |
| 19:00 KST · 17:00 HCMC | IAN KIM (`_loha2018`) | MC **Blocks** | a variable that grows inside the `repeat` — square becomes a spiral | `ian-kim-the-square-that-grows.html` |
| 21:00 KST · 19:00 HCMC | LUCY & AMBER | **Debate DB001** | Week 1 — AI and homework · claim + reason | `../../debate/db001-tech-ai/week-01.html` (existing, reused) |

**Cancelled / moved today, no deck:**
- JADEN [PH] 17:15 KST — taking a break, class next week instead.
- DAVID P [USA] 22:00 KST — moved to Sunday. Tracker still says Friday.
- JIYU [TASHKENT_LAMU] 21:00 KST — tracker row, no calendar event, never taught.

---

## Hard rules for every deck

Read first, in this order:
1. `../../TEMPLATE.md` — the slot structure and per-slide rules
2. `../../PEDAGOGY.md` — why each slot exists
3. `../../assets/style.css` — the only styling allowed
4. The reference deck named in that student's section below, for tone

Then:
- Save to `lessons/2026-09-04/<file>.html`. Stylesheet `../../assets/style.css`,
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

### Shape of the hour
Short recap of last week, then **most of the hour on the new idea**. A deck that
spends half the hour on last week is a failed deck.

### Copy-this-and-it-works contract
The student makes **zero decisions**. If a slide needs the student to infer
anything, it is wrong.

- **One change per slide**, numbered `STEP n / total`.
- Every step carries all five:
  - **the blocks** — full OLD stack and full NEW stack, never `…` inside a changed region
  - **🔍 FIND** — the exact block to look at (block track: name the block, not a search string)
  - **📍 where** — which block it goes inside or under, quoted
  - **🟣 why** — one line
  - **✅ check** — one line: what running it should show
- **Big builds ramp v1 → v2 → v3 → v4.** Never the finished build first. New
  blocks `.hot`, unchanged blocks `.dim`, changed blocks get an explicit OLD/NEW pair.

---

## BLOCKS TRACK — applies to all three coding decks today

**All three students today drag MakeCode blocks. Kasim confirmed this morning.**

**Zero Python anywhere.** Not in a code block, not in a debug card, not in a
comment, not in a heading. The tracker logs for these three are written in
Python-ish text (`blocks.fill`, `agent.move("forward", n)`) because they are AI
summaries of a recording — **that is not what these students see or type.**
Redraw every one of those ideas as a block.

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
already match this table; the `.mcb-from .drawer` inline hex does **not** in
older decks, so type it from here:

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

### Coordinates rule — all three block decks

**y starts at 0. x and z start at 1.** The first free square is `~1 ~0 ~1`.

Never write "coordinates start at 0" as one blanket rule. **JUNWOO was taught
exactly that wrong rule on 28 Aug and it is the thing he kept getting confused
about** — his deck must correct it explicitly, and the other two must not repeat
it. Counting a range is unchanged either way: end minus start, then add 1.

### Reference decks for tone (blocks)
- `../2026-09-02/seohoo-pixels-with-a-loop.html`
- `../2026-09-02/ihyeon-maze-first-turn.html`
- `../2026-09-03/jj-the-growing-staircase.html`
- `../2026-09-03/seohyeon-loop-inside-a-loop.html`

---

## Transcript note — all three coders

**There is no Gemini transcript for Friday 28 August.** Drive jumps from 26 Aug
straight to 29 Aug, so the recording was off. The lesson log and the log draft
for 28 Aug are identical for all three students, so the facts below stand — but
nothing was cross-checked against a recording.

No ledger file exists for any of the three, so there is no `gap` and nothing
recorded as promised-and-missed.

---

## 16:00 KST · 14:00 HCMC · JUNWOO — `junwoo-one-repeat-many-rows.html`

**Track:** MS002, Minecraft **BLOCKS** · **Source:** log + draft, 2026-08-28
**Topic:** a `repeat` around `fill` — one block draws row after row

**Covered last time**
- The `fill` block: pick a start position, an end position, a block type
- Counting along x (left to right) and up y (bottom to top)
- Pixel art on a wall: a skeleton, then a creeper face
- Swapping the block type: grass block, diamond ore, obsidian
- ✓ Given the hint "1 to 15", counted it himself and filled a 15×15 grid green
  in a single `fill`
- ✓ Caught his own missed colour change when asked, fixed it, ran it again
- △ **Needed the coordinate rule re-explained again and again.** He was told
  "coordinates start at 0", which is wrong, and that is very likely why it never
  stuck.
- △ Struggled to count one grid square on the creeper's mouth; Kasim added
  visual markers on the wall to help

**Promised:** nothing recorded.

**What today teaches**

Right now every row of his pixel art costs him one `fill` block. Fifteen rows,
fifteen blocks dragged. Today one `repeat` block does all fifteen.

Build it in this order, each as its own ramp version:

1. **v1** — the `fill` he already knows, one row, drawn as blocks.
2. **v2** — a `repeat 4 times` wrapped around it. Same row four times, in the
   same place. Ask what went wrong *before* showing the fix: nothing moved,
   because nothing changes between passes.
3. **v3** — make a variable (call it `row`), set it before the loop, and use the
   variable oval in the y hole instead of a typed number.
4. **v4** — `change row by 1` inside the loop. Now each pass draws one row
   higher. This is the whole lesson.
5. **Then push past it:** `repeat 15 times` for the full grid · changing the
   block type per pass so the wall stripes · a second variable for width ·
   two `repeat`s nested to fill a square without counting anything.

**Mandatory visuals**
- The coordinate correction gets its own slide with a drawn wall: y labelled
  from 0 up, x labelled from 1 across. Contrast it against the wrong "all start
  at 0" rule with a ✗.
- **One frame per loop pass** for the `repeat` — show the `row` oval's value and
  which row lights up on the wall, pass by pass. Use `.viz-3` / `.viz-4` /
  `.viz-5` (the `.iter-item` and `.out-line` counts must match the nth-child
  selectors or the animation dies).
- His creeper-mouth counting problem becomes a "count the range" slide with the
  squares drawn and numbered, plus the end−start+1 rule.

**Debug slots — use his own real errors, not invented ones**
- Forgetting `change row by 1`, so all fifteen rows land on top of each other.
- Counting a range as end−start and being one short.
- Assuming y starts at 1.

---

## 18:00 KST · 16:00 HCMC · NELLIE — `nellie-the-agent-does-the-placing.html`

**Track:** MS002, Minecraft **BLOCKS** · **Source:** log + draft, 2026-08-28
**Topic:** agent `place on move` inside a `repeat` — the loop places, not her hands

**Covered last time**
- `fill` with a coordinate range across x, y and z
- A rainbow tower: red, orange, yellow, green, blue, purple, pink wool layers
- That a range of 0, 1, 2 is three numbers
- Building layer by layer, working out the start and end position of each layer
- `air` blocks to hollow out the inside of a structure
- First look at the agent: move forward, turn left, a `repeat` of 7, and giving
  the agent items so it can place blocks
- ✓ **Saw the pattern from the first two demoed layers and wrote the remaining
  five herself**, coordinates correct (3–5, 6–8, …)
- △ **Kept trying to place the agent's blocks by hand** — picked up a fence and
  placed it manually instead of coding the loop to do it

**Promised:** nothing recorded. (Her 21 Aug promise, the rainbow tower, was
delivered on 28 Aug. Nothing outstanding.)

**What today teaches**

Her △ is the whole lesson. She already understands the agent moves. What has not
landed is that the agent can *place while it moves*, so her hands never touch a
block again.

Build it in this order:

1. **v1** — the agent she saw last week: `agent move forward 7` inside a
   `repeat`, drawn as blocks. It walks and leaves nothing behind.
2. **v2** — `agent set block` to choose what it carries (start with wool so it
   is visible), then `agent place forward` once. One block appears. Slow.
3. **v3** — `agent place on move ON`. Now `agent move forward 7` leaves a trail
   of 7 blocks. **This is the moment the lesson turns.** Give it an animation:
   the agent walking, a block dropping behind each step.
   (Block label is `agent place on move [ON]` — that is what 92 shipped block
   slides already use. `set_assist(PLACE_ON_MOVE, True)` is the Python-track
   form and must never appear on this track.)
4. **v4** — wrap move + turn in `repeat 4 times`. A closed square wall, zero
   hand placement.
5. **Then push past it:** changing the wool colour between sides so each wall is
   a different colour · `agent move up` and a second lap to stack a second
   course of blocks · a rainbow tower rebuilt with the agent instead of seven
   `fill` blocks, which ties straight back to what she did last week ·
   `repeat` inside `repeat` to raise the wall to any height.

**Mandatory visuals**
- A side-by-side: her hand placing one block vs the agent's trail. This is the
  hook and it must be the first thing she sees.
- **One frame per pass** of the `repeat 4` square — the agent's position and
  facing, and the wall growing. `.viz-4`.
- A top-down grid showing why the agent cannot place a block on the square it is
  standing on, and that moving first fixes it.

**Debug slots — her own real errors**
- Placing by hand and then wondering why the code did nothing.
- `place on move` left OFF, so the agent walks and leaves nothing.
- Forgetting `agent set block`, so the agent has nothing to place.
- The square not closing because the turn is outside the `repeat`.

---

## 19:00 KST · 17:00 HCMC · IAN KIM (`_loha2018`) — `ian-kim-the-square-that-grows.html`

**Track:** MS000, Minecraft **BLOCKS** · **Source:** log + draft, 2026-08-28
**Topic:** a variable that grows inside the `repeat` — the square becomes a spiral

**Covered last time**
- `agent place on move` so blocks appear while the agent walks
- `agent set item` to choose what it carries: fence, flowers, bamboo
- `agent move forward n` combined with `agent turn left`
- A `repeat 4 times` loop around the forward-then-left pattern
- Inside vs outside the loop: what repeats and what runs once
- That the agent cannot place a block on its own square; the fix is to move
  forward or up by 1 first
- ✓ **Explained inside vs outside the loop in his own words:** "inside does it
  together, outside doesn't"
- △ Kept typing the chat word without pressing play first, so nothing ran

**Promised:** nothing recorded.

**What today teaches**

He can build a square. Every side is the same length because the number in the
`move forward` hole is typed and frozen. Today that number becomes a variable
that grows each pass, and the square opens into a spiral.

Build it in this order:

1. **v1** — his square from last week: `repeat 4` around move forward 5 + turn
   left. Drawn as blocks, all `.dim` — this is the thing he already owns.
2. **v2** — make a variable `side`, `set side to 2`, drop the oval into the
   `move forward` hole. Same square, but now one number controls it. Change 2 to
   6 and watch every side change at once. **This is the idea, before any growth.**
3. **v3** — `change side by 1` inside the `repeat`. Each side is one longer. Run
   `repeat 4` — it no longer closes. Show that, name it, do not call it a bug.
4. **v4** — `repeat 20` instead of 4. A spiral. This is the payoff slide and it
   gets an animation.
5. **Then push past it:** `change side by 2` for a faster spiral · `set side to
   20` with `change side by -1` for a spiral winding inwards · changing the item
   with `agent set item` inside the loop so the spiral changes colour as it goes
   · `agent move up 1` before each lap to spiral upward into a tower.

**Mandatory visuals**
- **The variable box.** Use `.var-fill` for `set side to 2`, and `.viz-reassign`
  for `change side by 1` — the box value visibly swapping is the point.
- **One frame per pass** of the spiral: pass number, the `side` value, the
  length of the line just drawn. `.viz-5`. Without this the spiral is magic.
- Inside vs outside the loop is his own win — recall it with a two-column
  drawing (`change side by 1` inside vs outside) and let him predict which one
  spirals. Reward, not revision.

**Debug slots — his own real errors**
- Not pressing play before typing the chat word. Put this early and make it a
  habit slide, not a telling-off.
- `change side by 1` dropped outside the `repeat`, so every side stays equal.
- Never setting `side` at the start, so it carries the value from the last run.
- The spiral drawing over itself because the agent placed on its own square.

---

## 21:00 KST · 19:00 HCMC · LUCY & AMBER — debate, first ever class

**Not a new deck. Reuse `../../debate/db001-tech-ai/week-01.html` as it is.**

It was generated from the course's own build script; a hand-built replacement
would drift from the sixteen-week system.

**Course:** DB001 Tech & AI Debate, week 1 of 16. CEFR B1.
**Motion:** *Students should be allowed to use AI to help with homework.*
**Skill:** claim + reason. **Frame:** "I think ___ because ___."
**Rule set today and kept all term:** an opinion with no "because" doesn't count.

**Lesson shape** (from `dev/courses/tech_ai_debate/lessons/week-01.md`)
- Open on the picture: is the student working, or is the computer working? One
  sentence each, no correction yet.
- Teach claim and reason separately. Model on something harmless (dogs vs cats),
  then say an opinion with no reason and let them catch what is missing.
- Practise on easy prompts, not the motion — school start times, video games,
  winter vs summer. Correct the frame, never the opinion.
- Four Corners on the motion, 30 seconds defending your zone. Then ask each of
  them for the best reason on the *other* side. First taste of assigned sides.
- Close with errors on screen, no names. Show the homework.

**Vocabulary (teach cold — there is no week 0 behind them):** allow · cheat ·
effort · tool · depend on · practice · shortcut · honest · struggle · temptation

**Housekeeping**
- Lucy and Amber are **not in `tools_students`** and were **not in
  `roster.json`** before today. Two new folders were created this morning:
  `students/lucy-debate-fri-2100/` and `students/amber-debate-fri-2100/`, both
  marked `lesson_kind: "debate"`.
- `dev/courses/tech_ai_debate/resources/sentence-frames.md` and the week-0
  vocabulary list are meant to reach the students on KakaoTalk **before** week 1.
  Neither has been sent. Kasim's call.
