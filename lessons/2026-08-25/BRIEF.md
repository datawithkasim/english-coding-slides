# Today's decks — 2026-08-25 (Tue)

One deck per student, built from what the tracker says they last did and what was
promised for next time. Requested slots: JASON 17:00, HWON 18:00, LEO 20:00,
DAVID 21:00, YURA 22:00, JIYU 23:00 Korea time.

## Hard rules for every deck

Read first, in this order:
1. `../../TEMPLATE.md` — the slot structure and the per-slide rules
2. `../../PEDAGOGY.md` — why each slot exists
3. `../../assets/style.css` — the only styling allowed
4. One finished deck in the matching course folder, as the reference for tone

Then:
- Save to `lessons/2026-08-25/<file>.html`. Stylesheet path is
  `../../assets/style.css` and the script is `../../assets/deck.js`.
- **Overshoot on purpose.** Target **26–30 slides**, extras marked
  `<span class="activity-tag">OPTIONAL</span>`.
- Per-slide caps hold everywhere: **≤ 40 English words, ≤ 15 Korean words**.
- Slot 2 (Recap) must recall **that student's own last lesson**.
- △ lines are what the student actually got wrong — they become Common
  Mistake / Debug slides, not invented bugs.
- Big programs ramp v1→v2→v3→v4, new lines hot, old dim, OLD/NEW markers,
  📍 placement lines quoting the student's real file.

## JASON · 화 17:00 · ide track

Deck: `jason-finish-the-game.html` — Finish the Game (fix, boss levels, spread, win)

Facts (tracker draft 2026-08-18 + IDE `Homework/main.py`, edited 2026-08-25 15:45 KST):

- Game nearly complete: movement, 5 weapons, homing missiles + splash, two enemy
  types that shoot, boss with HP bar / bounce / bullets, combo multiplier, nukes,
  lives + invuln, power-up fall/catch, game over + retry, sprites
- He typed the power-up drop TODO himself — with a real bug:
  `"color": POWERUP_SIZE` (12 → near-black → invisible). That is v1's Bug Hunt.
- ✓ writes boundary conditionals independently
- △ syntax slips (commas, colon/equals) → deck repeats "read it back" checks
- promised (08-11 log): complete the boss, enemies shoot back, **finish** —
  Kasim wants a fully working game by end of today
- Deck ships the ending: v1 fix drop colour, v2 boss levels (hp/speed scale,
  abs() bounce), v3 boss 3-bullet spread (`.get("vx", 0)`), v4 BOSSES_TO_WIN +
  YOU WIN screen; final-test checklist instead of a 600-line full-program slide

## HWON · 화 18:00 · ide track

Deck: `hwon-drive-super-dario.html` — Drive Super Dario (events, keyboard, walls)

Facts (tracker draft 2026-08-18 + IDE `Workspace/main.py`):

- covered: RGB colors 0–255, `pygame.draw.rect()` four numbers, coordinate
  system (y down), `super_dario` + `bread` dictionaries with x/y/h/w/color/speed
- ✓ explained all four rect parameters unprompted
- △ waits for teacher to type first → deck adds explicit YOU-type moments
- promised (08-11 log): movement for the player, possibly enemy movement +
  color change — today is movement; enemy move + color are OPTIONAL stretch
- Real file state: both dicts drawn, sky-blue background, **no event loop**
  (✕ does nothing), h/w swapped in both draw calls (his real bug → Common
  Mistake slide), both dicts at the same spot (warmup moves the bread)
- Homework in flight: `name_art.py` (rectangles HWON) — separate worksheet, not
  this deck's topic

## LEO KIM · 화 20:00 · minecraft track (M002)

Deck: `leo-algorithms-nested-loops.html` — Intro to Algorithms (nested loops, changing variables — NOT fizzbuzz, Kasim's explicit brief)

Facts (tracker 2026-08-11, LEO KIM [PH] M002):

- covered: `for` loops + `range()`, coordinate variables `x_start`/`y_start`/`z_start`/
  `x_end`/`y_end`/`z_end`, `blocks.fill()` regions, incrementing loop variables each
  pass to grow structures
- ✓ found pattern X/Y +1, Z +2 unaided; picked `blocks.fill` correctly
- △ struggled adjusting start & end values together; rushed second task (tree)
- Today per Kasim: **intro to algorithms** — what an algorithm is (recipe of exact
  steps), nested loop (loop inside loop, rows × layers), variables that change each
  pass. Minecraft build context (e.g. staircase / stacked-wall / pyramid ramp),
  NOT fizzbuzz. v1→v4 ramp: v1 one row, v2 loop the row, v3 nest to stack layers,
  v4 change two variables per pass.
- Common Mistake slide from his real △: changing `y_end` but forgetting `y_start`
  (start & end must move together)

## DAVID · 화 21:00 · python track (RS001 text adventure)

Deck: `david-input-validation.html` — Validation loop + variables named by purpose

Facts (tracker 2026-08-11, DAVID G8):

- covered: `input()`, `if`/`elif` branching, `.lower()`, indentation & nesting,
  lists (`inventory.append()`, `if "item" in inventory`)
- ✓ self-fixed syntax error from Python's error message before teacher explained
- △ generic variable names (`name`, `question`); repeated `if` instead of `elif`
- promised: practice naming variables by purpose (`strike_or_leave`, not `name`)
- Today: RS001 week-04 territory — validate player input with a `while` loop
  (re-ask until the choice is valid), every new variable named by purpose.
  Common Mistake slides from his real △s: `if`/`if` instead of `if`/`elif`,
  and a variable called `question` that stores an answer.

## YURA · 화 22:00 · minecraft track (Coordinates, MC Education)

Deck: `yura-maze-conditionals.html` — Maze project: conditionals inside loops

Facts (tracker 2026-08-11, YURA G5):

- covered: aquarium build with `fill` + coordinates (glass 1,1,1→15,15,15, water
  2,2,2→14,14,14), `spawnAnimalAt`, `repeat` loop to spawn multiple animals
- ✓ persisted through wrong tries (0.5, 13) to find water-fill coordinate 14 unaided
- promised: **maze project — conditionals inside loops to create patterns**;
  4-week goal: house with stairs/roof/door using nested `repeat` + variables
- Today: start the maze — `if` inside a `repeat` loop decides wall vs gap
  (pattern building). Recap slide recalls her aquarium coordinates.
- Common Mistake: inner fill coordinates matching the outer shell (off-by-one —
  her aquarium 14-vs-15 discovery becomes the teaching moment)

## JIYU · 화 23:00 · minecraft track

Deck: `jiyu-3d-pixel-art.html` — 3D pixel art, first lesson (Kasim's brief today)

Facts (tracker 2026-08-11, JIYU [TASHKENT_LAMU]):

- covered: built her maze, needs to keep practising it
- promised was advanced mazes (if gold do x / if emerald do y) — **overridden by
  Kasim today: she moves onto 3D pixel art, this is her first lesson on it**
- Today: what pixel art is (grid of colored blocks), plan on paper grid → place
  block rows with loops → stack a second layer to make it 3D. Recap slide recalls
  her maze (loops + blocks she already knows).
- First-lesson framing: more worked examples, gentler Modify steps; OPTIONAL
  extras push to a small 3D letter or heart
