# Today's decks — 2026-09-02 (Wed)

Six lessons, 15:00 → 21:00 Korea time. Five need a deck; EUNWOO's is already
built and is copied in unchanged.

**Roster source of truth today is the calendar, not `tools_students`.** Kasim
confirmed the six by name this morning: SEOHOO, EUNWOO, NEO, YUNA, LUCY (one-off)
and 이현 (LEE HYEON). The tracker is stale in four places — see the drift note at
the bottom.

**Topics are Kasim's, given this morning. They override `promised`.**

| Time | Student | Topic Kasim gave | Deck |
|---|---|---|---|
| 15:00 KST · 13:00 HCMC | SEOHOO | pixels | `seohoo-pixels-with-a-loop.html` |
| 17:00 KST · 15:00 HCMC | EUNWOO | (built deck, unchanged) | `eunwoo-see-the-numbers.html` |
| 18:00 KST · 16:00 HCMC | NEO | *(Kasim did not name — enemy bullets hit the player + player health)* | `neo-bullets-that-hurt.html` |
| 19:00 KST · 17:00 HCMC | YUNA | *(Kasim did not name — loop through a whole dictionary)* | `yuna-every-team-at-once.html` |
| 20:00 KST · 18:00 HCMC | LUCY | speech contest delivery practice | `lucy-say-it-in-time.html` |
| 21:00 KST · 19:00 HCMC | 이현 | mazes, from today | `ihyeon-maze-first-turn.html` |

## Hard rules for every deck

Read first, in this order:
1. `../../TEMPLATE.md` — the 20-slot structure and the per-slide rules
2. `../../PEDAGOGY.md` — why each slot exists
3. `../../assets/style.css` — the only styling allowed
4. The reference deck named in that student's section below, for tone

Then:
- Save to `lessons/2026-09-02/<file>.html`. Stylesheet path is
  `../../assets/style.css`, script is `../../assets/deck.js` — this folder sits
  two levels deep, same as every other lesson folder.
- **Overshoot on purpose.** No slide-count target and **no ceiling**. If the
  teacher could plausibly reach the last slide inside the hour, the deck is too
  short — go back and add taught ideas. Extra room goes to **new concepts with a
  visual each**, never more debug cards. Tag surplus slides
  `<span class="activity-tag">OPTIONAL</span>`.
- Update the `counter` span to `1 / <total>`; check `deck.js` for how it counts.
- Per-slide caps: **≤ 40 English words, ≤ 15 Korean words**.
- Korean glosses only on Tier-3 vocab, concept hooks and bridges.
- Only reuse existing CSS classes. No new inline component styling.
- Slot 2 (Recap) recalls **that student's own last lesson**, from the facts in
  their section below. Never generic.
- The △ lines are what the student actually got wrong. Turn each into a Common
  Mistake or Debug slot rather than inventing a bug.

### Shape of the hour — Kasim's instruction, 2026-09-02

> "Spend a **short** time reviewing last week and **THEN most of the time**
> exploring a new concept."

So: recap and warm-up are the first few slots only. The bulk of every deck is the
new idea. A deck that spends half the hour on last week is a failed deck.

### Copy-this-and-it-works contract

The student makes **zero decisions**. If a slide needs the student to infer
anything, it is wrong.

- **One change per slide**, numbered `STEP n / total`. A re-indent is its own step.
- Every code step carries all four:
  - **the code** — full OLD block and full NEW block, never `...` inside a
    changed region
  - **🔍 FIND** — the exact string to search for (or, on the block track, the
    exact block to look at)
  - **📍 where** — quote the existing line it goes under, and the indent count
  - **🟣 why** — one line
  - **✅ check** — one line: what running it should show
- **Big programs ramp v1 → v2 → v3 → v4.** Never the finished program first. New
  lines hot, unchanged lines dim, changed lines get an explicit OLD/NEW block.
- **Visuals beat words, and are mandatory for loops, iteration and any maths** —
  one frame per pass with the counter value shown; spacing as boxes on a number
  line; x positions as jumps.

### API form — Minecraft Python (EUNWOO only today)

```python
blocks.fill(QUARTZ_BLOCK, pos(2, 0, 0), pos(4, 6, 0))
agent.move(FORWARD, 5)
```

Bare CAPS constants. No quotes. `agent.move("forward", 5)` is wrong and will not
run. Never copy API form from `../2026-08-29/dewy-agent-loops.html` — that deck
uses the string form.

### Block track — SEOHOO and 이현 only

**Kasim's call, 2026-09-02: their slides DRAW THE BLOCKS.** These two drag blocks
in MakeCode and do not read Python. A slide must be a picture of the thing on
their screen, using the words printed on the real block.

New CSS components exist for this in `assets/style.css` — use them, do not invent
markup:

```html
<div class="mcb-c player">
  <div class="hat">on chat command <span class="val">"go"</span></div>
  <div class="mcb-in">
    <div class="mcb agent">agent move <span class="dd">forward</span> <span class="val">5</span></div>
    <div class="mcb agent">agent turn <span class="dd">left</span></div>
  </div>
</div>
<p class="mcb-from">from the <span class="drawer" style="background:#5c2d91">Agent</span> drawer</p>
```

- `.mcb-c` = a C-shaped block that wraps others (`on chat command`, `repeat`,
  `if`). Its `.hat` is the top bar, its `.mcb-in` holds the blocks inside.
- `.mcb` = a single block. Category class sets the colour: `player` `agent`
  `blocks` `pos` `mobs` `loops` `logic` `vars` `math`.
- `.dd` = a dropdown hole · `.val` = a white number or text hole · `.ovar` = a
  variable oval · `.swatch` = a colour square for a wool or concrete colour.
- `.mcb-drop` = an empty dashed socket, for "drag the next block in here".
- `.hot` / `.dim` on `.mcb` or `.mcb-c` mean the same as in the text decks: hot =
  the block added this step, dim = already there.
- `.mcb-from` names the toolbox drawer the block comes from. Every new block gets
  one, so the student can find it without help.

**Never show Python text to these two.** No `agent.move(FORWARD, 5)` anywhere in
their decks — not in a code block, not in a debug card, not in a comment.

### Coordinates rule — both block decks

y starts at **0**. x and z start at **1**. Never say "coordinates start at 0" as
one blanket rule; that is the exact thing SEOHOO keeps getting wrong.

---

## 15:00 KST · 13:00 HCMC · SEOHOO — `seohoo-pixels-with-a-loop.html`

**Track:** MS001, Minecraft **BLOCKS** (MakeCode) · **Source:** log + draft, 2026-08-26
**Topic Kasim gave:** pixels
**Reference deck for tone:** `../2026-08-31/yunho-pixel-art-bigger.html` and
`../2026-09-01/jiyu-pixel-art-with-loops.html` — **for structure and pacing only.
Both are Python-text decks. Redraw every code idea as blocks.**

**Covered last time**
- 3D block placement using x, y, z
- Working out a coordinate range by counting the start and the end block
- The rule that y starts at 0
- Running, checking the result, fixing the error
- Building a structure with more than one layer

**✓ Wins** — worked out the x range 6→11 on his own, then spotted and fixed a
wrong y with no prompt. Got x 3→13 right while stacking several layers.

**△ Got wrong (turn these into Debug / Common Mistake slots)**
- Still not solid that y starts at 0 — began ranges at 1, and miscounted the end
  block several times
- Guessed coordinates instead of counting the blocks

**Homework he was set (26 Aug)** — build a 15×15 pixel creeper face on the wall
in `pixel-art-homework-2026-08-26.mcworld`, 172 lime wool and 53 black wool, then
a bug hunt on paper. He has no IDE account, so nothing confirms whether it is
done. **Open the deck by asking to see the creeper**, and let the answer steer
the warm-up — do not assume either way.

**Short review (first slots only)** — the creeper face he built by hand, and one
range he has to count out loud, start and end both included.

**Then the new idea, and it takes most of the hour: a `repeat` block draws a row
for you.** He has been placing pixels one at a time. Today one `repeat` block plus
a variable for the row number fills a whole row, then a whole square.

Ramp:
- **v1** — one `fill` block, one row of the face, by hand
- **v2** — a `repeat 15` block wrapped round it, nothing else changed → the same
  row 15 times in the same place. Broken on purpose, and the fix is the lesson.
- **v3** — a variable `row`, `change row by 1` inside the repeat → the rows climb
- **v4** — two colours: an `if` on `row` so some rows come out black → stripes,
  then the creeper mouth

**Visual, mandatory** — one frame per pass of the repeat with the value of `row`
shown next to the wall, so he sees 0, 1, 2, 3 climbing. Loops are never taught in
words here.

**Debug slides (4+)**
1. `repeat` with no `change row by 1` → every row lands on top of the last
2. `row` starting at 1 instead of 0 → the whole face floats one block up (his own
   △, and the y-starts-at-0 rule)
3. `repeat 15` where the face is 15 tall but the count starts at 0 → one row too
   many, the classic off-by-one he already met with 6→11
4. `change row by 1` placed *outside* the repeat instead of inside → one row only

**Stretch (OPTIONAL)** — his own emoji, 2 or 3 colours, drawn on the grid first,
then coded with the same repeat.

**Exit question** — "The repeat runs 15 times. What is `row` on the last pass?"
The answer is 14, and he must say why.

---

## 17:00 KST · 15:00 HCMC · EUNWOO — `eunwoo-see-the-numbers.html`

**Track:** MS002, Minecraft Python · **Source:** log + draft, 2026-08-24
**Status: BUILT. DO NOT REGENERATE. DO NOT EDIT.**

The deck was written for 08-31 from the 08-24 draft, re-verified on 09-01
(38 slides, counter correct, asset paths correct, constant-form API), and never
delivered because his slot moved twice — Monday 19:00 → Tuesday 17:00 →
Wednesday 17:00. Kasim confirmed this morning: **use it as-is.**

It has been copied into `lessons/2026-09-02/eunwoo-see-the-numbers.html`
unchanged. The student folder already holds it as
`slides/2026-09-02-see-the-numbers.html`.

**Covered last time (2026-08-24)**
- Coordinate values stored in lists (`XS`, `ZS`)
- A `for` loop running 24 iterations
- The modulo operator `%` for index calculation (`i % 8`, `i % 4`)
- Calculated coordinates in `ax`, `az`, `bx`, `bz`, `k`, `j`
- Gold and emerald placed with `blocks.fill()` and `pos()`
- A DNA-spiral structure

**✓ Wins** — worked out on his own that the spiral needed obsidian; noticed his
code ran clean where the teacher's did not.

**△ Got wrong** — fixed a bug but could not say what changed ("it just got
fixed"); does not yet follow how `ax`, `az`, `bx`, `bz` are calculated, because
the algebra is new.

The deck's Recap slot already recaps exactly this, which is why it still fits
nine days later.

**Overflow if he flies** — `../2026-09-01/eunwoo-two-strands.html`, 30 slides,
the second strand offset from the first. Already in his student folder as
`slides/2026-09-01-two-strands.html`. Do not copy it into today's folder; open it
from there only if he finishes.

---

## 18:00 KST · 16:00 HCMC · NEO — `neo-bullets-that-hurt.html`

**Track:** RS003, Python / Pygame · **Source:** **Notion 2026-08-31** — the
tracker is a week behind and its newest row (08-26, hexagon formations) is not
his last lesson.
**Topic:** Kasim did not name one. Chosen: enemy bullets hit the player, then a
player health bar.
**Reference deck for tone:** `../2026-08-31/neo-formation-trig-solo.html` and
`../2026-09-01/ryan-enemy-name-tags.html`

**Covered last lesson (2026-08-31)**
- Per-enemy bullet cooldown added to `make_enemy`
- Firing rate set per enemy type with `random.randint()`, counted in frames
- `enemy["bullet_cooldown"] -= 1` every frame
- Appending a dict to `enemy_bullets` when the cooldown reaches 0, keys `x`, `y`,
  `vx`, `vy`
- Coordinates: what `x`, `y` (position) and `w`, `h` (size) mean
- Bullet spawn from the enemy centre:
  `enemy["x"] + enemy["w"] / 2 - bullet_width / 2` and `enemy["y"] + enemy["h"]`
- Drawing enemy bullets with `pygame.draw.rect()`
- Velocity vectors `vx`, `vy`

**✓ Wins** — ran the code, saw no error but no bullets, and worked out the
drawing code was missing before the teacher said anything. Explained
`BY = EY + EH` in his own words. After one diagram, got that
`enemy["x"] + enemy["w"] / 2` is the enemy's centre x.

**△ Got wrong** — misspelled `angle_1` / `angle_2` as `angle to` (08-26); waits
for the teacher to type instead of trying first.

**His homework, and the state of it — this is the spine of the review.**
File `31august.py` in his IDE Homework project. He opened it on 1 Sept but the
markers are still in place:

- `## HOMEWORK 1 ##` (line ~321) — the bullet flood. The line under it reads
  `enemy["bullet_cooldown"] = enemy["bullet_cooldown"]`, which never resets the
  timer, so every enemy fires every frame and drags a bronze bar. **Unfixed.**
- `## HOMEWORK 2 ##` (line ~681) — "enemy bullets hit the player. write it here".
  **Empty.** This is today's build.
- `## HOMEWORK 3 ##` (line ~508) — the boss will not die, three lines in the wrong
  order. **Unfixed.**

**Short review (first slots only)** — HOMEWORK 1 and HOMEWORK 3, fast. One slide
each for the bug, one for the fix. `bullet_cooldown = bullet_cooldown` is a
perfect Common Mistake card: the line looks like it does something and does
nothing.

**Then the build, most of the hour.** HOMEWORK 2 first, then the genuinely new
thing on top of it:

- **v1** — a `pygame.Rect` for the player, a `pygame.Rect` for one enemy bullet
- **v2** — `.colliderect()` between them, `lives -= 1` on a hit
- **v3** — remove the bullet on impact, so one bullet costs one life not thirty.
  This is the bug that will bite him and it deserves its own slides.
- **v4 — the new idea he has never had: a player health bar.** He already draws
  the boss bar with `health_percentage = boss["hp"] / boss["max_hp"]`. Today he
  reuses that exact shape for himself: `player_hp`, `player_max_hp`, a bar under
  the ship. Point at his own boss-bar code and have him say what changes.

**Visual, mandatory** — two rectangles closing on each other frame by frame, with
the overlap shaded, so `colliderect` is a picture before it is a method.

**Debug slides (4+)**
1. The rect built from `x, y` but with the *enemy's* width → hitbox in the wrong
   place
2. `lives -= 1` with no `remove` → lives fall to zero in one frame (the v3 bug,
   posed before it is fixed)
3. Removing from `enemy_bullets` while looping over it → bullets skipped
4. `player_hp` drawn before it is decremented, so the bar lags one frame

**Stretch (OPTIONAL)** — brief invincibility after a hit, using the same cooldown
counter he wrote last week for the enemies. He already owns the pattern.

**Push him to type.** His own △ says he waits. Every `✅ check` slide is his to
run, not the teacher's.

---

## 19:00 KST · 17:00 HCMC · YUNA — `yuna-every-team-at-once.html`

**Track:** Python · **Source:** log + draft, 2026-08-26
**Topic:** Kasim did not name one. Chosen: looping through a whole dictionary.
**Reference deck for tone:** `../2026-08-30/logan-nested-pokedex.html` and
`../2026-08-26/yuna-cafe-menu-debug.html` (her own last deck)

**Covered last time**
- Reading values out of a dictionary with `dictionary[key]`
- Debugging key errors and capital letters
- `.lower()` to tidy what the user types
- `input()` to ask the user, then look the answer up
- Nested dictionaries: team → country, players, team colour
- Reaching inside with `dictionary[key1][key2]`

**✓ Wins** — worked out on her own that the key error was capital L against
lowercase l.

**△ Got wrong** — did not chain `[more_info]` after `hockey[team]` without a hint.

**Her homework, and the state of it — check this in the first five minutes.**
File `main.py` in her IDE Homework project, the hockey machine. Last saved
2026-08-26 09:53, which is *during* the lesson. **All four JOBS are untouched:**

1. JOB 1 — `.strip().upper()` and `.strip().lower()` on the two inputs. Not done.
2. JOB 2 — turn the second `print` into an f-string. Not done.
3. JOB 3 — add her own team to the dict. Not added.
4. JOB 4 — ask which player 1–4 and print that player. Half written: the `input()`
   line exists, nothing prints.

Say it plainly and kindly, then use JOB 4 as the way in — it is one line from
today's idea.

**Short review (first slots only)** — one slide on `hockey[team]["players"]`
returning a *list*, which is the fact JOB 4 needs and the bridge to today.

**Then the new idea, most of the hour: a `for` loop over a dictionary.**
Right now she can only see one team per run. Today she prints all of them.

Ramp:
- **v1** — `for team in hockey:` printing just the names. The surprise worth a
  whole slide: looping a dict gives you the **keys**, not the values.
- **v2** — `hockey[team]["country"]` inside the loop → every team with its country
- **v3** — `for team, info in hockey.items():` → the same thing, shorter, and
  `info["country"]` explains what `.items()` handed her
- **v4** — a loop inside a loop: for each team, loop its `players` list and number
  them. That is JOB 4 solved for every team at once, and it lands her own homework.

**Visual, mandatory** — the dictionary drawn as five labelled boxes, and one
frame per pass with the current `team` highlighted. Then a second track under it
for the inner players loop, so the nested loop is two moving pointers, not words.

**Debug slides (4+)**
1. `for team in hockey: print(team["country"])` → `TypeError`, because `team` is a
   string not a dict. Her most likely mistake and it comes straight out of her △.
2. `.items()` unpacked into one variable instead of two
3. A key typed with a capital inside the loop → `KeyError`, her own 26 Aug bug,
   now inside a loop where it is harder to see
4. The inner players loop indented level with the outer one → only the last team's
   players print

**Stretch (OPTIONAL)** — count the teams with `len(hockey)`, then print only the
Korean teams with an `if` inside the loop.

---

## 20:00 KST · 18:00 HCMC · LUCY — `lucy-say-it-in-time.html`

**Track:** Speech contest, one-off · **Source:** `lucy-essay-comp/` folder
**Topic Kasim gave:** speech contest delivery practice
**Reference deck for tone:** `../2026-08-27/lucy-finish-the-speech.html`
**Not a coding deck. No code slides, no `.mcb`, no `pre` blocks of Python.**

**Where she is**
- The script is **locked**: `lucy-kim-speech-final.docx`, 282 words
- **The limit is TIME, not words: 2:00–2:30.** Never coach her to a word count.
- Prelim **19 Sept**, final **3 Oct**
- Existing delivery notes: `lucy-essay-comp/feedback/video-01-delivery-critique.md`
  — read it and build the practice round on what it actually says, not on generic
  public-speaking advice
- Homework she was set: `homework-01-lucy-speech-tone-pacing`

**Short review (first slots only)** — one slide on the single biggest note from
the delivery critique, and a first full read for a raw time.

**Then most of the hour: run it, time it, fix one thing, run it again.** The deck
is a rehearsal engine, not a lecture. Use `.dtimer` from `style.css` — it is
already built for exactly this and it is on the slide, not on her phone.

Structure the practice as passes, each with its own slides:
- **Pass 1** — full read, no notes, just the clock. Write the time down.
- **Pass 2** — pauses. Mark the script where she breathes; one slide per marked
  line with the line printed and the pause drawn in.
- **Pass 3** — the opening 20 seconds only, repeated. First impressions carry the
  prelim.
- **Pass 4** — the closing 20 seconds only.
- **Pass 5** — full read again, timed, compared against Pass 1 on screen.

**Visual, mandatory** — the 2:00–2:30 window drawn as a bar with her Pass 1 time
marked on it, so "too fast" and "too long" are a picture and not a scolding.

**Overshoot** — add per-section target times, a filler-word tally card, an
emphasis drill on three chosen lines, and a "what if you blank" recovery slide.

**Parent card:** yes, draft one. It is a lesson she attended, and an unwanted card
costs nothing while a missing one is a gap. Speech language, not coding language.

---

## 21:00 KST · 19:00 HCMC · 이현 (LEE HYEON) — `ihyeon-maze-first-turn.html`

**Track:** MS000, Minecraft **BLOCKS** (MakeCode) · **Source:** log + draft, 2026-08-26
**Topic Kasim gave:** "mazes, from today" — this is a **new unit**, day one.
**Reference deck for tone:** `../2026-08-31/siyun-maze-and-or.html` — **for the
teaching order of detect → if → if/else only. It is a Python-text deck. Redraw
every single thing as blocks.**

**World:** Kasim hosts the maze world and 이현 joins it. There is no file to open
at the start of the lesson. The `.mcworld` only matters for homework. Do not write
a "double-click the world file" slide.

**Covered last time**
- `change side by -2` to shrink each pyramid layer
- Automating the pyramid with the code inside a loop
- Working out the loop count for odd and even numbers (÷2, round up)
- Garden fence combining agent move, agent place and agent turn
- Placing flowers — peony, lily of the valley, lilac
- Pond with fill, fish and animals with spawn

**✓ Wins** — built the whole garden fence alone after one demo. Picked and placed
his flower types with no guidance.

**△ Got wrong** — starts the next step before the agent has finished moving. Needs
telling to wait.

**Homework he was set (26 Aug)** — his own garden in
`flower-garden-homework-2026-08-26.mcworld`: fence, 3+ flower types, pond, 2+
animals, **code only, no hand-placing**, plus one written bug answer about the
last fence block. No IDE account, so ask to see it.

**Short review (first slots only)** — the fence he built with move + place + turn.
That is the exact skill the maze reuses, so it earns its place by leading straight
in.

**Then the new idea, most of the hour: the agent can look before it moves.**
Everything so far has been "walk 5, turn left" written in advance. A maze cannot
be written in advance, because the walls decide.

Ramp:
- **v1** — walk the maze by hand with move and turn blocks. It works for *this*
  maze and breaks the moment the maze changes. Show it breaking.
- **v2** — the `agent detect` block on its own, printing true or false. One new
  block, one slide, nothing else.
- **v3** — `if <agent detect block ahead> then turn right`, wrapped round it
- **v4** — `if / else`: no wall ahead → move 1, wall ahead → turn right
- **v5 (OPTIONAL, likely next week)** — the whole thing inside a `repeat`, so the
  agent keeps going until it is out

**Visual, mandatory** — a top-down maze grid, one frame per step, the agent arrow
in the cell and the answer to "wall ahead?" written beside it as true or false.
He sees the decision happen before he builds it.

**The wait rule is a slide, not an aside.** His own △. `agent detect` answers
about *where the agent is now*, so asking while it is still moving gives the wrong
answer. Give it a Common Mistake card of its own — here it is not a manners note,
it is a bug.

**Debug slides (4+)**
1. `if` with the turn block dropped *outside* it instead of inside → turns every
   step
2. detect pointed left when the wall is ahead → walks into the wall
3. `if` with no `else` → the agent stops dead when the way is clear
4. move and turn swapped inside the `if` → turns first, walks into the wall

**Stretch (OPTIONAL)** — the agent drops a wool trail behind it with place-on-move,
so he can see the path it chose after it finishes.

**Name check:** the tracker calls him `이현 MC`. Kasim calls him LEE HYEON. Use
**이현** on the slides.

---

## Drift and exceptions — report only, no DB writes

- **RIHAN [BBORAKING]** — tracker says Wed 16:00, active. **Zero calendar events
  in all of September.** Last lesson 26 Aug. Needs Kasim to confirm dropped.
- **DANIEL LEE M000** — tracker says Wed 20:00, active. **Zero calendar events in
  all of September.** Last lesson 12 Aug. Needs Kasim to confirm dropped.
- **JADEN [PH]** — tracker says Wed 18:00. Calendar has him **Saturday 19:00 KST**.
  Moved, tracker not updated.
- **EUNWOO COORDINATES** — tracker says Monday 19:00. Calendar has him **Wednesday
  17:00** (event edited 1 Sept). Moved twice in a week.
- **NEO** — `tools_lesson_logs` and `tools_log_drafts` both stop at 26 Aug. The
  31 Aug lesson happened (Notion meeting note exists) and was never logged.
- **LUCY SPEECH PRACTICE 20:00** sits in DANIEL LEE M000's old tracker slot. It is
  a real one-off, not a mis-titled event. No rename.

No calendar renames were needed today — every lesson event title already matches a
tracker `name` or `transcript_alias` exactly.
