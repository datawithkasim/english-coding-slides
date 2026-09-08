# Today's decks — 2026-09-08 (Tue)

Times are Korea first, Ho Chi Minh second (KST − 2).

**Calendar is the source of truth for times.** Tracker drift is noted, never fixed here.

Four lessons today. Kasim confirmed the list and the platform for each:

| KST | HCMC | Student | Platform |
|---|---|---|---|
| 16:00 | 14:00 | RIO | Minecraft Python |
| 18:00 | 16:00 | HWON | Python / Pygame |
| 19:00 | 17:00 | JASON | Python / Pygame (app IDE) |
| 20:00 | 18:00 | LEO KIM | Minecraft Python |

**Not today, do not build:** JIYU (Kasim dropped her from today's list) ·
DAVID G8 (moved to Sunday 19:00, taught 2026-09-06) · YURA G5 (Saturday, taught
2026-09-05). The tracker still lists all three on Tuesday. Report only.

## Hard rules for every deck

Read first, in this order:
1. `../../TEMPLATE.md` — slot structures and per-slide rules
2. `../../PEDAGOGY.md` — why each slot exists
3. `../../assets/style.css` — the only styling allowed
4. That student's own most recent deck, named in their section — tone and markup reference

Then:
- Save to `lessons/2026-09-08/<file>.html`. Stylesheet `../../assets/style.css`,
  script `../../assets/deck.js`.
- **Overshoot hard.** The deck must hold far more than one lesson can get through.
  No slide ceiling, no slide target. If the teacher could plausibly reach the last
  slide inside the hour, it is too short — go back and add taught ideas. Extra room
  goes on **new concepts with a visual each**, never on more debug cards.
- Per-slide caps: **≤ 40 English words, ≤ 15 Korean words.**
- **One change per slide**, numbered `STEP n / total`. A re-indent is its own step.
- Every code step carries all five:
  **the code** (full OLD block and full NEW block, never `...` inside a changed region) ·
  **🔍 FIND** the exact Ctrl+F string ·
  **📍 where** — quote the existing line it goes under, and the indent count ·
  **🟣 why**, one line ·
  **✅ check**, one line (what running it should show).
- Big programs ramp **v1 → v2 → v3 → v4**. Never the finished program first. New
  lines hot, unchanged lines dim, changed lines get an explicit OLD/NEW block.
- **Visuals are mandatory for loops, iteration and any maths** — one frame per pass
  with the counter value shown; spacing as boxes on a number line; x positions as jumps.
- Only reuse existing CSS classes (`.var-fill`, `.viz-reassign`, `.viz-if`, `.viz-3`
  and friends). No new inline component styling.
- Update the `counter` span to `1 / <total>`.
- **Every deck teaches at least one new idea** — the one named in its section. A
  homework check or a revisited mistake is the warm-up that leads into it, never the
  whole lesson.
- **The carry slides listed in each section come across verbatim.** Today's deck is
  built on top of them, not instead of them.

### Minecraft API form (RIO and LEO only)

Constant form, always: `blocks.fill(QUARTZ_BLOCK, pos(1, 0, 1), pos(6, 0, 1), REPLACE)`,
`player.on_chat("towers", towers)`. **Never** string names like `"quartz_block"`.

**Axis rule, confirmed from RIO's own 1 Sept transcript and never to be paraphrased
the other way:** `pos(x, y, z)` — x across, y up, z forward. **y counts from 0.
x and z count from 1.** Do not write "coordinates start at 0" for all three; that is
the exact thing RIO was corrected on.

---

## 16:00 KST · 14:00 HCMC · RIO — `rio-loops-do-the-counting.html`

**Track:** MS002, Minecraft Python · **Source:** Drive transcript 2026-09-01
(doc "Meeting started 2026/09/01 14:00 GMT+07:00"), speaker label `GA BI CHO`.

**Reference deck for tone and markup:** `../2026-09-01/rio-x-before-y.html`

### What he actually did last lesson (from the transcript, not the log)

- Named the three axes off the screen share: green = y, purple = z, red = x.
- Settled the counting rule: **y starts at 0, x and z start at 1.**
- Wrote `blocks.fill` inside `player.on_chat` and built a flat square from
  `pos(1,0,1)` to `pos(6,0,1)`.
- Made it taller by changing **only the second number** — he chose the end y himself.
- **Wrote a second `blocks.fill` line in the same chat command** so two shapes build
  at once, instead of retyping numbers over an old line.
- Finished a five-fill complex shape, working out each range himself.
- Debugged: a missing closing parenthesis on line 4, and `pos` sitting in front of the
  numbers instead of wrapping them.

**✓ Wins** — worked out the y height (4 blocks) unaided · found the x start/end (2 to 3)
unaided · spotted the missing parenthesis fast and fixed it · counted a long strip
(1…18) out loud without help.

**△ Watch** — he still narrates coordinates as three loose numbers ("one zero one")
rather than as `pos(x, y, z)`. Keep the three-slot picture on screen.

**Unmet last week:** nothing. He finished what was set.

**Homework he was sent:** the "alien pyramid" — build a shape from left-view,
right-view and top-view drawings, reading x, y and z off each view.

### Today's new idea — this is what Kasim promised him out loud

At 00:35–00:37 of that transcript Kasim told RIO, in these words, what today is:

> "Instead of you typing in numbers manually, I'm going to give you variables. So we're
> going to say, for example, x is equal to six. And then instead of us writing six, we're
> going to write x. And then we're going to loop our code. And then every time we loop we
> can say, oh, increase x by two."

So today is **a variable inside `pos()`, then a `for` loop that changes it.** Nothing else.

Build it as a ladder:

- **v1 — the variable exists.** `x = 2` above the fill, then swap the literal `2` in
  `pos()` for `x`. Run it. Same tower, different code. Prove the swap changed nothing.
- **v2 — change the variable, change the build.** Set `x = 5`, run again. One number
  edited at the top moved the whole tower. This is the payoff slide; give it a visual
  of the one edit rippling into the build.
- **v3 — `for i in range(5)`.** The same fill line indented inside the loop. It builds
  five towers in the *same place*, one on top of the other. **This failure is the point** —
  show it, then ask why.
- **v4 — `x = x + 3` inside the loop.** Now five towers march across. Mandatory visual:
  **one frame per pass**, five frames in a row, each showing `i` and the value of `x`
  before and after the add. Boxes on a number line — 2, 5, 8, 11, 14.
- **v5 — spacing as its own variable.** `spacing = 3`, then `x = x + spacing`. Change
  spacing to 1 and to 6 and show both skylines.
- **v6+ — overshoot room, spend it on new taught ideas:** the loop counter `i` used
  *inside* `pos()` so towers get taller as they march (`pos(x, 0, 1)` → `pos(x, i, 1)`);
  then a second variable changing at a different rate; then `range(start, stop)`.

**He has never seen a loop in Python.** Kasim confirmed it in the transcript
("I don't think I have ever taught you about loops? Not in Python"). He *has* seen loops
in block coding. So the loop needs its own plain-words slide before any code: a loop is
"do this line again, this many times", and the counter is a box whose number changes.

**Indentation gets its own STEP slide.** Pushing the fill line in is one change, on one
slide, with the indent count spelled out.

### Debug slides (4+)

1. The update line `x = x + 3` written **outside** the loop, so all five towers stack in
   one place — his most likely mistake, and the exact one LEO made on the same idea.
2. `x = 3` instead of `x = x + 3` inside the loop — resets every pass, one tower.
3. `range(5)` expected to count 1–5, actually counts 0–4 — number-line visual.
4. A missing colon after `for i in range(5)` — he missed colons and parentheses last week.
5. OPTIONAL: `pos` written in front of the brackets instead of wrapping the numbers —
   his real 1 Sept bug.

### Code Talk Frame

"`x` starts at ___. Each time round the loop, `x` becomes ___ plus ___. After ___ turns
`x` is ___." Make him read it aloud on every build, not once.

### Carry from last week

`../2026-09-01/rio-x-before-y.html` — **33 slides, reached about slide 28.** The lesson
covered the whole teaching body. Only the wrap-up tail was unreached: "Three slots, three
jobs", "Two questions", "Build it 🚀", "Bonus rungs", "One last count". Carry the
**"Three slots, three jobs"** slide across verbatim as today's warm-up — it is the
`pos(x, y, z)` picture he still needs. The rest of the tail is spent; do not re-teach the
body.

---

## 18:00 KST · 16:00 HCMC · HWON — `hwon-walls-then-the-bread.html`

**Track:** RS003, Python / Pygame · **Source:** log 2026-08-25.

**Reference deck for tone and markup:** `../2026-09-01/hwon-four-walls-and-the-bread.html`

### ⚠ Read this first — the whole of last week's deck is carry

**HWON has no lesson transcript since 2026-08-25 — 14 days.** There is no Drive doc
anywhere near his 18:00 KST slot on 1 Sept. The deck built for him that day,
`../2026-09-01/hwon-four-walls-and-the-bread.html`, **was never opened. All 30 slides are
unused.**

So today's deck is that deck, **carried across verbatim as its opening body**, with new
taught ideas built on top of it. Do not rewrite those 30 slides. Do not re-plan them.
Read that file and carry it.

### What he actually did on 2026-08-25

- The event loop and the quit button (`pygame.event.get()`, `pygame.QUIT`)
- `pygame.key.get_pressed()` with `K_RIGHT` / `K_LEFT` / `K_UP` / `K_DOWN`
- Four-direction movement: `x` / `y` plus or minus `speed` every frame
- Boundary conditionals; **y counts DOWN from the top**; the right wall needs
  `WIDTH - width`
- Screen resized to 800 × 800

**✓ Wins** — explained x/y = position and w/h = size the moment he was asked. Wrote the
UP/DOWN key blocks himself after seeing the LEFT/RIGHT pattern.

**△ Mistakes the deck exists because of**
- **The y-axis direction (0 at the top) is still shaky** after several explanations.
- **Wrote the right boundary as `x > 800`** — forgot `x` is the left edge. Fixed only
  after a diagram.
- **The down wall was left as a copy of the up wall** at the end of the lesson.

**Unmet last week:** the down wall was never fixed, and the right wall still hardcodes
800 instead of using `super_dario['w']`. Both were his homework. **This is the strongest
input to today** — it is two weeks old now.

**Homework he was sent:** walls worksheet — find and fix the down wall, make the right
wall use `super_dario['w']`.

### Today

**Body (carried verbatim from the 09-01 deck, 30 slides):** four walls one edge at a
time, then the bread and `colliderect`. The mandatory y-axis visual — the 800×800 screen
with `y = 0` at the TOP and an arrow pointing DOWN labelled "y gets bigger" — goes early
and is reused on every wall slide.

**New ideas built on top — this is where the overshoot goes.** After the bread is eaten:

- **v5 — a score that goes up.** `score = 0`, `score += 1` inside the collision `if`.
- **v6 — draw the score on screen.** `pygame.font.Font`, `render`, `blit`. Give the font
  object its own STEP slide, created once *before* the loop, never inside it.
- **v7 — the bread respawns somewhere new.** `random.randint` for the x and y, kept
  inside the screen by subtracting the bread's width.
- **v8 — many breads, one list.** `breads = []`, a `for` loop that draws each one, and
  the same `colliderect` check inside the loop. **Iteration visual mandatory:** one frame
  per bread, showing which one is being checked.
- **v9+ if room:** a timer counting frames down, and a "GAME OVER" screen when it hits 0.

### Debug slides (4+)

1. `x > 800` instead of `x > WIDTH - width`, so half of Dario leaves the screen.
2. The down wall still checking `y < 0` — his exact homework bug. Show it on the y-axis
   diagram so the direction is visible, not just stated.
3. `colliderect` written without `()` so it never fires.
4. The bread respawn placed outside the `if`, so it teleports every frame.
5. The font created inside the game loop, so the game crawls.

### Code Talk Frame

"`y = 0` is the ___ of the screen, so bigger `y` means ___." And: "`x` is the ___ edge,
so the right edge is `x` plus ___."

---

## 19:00 KST · 17:00 HCMC · JASON — `jason-land-on-the-platform.html`

**Track:** RS003, Python / Pygame, app IDE · **Source:** Drive transcript 2026-09-01
(doc "Meeting started 2026/09/01 16:59 GMT+07:00"), speaker label `김동욱`.

**Reference deck for tone and markup:** `../2026-09-01/jason-pick-the-next-project.html`

⚠ **Slot correction:** the tracker says 17:00 KST. It is wrong and stale. The calendar,
the Kakao thread (mother chose 화요일 7시 on 12 Aug, confirmed 18 Aug as Korea time) and
the transcript start time all say **19:00 KST**. Do not use 17:00 anywhere.

### What he actually did last lesson

Started a brand-new platformer file from scratch:

- `screen.fill()` takes an **RGB colour**, not sizes — he first guessed "a square".
- `WIDTH` / `HEIGHT` as variables replacing hardcoded 800 / 600.
- `GRAVITY = 0.6` added to `vy` every frame; `vy` then added to `y`.
- **Reasoned the sign himself:** y = 0 is the top, so jumping is negative `vy`, falling
  is positive.
- Traced the physics frame by frame out loud — worked out `vy` at frame 2 (−10.8),
  `y` at frame 2 (267.6), and that `vy` hits 0 at frame 20.
- Player attributes gathered into a **dictionary**: `x`, `y`, `w`, `h`, `vy`,
  `on_ground`, `speed`.
- Ground collision: `if player["y"] >= GROUND_Y` → snap to `GROUND_Y`, `vy = 0`.
- Jump on `pygame.KEYDOWN` + `K_SPACE`, and *why* KEYDOWN and not `get_pressed` —
  holding space would fly.
- Left / right with `player["speed"]`.

**✓ Wins** — got the negative-jump reasoning unprompted · did the frame-by-frame
arithmetic correctly · read `if player["y"] >= GROUND_Y` back in his own words.

**△ Watch** — repeated syntax slips (missing commas, `:` vs `=`), and he waits to be told
where code goes rather than looking for a similar line first.

**Unmet last week — say it plainly, it is today's opening:** the ground platform was
added and drawn, **but it does not appear at the ground.** Kasim's own closing words:
"it's not the ground, right. Okay, we'll work on this next time. Well, maybe for your
homework." Gemini logged it as the single next step: *Fix Ground*.

### His live file, read from the app IDE this morning

His workspace `main.py` is the homework starter and **is untouched — none of the three
planted bugs are fixed.** Build from exactly this. Quote these lines when you write the
🔍 FIND strings; they are real.

```python
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player["x"] -= player["speed"]
        if keys[pygame.K_RIGHT]:
            player["x"] += player["speed"]
        player["vy"] += GRAVITY

        ## CONTROLS ##
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player["on_ground"]:
                player["vy"] = JUMP_POWER
                player["on_ground"] = False

    player["vy"] += GRAVITY
    player["y"] += player["vy"]

    if player["y"] >= GROUND_Y:
        player["y"] = GROUND_Y
        player["vy"] = 0
        player["on_ground"] = True

    screen.fill(GRAY)

    pygame.draw.rect(screen, GOLD, (player["x"], player["y"], player["h"], player["w"]))
    pygame.draw.rect(screen, GREEN, (ground_platform["x"], ground_platform["y"], ground_platform["h"], ground_platform["w"]))
```

The three live bugs, in the order the worksheet sets them:
1. **Gravity is added twice** — once inside the event loop, once after it. He falls at
   double speed.
2. **Left / right only work when an event happens** — `get_pressed()` sits inside
   `for event in ...`, so movement stutters and stops when the mouse is still.
3. **Width and height are swapped in both draw lines** — `player["h"], player["w"]` and
   `ground_platform["h"], ground_platform["w"]`. **This is why the green platform looks
   wrong**: 16 wide × 140 tall instead of 140 wide × 16 tall. Bug 3 *is* the unmet
   promise. Land that connection explicitly on its own slide — he has been staring at it
   for a week.

### Today's new idea

**Landing on a platform instead of falling through it.** The ground check he already has
is one line comparing to one number. A platform check compares four things: is he
overlapping it left-to-right, and is he crossing its top this frame, and is he moving
down.

Ramp:

- **v1** — the three bugs fixed, one per STEP slide, run after each. Warm-up only.
- **v2** — the platform check, written out long-hand with `and`, in one `if`. Mandatory
  visual: the player rect and the platform rect side by side, four arrows, one per test.
- **v3** — `vy > 0` added, so he can jump up *through* a platform but land on top.
  Show both cases as two frames.
- **v4** — **one platform → a list of platforms.** `platforms = [ {...}, {...} ]`, a
  `for p in platforms:` loop drawing each, and the same landing check inside the loop.
  **Iteration visual mandatory:** one frame per platform, showing which one is being
  tested and whether it catches him.
- **v5** — three platforms with a gap, so missing one means falling past.
- **v6+ overshoot, new taught ideas:** tap = small hop / hold = big jump (cut `vy` on
  KEYUP) · coyote time, six frames of mercy after leaving an edge · a platform that
  patrols left and right and carries him · fall off the bottom and restart.

Slides 16–37 of `../2026-09-01/jason-pick-the-next-project.html` already teach v4, v5 and
v6. **Carry them across verbatim** and build the new v1–v3 in front of them.

### Debug slides (4+)

1. The landing check without `vy > 0`, so he sticks to the underside of a platform.
2. `and` written as `&&`.
3. The landing check placed outside the platform loop, so only the last platform works.
4. `platforms` looped with `for p in range(platforms)`.
5. OPTIONAL: `=` where `==` was meant, inside the `if`.

### Code Talk Frame

"He lands if his ___ is past the platform's ___, **and** his ___ is inside the platform's
___ to ___, **and** his `vy` is ___."

### Carry from last week

`../2026-09-01/jason-pick-the-next-project.html` — **37 slides, reached about slide 15**
("One platform"). **Slides 16–37 are unreached and come across verbatim:** one platform →
a list of them, loop the check, three platforms and a gap, which one catches him, tap vs
hold, let go early jump lower, coyote time, six frames of mercy, moving platform, the
platform slides out from under you, what if you miss, fall off start again. This is the
biggest carry of the day — do not rebuild it from nothing.

---

## 20:00 KST · 18:00 HCMC · LEO KIM — `leo-one-loop-two-jobs.html`

**Track:** Minecraft Python · **Source:** Drive transcript **2026-09-06** (Sunday, doc
"Meeting started 2026/09/06 16:00 GMT+07:00"), speaker label `Dongha Kim`.

**Reference deck for tone and markup:** `../2026-09-06/leo-remainder-patterns.html`

⚠ **His most recent lesson is Sunday 6 Sept, not Tuesday 1 Sept.** He is taught twice a
week. Do not build from the Fibonacci lesson — that is two lessons ago and it is done.

### What he actually did on Sunday

- Reviewed `for i in range(...)` and confirmed that `range(10)` stops at 9.
- Put a **list** of six colours into the function — red, orange, yellow, green, blue,
  purple.
- **`i % 6` to cycle the colours** — the remainder picks the index, so the list repeats
  forever however long the loop runs.
- Pushed `range` up to 30 and watched the pattern repeat.
- Read the output back: red, gold, green and purple pillars repeating every 4 blocks.

**✓ Wins** — read the repeat length off the build himself.

**△ Watch** — he goes quiet in English when he is stuck rather than saying what broke.
Kasim's own next step for him: practise saying the problem out loud. Put the
**"three things to say when stuck"** slide in early, same as the 09-06 deck.

**Unmet last week:** nothing recorded.

**Fibonacci and `%`-for-colour are both DONE. Do not teach either again.**

### Today's new idea

**One `%` doing a second job — `%` deciding something other than colour.**

Ramp:

- **v1** — his Sunday code back on screen, running. Warm-up, one slide.
- **v2** — `if i % 3 == 0:` inside the loop, changing the **height** of every third
  tower. Mandatory visual: a row of towers with every third one marked, and a table of
  `i`, `i % 3`, and whether the `if` fires.
- **v3** — two remainders in one loop: `i % 6` still picking the colour, `i % 3` picking
  the height. Show that they line up every 6.
- **v4** — `if / else` so the non-third towers get their own height, not just the
  default.
- **v5** — `i % 2` for a stripe, and what changes when the two rules disagree.
- **v6+ overshoot, new taught ideas:** `%` on a *different* variable, not the counter ·
  `x % 5` to wrap a row of towers back to the start and begin a second row (this is the
  5 × 5 floor idea) · a nested loop, `for row` inside `for col`, so `%` is no longer
  needed for the wrap — and a slide saying plainly which of the two is easier to read.

### Debug slides (4+)

1. `i % 3 = 0` written with one `=` instead of `==`.
2. The `if` body not indented, so it runs every pass.
3. `i % 3 == 1` when he meant every third *starting from the first* — off-by-one, with
   the `i` / `i % 3` table beside it.
4. The height change written **after** the `blocks.fill`, so it applies one tower late.
5. OPTIONAL: `%` confused with `/`.

### Code Talk Frame

"`i` is ___. `i % 3` is ___. So the `if` is ___, and this tower is ___."

### Carry from last week

`../2026-09-06/leo-remainder-patterns.html` — **65 slides, reached about slide 45.** The
lesson got through the list, the index picture, `i % 6`, the crash when the index runs
past the end, bracket placement, and the rainbow build. **Unreached and carried across
verbatim:** "Stone or gold?", "It will not even run", "A 5 × 5 floor, turned sideways",
"One cycle, two jobs", "Mark every third tower". Note that **"Mark every third tower" and
"One cycle, two jobs" are exactly today's new idea already drafted** — carry those slides
in and build the ramp around them rather than writing them again.
