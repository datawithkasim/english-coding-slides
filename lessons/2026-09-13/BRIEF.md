# Today's decks — 2026-09-13 (Sun)

**Kasim's instruction this morning, verbatim: "use last transcript or their
current IDEs please."** So every topic below is taken from that student's own
Drive transcript of their most recent lesson, or from their live file in
`student_ide`, read SELECT-only. **No topic here comes from the tracker's
`promised` field**, and none comes from last week's deck. Each section names the
evidence its topic came from.

Times are Korea first, Ho Chi Minh second (KST − 2).

| Time | Student | Track | Topic | Deck |
|---|---|---|---|---|
| 08:00 KST · 06:00 HCMC | YUNGUN | IDE Python (pygame) | the food you can never reach, then a high score that survives, then the snake speeds up — **deck is all English** | `yungun-high-score-and-faster.html` |
| 10:00 KST · 08:00 HCMC | DIS (Cian, Leah, Danny) | Minecraft **Python** | land the loop inside a loop for all three, then `i % 3` makes the weird rainbow pattern | `dis-a-weird-rainbow-pattern.html` |
| 18:00 KST · 16:00 HCMC | LEO KIM | Minecraft **Python** | `//` — one loop fills a whole floor | `leo-one-loop-fills-the-floor.html` |
| 19:00 KST · 17:00 HCMC | DAVID G8 | IDE Python (text game) | the file does not run — one comma, then two names in one loop | `david-g8-two-names-one-loop.html` |
| 20:00 KST · 18:00 HCMC | LOGAN | IDE Python (pygame) | the wall you cannot walk through — `colliderect` | `logan-the-wall-you-cannot-cross.html` |
| 21:00 KST · 19:00 HCMC | CLAIRE | IDE Python (pygame) | damage first, then the boss health bar | `claire-damage-then-the-bar.html` |
| 22:00 KST · 20:00 HCMC | DAVID P | Minecraft **BLOCKS** | the upside-down pyramid, one `step` variable flips it | `david-p-upside-down-pyramid.html` |

**Not a lesson:** NO GI OPEN MATT, 14:00 KST · 12:00 HCMC. Left alone.

---

## Report-only drift — nothing was auto-fixed, no calendar event was renamed

The tracker lists only **5** students for Sunday. The calendar lists **7**, and
last Sunday's own BRIEF (`../2026-09-06/BRIEF.md`) also had 7. The calendar is
the roster truth.

- **DAVID G8** — calendar says Sunday 19:00. `tools_students` says **Tuesday
  21:00** and still has `lesson_kind = 'experience'`. Both stale; he is a
  regular Sunday student. Do not edit the tracker.
- **DAVID P [USA] M000** — calendar says Sunday 22:00. `tools_students` says
  **Friday 22:00**. His `roster.json` folder is `david-p-fri-2200`; the folder
  name is the join key, so leave it.
- **LOGAN** — calendar 20:00, tracker `slot_time` 19:00.
- **YUNGUN** — calendar 08:00, tracker `slot_time` 08:10. His calendar event is
  **one recurring series that fires on both Saturday and Sunday**, so he is a
  twice-weekly student. `roster.json` still stores `sat 20:00` / `sun 20:00`,
  both wrong.
- **LEO KIM** — calendar title is `LEO KIM [PH]` with two trailing spaces. That
  still matches on the whitespace-insensitive rule, so it is **not** a rename
  candidate. Left alone.
- **No ledger file** exists for YUNGUN, DIS, LOGAN or CLAIRE. Their facts below
  came from the Drive transcript plus the live IDE file instead.

## Transcripts — what was read for this brief

| Student | Doc (GMT+7 title) | Real date | Days ago |
|---|---|---|---|
| YUNGUN | `2026/09/12 06:09` | Sat 12 Sept | 1 |
| DIS | `2026/09/06 08:00` | Sun 6 Sept | 7 |
| LEO KIM | `2026/09/06 16:00` + `2026/09/08 18:00` | Sun 6 + Tue 8 Sept | 7 / 5 |
| DAVID G8 | `2026/09/06 17:00` | Sun 6 Sept | 7 |
| LOGAN | `2026/09/06 17:59` | Sun 6 Sept | 7 |
| CLAIRE | **none since 30 Aug** | Sun 30 Aug | **14** |
| DAVID P | `2026/09/06 20:00` | Sun 6 Sept | 7 |

**CLAIRE's 6 Sept lesson did not happen.** No recording exists at her slot, and
her `student_ide` file has not been saved since 30 Aug 13:19 UTC. Her 108-slide
deck from that day was built and never delivered.

---

## Hard rules for every deck

Read first, in this order:
1. `../../TEMPLATE.md` — the slot structure and per-slide rules
2. `../../PEDAGOGY.md` — why each slot exists
3. `../../assets/style.css` — the only styling allowed
4. The reference deck named in that student's section below, for tone

Then:
- Save to `lessons/2026-09-13/<file>.html`. Stylesheet `../../assets/style.css`,
  script `../../assets/deck.js`.
- **Overshoot on purpose.** No slide-count target and **no ceiling**. If the
  teacher could plausibly reach the last slide inside the hour, the deck is too
  short — add more taught ideas. Extra room goes to **new concepts with a visual
  each**, never more debug cards. Tag surplus `<span class="activity-tag">OPTIONAL</span>`.
- Update the `counter` span to `1 / <total>`.
- Per-slide caps: **≤ 40 English words, ≤ 15 Korean words**.
- Korean glosses only on Tier-3 vocab, concept hooks and bridges —
  **except YUNGUN, whose deck carries no Korean at all** (see below).
- Only reuse existing CSS classes. No new inline component styling.
- Slot 2 (Recap) recalls **that student's own last lesson**, from the facts in
  their section below. Never generic.
- The △ lines are what the student actually got wrong. Turn each into a Common
  Mistake or Debug slot rather than inventing a bug.
- **Every slide carries a visual.** A heading plus a bulleted list is not a
  finished slide.
- **Never gendered pronouns.** No he / she / his / her anywhere in a deck. Use
  the student's name or *they*.

### ALL ENGLISH — YUNGUN only, today

Standing instruction from Kasim, carried forward from `../2026-09-12/BRIEF.md`:
- `<html lang="en">`, no `<p class="bilingual">`, no `.ko` cells in a vocab
  table, no Korean in a pill, heading, bridge or closer.
- The vocab table keeps `term` + `gloss` and drops the `ko` column.
- Everything else about the deck is unchanged.

(The same instruction covers ANDY and Jaden Shin, who do not teach today.)

### Shape of the hour
Short recap of last lesson, then **most of the hour on the new idea**. A deck
that spends half the hour on last week is a failed deck.

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

### 🔴 FIND strings come from the live file, never from last week's deck

Four students' files **changed shape** since their last deck was written, so
copying a `🔍 FIND` string out of the old deck will send them hunting for a line
that no longer exists. Each section below pastes the real current lines. Use
those, verbatim, including any typo — **a typo in their file is a better anchor
than a corrected version**, because Ctrl+F has to match what is on their screen.

### The carry — read this before writing a single slide

Every student below has a **carry**: the slides of last lesson's deck the lesson
never reached. Decks are built to overshoot, so those slides are good, already
reviewed, and already in that student's voice.

- **Carry verbatim.** Copy the slide HTML across unchanged. Do not "improve" it.
- **Never carry** Slot 1 (title) or Slot 2 (Recap) — both are rebuilt from this
  week's facts.
- **Drop a carried slide whose code no longer matches the live file.** Several
  carries below are flagged `REWRITE ANCHORS` for exactly this reason — the
  teaching is good, the FIND string is dead.
- **Renumber after carrying:** the `counter` span, every `STEP n / total`, the
  `footer-tag` date, the Recap pill date, and the `<!-- N · SLOT -->` comments.
- **The carry is the start of today's deck, not the whole of it.** Today still
  teaches its new idea, and the deck still overshoots.

---

## BLOCKS TRACK — applies to DAVID P only today

**DAVID P drags MakeCode blocks.**

**Zero Python anywhere in that deck.** Not in a code block, not in a debug card,
not in a comment, not in a heading. Note that **last week's own deck
(`../2026-09-06/david-p-inverted-pyramid.html`) breaks this rule** — it writes
`agent.move(FORWARD, 5)` in Python text form. Kasim worked around it live by
saying *"this is in Python, but I'm going to show you what to do"*. Today's deck
must redraw every one of those ideas as a block, so the carry is
**REWRITE ANCHORS**, not verbatim.

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

### Chat commands — the real starter layout

Kasim's own world uses **separate one-letter chat commands**, not one `"go"`:

- `rl` = `agent teleport to player` (re-line the agent)
- `r` = `agent turn right` · `l` = `agent turn left`
- `run` = the build itself

**A teleport block never goes inside `run`** — it makes the agent miss the first
block. Keep `rl` as its own command. DAVID P wrote his own `stop` command last
week, unprompted — keep it in every drawing of his program.

### Coordinates rule

**y starts at 0. x and z start at 1.** The first free square is `~1 ~0 ~1`.
Never write "coordinates start at 0" as one blanket rule. Counting a range is
unchanged either way: end minus start, then add 1.

### Reference decks for tone (blocks)
- `../2026-09-05/yura-one-repeat-many-steps.html`
- `../2026-09-10/jj-the-spiral-staircase.html`
- `../2026-09-11/jaden-one-command-many-flowers.html`

---

## 08:00 KST · 06:00 HCMC · YUNGUN — `yungun-high-score-and-faster.html`

**Track:** IDE Python, pygame · **🔴 DECK IS ALL ENGLISH, NO KOREAN ANYWHERE**
**Topic (from his live file + yesterday's transcript):** the food you can never
reach, then a high score that survives a restart, then the snake speeds up.

**He was taught YESTERDAY, Saturday 12 Sept**, not last Sunday — he skipped that
one. His recap must describe *yesterday*.

### 🔴 THE SNAKE GAME IS FINISHED. Today is not a new mechanic.

Checked against his live file, every core feature is already present and working:
food spawning, eating, growing, score, wall-collision death, self-collision
death, a GAME OVER screen, a final score, and `R` to restart. **Do not build any
of those again.** Today is about the two real bugs left in the file and then
three things the game still does not do.

### Covered yesterday (transcript `2026/09/12 06:09`, full 41 minutes)

- `game_over = True` replacing `running = False`, so the window stays open
- `if not game_over` guarding the movement block
- `big_font`, a new `RED`, and the `GAME OVER` text drawn with `blit`
- the final score drawn under it with an f-string
- `K_r` to restart, with all six resets: snake body, direction, food, score,
  `game_over`, and the move timer
- an extra `restart_prompt` line ("Press 'R' to restart...") — **Kasim typed
  this one himself**, saying *"let me let me do that really quickly for you"*,
  because time ran out

### ✓ Wins to name in the Recap

- Explained the restart flag in a full sentence, unprompted: *"If game over and
  when we press the R, you're restarting."* This is the single best thing he did.
- *"Plusing the score"* — described `score = score + 1` in his own words.
- Spotted a bug Kasim had missed: *"Yeah, but the score is still white."*

### △ What actually went wrong — turn each into a slot

- Rendered `game_over_text` but never blitted it, so nothing appeared. His words:
  *"Oh, nothing. Nothing happens."* **Render and blit are two separate steps** —
  this earns a Common Mistake slide.
- Chose font size 200, which filled the screen.
- Put a colour inside the wrong brackets.
- Forgot the `()` on `spawn_food` — *"Where's the parenthesis?"*
- Confused a string with a variable name; needed a four-question drill.
- Kasim had to take over the last two resets: *"Let me just help you because
  we're running out of time."* So the resets were finished FOR him — a short
  re-derivation of one reset is fair warm-up, not review for its own sake.

### 🔴 His live file, verbatim — every FIND string comes from here

`student_ide`, project `Workspace`, `main.py`, saved 2026-09-11 23:51 UTC.
Header: `pygame.init()`, `font` / `medium_font` / `big_font` (60), `score = 0`,
`game_over = False`, ten `PASTEL_*` plus `BLACK` / `WHITE` / `RED = (255, 0, 0)`,
`WIDTH, HEIGHT = 600, 600`, `CELL_SIZE = 20`, `GRID_WIDTH` / `GRID_HEIGHT`,
`MOVE_INTERVAL = 150`, `snake_body = [(start_x, start_y)]`, `direction = (1, 0)`.

```python
def spawn_food():
    while True:
        pos = ((random.randint(0, GRID_WIDTH) - 1), random.randint(0, GRID_HEIGHT-1))
        if pos not in snake_body:
            return pos

food = spawn_food()

running = True
while running:
    dt = clock.tick(60)
    time_since_last_move += dt
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and direction != (-1, 0):
                direction = (1, 0)
            elif event.key == pygame.K_LEFT and direction != (1, 0):
                direction = (-1, 0)
            elif event.key == pygame.K_UP and direction != (0, 1):
                direction = (0, -1)
            elif event.key == pygame.K_DOWN and direction != (0, -1):
                direction = (0, 1)

        if game_over and event.key == pygame.K_r:
            snake_body = [(start_x, start_y)]
            direction = (1, 0)
            food = spawn_food()
            score = 0
            game_over = False
            time_since_last_move = 0

    if not game_over and time_since_last_move >= MOVE_INTERVAL:
        time_since_last_move -= MOVE_INTERVAL
        head_x, head_y = snake_body[0]
        ## IF ITS BIGGER THAN THE X or Y OR LESS THAN 0 or Y OR X ##
        new_head = (head_x + direction[0], head_y + direction[1])

        if (new_head[0] < 0 or new_head[0] >= GRID_WIDTH or new_head[1] < 0 or new_head[1] >= GRID_HEIGHT) or new_head in snake_body:
            game_over = True

        snake_body.insert(0, new_head)
        if new_head == food:
            food = spawn_food()
            score = score + 1
        else:
            snake_body.pop()

    screen.fill(PASTEL_MINT)
    for (gx, gy) in snake_body:
        rect = (gx * CELL_SIZE, gy * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, PASTEL_LAVENDER, rect)
    food_rect = (food[0] * CELL_SIZE, food[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)

    ## DRAW OBJECTS ##
    pygame.draw.rect(screen, PASTEL_YELLOW, food_rect)

    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))
    if game_over:
        game_over_text = big_font.render("GAME OVER", True, RED)
        screen.blit(game_over_text, (170, 250))

        score_game_over = big_font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_game_over, (210, 350))

        restart_prompt = medium_font.render("Press 'R' to restart...", True, RED)
        screen.blit(restart_prompt, (230, 400))

    pygame.display.flip()

pygame.quit()
```

**Exact FIND anchors (unique, verified):**
- `if game_over and event.key == pygame.K_r:`
- `restart_prompt = medium_font.render("Press 'R' to restart...", True, RED)`
- `MOVE_INTERVAL = 150`
- `pos = ((random.randint(0, GRID_WIDTH) - 1), random.randint(0, GRID_HEIGHT-1))`

### Reached yesterday — `reached slide 71 of 119`, and there are TWO carries

Last deck: `../2026-09-12/yungun-game-over-and-go-again.html` (**119 slides**).

- **Carry A — slides 9 to 15.** These were **skipped mid-deck**, not unreached.
  They are the `- 1` bracket fix on the food line. Kasim flicked past them:
  *"Okay, get rid of this. Good, good, good."* **The bug is still live in his
  file**, so these slides are exactly today's opening. Carry them to the FRONT.
- **Carry B — slides 72 to 119.** Never reached: drills and debug cards 72–83,
  then the whole bonus overshoot — high score 85–91, pause 92–98, countdown
  99–108, Q-to-quit 109–110, six slides carried from the 09-05 deck at 111–116,
  closers 118–119. **Slides 85–91 are today's high-score block** — carry them
  verbatim and build on them.

How the stop point was found: every `<div class="slide">` was indexed and matched
against the live file. Slides 9–15 must be unreached because the `- 1` bug is
still in `spawn_food`. Slides 72–119 must be unreached because none of their code
exists in the file. Kasim closed immediately after the ad-hoc prompt line:
*"So, Yoongun, that's everything today. Any questions?"*

### What today teaches

**Open on the real bug, because it is visible and it is his.**

1. **Warm-up, two or three slides** — run the game, play it, and notice the food
   sometimes never appears. Then the picture: `random.randint(0, GRID_WIDTH) - 1`
   picks a column and *then* subtracts one, so column 0 becomes **column −1**,
   which is off the left edge of the screen. Draw the grid with a highlighted
   column at −1 outside the frame.
2. **v1 — move the `- 1` inside the brackets.** This is Carry A.
   OLD: `random.randint(0, GRID_WIDTH) - 1`
   NEW: `random.randint(0, GRID_WIDTH - 1)`
   ✅ check: the food now always lands on the board.
3. **v2 — the second bug, and it is a crash.** The `if game_over and
   event.key == pygame.K_r:` block sits at `for event` level, one indent too far
   out, so it runs for **every** event. A mouse move has no `.key`, so after
   dying, moving the mouse raises `AttributeError`. Draw the event loop as two
   boxes — "any event" outside, "key events only" inside — and move the block in
   one indent level. ✅ check: die, wiggle the mouse, nothing crashes.
4. **v3 — the high score that survives.** This is the new idea and the heart of
   the lesson. `high_score = 0` must go **above** the `while running:` loop,
   because anything inside the restart block gets wiped. Then
   `if score > high_score: high_score = score` at the moment of death, and a
   third line of text on the game-over screen. **Visual: two boxes side by side,
   `score` inside the restart box and `high_score` outside it, with the restart
   arrow only emptying the inside one.** Carry slides 85–91.
5. **v4 — the snake speeds up.** `MOVE_INTERVAL` is a variable, so it can change.
   `MOVE_INTERVAL = MOVE_INTERVAL - 5` when food is eaten, with a floor:
   `if MOVE_INTERVAL < 60: MOVE_INTERVAL = 60`. **Visual: a number line from 150
   down to 60 with the snake drawn faster at each step**, and a frame showing why
   the floor is needed (without it the snake becomes unplayable).
6. **v5 and beyond, OPTIONAL** — pause on `P` (carry 92–98), the countdown
   before the game starts (carry 99–108), `Q` to quit (carry 109–110).

**Overshoot:** after v5 keep going with new taught ideas — a colour that changes
as the score rises, the food worth more points the longer it survives, a second
piece of food. Each needs its own visual.

### One thing Kasim said that the deck must not contradict

At the end he said *"tomorrow we'll finish this game and we'll do something
else"* and Yungun answered **"No."** Then *"we'll do another game"* and Yungun
said **"Yeah."** The deck stays in this file, because the file is where the two
real bugs are, and the bonus features are genuinely new work rather than review.
Do not put "we are starting a new game" anywhere in the deck — that is Kasim's
call to make in the room.

### Reference deck for tone
`../2026-09-12/yungun-game-over-and-go-again.html` — same student, yesterday,
all-English, and the source of both carries.

---

## 10:00 KST · 08:00 HCMC · DIS — GROUP CLASS, 3 STUDENTS, 50 MINUTES — `dis-a-weird-rainbow-pattern.html`

**Track:** Minecraft **Python** (constant form: `RED_WOOL`, `pos(...)`, `REPLACE`)
· **Korean glosses allowed**
**Topic (from the transcript):** land the loop inside a loop for all three, then
`i % 3` makes the weird rainbow pattern Kasim promised out loud.

**Students: Cian, Leah, Danny.** Spell them exactly like that. The tracker
misspells two as *Shian* and *Leia* — ignore it. The transcript speaker labels
are family Google accounts: 허문정 = **Cian**, Miae Ahn = **Leah**,
Youngki Park = **Danny**. Confirmed by four direct question-and-answer pairs.

### Covered last week (transcript `2026/09/06 08:00`, full length)

- Oral recap quiz: how many layers, which axis goes up, what `range(6)` does.
  **Not** a rebuild from memory — they opened last week's file.
- Rewrote the colour list to exactly six items so it matches `range(6)`:
  purple, blue, green, yellow, orange, red.
- **Stage 1 landed for all three** — deleted `y` entirely and put `i` straight
  into the coordinate. Kasim: *"Let's move on since all of you are now on the
  same step."*
- **Stage 2, the loop inside a loop, was taught and typed but only WORKED for
  Leah.** Kasim: *"Oh, Leia, you've done it. Whoa, Leia, look at that."*

The code dictated at 00:43:38:

```python
for x in range(3, 9):
    for i in range(6):
        blocks.fill(colors[i], pos(x, i, ?), pos(x, i, ?), REPLACE)
```

**The `pos()` Z numbers were never spoken.** Keep them consistent but never build
a slide whose point depends on them.

### 🔴 The gap — this is the strongest input to today

**The nested loop did not land for Cian or Danny.**
- **Danny ended unresolved**, still saying *"There's an error on I"* and *"What
  is I?"* when the lesson stopped.
- **Cian's was wrong too** — *"Yeah, but like it's kind of wrong."*
- Stop point: *"Okay, guys. We'll stop right there."* (00:49:50)

So today opens by **finishing Stage 2 for all three**, then moves to the new
idea. That is a warm-up that earns its place, not review.

**The Ctrl+Z / undo slide from last week was SKIPPED entirely** — never
mentioned. Kasim cleared builds himself with an air `blocks.fill` chat command.
Carry the undo slide, and put it near the front again.

### Promised out loud — the parent heard this

Kasim: *"Next week, we're going to be continuing this, but we're going to make a
weird pattern with the rainbows. So, it should be a fun activity."*
**The weird pattern IS today's new idea.** `i % 3` is how it happens.

### ✓ Wins, one per student — name them individually in the Recap

- **Cian** — pre-empted the next edit before Kasim asked: *"Can I get rid of
  y = y + 1?"*
- **Leah** — the only one to get the nested loop running. *"Wow, very good.
  Super smart."*
- **Danny** — read the whole program back correctly: *"it makes a layers of red
  wool, orange, yellow, lime, light blue, purple."*

### △ Real bugs from the lesson — turn each into a slot, name no one

- **The colours list written outside `def on_chat`**, so the function cannot see
  it. Cian hit this, and said *"I think we had the same problem last week"* — so
  it is a repeat and it needs a proper visual, not a one-liner. Draw the function
  as a box with the list inside it or outside it.
- A block list with **ten colours against `range(6)`** (Leah) — four never used.
- `y` → `i` swaps missed in some of the coordinate slots (Danny).
- Danny's unresolved `I` error — the inner loop variable used in the outer loop,
  or the inner `for` missing entirely. Build the fix as its own slow sequence.
- Cian's fourth layer exploded because slime blocks landed between the wool.
- Building while standing in the way, so blocks land wrong.

### Reached last week — `reached slide 46 of 78`

Last deck: `../2026-09-06/dis-loop-inside-loop.html` (**78 slides**).
Stop point mapped from the transcript: the dictated `for x in range(3, 9)` edit
matches the deck's slide 46. Slides 40–42 (the 12→3 thinning) are not in the
transcript either.

**The carry — slides 47 to 78, plus the skipped undo slide:**
- the rest of Stage 2 (the nested-loop trace frames) — **carry, and this is the
  warm-up**
- Stage 3, `range(start, stop, step)` for spacing — carry
- the stretch material, `i % 3` and the shrinking pyramid — carry, and `i % 3`
  is now promoted to the **main new idea**
- the Ctrl+Z slide from near the front — carry forward, still unused

### What today teaches

1. **Warm-up — finish the nested loop, for everyone.** One frame per pass on a
   grid: the outer counter `x` on the left, the inner counter `i` ticking
   through 0–5 inside each single outer step. This is the picture Danny needed
   and did not get. Two counters drawn as two separate dials.
2. **Fix the scope bug properly** — the list lives above the loop, inside the
   function. Draw the function as a box.
3. **The new idea: `i % 3`.** `%` is what is left over after dividing. Draw it
   as sweets shared into bags — how many stay in your hand. No code on this
   slide.
4. **A counter strip** with `i` on the top row running 0 to 11 and `i % 3` on the
   bottom row running 0 1 2 0 1 2 0 1 2 0 1 2. Point at the moment it snaps back
   to zero. **This one picture is the whole idea.**
5. **v1 — `colors[i % 3]`** so a six-layer tower uses only three colours and
   repeats them. Draw the tower with the repeat visible.
6. **v2 — the weird pattern.** `if i % 3 == 0:` build wool, `else:` build glass
   or stone. Now the tower is striped in a pattern rather than a plain rainbow.
   This is what the parent was told.
7. **v3 — the pattern across the row.** Put `x % 3` in the outer loop so every
   third tower is different. Two `%` rules at once, drawn as a grid with the
   special towers shaded.
8. **v4, OPTIONAL — `range(3, 15, 4)`** so towers space themselves out without
   arithmetic. Then the shrinking pyramid from the old stretch.

**Overshoot hard:** this is a 3-student group where one finished early last
week, so there must be plenty past step 6. Keep adding taught ideas with visuals
— `i % 2` for two-colour stripes, a tower whose height also follows `i`, a
checkerboard floor.

### One classroom note for Kasim, not for the slides

Last week ran with heavy off-task play. Kasim jailed all three, set the world
immutable and made them visitors to force focus, and Leah was on YouTube. After
Kasim left at 00:53 the three free-played in Danny's survival world until
01:19:45 with no teacher present. **Put a STAGE divider and a "Now you build it"
slide closing each block**, so there is a visible place to stop talking and a
visible place to pull attention back.

### Reference deck for tone
`../2026-09-06/dis-loop-inside-loop.html` — same group, last week, source of the
carry.

---

## 18:00 KST · 16:00 HCMC · LEO KIM — `leo-one-loop-fills-the-floor.html`

**Track:** Minecraft **Python** (constant form: `QUARTZ_BLOCK`, `RED_WOOL`,
`pos(...)`, `REPLACE`, `player.on_chat`) · **Korean glosses allowed**
**Topic (from Tuesday's transcript):** `//` floor division — one loop fills a
whole floor.

### 🔴 He is ONE student in TWO slots. Check novelty across both.

`leo-kim-sun-1800` (today) and `leo-kim-tue-2000` are the same child. His most
recent lesson is **Tuesday 8 Sept**, not last Sunday. Both transcripts were read
for this brief.

### Covered Tuesday 8 Sept (transcript `2026/09/08 18:00`, 51 minutes)

- Wide modulo revision — `1%6`, `1%3`, `2%3`, `3%3`, `4%2`, `5%10`, `6%3`, `7%14`
- `range(6)` gives 0, 1, 2, 3, 4, 5
- the difference between `=` and `==`
- `height = 5` as a default set inside the loop
- `if i % 3 == 0: height = 9`
- `elif i % 5 == 0: height = 7`
- wool colour list plus `colors[i % 6]` to cycle colour
- `x = x + 1` to space the towers — **omitted twice, debugged both times**
- declaring `z`, then `z = z + 1` gated on `if x % 2 == 0:`

Reconstructed end state — **skeleton is reliable, the flagged details are not**:

```python
def <cmd>():
    x = 1 ; z = 1                      # approximate, speech garbled
    colors = [RED_WOOL, LIME_WOOL, YELLOW_WOOL, ...]   # exact list unclear
    for i in range(12):                # taught 12; Leo read "range 13" once
        height = 5
        if i % 3 == 0: height = 9
        elif i % 5 == 0: height = 7
        blocks.fill(colors[i % 6], pos(...), pos(...), REPLACE)   # coords never spoken clearly
        x = x + 1
        if x % 2 == 0: z = z + 1
```

**Never build a slide whose point depends on the coordinate numbers** — they were
not spoken clearly. The last thing reached was *"Add four more colors"*, which
ran out of time.

### What happened on Sunday 6 Sept (transcript `2026/09/06 16:00`, full 50:40)

The small file size is just Gemini's short-notes format — the lesson was full
length. Of the six planned stages **only stages 1 and 4 landed**:
- the IndexError hook **never fired** — no crash happened. Leo reported *"only
  six are colored and left over it is same"* instead.
- `colors[i % 6]` landed — he read out *"Red, orange, yellow, green, blue,
  purple, red, orange"*.
- The lesson then jumped **out of order into stretch material**: `y = 2 + i % 6`
  and `if i % 3 == 0` with a gold cap, then *"So, we'll stop right there."*
- Stages 2, 3, 5 and 6 were **never taught**. No remainder-as-sweets explanation
  happened at all. Kasim asked *"So what does I percentage 6 do?"* and Leo never
  answered; the lesson moved on.

### 🔴 Novelty check — what he has NOT been taught

Verified against both transcripts:
- **`//` floor division — NOVEL.** `//` was never written. Only the phrase
  "floor division" was said out loud once, on Tuesday, with no code.
- **One loop filling a square — FULLY NOVEL.**
- **`(x + z) % 2` checkerboard — FULLY NOVEL**, and both `x` and `z` already
  exist in his file, so it is cheap to reach.
- **`i % 2` as even/odd — effectively novel.** `x % 2 == 0` was typed once
  mechanically on Tuesday and never explained as odd-versus-even.

### The unmet promise

Tuesday's ledger `gap`: the table showing which towers hit both the `i % 3` and
`i % 5` rules was **not done** and moved to homework. Also *"add four more
colors"* was promised, but **it is a no-op while the index stays `i % 6`** — if
the deck touches it, it must be as the reveal that the index has to change too.

**Kasim also said, and it matters:** *"I want to level you up... Minecraft is
just stifling your limit right now."* Today's topic is the most algorithmic
thing available inside Minecraft, which is the right direction for that.

### ✓ Wins to name in the Recap

- Self-diagnosed the colour bug: *"only six are colored and left over it is
  same"*, then said the fix was *"Rewrite this"*.
- `3 % 3`: *"then zero. There's no remainder."*
- Named the multiples for `i % 3` unprompted.
- **Best one: he predicted that adding four more colours would change nothing —
  *"I knew that the same"* — while Kasim said *"It's not going to be the same.
  You'll see."* Leo was right.** Open the Recap with this.

### △ Real mistakes — turn each into a slot

- `x = x + 1` left out **twice** on Tuesday. Reassignment order inside a loop is
  his weakest thing and the teacher had to point at the exact line both times.
- `z = z + 1` written before `z` existed.
- Wrote 8 for the `elif` height, then corrected himself.
- On Sunday: repeated *"nothing happened"* because the chat command was not run.
- Could not find the `%` key — *"Where's percent in my keyboard?"* Put a picture
  of the key on a slide.
- Added the colours list but left it out of the `fill` call.

**Behaviour correction for the deck:** the old brief said he *"waits for the
teacher to type first"*. The transcripts say the opposite — he **types ahead and
races**, saying *"I'm done"* and *"I didn't just copy and paste like you"*. He
stalls only when he cannot see the shared screen (*"I cannot see anything"*).
So **do not** put type-first markers on every Make slide. Instead make every code
block big enough to read at a glance. The *"I don't know"* habit is confirmed,
but he reads his code aloud token by token when pushed — keep the sentence frames.

### Reached last Sunday — `reached about slide 38 of 65`, non-contiguous

Last deck: `../2026-09-06/leo-remainder-patterns.html` (**65 slides**).

**The carry:**
- **slides 9–19** — remainder vocab, the sweets picture, `//`, the counter-wrap
  strip, the `i % n` rule, the quiz. **These are the heart of today.** Carry them
  to the front.
- **slide 25** — read-the-error. Carry, but note **no crash actually happened**,
  so it cannot be framed as "remember when it broke".
- **slides 27–28, 30–36, 38** — scattered unreached slides.
- **slides 39–46** — `i % 2` stripes. Carry.
- **slides 47–54** — `//`, the grid, the checkerboard. **This is today's main
  block.** Carry verbatim and build on it.
- **slides 60, 64** — unreached.

Method: every one of the 65 slides was dumped and matched against spoken code
strings and quotes from both transcripts.

### What today teaches

1. **Warm-up, short** — his Tuesday build, and the table he owes: which towers
   get height 9, which get 7, which get both. Draw it as a strip of 12 towers
   with the two rules marked. This settles the unmet promise in two slides.
2. **`//` is the other half of `%`.** Divide 7 by 3: `7 // 3` is 2 whole bags,
   `7 % 3` is 1 left in your hand. **Same picture, two answers.** Carry slides
   9–19 here.
3. **The counter strip, twice over.** `i` on the top row 0 to 24. `i % 5` on the
   middle row cycling 0 1 2 3 4. `i // 5` on the bottom row stepping 0 0 0 0 0
   1 1 1 1 1 2 2 2 2 2. **Point at the column where the middle row resets and
   the bottom row ticks up.** This one picture is the whole lesson.
4. **v1 — the payoff.** One loop fills a 5×5 floor:
   ```python
   for i in range(25):
       x = i % 5
       z = i // 5
       blocks.fill(STONE, pos(x, 0, z), pos(x, 0, z), REPLACE)
   ```
   Draw the grid filling in, one frame per pass, with `i`, `x` and `z` written
   under each square. Twenty-five blocks, one loop.
5. **v2 — put it beside the nested loop he already knows.** He has written a loop
   inside a loop before. Two routes, same floor. Draw them side by side.
6. **v3 — `(x + z) % 2` gives a checkerboard.** `if (x + z) % 2 == 0:` white
   wool, `else:` black wool. Draw the grid with the sum written in each square
   so he can see the alternation fall out of the maths.
7. **v4 — colour by row instead of column.** `colors[i // 5]` paints each row a
   single colour; `colors[i % 5]` paints each column. **Two lines, one character
   different, completely different floor.** Draw both.
8. **v5, OPTIONAL** — make it 3D by adding `y = i // 25`; a floor that is also a
   wall; `i % 2` stripes from carry slides 39–46.

**Overshoot hard.** He finished a 30-slide deck fully on 1 Sept and raced ahead
on Tuesday. This deck must run far past step 7.

### Reference deck for tone
`../2026-09-06/leo-remainder-patterns.html` — same student, source of the carry.

---

## 19:00 KST · 17:00 HCMC · DAVID G8 — `david-g8-two-names-one-loop.html`

**Track:** IDE Python, **text adventure game**, NOT Minecraft ·
**Korean glosses allowed**
**Topic (from his live file):** the file does not run — one comma — then two
names in one loop.

He is David Seo, IDE username `hcseo31`. His game is a text dungeon crawler
called the Abandoned Amusement Park.

### Covered last week (transcript `2026/09/06 17:00`, full 51:17)

The small doc is Gemini's compact notes format, not a short lesson.

- **Chapter flags, first** — *"on line 45. Yeah, we should say chapter one equals
  false."* Then `chapter_two = False`, then `chapter_four = True`.
- **An ask-until-valid gate, but in a different shape from the deck** — he built
  `asking = True` with `while asking:`, not the deck's
  `while answer not in [...]`. His words: *"we're going to say asking equals
  through strike or leave while asking."*
- Then the lesson **left the deck entirely** and went into **dictionaries and
  nested dictionaries** — *"it's called a dictionary."* He proposed the chapter
  himself: *"we can add the merchants in chapter three."*

**All six bugs from before the lesson are now FIXED.** Three of them (the chapter
flags, the railway key, the unstored wrench answer) he had already fixed
**himself**, between the deck being written and the lesson — he had reached
chapter 4 by 00:03:52, saying *"The latest version is my project"*. Say this in
the Recap; it is the best thing in the transcript.

### 🔴 HIS FILE DOES NOT RUN. This is slide 3.

`student_ide`, project `Workspace`, `main.py`, saved 2026-09-06 10:49 UTC.
**Nothing has been saved since the lesson ended**, so the homework was never
started.

**A missing comma** after the music box `"description"` value raises a
`SyntaxError` at the `"rarity": 'A',` line. Verified with `py_compile`. **The
whole game is dead until that comma goes in.** This is the opening of the lesson:
run it, read the error out loud, fix one character, run it again.

**Second real bug, and it is the new idea's hook:**
`for key in merchant_invetory.items():` yields **pairs**, not names. Kasim said
it would print "katana axe music box" — it will not; it prints tuples. It was
never tested, because the file cannot run.

### Exact FIND anchors — the typo IS the anchor, keep it

- `merchant_invetory = {`  (misspelled "invetory" — do not correct it in a FIND)
- `### dialogue that asks if u want to see the items###`
- `for key in merchant_invetory.items():`

### Current structure

Top of file: the `inventory` list, then `merchant_invetory = {}` as a nested
dictionary (katana, axe, music box), a debug
`print(merchant_invetory['katana'])`, then `chapter_one` through `chapter_four`
and `game_over` all set to `None`, then status flags
`poisoned` / `burned` / `drunk` / `ripped = None`.

Flow: intro prints → `while asking:` strike-or-leave gate → `while chapter_one:`
→ `while chapter_two:` → `while chapter_three:` (the merchant, new) →
`while chapter_four:` → `if game_over:` / `else:` with an f-string ending.

**Three latent traps to use as debug slides:**
- `chapter_three` is never set `True`, and its loop has no exit — the merchant
  chapter is dead code today and an infinite loop the moment it is armed.
- `while chapter_two:` loops forever if the answer is `no`.
- `poisoned = True` is set on the red chest and then never read.

### ✓ Wins to name in the Recap

- Reasoned the flags out himself: *"Since the chapter 4 is already in true the
  chapter one two should be false."*
- Counted his own death endings: *"one, two, three, four, five, six, seven."*
- Spotted a fix instantly: *"Ah lower"*.
- Proposed the merchant chapter himself.
- Edited his own writing for sense: *"Maybe just say emotionless."*

### △ Real mistakes — turn each into a slot

- **f-string**: quoted the variable and left the `f` off. Kasim: *"Inside those
  curly braces, you've added something that's making it a string."*
- **Indentation**: *"the LF um has eight spaces. Uh the print has 12."* He needs
  telling which block a line belongs to, every time — so every 📍 where marker in
  this deck must give the **exact indent count**.
- Flag direction confusion: *"we have to let the chapter two goes on"* when the
  answer was `False`.
- Forgot how list indexing works — asked what `inventory[0]` does, then *"Um,
  not really."*
- `=` versus `==` did **not** come up this time. Do not build a slide on it.

### Reached last week — non-contiguous, and there are three carries

Last deck: `../2026-09-06/david-g8-ask-until-valid.html` (**100 slides**).

- **Covered:** slides 66–78 (the chapter flags).
- **Carry A — slides 43 to 64**, the whole `def ask(question, options):` build,
  from *"Write the gate once"* through to *"Five gates, five lines"*. **Never
  taught. This is a whole contiguous block and it is still exactly right for
  him**, because he now has five hand-written gates in his file.
- **Carry B — slides 25–28 and 33–41.** `not in` with a list of allowed answers,
  and the v3 gate. He built a **boolean-flag variant instead**, so the idea
  landed in a different shape and the exact code never did. `REWRITE ANCHORS` —
  reframe these as "your gate, written a shorter way", comparing his real
  `while asking:` against `while answer not in [...]`.
- **Carry C — slides 85 to 96**, the stretch: `yes_no()` 85–87, the unused
  `poisoned` flag 88–89, a retry counter 90–91.

Method: the deck was grepped for each idea's exact code token (`not in`,
`def ask`, `chapter_* = True`, `yes_no`, `poisoned`, `answer = ''`), each hit
mapped to a slide number, then checked against the live file and the transcript
timestamps.

### What today teaches

1. **Slide 3 — run it. It crashes.** Read the `SyntaxError` out loud, find the
   line, add one comma. ✅ check: the game starts. **A whole slide on reading the
   error message**, because the error names the line for him.
2. **Warm-up — the dictionary he built.** Draw `merchant_invetory` as a chest of
   drawers: the outer key is the drawer label, the inner dictionary is what is
   inside. Two or three slides.
3. **The new idea: `.items()` gives you TWO things, so catch them with two
   names.**
   OLD: `for key in merchant_invetory.items():`
   NEW: `for name, item in merchant_invetory.items():`
   **Visual: the loop handing out two labelled boxes per pass** — `name` holding
   `'katana'`, `item` holding the inner dictionary. One frame per item.
4. **v1 — print a real shop menu.** `print(name, item['price'])` inside the loop.
   ✅ check: three lines of shop stock, not three lines of brackets.
5. **v2 — the three ways to walk a dictionary**, side by side and drawn:
   `.keys()` gives names, `.values()` gives the insides, `.items()` gives both.
   A table with the loop line and its output next to each other.
6. **v3 — number the menu.** `for i, (name, item) in enumerate(...)` so the
   player can type 1, 2 or 3 instead of spelling "music box". This is a real
   improvement to his game and it needs the counter drawn.
7. **v4 — one `ask()` function for every choice.** Carry A, slides 43–64. He has
   five hand-written gates; this replaces all five with five calls. **Show the
   before-and-after wall of code side by side** — that picture is the payoff.
8. **v5 — arm chapter three safely.** `chapter_three = True` at the end of
   chapter two, plus the `break` its loop is missing. Draw the four chapters as
   boxes with arrows that only appear when a flag flips.
9. **OPTIONAL** — buying an item actually moves it into `inventory` and takes the
   price off his gold; the `yes_no()` wrapper from Carry C; the unused `poisoned`
   flag finally doing something.

**Overshoot hard.** He fixed three bugs unsupervised between lessons and writes
fluently, so he moves fast. Run well past step 8.

### Reference deck for tone
`../2026-09-06/david-g8-ask-until-valid.html` — same student, source of all
three carries.

---

## 20:00 KST · 18:00 HCMC · LOGAN — `logan-the-wall-you-cannot-cross.html`

**Track:** IDE Python, pygame · **Korean glosses allowed**
**Topic (from his live file):** the wall you cannot walk through — `colliderect`.

### Covered last week (transcript `2026/09/06 17:59`, full 41:49)

- `keys = pygame.key.get_pressed()` with an `if` per arrow key. **Diagonals
  landed too** — he found them himself: *"Oh, it goes to D. It goes diagonally."*
- Edge stops on both axes, with the rectangle's width subtracted. His own words:
  *"the player's W is 100 and the W is 500. So, it teleports you to 400."*
- A `speed` variable. *"Oh yeah. Yeah. It works very speedy."* **This was the
  last thing done.**
- **Two things not in the deck at all, improvised live:** he rebuilt every
  attribute into a `player` **dictionary**, and added a colour that changes while
  moving.

### 🔴 His file changed SHAPE last week. Last week's carry is anchored to names that no longer exist.

The unreached slides 49–74 are written against `X_EXAMPLE`, `Y_EXAMPLE` and a
bare `speed = 5`. **None of those exist any more.** Every FIND string must be
re-cut from the live file below. The teaching in those slides is fine; the
anchors are dead.

### His live file, verbatim — every FIND string comes from here

`student_ide`, project `Workspace`, `main.py`, saved 2026-09-06 11:42 UTC.
Fifteen `PASTEL_*` constants, then `WIDTH, HEIGHT = 500`, then:

```python
player = {
    "x": WIDTH // 2 - (50),
    "y": HEIGHT // 2 - (50),
    "color": PASTEL_CYAN,
    "width": 100,
    "height": 100,
    "speed": 10
}
...
    keys = pygame.key.get_pressed()
    moving = False
    if keys[pygame.K_LEFT]:
        player["x"] = player["x"] - player["speed"]
        moving = True
    if keys[pygame.K_RIGHT]:
        player["x"] = player["x"] + player["speed"]
        moving = True  + 10
    if keys[pygame.K_UP]:
        player["y"] = player["y"] - player["speed"]
    if keys[pygame.K_DOWN]:
        player["y"] = player["y"] + player["speed"]

    ## COLOR CHANGE ON MOVE ##
    if moving:
        player['color'] = PASTEL_RED
    else:
        player['color'] = PASTEL_ROSE

    ## BOUNDARIES ##
    if player['x'] < 0:
        player['x'] = 0
    if player['x'] > WIDTH - player["width"]:
        player['x'] = WIDTH - player["width"]
    if player['y'] < 0:
        player['y'] = 0
    if player['y'] > WIDTH - player["width"]:
        player['y'] = WIDTH - player["width"]
    screen.fill(PASTEL_CYAN)
    pygame.draw.rect(screen, player['color'], (player['x'], player['y'], player['width'], player['height']))
```

**Note his file mixes `'x'` and `"x"` quote styles.** Copy whichever style the
line actually uses into each FIND string.

**Exact FIND anchors:**
- `    "speed": 10`
- `        moving = True  + 10`  (the double space is real)
- `    if player['y'] > WIDTH - player["width"]:`

**Two real bugs sitting in the file — both are debug slides:**
- `moving = True  + 10` — a stray `+ 10` from a mistyped line. `True + 10` is
  `11`, which is still truthy, so **the program works by accident**. Excellent
  slide: it runs, and it is still wrong.
- The last boundary check uses **`WIDTH`** where it should use **`HEIGHT`**. It
  works today only because both are 500. Change `HEIGHT` to 400 on a slide and
  show the square escaping out of the bottom.

### ✓ Wins to name in the Recap

- Worked out diagonal movement unprompted.
- Explained the `WIDTH - 100` limit himself.
- Derived that bottom-right means *"down, and right"*.
- Chose and tuned every colour himself.

### △ Real mistakes — turn each into a slot

- `get_pressed` `AttributeError`.
- `name 'moving' is not defined`.
- `x_example is not defined` after the dictionary swap — **renaming one thing
  means renaming it everywhere**, which is its own slide.
- `width` / `height` key typos.
- The square vanished off-screen from a missing `- player width`.
- `name 'speed' is not defined` **three times** before `player["speed"]` was
  right. Dictionary access is the thing to keep drawing.

**Resolved, do not re-teach:** the top-left origin and y-growing-downward. He
explained it back correctly: *"if the X goes down, it goes left... And if the Y
goes down, it goes up. And the Y number, if it goes big, it goes down."*
One quick recap picture at most.

### Reached last week — `reached slide 48 of 74`

Last deck: `../2026-09-06/logan-keyboard-control.html` (**74 slides**).
Slide map: v3 keyboard 19–26, v4 walls 30–38, v5 speed 43–48, v6 SIZE variable
49–55, v7 the wall you cannot cross 56–67, WASD 68–73, close 74.

Stop point: the speed variable, transcript 00:36:31–00:39:44, matching the v5
block that ends at slide 48.

**The carry — slides 49 to 74, ALL FLAGGED `REWRITE ANCHORS`:**
- 49–55 a `SIZE` variable — rewrite as `player["width"]` and `player["height"]`
- **56–67 the wall you cannot cross — this is today's main block**, rewrite
  against the `player` dictionary
- 68–73 WASD keys — carry, cheap and satisfying
- 74 close

### What today teaches

1. **Warm-up — the two bugs above.** Run it, it works, then show why
   `moving = True  + 10` and the `WIDTH`/`HEIGHT` mix-up are still wrong. Real,
   his, and visible.
2. **The new idea: a rectangle that knows where it is.** Right now his square is
   four separate numbers. `pygame.Rect(x, y, w, h)` is all four in one object.
   **Visual: four loose number cards versus one card with four fields.**
3. **v1 — draw a wall.** A second `wall` dictionary, a second `draw.rect`. It
   appears and does nothing yet. ✅ check: a coloured block sits on screen.
4. **v2 — `colliderect` answers one question: are these two touching?** Draw
   four pictures — apart, touching edges, overlapping, one inside the other —
   with True or False under each. **No code on this slide.**
5. **v3 — notice the crash first.** `player` is a dictionary, not a `Rect`, so
   `colliderect` cannot be called on it. Build
   `player_rect = pygame.Rect(player['x'], player['y'], player['width'], player['height'])`
   inside the loop. This is the step that must not be skipped.
6. **v4 — stop the player at the wall.** Remember the old `x`, move, and if the
   new position collides, put it back. Draw it as three frames: before, the
   illegal overlap, and the snap back.
7. **v5 — the reason it must be one axis at a time.** Check `x` then `y`
   separately, or he slides along walls strangely. Draw the corner case.
8. **v6, OPTIONAL** — several walls in a list and one loop checking them all; a
   coin that disappears when touched (same `colliderect`, opposite outcome);
   WASD from carry 68–73; the `SIZE` variable from carry 49–55.

**Overshoot hard.** He improvised a whole dictionary refactor mid-lesson last
week, so he moves fast. Run well past step 7.

### Reference deck for tone
`../2026-09-06/logan-keyboard-control.html` — same student, source of the carry.

---

## 21:00 KST · 19:00 HCMC · CLAIRE — `claire-damage-then-the-bar.html`

**Track:** IDE Python, pygame space shooter · **Korean glosses allowed**
**Topic (from her live file):** damage first, then the boss health bar.

### 🔴 Her last real lesson was 30 August. That is FOURTEEN days ago.

**Her 6 September lesson did not happen.** No recording exists at her slot, and
her `student_ide` file has not been saved since 30 Aug 13:19 UTC. The 108-slide
deck built for her that day was **never delivered**.

So the health bar is still completely new to her, and there is no risk of
repeating anything. But **build in more recap than usual** — two weeks is a long
gap, and her file is exactly where she left it.

### Covered 30 August (the last real lesson)

- `hp` added to each enemy type: how many hits before it dies
- `hp`, `max_hp` and `is_boss` keys inside `make_enemy`
- a `BOSS_TYPE` dictionary: colour, size, speed, points, hp
- `BOSS_SCORE_TRIGGER` and `BOSS_STOP_Y` constants
- `make_boss()`, spawning from the centre and stopping at a Y limit
- spawning gated with a `boss_active` boolean
- `.get()` and `if enemy.get("is_boss"):` to split boss from normal enemies
- Alt+click multi-cursor editing

### ✓ Wins to name in the Recap

- Remembered by herself to paste her homework code in before testing.
- Asked whether missiles and bullets should do different damage — her own
  question, and **it is exactly what today builds**.
- Caught the edge case first: *"what happens if it's equal?"* on the boss Y limit.

### △ Real mistakes — turn each into a slot

- **`[]` versus `()` when reading a dictionary key.** Repeatedly. This is the
  one. Today's main line is full of square brackets, so it cannot be dodged.
- `.get()` returning `None` was explained and still did not hold in use.
- Alt+click multi-cursor failed after several demos. **Do not build the lesson on
  it** — one optional slide at most.

### 🔴 Verified from her live file — corrections to last week's brief

`student_ide`, project `Workspace`, `main.py`, **337 lines**, saved
2026-08-30 13:19 UTC.

**Keys are lowercase snake_case. There is ZERO camelCase in the file.** The
tracker log and the old report both write `HP` and `maxHP`; **those spellings do
not exist**. Real lines:
- `    {"color": RED, "w": 50, "h": 50, "speed": 12, "points": 40, "hp": 2},`
- `        "hp": kind["hp"],`
- `        "max_hp": kind["hp"],`
- `        "is_boss": False,`

**Exact worksheet markers — these are the FIND anchors, verbatim and in order:**

| Line | Marker | The line after it |
|---|---|---|
| 60 | `# --- WORKSHEET STEP 1 : read the "hp" numbers below, do not change them ---` | `ENEMY_TYPES = [` |
| 203 | `                # --- WORKSHEET STEP 3 : a bullet takes 1 hp off ---` | `                if bullet.colliderect(enemy["rect"]):` |
| 225 | `                # --- WORKSHEET STEP 4 : a missile takes 3 hp off ---` | `                if missile.colliderect(enemy["rect"]):` |
| 246 | `            # --- WORKSHEET STEP 2 : make the boss stop ---` | `            if enemy.get("is_boss"):` |
| 285 | `    # --- WORKSHEET STEP 5 : the boss health bar goes under this line ---` | blank, then `    ## DRAW BULLETS ##` |
| 164 | `                # --- WORKSHEET STEP 6 : one line goes under this line ---` | blank; previous line is `                spawn_timer = 30` |

**DAMAGE IS NOT BUILT. Confirmed — nothing in the file subtracts from `hp`, and
no `if enemy["hp"] <= 0:` exists anywhere.** The bullet block, lines 204–210:

```python
                if bullet.colliderect(enemy["rect"]):
                    hits.append([enemy["rect"].centerx, enemy["rect"].centery, 12])
                    score += enemy["points"]
                    enemies.remove(enemy)
                    bullets.remove(bullet)
                    hit_enemy = True
                    break
```

The missile block, lines 226–229:

```python
                if missile.colliderect(enemy["rect"]):
                    hits.append([enemy["rect"].centerx, enemy["rect"].centery, 25])
                    score += enemy["points"] * 2
                    enemies.remove(enemy)
```

**So a health bar drawn today would sit permanently full and then vanish. Damage
has to be built first — that is the running order of the whole lesson.**

Note the score and spark lines currently sit **inside the collision `if` but
outside any hp branch**, because there is no hp branch. When removal moves into
`if enemy["hp"] <= 0:`, **the score and spark lines must move with it**, or she
scores on every single bullet. That is a slide of its own.

**Two more real bugs to use:**
- **The boss stops in the wrong place.** Line 248 `if enemy["rect"].y <
  BOSS_STOP_Y:`, line 251 `enemy["rect"].y = BOSS_STOP_Y` — but line 253
  `enemy["rect"].y += enemy["speed"]` runs **unconditionally afterwards**, so the
  boss parks at **265**, not the 250 she set. Fix this early or the health bar
  will be drawn in the wrong place.
- The missile block **never removes the missile** and has **no `break`**, so it
  mutates `enemies` while looping over it.

**No health bar code exists yet** — only the line 285 marker. `draw.rect` calls
are at 279 (player), 283 (enemies), 289 (bullets), 293 (missiles).

Verbatim, for exact use in slides:

```python
def make_enemy():
    kind = random.choice(ENEMY_TYPES)
    x = random.randint(0, WIDTH - kind["w"])
    y = -kind["h"]
    return {
        "rect": pygame.Rect(x, y, kind["w"], kind["h"]),
        "color": kind["color"],
        "speed": kind["speed"],
        "w": kind["w"],
        "h": kind["h"],
        "points": kind["points"],
        "hp": kind["hp"],
        "max_hp": kind["hp"],
        "is_boss": False,
    }
```

```python
BOSS_TYPE = {
    "color": WHITE,
    "w": 160,
    "h": 160,
    "speed": 15,
    "points": 200,
    "hp": 10
}
```

Line ranges for 📍 where markers: bullet update 196–216 (collision 201–213),
missile update 220–232 (collision 224–229), spawn 234–242, enemy movement
244–257, player collision 259–271, drawing 274–300.

**One correction that changes the framing:** last week's brief said she wrote the
boss-stop code herself as homework. **She did not.** Byte-identical code sits in
her archived project saved 34 minutes *before* the live file existed, so it was
pre-supplied in the starter. Treat step 2 as **given, not completed** — and its
double-move bug makes it a fair thing to open on. Her file's own header comment
still says *"Your boss already spawns. But it does not stop"*, which now
contradicts the code below it.

### Reached — `nothing. The whole 108-slide deck is unreached.`

Last deck: `../2026-09-06/claire-hp-bar.html` (**108 slides**) — built, never
delivered.

**The carry is the entire deck, but it is `REWRITE ANCHORS`:**
- It was written before her file was re-read in full, and it uses `enemy["HP"]`
  and `enemy["maxHP"]` in places. **Those keys do not exist.** Every one becomes
  `enemy["hp"]` and `enemy["max_hp"]`.
- Its damage-before-bar running order is correct and confirmed — keep it.
- Slot 1 and Slot 2 are rebuilt from scratch: the recap must say *two weeks ago*,
  not *last week*.

### What today teaches

1. **Warm-up — run it and find the boss parked in the wrong place.** Read lines
   246–253 together, spot the extra move, fix it. Draw the boss descending with
   the clamp and then one more step past it.
2. **The new idea, part one: a hit takes hp off instead of deleting.**
   OLD: `enemies.remove(enemy)` straight after the collision
   NEW: `enemy["hp"] -= 1` and removal only inside `if enemy["hp"] <= 0:`
   **Visual: a row of hearts emptying one at a time**, with the enemy vanishing
   only when the last one goes.
3. **Move the score and the spark INTO the death branch.** Show the bug first —
   score climbing on every bullet. This is a consequence slide and it needs the
   before-and-after side by side.
4. **A missile takes 3.** `enemy["hp"] -= 3`, marker STEP 4. Same hearts picture,
   three at a time. Answers her own question from two weeks ago — say so.
5. **The new idea, part two: a bar whose width is a fraction.**
   `bar_width = (enemy["hp"] / enemy["max_hp"]) * 200`
   **Every symbol in that line is a square bracket**, so the thing she keeps
   getting wrong is now unavoidable. **Visual: full bar, half bar, empty bar,
   with the fraction written under each and the multiplication shown.**
6. **v2 — two rectangles stacked.** A dark background bar drawn first, the green
   bar on top, so an empty bar still has an outline. Draw the two rects offset so
   the layering is obvious.
7. **v3 — colour that changes with health.** `if` / `elif` on the fraction:
   green above 0.5, orange above 0.25, red below. Ties the conditionals to the
   number she just worked out.
8. **v4, OPTIONAL** — a bar over every enemy, not just the boss; a bar that
   slides down smoothly instead of jumping; a number printed inside the bar.

**Slot 5 must be the drawer picture** she already knows: `["hp"]` as opening a
labelled drawer, `.centerx` as a machine you name, and a third panel showing
`.get("is_boss")` as *look in the drawer, and do not crash if it is empty*.

**Put a visible WAIT marker on every Make slide.** Kasim's own note: leave more
wait time before hinting.

### Reference deck for tone
`../2026-09-06/claire-hp-bar.html` — same student, the undelivered deck.

---

## 22:00 KST · 20:00 HCMC · DAVID P — `david-p-upside-down-pyramid.html`

**Track:** Minecraft **BLOCKS** (MakeCode) · **Korean glosses allowed**
**Read the BLOCKS TRACK section above before writing a single slide.**
**Topic (from the transcript):** the upside-down pyramid, one `step` variable
flips it.

He has no IDE account. **Zero Python anywhere in this deck.**

### Covered last week (transcript `2026/09/06 20:00`, 51 minutes)

- A `fill` block driven by **six variables** — `x1 x2 y1 y2 z1 z2`. His words at
  00:22:29: *"how many variables do we need? We need six variables."*
- Inside a `repeat`, each of the six changes by ±1 per pass — 00:27:23: *"X1
  this be minus one this will be one one this will be one minus one"*
- The repeat count went **13 → 100**. He tried 1,500 and 10,000.
- **The build was flipped and an upside-down shape was seen**: 00:30:51 *"now
  that we've done this, we actually do it in reverse"*, then 00:41:19 *"look at
  this. There's a pyramid of head down."*
- He found the size limit himself, 00:32:29 — Kasim: *"the maximum you can do is
  199 I believe"*, David: *"I think it's only 200 the maximum."*
- Block swaps with the code untouched: stone, cake, cobweb, beacon, snow, ice.
  Final build was ice — *"No, that's a big pyramid. That's a ice pyramid."*

### 🔴 The unmet promise — the agent-built inverted pyramid still has not run

The agent program (`give` block, `repeat`, `agent place`, `agent move forward`,
`agent move up`) was **typed out between 00:14:30 and 00:20:27 and never once
run.** Abandoned at 00:20:27: *"Okay. Well, this is taking a very long time. Um,
there is an easy way to do it... Let's get rid of everything."* Then *"Let me
show you the super super super duper the easy way."*

**The spoken reason was time, not his computer** — the ledger says the computer,
and that is a small correction worth knowing.

**Zero of last week's three planned ideas landed.** The words *step*, *offset*
and *one layer at a time* never appear in the transcript.

### 🔴 His machine is the real design constraint

- 00:06:13: *"It takes like five minutes just for a presentation to pop up.
  That's this computer."*
- CPU pinned at 100%, confirmed by David: Kasim *"your CPU is always at 100%,
  right?"* — David: *"Yes."*
- Minecraft took about two minutes to join.
- **A full crash at 00:43:58** — *"my character is crashing right now"* / *"I
  crashed out"* — needing a clear and a teleport rescue.

**What actually killed it:** huge `fill` volumes and animated or entity blocks
(cake, beacon, cobweb). Kasim at 00:42:32: *"this is going to break your game.
So, I want to stop this."*

**This does not rule out an agent build** — no agent program ever ran, so it is
untested. But the deck must **keep layer counts tiny and stay on plain stone**,
and it must teach `repeat 1` before `repeat 9`. Design for a slow machine: small
numbers first, every time.

### ✓ Wins to name in the Recap

- **Wrote his own `stop` chat command, unprompted**, 00:18:22: *"I'm also
  creating a code called stop in case the agent needs to stop."* Best moment of
  the lesson — keep `stop` in every drawing of his program.
- Predicted the crash before it happened: *"Yeah, I think this is going to cause
  the game lag."*
- Asked instead of guessing: *"Can you show me the variables you're using?"*
- Found undo himself: *"Oh, there's undo thankfully."*
- Reasoned about the inside of the shape: *"It's hollow... This is not hollow."*

### △ Real mistakes — turn each into a slot

- Walked around while the script ran, so blocks landed wrong. Kasim: *"That's
  because you're moving. So, don't move."*
- **Deleted his whole program** — *"Hey, I just deleted all my codes."* Pair this
  with his own undo discovery on one slide.
- Jumped straight from 100 to 1,500 to 10,000 with no step-up. **This is the
  habit the `repeat 1` technique fixes**, and it is now backed by a real crash.
- Chose animated blocks that broke the game.
- Got stuck in bedrock and needed a teleport.

**Two habits could NOT be confirmed** — where the agent must start for an
upside-down build, and counting the moves between layers. Neither was ever
tested, because the agent program never ran. Teach them fresh, not as revision.

**Homework was not returned:** 00:01:33 *"my mom forgot to send the homework."*
Keep the homework check to one gentle slide with no blame.

### Reached last week — `reached slide 16 of 70`

Last deck: `../2026-09-06/david-p-inverted-pyramid.html` (**70 slides**).
Slides 1–16 are the recap of the existing agent layer-walker. That content was
rebuilt live but **never run**. Slide 17 is where idea 1 begins.

**The carry — slides 17 to 70, 54 of 70, ALL FLAGGED `REWRITE ANCHORS`** because
the old deck writes Python text form and he drags blocks:
- 17–25 one number decides the direction (`step = -2` at 20, `side = side + step`
  at 21)
- 26–38 working out the start from the finish (the offset table at 31, the two
  move blocks at 32–33, `side = 1` at 34)
- 39–56 one layer at a time (`repeat 1` at 42, back to `repeat 9` at 45)
- 57–70 the stretch, hollow at 60

Method: the deck was grepped for `step`, `range(1)`, *widest* and *offset*, each
hit mapped to a slide, then the same terms checked against the transcript — none
were present.

### What today teaches

1. **Warm-up, short — his six-variable `fill` pyramid, redrawn as blocks.** One
   `repeat`, six `change ... by` blocks inside it. This is what his machine
   survives, and it is the foundation for everything today. Keep the repeat count
   at a small number in every drawing.
2. **The new idea: one variable decides which way the pyramid grows.** A `step`
   variable in the six `change` blocks. `step = 1` grows it, `step = -1` shrinks
   it. **Visual: the same pyramid twice, side by side, with only the sign
   different and the widest layer marked on each.**
3. **v1 — draw the two pyramids before any blocks.** Widest layer at the bottom,
   widest layer at the top. Mark the start square on each with a dot, and count
   the offset **on the picture**. He could not do this last week and it was never
   taught.
4. **v2 — put `step` into one `change` block**, then the second, then all six.
   One block per slide, six slides. Each one gets its own ✅ check.
5. **v3 — `repeat 1` first, then 3, then 9.** Build one layer, look at it, then
   raise the number. **This is the technique that fixes his real habit**, and it
   is now justified by his own crash. Teach it as a method with its own slide,
   never as advice. Draw one layer, three layers, nine layers as three pictures.
6. **v4 — the block type is a separate decision from the shape.** Plain stone
   while testing, the pretty block only once it works. Ties directly to the cake
   and beacon crash.
7. **v5, OPTIONAL** — a hollow pyramid (carry slide 60); a start-height variable
   so one number lifts the whole build off the ground; a `step` of 2 for a
   steeper pyramid; the sofa Kasim offered at 00:41:19 — *"Why don't you try to
   do a sofa?"* — as a free-build closer.

**Overshoot hard**, but remember every drawn build must use small numbers,
because his machine cannot take anything else.

### Reference deck for tone
`../2026-09-11/jaden-one-command-many-flowers.html` — correct blocks-track
drawing style. **Do not copy tone from
`../2026-09-06/david-p-inverted-pyramid.html`** — it is the right teaching in the
wrong notation.
