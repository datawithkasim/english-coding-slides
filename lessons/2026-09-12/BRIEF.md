# Today's decks — 2026-09-12 (Sat)

Seven lessons. **Three are Minecraft BLOCKS (MakeCode), three are IDE Python
(pygame / text Python / Manim), one is debate.** 08:10 → 20:45 Korea time.

**Kasim ran `/morning` the night before and then said: "ill leave you on all
night generate all slides please. FYI Jaden Shin ALL ENGLISH. ANDY ALL ENGLISH.
YUNGUN ALL ENGLISH."** That reply replaced the usual topic walkthrough, so
**the topics below were chosen by Claude**, each one from that student's own
ledger `gap`, their live IDE file, or their Drive transcript. Every pick is
named in that student's section with the evidence it came from.

| Time | Student | Track | Topic | Deck |
|---|---|---|---|---|
| 08:10 KST · 06:10 HCMC | YUNGUN | IDE Python (pygame) | the game does not just stop — a Game Over screen, then restart with R | `yungun-game-over-and-go-again.html` |
| 09:00 KST · 07:00 HCMC | SUHO | IDE Python (**text, not Minecraft**) | `input()` — the program asks a question and uses the answer | `suho-the-program-asks-you.html` |
| 11:00 KST · 09:00 HCMC | DEBATE [LEO + APRIL] | **Debate DB001** | Week 2 — existing course deck | `../../debate/db001-tech-ai/week-02.html` (existing, reused — **do not rebuild**) |
| 13:00 KST · 11:00 HCMC | JOY | MC **Blocks** | `repeat` — one loop walks the whole square | `joy-one-repeat-walks-the-square.html` |
| 18:00 KST · 16:00 HCMC | YURA | MC **Blocks** | the square becomes a spiral — `change side by 1` inside the loop | `yura-the-square-unrolls.html` |
| 19:45 KST · 17:45 HCMC | Dewy | MC **Blocks** | a loop inside a loop — the square fills in, then stacks | `dewy-a-loop-inside-a-loop.html` |
| 20:45 KST · 18:45 HCMC | ANDY | IDE Python (Manim) | `VGroup`, `self.wait` and `run_time` — ANDY sets the clock | `andy-andy-sets-the-clock.html` |

**Kasim's schedule for the day, in his own words (HCMC clock):**
> class from 610-650 and then 7-740. gym 830-1030. class from 11-11:50.
> cleaner 1-4. Yura at 4PM and Andy at 6:45.

---

## Report-only drift — nothing here was auto-fixed, no calendar event was renamed

- **No rename candidates existed.** Every calendar title matches a tracker
  `name` or `transcript_alias` exactly. `MS001 [화 9시]` is SUHO's
  `transcript_alias`, so it matched and was **not** renamed.
- **DEBATE [LEO + APRIL] is 11:00 KST = 09:00 HCMC, which sits inside the gym
  block Kasim named (08:30–10:30 HCMC).** He did not mention this class at all.
  Report it, change nothing.
- **Dewy 19:45 KST = 17:45 HCMC is not in Kasim's list either.** The calendar
  event is live and recurring, so the deck is built.
- **YUNGUN** — calendar says 08:00 KST, tracker `slot_time` says 08:10, Kasim
  said 06:10 HCMC (= 08:10 KST). Headings use Kasim's time.
- **YURA G5** has a live Saturday 18:00 KST calendar event but the tracker
  stores Tue 22:00 and `lesson_kind = experience`. `roster.json` folder is
  `yura-tue-2200`. Folder name is the join key — leave it.
- **SUHO** — tracker `track` still reads `MS004` (Minecraft) and `roster.json`
  files him under `ms001-fri-0900` with `app_user_id: null`. Both are stale;
  see his section.
- **JOY** — `transcript_alias` is still `JOY [EXPERIENCE LESSON]`. Joy is a
  regular student now with a real lesson 1 behind them.
- **`roster.json` slots are stale for YUNGUN** (`sat 20:00`, really 08:10).

## Transcripts

Drive "Meet Recordings" for **2026-09-05** holds five docs. Mapped by start
time (doc time = KST − 2):

| Doc (GMT+7) | = KST | Student |
|---|---|---|
| 07:10 | 09:10 | **SUHO** — `1GYkq0YYPu3D30rrvEzLsd1WI_19Xf6r9Xj5MovdKKYw` |
| 08:58 | 10:58 | DEBATE [LEO + APRIL] |
| 10:59 | 12:59 | **JOY** — `1hl6J-Dhe7EAv3yK8TPa_zx9km1GvABm5bXdpuuTlPKQ` |
| 15:59 | 17:59 | **YURA** — `1_h3KyfvaGFYAyOtcdQ2oujvZO67nOewP_k0vTiWUFHo` |
| 17:44 | 19:44 | **Dewy** — `1ESC7CZLgus4TkbPKhxsiE81cik5_x6MevIOit1r-3u8` |

**No doc exists for YUNGUN (06:10 GMT+7) or for ANDY (18:45 GMT+7).** Both were
prepped from their **live IDE file** instead, read SELECT-only from
`student_ide.files`. That file is stronger evidence than any transcript, because
it is the code actually on their screen right now.

---

## Hard rules for every deck

Read first, in this order:
1. `../../TEMPLATE.md` — the slot structure and per-slide rules
2. `../../PEDAGOGY.md` — why each slot exists
3. `../../assets/style.css` — the only styling allowed
4. The reference deck named in that student's section below, for tone

Then:
- Save to `lessons/2026-09-12/<file>.html`. Stylesheet `../../assets/style.css`,
  script `../../assets/deck.js`.
- **Overshoot on purpose.** No slide-count target and **no ceiling**. If the
  teacher could plausibly reach the last slide inside the hour, the deck is too
  short — add more taught ideas. Extra room goes to **new concepts with a visual
  each**, never more debug cards. Tag surplus `<span class="activity-tag">OPTIONAL</span>`.
- Update the `counter` span to `1 / <total>`.
- Per-slide caps: **≤ 40 English words, ≤ 15 Korean words**.
- Korean glosses only on Tier-3 vocab, concept hooks and bridges —
  **except YUNGUN and ANDY, whose decks carry no Korean at all** (see below).
- Only reuse existing CSS classes. No new inline component styling.
- Slot 2 (Recap) recalls **that student's own last lesson**, from the facts in
  their section below. Never generic.
- The △ lines are what the student actually got wrong. Turn each into a Common
  Mistake or Debug slot rather than inventing a bug.
- **Every slide carries a visual.** A heading plus a bulleted list is not a
  finished slide.
- **Never gendered pronouns.** No he / she / his / her anywhere in a deck. Use
  the student's name or *they*.

### ALL ENGLISH — YUNGUN and ANDY only

**Kasim's instruction tonight, verbatim: "ANDY ALL ENGLISH. YUNGUN ALL
ENGLISH."** In those two decks:
- `<html lang="en">`, no `<p class="bilingual">`, no `.ko` cells in a vocab
  table, no Korean in a pill, heading, bridge or closer.
- The vocab table keeps `term` + `gloss` and drops the `ko` column.
- Everything else about the deck is unchanged.

(The same instruction covers **Jaden Shin**, who does not teach today. Noted so
it is not lost.)

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

### The carry — read this before writing a single slide

Every student below has a **carry**: the slides of last week's deck the lesson
never reached. Decks are built to overshoot, so those slides are good, already
reviewed, and already in that student's voice.

- **Carry verbatim.** Copy the slide HTML across unchanged. Do not "improve" it.
- **Never carry** Slot 1 (title) or Slot 2 (Recap) — both are rebuilt from this
  week's facts.
- **Renumber after carrying:** the `counter` span, every `STEP n / total`, the
  `footer-tag` date, the Recap pill date, and the `<!-- N · SLOT -->` comments.
- **The carry is the start of today's deck, not the whole of it.** Today still
  teaches its new idea, and the deck still overshoots.

---

## BLOCKS TRACK — applies to JOY, YURA and Dewy

**All three drag MakeCode blocks.**

**Zero Python anywhere.** Not in a code block, not in a debug card, not in a
comment, not in a heading. The tracker logs for these three are written in
Python-ish text (`agent.move("forward", n)`, `agent.set_block_or_item()`)
because they are AI summaries of a recording — **that is not what these students
see or drag.** Redraw every one of those ideas as a block.

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

**The place-on-move switch is drawn as `agent place on move [ON]`** from the
AGENT drawer. `set_assist(PLACE_ON_MOVE, True)` is the Python-track form and
must never appear.

### Chat commands — the real starter layout

Kasim's own world uses **separate one-letter chat commands**, not one `"go"`:

- `rl` = `agent teleport to player` (re-line the agent)
- `r` = `agent turn right` · `l` = `agent turn left`
- `run` = the build itself

**A teleport block never goes inside `run`** — it makes the agent miss the first
block. Keep `rl` as its own command.

### Coordinates rule — all three block decks

**y starts at 0. x and z start at 1.** The first free square is `~1 ~0 ~1`.
Never write "coordinates start at 0" as one blanket rule. Counting a range is
unchanged either way: end minus start, then add 1.

### Reference decks for tone (blocks)
- `../2026-09-05/dewy-the-loop-turns-the-corner.html`
- `../2026-09-05/yura-one-repeat-many-steps.html`
- `../2026-09-10/jj-the-spiral-staircase.html`
- `../2026-09-11/jaden-one-command-many-flowers.html`

---

## 08:10 KST · 06:10 HCMC · YUNGUN — `yungun-game-over-and-go-again.html`

**Track:** IDE Python, pygame · **ALL ENGLISH, zero Korean**
**Topic (Claude's pick):** the game does not just vanish — a **Game Over
screen**, then **press R to play again**

### 🔴 READ THE LIVE FILE FIRST — it is the only truth about YUNGUN

There is **no Drive transcript** for 2026-09-05 (no doc anywhere near 06:10
GMT+7) and **no ledger file**. Everything below comes from his live
`student_ide` workspace `main.py`, last saved **2026-09-05 23:50 UTC** = Sunday
06 Sep 08:50 KST. This is what is on his screen right now, verbatim:

```python
import pygame
import random

pygame.init()
font = pygame.font.SysFont(None, 20)
score = 0
game_over = False

## COLORS ##
PASTEL_PINK = (255, 179, 186)
PASTEL_PEACH = (255, 223, 186)
PASTEL_YELLOW = (255, 255, 186)
PASTEL_MINT = (186, 255, 201)
PASTEL_CYAN = (186, 255, 255)
PASTEL_SKY_BLUE = (186, 225, 255)
PASTEL_LAVENDER = (202, 186, 255)
PASTEL_MAGENTA = (255, 186, 255)
PASTEL_LILAC = (230, 230, 250)
PASTEL_SALMON = (255, 214, 214)
## END COLORS ##

## SCREEN AND GRID ##
WIDTH, HEIGHT = 600, 600

CELL_SIZE = 20
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

MOVE_INTERVAL = 150

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

start_x, start_y = GRID_WIDTH // 2, GRID_HEIGHT // 2
snake_body = [(start_x, start_y)]

direction = (1, 0)
time_since_last_move = 0

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

    if time_since_last_move >= MOVE_INTERVAL:
        time_since_last_move -= MOVE_INTERVAL
        head_x, head_y = snake_body[0]
        ## IF ITS BIGGER THAN THE X or Y OR LESS THAN 0 or Y OR X ##
        new_head = (head_x + direction[0], head_y + direction[1])

        if (new_head[0] < 0 or new_head[0] >= GRID_WIDTH or new_head[1] < 0 or new_head[1] >= GRID_HEIGHT) or new_head in snake_body:
            running = False


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

    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()
```

**Use these exact names in every FIND string: `snake_body`, `new_head`,
`direction`, `spawn_food`, `food_rect`, `score_text`, `MOVE_INTERVAL`,
`PASTEL_*`, `game_over`, `running`.** Never `snake_pos`, never `GREEN`, never
`dx`/`dy` — they exist nowhere on his screen. **Never invent a colour name:**
only the ten `PASTEL_*` constants above exist.

### Reached last time — `reached the whole 09-05 deck except slides 64–69`

Last deck: `STUDENTS/students/yungun-sun-sat-2000/slides/` newest, same file as
`../2026-09-05/yungun-the-snake-that-keeps-going.html` (**80 slides**).
**Stop point found from the live IDE file**, not from a ledger or a transcript —
neither exists. Every idea up to slide 63 is provably in his code:

- food with `random` ✓ · `food_rect` drawn ✓ · eat and respawn ✓ ·
  `snake_body.pop()` in the `else` so the snake **grows** ✓
- `score` variable ✓ · `score_text` with an f-string, blitted at `(10, 10)` ✓
  (slides 59–63)
- `while True:` + `if pos not in snake_body` inside `spawn_food` ✓ (slides 70–72,
  reached out of order — **drop these from the carry, they are done**)
- wall hit **and** self hit end the game ✓ (slides 73–74, also done — drop)

**The carry — slides 64 to 69 of the 09-05 deck, verbatim:**

| Old # | Title |
|---|---|
| 64 | MOVE_INTERVAL is a wait, not a speed |
| 65 | Ten off, every bite |
| 66 | Bonus · Faster every bite ⚡ |
| 67 | What happens at square 30? |
| 68 | % wraps the number round |
| 69 | Bonus · Walk through the wall 🌀 |

Carry those six across verbatim, renumbered, as **optional extras near the end**
— they are not today's lesson. Drop everything else from that deck.

### What today teaches

Right now, when the snake hits a wall or itself, **`running = False` and the
window just disappears.** No message, no score, no way to play again. The
variable `game_over = False` sits on line 7 and is never used anywhere. Today it
gets its job.

Ramp it:

1. **v1 — warm-up debug, the real bug in his own file.** In `spawn_food`,
   `pos = ((random.randint(0, GRID_WIDTH) - 1), random.randint(0, GRID_HEIGHT-1))`
   puts the `- 1` **outside** the `randint(...)` brackets for x, but **inside**
   for y. So x can come back as **-1** and the food is drawn off the left edge,
   invisible, unreachable. Full OLD/NEW:
   - OLD `pos = ((random.randint(0, GRID_WIDTH) - 1), random.randint(0, GRID_HEIGHT-1))`
   - NEW `pos = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))`
   Draw the grid with a food square at x = -1 sitting off the edge. One slide for
   the symptom, one for the spot, one for the fix.
2. **v2 — stop closing the window.** Change the crash line from `running = False`
   to `game_over = True`, and make the movement block only run when the game is
   not over: `if not game_over and time_since_last_move >= MOVE_INTERVAL:`.
   Draw the loop as a box: the window keeps redrawing, the snake stops moving.
3. **v3 — the Game Over text.** A bigger font
   (`big_font = pygame.font.SysFont(None, 60)`), a `game_over_text` rendered from
   a plain string, blitted near the middle, **inside `if game_over:`**. Draw the
   600 × 600 window with the text centred so the position numbers mean something.
4. **v4 — show the final score too.** A second `render` with an f-string,
   blitted underneath. This reuses the f-string he already wrote for
   `score_text`, so it is a familiar move on a new line.
5. **v5 — press R to play again.** Inside the `KEYDOWN` branch, `if game_over and
   event.key == pygame.K_r:` and then reset **every** variable that changed:
   `snake_body`, `direction`, `food`, `score`, `game_over`,
   `time_since_last_move`. **This is the whole lesson** — one slide per variable
   reset, with a before/after value table, so "what does a restart actually mean"
   becomes concrete.
6. **Then push past it:** a `high_score` that survives the reset · a `paused`
   flag on the space bar, which is the same on/off idea as `game_over` · a
   three-second countdown before the snake starts moving again · a "press Q to
   quit" that sets `running = False` properly · the six carried slides above
   (speed-up, `%` wrap-around) as the last optional block.

### Turn the △ into a slot

The one recorded △ for YUNGUN (log 2026-08-29) is: *could not explain what a
loop variable means in a full sentence.* Give him a **say-the-sentence** slide
for the new flag: "`game_over` is True when the snake has crashed, so the snake
stops moving but the window stays open." One sentence, read aloud, then a
fill-the-blank twin. `.frame-card` with visible `___` blanks.

**Reference deck:** `../2026-09-05/yungun-the-snake-that-keeps-going.html` — for
tone, for the ramp style, and for the exact variable names. Match them, never
rename.

---

## 09:00 KST · 07:00 HCMC · SUHO — `suho-the-program-asks-you.html`

**Track:** IDE Python, **text Python in the app IDE** · **Korean glosses allowed**
**Topic (Claude's pick):** `input()` — the program asks a question and then uses
the answer

### 🔴 SUHO IS NOT ON MINECRAFT ANY MORE. THIS IS NOT A BLOCKS DECK.

The tracker still says `track = MS004` and `roster.json` still files SUHO under
`ms001-fri-0900`. **Both are stale.** The Drive transcript for 2026-09-05
(`1GYkq0YYPu3D30rrvEzLsd1WI_19Xf6r9Xj5MovdKKYw`, 07:10 GMT+7) opens with Kasim
saying *"this is actually our Minecraft lesson, but we're not going to be doing
this"* and the whole 38 minutes are spent in the text IDE. **Zero MakeCode
blocks in this deck. No `.mcb` markup anywhere.**

SUHO has an app account: username `SUHO`, created 2026-08-30, and his live
workspace `main.py` was saved during that lesson. Verbatim, right now:

```python
favorite_food = 'pepperoni pizza'
favorite_color = 'rainbow'
favorite_animal = 'hamster'

print('I like to eat ' + favorite_food)
print('my favorite color is ' + favorite_color)
print('my favoite animal is ' + favorite_animal)
```

(The typo `favoite` on the last line is really in his file. Use it — see below.)

### Covered last time (transcript, 2026-09-05)

- The IDE itself: where the editor is, where **Run** is (top right), reading the
  output
- `print(...)` from absolutely zero — the three-step ritual Kasim drilled by
  name: **step 1 `print` · step 2 parentheses · step 3 apostrophes**
- Typing his own sentences inside the quotes: *"Hello, my name is …"*,
  *"I am going to the beach tomorrow"*, *"My favorite subject is math, science
  and social"*, *"My favorite candy is gum candy"*, *"I like eating chicken"*,
  *"My favorite animal is hamster"*
- **Variables**: `favorite_food = 'pepperoni pizza'`, then `favorite_color`, then
  `favorite_animal`
- **Joining text with `+`**: `print('I like to eat ' + favorite_food)`
- Underscores in a variable name matter — he deleted them and it broke
- ✓ Fixed his own `print` spelling after being asked to spell it out loud
- ✓ Ran the file himself and read the output back correctly, several times
- △ **Put text outside the quotes or outside the parentheses**, over and over —
  Kasim says the word "inside" more than twenty times in the transcript
- △ Spelled `print` wrong (`rint`, doubled letters), and doubled the quote marks
- △ Deleted the underscores out of `favorite_color` and the program broke

**Promised:** the transcript's own next-step line — *"continue coding exercises
from the current progress point in next week's session."* Nothing narrower.

**Lesson length:** only about 38 minutes and it started 10 minutes late (Kasim's
computer was updating). So less ground was covered than a normal hour.

### Reached last time — `no carry`

Last deck `../2026-09-05/suho-one-repeat-every-layer.html` (112 slides) is a
**Minecraft blocks deck and none of it was taught** — the lesson changed track on
the spot. **Carry nothing from it.** Do not copy its recap, its blocks, or its
rainbow tower. Today's deck is built fresh on the transcript and the file above.

### What today teaches

Right now the program only ever says the same three sentences. Today **the
program asks SUHO a question and uses the answer.**

Ramp it, in very small steps — he is 9, in grade 4, and typing is the hard part:

1. **v1 — his own file on screen, read aloud.** The three variables and the
   three `print` lines. One slide that re-draws a variable as a labelled box with
   text inside it, so `favorite_food` is a box holding `'pepperoni pizza'`.
2. **v2 — find the typo.** `my favoite animal is` — the real typo in his file.
   Show OLD / NEW. The program still runs, and that is the point: **Python does
   not check English spelling, only its own.** One slide.
3. **v3 — the three-step ritual, re-drawn.** Kasim's own step 1 / step 2 / step 3
   from the transcript, as three frames: `print` → `print()` → `print('')`.
   Reuse it as the visual pattern for the whole deck.
4. **v4 — `input()`.** `name = input('What is your name? ')` then
   `print('Hello ' + name)`. Draw it as: the program stops, a blinking box waits,
   SUHO types, the box hands the text to the variable. **This is the lesson.**
5. **v5 — ask for the favourites instead of typing them.** Change
   `favorite_food = 'pepperoni pizza'` into
   `favorite_food = input('What is your favorite food? ')`. Same three print
   lines underneath, untouched — and now the program says something different
   every run. OLD/NEW for each of the three lines, one slide each.
6. **Then push past it:** an f-string as a shorter way to join
   (`print(f'I like to eat {favorite_food}')`) shown **next to** the `+` version
   he already knows · `input()` with a number and `int(...)` so
   `age` can do `age + 1` · a two-question quiz program · `\n` for a blank line ·
   a tiny "about me" program that asks four questions and prints a paragraph.

### Turn the △s into slots

- **Inside vs outside.** A `.compare-row`: `print('hello')` in green against
  `print()'hello'` and `print(hello')` in red. Then a *point-at-the-inside* slide
  with an arrow showing exactly where the cursor must be. This is his single
  biggest problem — give it three slides, not one.
- **Spelling `print`.** A slide that spells it P-R-I-N-T one letter per box,
  then a find-the-broken-one card with `pirnt`, `Print`, `print`.
- **The vanishing underscore.** `favorite color` vs `favorite_color` side by
  side with the red error the broken one produces.

**Reference decks:** `../../python/pygame-starter/` for slot structure, and
`../2026-09-09/yoojun-first-square.html` for the tone a true beginner needs.
**Do not** use his own 09-05 Minecraft deck as a reference — wrong track.

---

## 11:00 KST · 09:00 HCMC · DEBATE CLASS [LEO + APRIL] — **no new deck**

Week 2 of DB001. Reuse the existing deck
`../../debate/db001-tech-ai/week-02.html`. Week 1 ran with this group on
2026-09-05.

**Do not rebuild it, do not run `build-debate-decks.py`** — that script wipes the
hand-built debate decks. Link it from the day `index.html` only.

Student folders `leo-debate-sat-1100` and `april-debate-sat-1100` exist but have
no `roster.json` entry, so **nothing is copied** into them.

**Flag for Kasim:** this class sits inside the gym block he named this morning.

---

## 13:00 KST · 11:00 HCMC · JOY — `joy-one-repeat-walks-the-square.html`

**Track:** Minecraft **BLOCKS** · **Korean glosses allowed**
**Topic (Claude's pick):** `repeat` — one loop walks the whole square

### Covered last time (ledger `joy-sat-1300.json`, 2026-09-05, from the transcript)

- `on chat command` blocks
- `rl` = `agent teleport to player`
- `r` / `l` = `agent turn right` / `agent turn left`
- The difference between turning and moving; turning around = the same side twice
- `run` = `agent move forward` with a number of squares
- `agent move up`
- Chaining several moves inside one command
- `agent place on move` + `agent set block`
- **The agent places the block in the square it just left**
- Built a line, an L shape, and a stepped L

**`gap`: none.** Everything promised to the parent landed.
**Homework concept:** `agent-place-on-move`. The worksheet sent was the existing
Builder Basics sheet `placing-blocks-beginner.pdf` plus `placing-blocks.mcworld`.

**△ to turn into a slot:** none is recorded from the lesson. Use the two
mistakes the 09-05 deck already anticipated — switching place-on-move OFF one
step too early, and a corner turned the wrong way.

### Reached last time — `reached slide 53 of 61`

Last deck: `../2026-09-05/joy-lesson-1-the-agent-obeys.html` (**61 slides**).
Stop point mapped from the ledger `actual`: the last bullet is the stepped L,
which is the deck's *"Side one / Corner one / Side two / Finish the square
yourself"* run, slides 50–53.

**The carry — slides 54 to 61 of the 09-05 deck, verbatim:**

| Old # | Title |
|---|---|
| 54 | Eight blocks, or two |
| 55 | OFF in the middle makes a gap |
| 56 | Switch it off at the end |
| 57 | Walk away and leave a gap |
| 58 | The line stops, the robot does not |
| 59 | You gave orders, in order |

Slide 54 (*"Eight blocks, or two"*) is the deck's own preview of `repeat` — it is
**the perfect opening for today**, so carry it early rather than at the end.
Slides 55–58 (gaps with place-on-move OFF) carry as a later block. Skip 59–61
(closers).

### What today teaches

JOY can already write out a square the long way: forward, turn, forward, turn,
forward, turn, forward, turn. Eight blocks. **Today one `repeat` does all four
sides.**

Ramp it:

1. **Warm-up, short** — the stepped L from last week, redrawn, with the
   builds-behind rule as a picture: the agent square highlighted one colour, the
   block square behind it another. One or two slides, then move on.
2. **v1** — the square written the long way, drawn as blocks inside `run`.
   Circle the repeating pair (one forward, one turn).
3. **v2** — `repeat 4 times` from the LOOPS drawer, wrapped around **one**
   forward and **one** turn. Eight blocks become two. **This is the lesson.**
4. **v3** — one frame per pass on a top-down grid, arrow showing the facing
   after each turn. Four frames, then the closed square.
5. **v4** — change the `4` to `3`, then to `6`. The repeat count decides the
   shape. Draw both results.
6. **v5** — `agent place on move [ON]` above the loop, so the square draws
   itself in blocks.
7. **Then push past it:** place-on-move OFF *inside* the loop for a dotted
   square (carried slides 55–58 land here) · a `repeat` inside a `repeat` for a
   thicker wall · `agent move up` outside the loop to start a second layer · a
   letter shape built from two loops.

**Reference decks:** `../2026-09-05/dewy-the-loop-turns-the-corner.html` (the
same lesson, one step further along, for a student one week ahead) and
`../2026-09-11/jaden-one-command-many-flowers.html`.

---

## 18:00 KST · 16:00 HCMC · YURA — `yura-the-square-unrolls.html`

**Track:** Minecraft **BLOCKS** · **Korean glosses allowed**
**Topic (Claude's pick — this is the recorded `gap`, so it outranks everything
else):** the square becomes a **spiral** — `change side by 1` inside the loop

### Covered last time (ledger `yura-tue-2200.json`, 2026-09-05, from the transcript)

- `repeat 4` builds a square
- The repeat **count** decides the shape — 6 instead of 4 and the middle fills in
- Reading the code out loud to find the wrong block
- Made a variable `side`
- `agent move forward by side`
- Changed `side` to 4, then 10, then 8 to see the square resize
- Started stacking one more layer on top of the square — **not finished**

### 🔴 The `gap` — the parent was told this would happen and it did not

> "나선까지 가지 못했어요. 정사각형 위에 한 층을 더 쌓는 것을 같이 해 보다가
> 수업 시간이 다 되어 나선은 다음 시간으로 옮겼어요. 수업 시작도 6분 정도 늦게
> 열렸어요."

**The spiral is today's topic.** The lesson also started about six minutes late.

**Homework concept:** `move-up-between-two-squares` — worksheet
`homework-the-second-square-2026-09-05.md`. It picks up exactly where the lesson
stopped: lift the agent one level and build square two. **Check it in the
warm-up**, then go to the spiral.

**△ to turn into a Debug slot:** the ledger's `note` records that last week's
homework was not done, and that Yura reads code aloud to find a wrong block.
Build the debug slide around a `change side by 1` placed **outside** the loop —
the square never grows — and let Yura read the blocks aloud to find it.
**Never put an effort or homework-not-done line on a slide.**

### Reached last time — `reached slide 47 of 72`

Last deck: `../2026-09-05/yura-one-repeat-many-steps.html` (**72 slides**).
Stop point mapped from the ledger `actual`: the last confirmed bullets are the
`side` variable, `agent move forward by side`, and changing its value — the
deck's slides 44–47 (*"A box that holds a number" → "Every side is 1"*).

**The carry — slides 48 to 72 of the 09-05 deck, verbatim:**

| Old # | Title | Use it as |
|---|---|---|
| 48 | Grow the box each pass | **today's core** |
| 49 | The square became a spiral | **today's core** |
| 50 | What is in the box? | today's core |
| 51 | Change side outside the mouth | today's Debug slot |
| 52 | Make the spiral bigger | today's core |
| 53 | Eight passes | today's core |
| 54–56 | Letter H · find the block · the fix | warm-up debug |
| 57 | The switch can live in the mouth | push-past block |
| 58–60 | New program: dots · a dotted border ×2 | push-past block |
| 61 | A loop inside a loop | push-past block |
| 62–64 | New program: box · a wall three high · three layers | push-past block |
| 65–67 | New program: stairs · forward and up, one loop · bridge grew stairs | push-past block |
| 68–71 | Say it out loud · Build it yourself · Go further · One question | closers |

That is a very large carry — **use it**, renumber it, and build the new material
in front of it rather than rewriting it.

### What today teaches

`side` already exists and already resizes the square. **Today `side` changes
while the loop is running**, so the four walls stop meeting and the square
unrolls into a spiral.

Ramp it:

1. **Warm-up, short** — the second square from the homework sheet: `agent move
   up` between two `repeat 4` loops. Two or three slides. Then move on.
2. **v1** — the square with `side` in the number hole, exactly as Yura left it.
   Ask what happens if `side` gets bigger *between* walls.
3. **v2** — `change side by 1` from the VARIABLES drawer, dropped **inside** the
   loop, as the last block. One frame per pass on a grid: 1, 2, 3, 4 squares
   long. The spiral appears. **This is the lesson.**
4. **v3** — the Debug slot: the same block **outside** the loop. Same picture,
   square not spiral, side by side.
5. **v4** — `repeat 8 times` instead of 4. The spiral wraps twice.
6. **v5** — `change side by 2`. A fatter spiral.
7. **Then push past it:** the carried dotted-border, loop-inside-loop, wall and
   staircase blocks · a spiral that also climbs, by adding `agent move up` inside
   the loop · turning right instead of left and predicting the mirror image.

**Reference decks:** `../2026-09-05/dewy-the-loop-turns-the-corner.html` and
`../2026-09-10/jj-the-spiral-staircase.html`.

---

## 19:45 KST · 17:45 HCMC · Dewy — `dewy-a-loop-inside-a-loop.html`

**Track:** Minecraft **BLOCKS** · **Korean glosses allowed**
**Topic (Claude's pick):** a **loop inside a loop** — the square stops being an
outline and fills in, then stacks

### Covered last time (ledger `dewy-sat-2200.json`, 2026-09-05, from the transcript)

- `repeat` for a repeating shape
- **Turning** (facing changes, square does not) vs **walking** (square changes)
- `agent place on move`
- A fence, with the last gap filled by a `back by 1` **outside** the loop
- Made a variable `side`
- `agent move forward by side`
- `side + side` and `side × side` to check what the value is
- `change side by 1`
- **A value that grows inside the loop turns the square into a spiral**

**`gap`: none.** The lesson actually overshot its promise.
**Homework concept:** `variable-grows-inside-repeat` — worksheet
`homework-the-snail-shell-2026-09-05.md`, which rebuilds the spiral and adds
`change side by 2`.

**△ to turn into a slot:** the older recorded △ is mixing up **which way the
agent faces** versus **which way it moves**. The 09-05 deck gave that nine
pictures and the ledger says it landed, so today it needs a **short** retrieval
check, not a re-teach. One slide.

### Reached last time — `reached slide 56 of 73`

Last deck: `../2026-09-05/dewy-the-loop-turns-the-corner.html` (**73 slides**).
Stop point mapped from the ledger `actual`: the last bullet is the spiral from a
growing `side`, which is the deck's slides 49–55 (*"A side that grows" → "Fill
the size row"*), and slide 56 is *"The same trap as last week"*.

**The carry — slides 57 to 73 of the 09-05 deck, verbatim:**

| Old # | Title | Use it as |
|---|---|---|
| 57 | A loop inside a loop | **today's core** |
| 58 | Make the move one square | **today's core** |
| 59 | Add a second repeat | **today's core** |
| 60 | Move the step inside | **today's core** |
| 61 | Same square, two loops | **today's core** |
| 62–64 | What if it turns right? · Flip the dropdown · Left or right, same ring | push-past block |
| 65–68 | Place before the turn · Switch place on move OFF · Place, then turn · One block per corner | push-past block |
| 69–72 | Say the loop out loud · Build a pen for the sheep · If there is time · One question | closers |

Slides 57–61 are exactly today's new idea, already written. **Carry them, then
build around and past them** — they are five slides and today needs far more.

### What today teaches

Dewy's `repeat` draws an **outline**. Today a second `repeat` **inside** the
first turns the outline into a filled floor, and then into a stack.

Ramp it:

1. **Warm-up, short** — the snail-shell homework: the spiral, and `change side
   by 2`. Two slides. Plus one retrieval card on turn-vs-move.
2. **v1** — the outline square as Dewy left it. Then the picture of what a
   **filled** square looks like on the grid. Ask how many squares that is.
3. **v2** — the carried slides 57–61: one row first, then a `repeat` around the
   row, then the turn moved to the outer loop. **This is the lesson.**
4. **v3** — one frame per pass of the **outer** loop, with a counter chip showing
   which row is being laid. Five frames.
5. **v4** — swap the inner count and the outer count, and watch a 5 × 3 floor
   become a 3 × 5 floor. Same blocks, two numbers.
6. **v5** — `agent move up` between the outer passes, and the floor becomes a
   **solid cube**. A third loop wrapped around the whole thing.
7. **Then push past it:** the carried right-turn mirror block · the carried
   place-on-move-in-the-mouth block (one block per corner) · a floor that changes
   block type per row using the inventory slot Dewy already knows · a
   `repeat` inside a `repeat` where the inner count is the variable `side`, so
   the floor grows as it climbs.

**Reference decks:** `../2026-09-10/jj-the-spiral-staircase.html` and
`../2026-09-09/seohoo-two-numbers-one-tower.html`.

---

## 20:45 KST · 18:45 HCMC · ANDY — `andy-andy-sets-the-clock.html`

**Track:** IDE Python, **Manim** · **ALL ENGLISH, zero Korean**
**Topic (the open promise, verbatim from the ledger `gap`):** `VGroup`,
`self.wait` and `run_time` — ANDY decides how long things take

(The tracker still stores `WD002` / `JAVASCRIPT`. That is a stale join key.
ANDY is on Manim.)

### 🔴 The open promise — the parent was told this and it is not proved

`ledger/andy-sat-2045.json`, row 2026-09-05:

> **promised:** `self.play(a, b, c)`로 여러 개를 한 번에 움직이기, `VGroup`으로
> 도형 묶기, `self.wait`과 `run_time`으로 시간 정하기
> **gap:** 확인 불가 — no Gemini transcript exists for that slot. The saved
> workspace shows only `self.play(Create, Create, Write)` and
> `self.play(shift, shift, shift)`. **No `VGroup`, no `run_time`, no
> `self.wait`.**

So **one third of that promise landed and two thirds did not.** Today closes it.

### The live file — read it first

`student_ide` workspace `main.py`, last saved **2026-09-06 09:02 UTC** = Sunday
18:02 KST. That is **after** the lesson, so this is ANDY's completed homework:

```python
# HOMEWORK - Many at Once
# Worksheet: homework-many-at-once-2026-09-05.pdf

from manim import *

CYAN = "#00FFFF"
ICE = "#E0F7FA"
WHITE = "#F8FAEE"
BLUE = "#0044FF"



class MotionScene(Scene):
    def construct(self):
        circle = Circle(color=ICE)
        square = Square(color=WHITE)
        title = Text("Shapes")

        self.play(Create(circle), Create(square), Write(title))

        self.play(
            circle.animate.shift(LEFT*3),
            square.animate.shift(RIGHT*3),
            title.animate.shift(UP*3)
            )
```

**Every FIND string comes from this file.** Names on his screen: `MotionScene`,
`circle`, `square`, `title`, `CYAN`, `ICE`, `WHITE`, `BLUE`. Do not rename them
and do not invent new colour constants.

**The homework is done** — open the deck by running it and praising it, then
build straight on top of it.

### Covered last time (log + draft 2026-08-29, plus the file above)

- Manim structure: `Scene`, `construct`, `self.play`
- `Circle()` — colour, radius, `.set_fill()` for fill colour and opacity
- Hex colour codes (`#00FFFF`, `#0A1128`)
- `Square()` and `Transform()`
- `Text()`; `.animate.shift()`, `.animate.rotate()`, `.animate.scale()`,
  `.animate.move_to()`
- **Several animations inside one `self.play(a, b, c)`** — proved by the file
- ✓ Spotted that a circle animation did not close fully, using the timeline
  scrubber
- ✓ Predicted that a negative shift moves text downward, then tested it
- △ Needed repeat guidance on **why `.animate` is required**
- △ `move_to()` uses Manim units, not pixels — kept expecting pixels

**Standing instruction (`promised`, 2026-08-22):** *"Andy types code first, help
only when needed. Practice autocomplete to build method-name familiarity."* Not
a topic — a way of running the hour. **Write every step slide as an instruction
to ANDY, not a demo for Kasim.**

### Reached last time — `reached slide 35 of 71`

Last deck: `../2026-09-05/andy-many-things-at-once.html` (**71 slides**).
Stop point read straight off the live file: `self.play(Create(circle),
Create(square), Write(title))` and the three simultaneous `.animate.shift` calls
are the deck's **v3**, slides 29–35. `VGroup` starts at slide 36 and appears
nowhere in his code.

**The carry — slides 36 to 71 of the 09-05 deck, verbatim:**

| Old # | Title | Use it as |
|---|---|---|
| 36 | v4 — three shapes, one object | **today's core** |
| 37 | VGroup is a bag | **today's core** |
| 38 | Tie them together | **today's core** |
| 39 | Move all three as one | **today's core** |
| 40 | Mistake — the group made too early | **today's core** |
| 41 | The same .animate rule | today's core |
| 42–47 | v5 — ANDY sets the clock · self.wait(1) = 15 still frames · Hold the picture · Stretch one play · run_time stretches the frames · Land the ending | **today's core** |
| 48–54 | Your whole scene · Say it out loud · Q1 · Q2 · ANDY drives · Before you go · closer | rebuild, do not carry the closers |
| 55–56 | Together, or one after another? · Stagger the entrance (`LaggedStart`) | push-past block |
| 57–59 | move_to is an address · Send the square to an address · Two changes, one second | push-past block — **this is the pixels-vs-units △** |
| 60–63 | Placing without numbers · Park the text above the circle · .arrange() tidies the bag · Line the group back up | push-past block |
| 64–68 | A shape that keeps up · A rubber band · Clear the stage · Animations that need no .animate · The whole timing toolkit | push-past block |
| 69 | Mistake — run_time in the wrong brackets | push-past block |

This is a 36-slide carry covering the entire promise. **Carry it verbatim and
renumber**, then add genuinely new material on top so the deck still overshoots.

### What today teaches

Slides 36–47 above **are** the lesson: `VGroup`, `self.wait`, `run_time`. Build
the recap and the ramp fresh around them, then extend.

New material to add beyond the carry (the carry alone is not enough for an hour
and a half of overshoot):

- **`Rotate` and `.animate.rotate()` on a VGroup** — the whole bag spins as one.
- **`AnimationGroup` with `lag_ratio`** as the honest version of `LaggedStart`.
- **`ReplacementTransform` vs `Transform`** — why the old shape sometimes stays
  behind. This is a real Manim trap and ANDY has used `Transform` already.
- **`ValueTracker` + `always_redraw`** for a number that counts up on screen,
  if there is room. Tag it `OPTIONAL`.
- **A finished 15-second scene** that uses everything: create, group, move
  together, wait, stretch one beat, fade out.

### Turn the △s into slots

- **Why `.animate`:** two lines side by side — `self.play(square.shift(RIGHT))`
  (jumps, no animation) against `self.play(square.animate.shift(RIGHT))`
  (slides). Same picture twice, one arrow. `.compare-row`.
- **Units, not pixels:** a drawn Manim frame with the axis marked — 8 units tall,
  about 14.2 wide, centre `0, 0`. `move_to([3, 0, 0])` lands on a marked spot.
  **Never say "pixels".** Carried slides 57–59 already do this; keep them.

**Reference deck:** `../2026-09-05/andy-many-things-at-once.html` — match its
variable names and its tone. **Strip every Korean line out of anything carried
from it.**
