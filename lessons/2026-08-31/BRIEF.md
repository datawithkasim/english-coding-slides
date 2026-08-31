# Today's decks — 2026-08-31 (Mon)

One deck per student, built from what the tracker says they last did and what was
promised for next time. Eight Monday slots, 15:00 → 21:00 Korea time
(13:00 → 19:00 Ho Chi Minh, KST−2).

JADEN is an extra slot Kasim added today — he is normally Wednesday 18:00.

## Hard rules for every deck

Read first, in this order:
1. `../../TEMPLATE.md` — the slot structures and the per-slide rules
2. `../../PEDAGOGY.md` — why each slot exists
3. `../../assets/style.css` — the only styling allowed; the BC-track section holds
   `.trace-grid`, `.debug-card`, `.err`, `.quiz-card`, `.stretch-list`, `.exit`,
   `.activity-tag`
4. One finished deck in the matching course folder, as the reference for tone

Then:
- Save to `lessons/2026-08-31/<file>.html`. Stylesheet path is
  `../../assets/style.css` and the script is `../../assets/deck.js` — this folder
  sits two levels deep, same as every course folder.
- **Overshoot hard. Kasim asked for this explicitly today.** Base is the 20-slot
  structure, then add **10–18 extra slots**: more debug cards, harder modifies,
  a second worked example, extra stretch challenges. Target **32–38 slides**.
  Running out of material is the one failure mode that is not allowed today.
  Mark every slot past the required 20 with
  `<span class="activity-tag">OPTIONAL</span>` so the must-teach spine stays
  obvious at a glance.
- Update the `counter` span to `1 / <total>` and check `deck.js` for how it
  counts, so navigation and the counter agree.
- Per-slide caps hold everywhere: **≤ 40 English words, ≤ 15 Korean words**.
  Overshooting means *more slides*, never denser slides.
- Korean glosses only on Tier-3 vocab, concept hooks, and bridges.
  **Exception: JADEN is in the Philippines — his deck is English only, no Korean.**
- Only reuse existing CSS classes. No new inline component styling.
- Slot 2 (Recap) must recall **that student's own last lesson**, using the facts
  in their brief below — not a generic recap.
- The △ lines in a brief are what the student actually got wrong. Turn each into
  a Common Mistake or Debug slot rather than inventing a bug.
- Big programs ramp **v1 → v2 → v3 → v4**: new lines hot, old lines dimmed, and
  changed lines carry OLD / NEW markers.
- **Minecraft API form — constant arguments, never quoted strings.** Repo-wide
  convention, verified 2026-08-31: `agent.move(FORWARD, 5)`, `agent.turn(LEFT_TURN)`,
  `agent.turn(RIGHT_TURN)`, `agent.detect(BLOCK, FORWARD)`, `agent.place(DOWN)`,
  `agent.set_assist(PLACE_ON_MOVE, True)`, `agent.set_block_or_item(GRASS, 1)`,
  `agent.teleport_to_player()`, `blocks.fill(STONE, pos(...), pos(...))`.
  The ONLY quoted string is the chat word: `player.on_chat("run", on_run)`.
  Reference decks: `lessons/2026-08-28/ian-agent-square-walls.html` and
  `lessons/2026-08-27/jj-count-moves-not-blocks.html`.
- Every coding step shows three things: the **code** itself, **where it goes**
  (quote the existing line it sits after or inside), and **why** in one short
  line. Never describe a change in prose — show it.

---

## 15:00 KST · 13:00 HCMC · JADEN — `jaden-my-own-command.html`

**Track:** Minecraft Education, MakeCode **Python**, **constant-argument API** —
`agent.move(FORWARD, 5)`, `agent.turn(LEFT_TURN)`, `agent.set_assist(PLACE_ON_MOVE, True)`,
`agent.set_block_or_item(RED_FLOWER, 1)`. Bare constants, never quoted strings. The only
quoted string is the chat word in `player.on_chat("flower", flower)`.
· **Source:** draft, 2026-08-29 · **English only — no Korean glosses.**

**Covered last time**
- `agent.move(FORWARD, n)`, `agent.turn(LEFT_TURN)`, `agent.move(UP, n)`
- Block placement with `agent.set_assist(PLACE_ON_MOVE, True)` and `agent.set_block_or_item()`
- A rectangular fence built from a repeated four-side sequence
- Writing his **own function** called `flower`, and calling it

**✓ Wins** — followed the repeat-4× fence pattern; noticed a gap and added the
missing `agent.move(UP, 1)` himself; caught his own `flower` misspelling once
asked to check.

**△ Mistakes — these are the deck's debug slides**
- Confuses `FORWARD` and `UP`: typed `agent.move(UP, 7)` where
  `agent.move(FORWARD, 5)` was needed.
- **Kept typing `run` in chat instead of `flower`** to call his own function,
  even after repeated correction. This is the headline problem.

**Today:** *the chat word you register is the chat word you type.*

The whole deck hangs off one idea Jaden has not internalised: a function you
write yourself gets its own chat command, and typing `run` fires the *other*
function, not yours.

```python
def flower():
    agent.set_block_or_item(RED_FLOWER, 1)
    agent.place(FORWARD)
player.on_chat("flower", flower)
```

Slot 5 must give him a physical model: the `player.on_chat("flower", flower)`
line is a **name tag** stuck on the function. Chat is a doorbell — press
`"flower"`, the `flower` function answers; press `"run"`, a different function
answers. Draw two labelled doorbells.

Then build up: v1 one flower · v2 `flower` called four times · v3 flower + move
between each · v4 a row of flowers along the fence he built last week.

**Direction drill.** Give `FORWARD` vs `UP` its own slide pair with a picture:
`FORWARD` = along the ground, `UP` = into the sky. Then a trace activity where
he predicts where the agent lands.

**Debug slides (3+)** — (1) `player.on_chat("run", flower)` but the student types
`flower` → nothing happens; (2) `agent.move(UP, 7)` where `FORWARD` was meant
→ agent builds a tower; (3) `def Flower():` vs `player.on_chat("flower", flower)`
→ name mismatch. All three come from his real errors.

**Code Talk Frame** — force the sentence: "I registered my function under the
chat word ___, so in chat I must type ___."

---

## 15:10 KST · 13:10 HCMC · SIYUN (시윤) — `siyun-maze-and-or.html`

**Track:** Coordinates → moving into conditionals · **Source:** draft, 2026-08-10
(the 08-24 slot has no draft at all — this is a **rebuild of the 08-24 deck**
`siyun-maze-conditionals.html`, which was never taught)

**Covered last time (2026-08-10)** — nothing. The lesson was **cancelled**:
Minecraft Education demanded a version update and the whole session went on
waiting for it, on a slow computer. No code was written.

Before that (2026-07-13): X/Y coordinates, `blocks.fill()` with ranges, counting
grid squares for pixel art, picking block materials.

**✓ Wins** — told a long detailed story in English about selling lemonade on her
America trip; sat through the technical failure patiently. On 07-13 she counted
the 1–15 range herself and confirmed X comes first, Y second.

**△ Mistakes** — mixed up X/Y order (put 1–15 on Y first); miscounted 8–9 as 10–11.

**Today:** her first real conditionals lesson — `if` / `elif` in a maze, then
`and` / `or`.

Because 08-10 produced no code, **Slot 2 recap must be honest and gentle**: recap
what she can already do (coordinates, `blocks.fill`, counting), then say plainly
that today is the maze lesson that got postponed. Do not recap content she never saw.

Ramp: v1 `agent.detect(BLOCK, FORWARD)` → v2 `if` / `else` turn → v3 `elif` chain
for three directions → v4 `and` for a two-condition junction, `or` for a
two-way exit.

Slot 5 model: a maze junction drawn from the agent's own point of view, with
"is there a wall in front?" as a yes/no box. `and` = **both** doors shut.
`or` = **either** door open. Draw both, do not only describe them.

**Debug slides (3+)** — (1) `if` and `elif` in the wrong order so the general
case swallows the specific one; (2) missing indent under `if`; (3) `and` used
where `or` was meant, so the agent freezes at a junction; (4) OPTIONAL: X/Y order
swapped in a `blocks.fill` warm-up, from her real 07-13 mistake.

She is coming off a dead lesson and a slow machine. Front-load one quick win in
the first five slides.

---

## 16:00 KST · 14:00 HCMC · AMY — `amy-player-card-solo.html`

**Track:** RS001, Python · **Source:** draft, 2026-08-24

**Covered last time**
- `.lower()`, `.title()`, `.strip()`, `.replace()` string methods
- Variable reassignment — the last value overwrites the earlier ones
- Chaining several string methods together
- **Started** the Python card project with `input()` and f-strings

**✓ Wins** — explained reassignment in her own words: *"doesn't forget, just saves
over it."*

**△ Mistakes** — typed `.title()` as `.titile()` (swapped l/e). Older but live:
forgets where quotation marks and parentheses go.

**Promised** — "more typing practice to build spelling familiarity" and
**"let Amy try the Python card project herself before showing an example."**

**The six-week arc (set by Kasim, 2026-08-31):** Amy is building a **small
text-based game** over roughly six weeks. Every deck from here teaches one idea
the game needs, and says out loud where that idea lands in the game. Today's
player card is the game's **character screen**, not a standalone exercise.

**Deck growth rule for her, learned the hard way today:** enlarging a deck means
**more taught ideas, each opening with an animation or diagram before the code** —
never more debug cards. Keep debug slides to her own real errors, about four.
Use the animated visualisation machinery already in `assets/style.css`
(`.viz-3` / `.viz-4` with `.iter-item`, `.var-val`, `.out-line`, and the
`hl3` / `vv3` / `out3a` keyframes) plus the reusable helpers in `assets/deck.js`.

**Idea ladder toward the game** — variable as a labelled box · `input()` filling
the box · f-string `{}` as a window · `"=" * n` as a stamp · `int()` turning text
into a number · `if` / `else` as the player's choice · a variable that changes
(`hp = hp - 1`, then `"♥" * hp`). `if` / `else` is the most important of these:
it is what makes a game a game.

**Today:** she builds the player card herself. This is a **do-first deck**, not a
lecture deck.

The order matters and the deck must enforce it: goal → she attempts → *then* the
worked example. Put a clear **"Amy builds it — no example yet"** slide before any
finished code appears, and put the reference solution behind it.

Target program:

```python
name = input("What is your name? ")
game = input("Favourite game? ")
name = name.strip().title()
print("=" * 30)
print(f"| PLAYER: {name}")
print(f"| GAME:   {game}")
print("=" * 30)
```

Ramp: v1 name only · v2 add `.strip().title()` cleaning · v3 add the `"=" * 30`
border · v4 add a third field and centre the text.

Slot 5 model for `"=" * 30`: a string times a number is a **stamp pressed 30
times**. She has not met this idea — give it a picture, not a sentence.

**Debug slides (4+)** — (1) `.titile()`, her exact typo, with the real
`AttributeError` message; (2) `print(f"| PLAYER: name")` — missing braces, prints
the word not the value; (3) a missing closing parenthesis; (4) `"=" * "30"` →
type error; (5) OPTIONAL: `.strip()` called but the result not reassigned, so
nothing changes — this is her reassignment idea used as a trap.

Add a short **typing accuracy** stretch: three method names to type correctly
from memory. That is the "practice typing" promise, made concrete.

---

## 17:00 KST · 15:00 HCMC · NEO — `neo-formation-trig-solo.html`

**Track:** PYGAME · **Source:** draft, 2026-08-26 (Wednesday — fresher than the
08-24 draft). Reference deck for tone:
`../../../english-coding-students/students/neo-mon-wed-1700/slides/2026-08-26-formation-shapes.html`
(also `lessons/2026-08-26/`).

**Covered last time**
- Hexagon formation: vertex positions from trigonometric functions
- Collision-detection areas for individual formation members
- Dictionary access by key — `M["w"]`, `M["h"]`
- Referencing object attributes inside nested loops

**✓ Wins** — answered `M["w"]` / `M["h"]` for formation width and height instantly;
found his own `mx` / `my` code to locate collision coordinates without help.

**△ Mistakes — all three shape this deck**
- Misspelled `angle_1` / `angle_2` as `angle to`; hit the error, fixed it with help.
- **Found the trig formulas for x1, y1, x2, y2 hard to follow.** Needed carrying.
- **Waited for the teacher to type instead of trying himself.** Repeat offence —
  the same note appears in the 07-13 log.

**Today:** make the trig *visible*, then hand him the keyboard.

Slot 5 is the centrepiece and must be a **drawing, not a formula**. A circle with
a centre point, one arm sweeping round, and the two shadows it casts:

```
x = cx + radius * math.cos(angle)   # how far across
y = cy + radius * math.sin(angle)   # how far down
```

`cos` = across. `sin` = down. That is the whole idea. Show the same circle at
0°, 90°, 180°, 270° with the x and y values written next to each — four pictures,
four slides if needed. Do not compress this.

Then the loop that places every member:

```python
for i in range(count):
    angle = (2 * math.pi / count) * i
    m["x"] = f["anchor_x"] + RADIUS * math.cos(angle)
    m["y"] = f["anchor_y"] + RADIUS * math.sin(angle)
```

Ramp: v1 three members in a triangle · v2 six in a hexagon · v3 the whole
formation drifting left across the screen · v4 the ring **rotating** by adding a
growing offset to `angle`.

**The solo-typing problem is a deck-design problem.** Put explicit
**"NEO TYPES THIS — hands off, Kasim"** slides before each version step, with the
target lines shown but the editing left to him. Add a trace activity where he
fills in x and y for `i = 0, 1, 2` before any code runs.

**Debug slides (3+)** — (1) `angle to` instead of `angle_2`, his real typo, with
the real `SyntaxError`; (2) `math.cos` and `math.sin` swapped, so the formation
comes out sideways; (3) angle stepped by degrees instead of radians, so all
members stack on one point; (4) OPTIONAL: `M["W"]` capitalised — the dict-key
case trap, which pairs with his older `pygame.Rect` case bug.

**Stretch (OPTIONAL, several)** — rotating ring, two nested rings, a formation
that shrinks its radius as it advances.

---

## 18:00 KST · 16:00 HCMC · JUN — `jun-bridge-how-many-blocks.html`

**Track:** Minecraft Education, agent · **Source:** draft, 2026-08-24

**Covered last time**
- `agent.move(FORWARD, n)`, `agent.move(UP, 1)`, `agent.move(DOWN, 1)`
- Placing blocks with `agent.place(DOWN)`
- Bridge structures: the **up → forward → down** pattern
- Adjusting `n` in `agent.move(FORWARD, n)` after seeing the result
- Fence structures and choosing the right block type

**✓ Wins** — spotted on his own that `forward` needed reducing when the bridge
midsection ran too long.

**△ Mistakes**
- **Could not judge how much to reduce** — 7 was too long, needed a hint to try 5.
- Mixed up **white block vs white fence** in `agent.set_block_or_item()`.

Older, still live (07-13): puts `agent.set_assist(PLACE_ON_MOVE, True)` and
`agent.teleport_to_player()` *outside* the top of the code; mixes up the letters
I and L in command names; guesses block counts instead of counting.

**Today:** *count it before you run it.* Turn "how much do I reduce?" from a guess
into a method.

The method, and the deck must teach it as three named steps:
1. **Stand at the start.** Mark it.
2. **Count the gap** — point at each block, one number per block.
3. **Write that number**, run, then check the end lands where you marked.

Slot 5 model: a side-on drawing of a river gap with the blocks numbered 1…5 along
it, next to `agent.move(FORWARD, 5)`. Then the same picture with 7, showing the
bridge overshooting past the far bank. He *saw* this happen — show him the picture
of what he saw.

Ramp: v1 a flat 5-block bridge · v2 up → forward → down arch · v3 fence rails on
both sides · v4 a wider gap where he must count first.

**Block vs fence** gets its own slide pair — two pictures side by side,
`WHITE_CONCRETE` vs `BIRCH_FENCE`, and what each looks like when placed. This
is his real 08-24 confusion, not an invented one.

**Debug slides (4+)** — (1) `agent.set_assist(PLACE_ON_MOVE, True)` written at
the bottom instead of the top, so nothing gets placed; (2) `agent.move(FORWARD, 7)`
on a 5-block gap → overshoot picture; (3) a fence constant typed where a block
constant was meant; (4) `LEFT_TURN` mistyped as `IEFT_TURN` — his I/L confusion,
shown in a monospace font where the two are distinguishable; (5) OPTIONAL: `up` and `down`
in the wrong order so the bridge dives.

Include a **predict-then-check** activity: show a gap, he writes his number, then
the answer is revealed. Repeat it three times with different gaps.

---

## 19:00 KST · 17:00 HCMC · EUNWOO — `eunwoo-see-the-numbers.html`

**Track:** Coordinates, Minecraft Python · **Source:** draft, 2026-08-24

**Covered last time**
- Coordinate values stored in lists (`XS`, `ZS`)
- A `for` loop running 24 iterations
- The **modulo operator** `%` for index calculation (`i % 8`, `i % 4`)
- Calculated coordinates in variables `ax`, `az`, `bx`, `bz`, `k`, `j`
- Gold and emerald blocks placed with `blocks.fill()` and `pos()`
- A DNA-spiral structure

**✓ Wins** — worked out on her own that the DNA spiral needed obsidian; noticed
that her code ran clean where the teacher's did not.

**△ Mistakes — the deck exists because of these two**
- **Fixed a bug but could not explain what changed** — *"it just got fixed."*
- **Does not understand how `ax`, `az`, `bx`, `bz` are calculated.** The algebra
  idea is new to her.

**Today:** make the numbers visible. Nothing new gets added to the program — the
program she already has gets **opened up and read**.

This is a **trace-heavy deck**. Use `.trace-grid` far more than usual.

Step 1 — `%` on its own, with no Minecraft in sight. A row of 12 numbers and what
`i % 4` gives for each. Slot 5 model: a **clock with 4 hours**; counting past 3
lands back on 0. Draw the wrap-around arrow.

| `i` | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|---|
| `i % 4` | 0 | 1 | 2 | 3 | 0 | 1 | 2 | 3 | 0 |

Step 2 — `XS[i % 4]`: the index picks a slot in the list, the list gives back a
coordinate. Draw the list as four labelled boxes and an arrow landing in one.

Step 3 — the coordinate table she was promised on 07-21 (*"build a coordinate
table so Eunwoo finds the pattern rule herself"*). Fill in `i`, `i % 4`, `ax`,
`az` for `i = 0…7`, and let her state the rule.

Ramp: v1 four blocks from a list · v2 the loop with `%` wrapping · v3 the second
strand `bx`, `bz` offset from the first · v4 the full spiral with height.

**Debug slides (3+)** — (1) `XS[i]` without `%` → `IndexError` once `i` passes
the list length; (2) `i % 8` where `i % 4` was meant → the pattern repeats too
slowly; (3) the index used as the coordinate directly, so blocks land at 0,1,2,3
instead of the list values; (4) OPTIONAL: `blocks.fill` vs `blocks.place` mixed
up — her real 07-21 mistake.

**Code Talk Frame** — force the sentence she could not produce:
"`i % 4` gives ___, so `XS[i % 4]` picks ___, which puts the block at ___."
This directly answers the *"it just got fixed"* problem. Make her say it twice.

---

## 20:00 KST · 18:00 HCMC · YUNHO — `yunho-pixel-art-bigger.html`

**Track:** Maze Madness → currently doing 2D pixel art · **Source:** draft,
2026-08-24 (the pixel-art one). Kasim confirmed on 2026-08-31 that the pixel-art
lesson is the real one; the second 08-24 draft records a session lost to an audio
failure. **Continue from pixel art, not from `agent.inspect`.** The 08-24 deck
`yunho-agent-inspect.html` was never taught and is not today's topic.

**Covered last time**
- `blocks.fill()` for 2D pixel art
- Adjusting and correcting Y-axis values in the 3D coordinate system
- Organising many `blocks.fill()` commands in one file
- Debugging syntax errors from parenthesis and comma placement
- A coordinate-counting strategy on a **15×15 canvas**

**✓ Wins** — invented his own counting method using slabs and signs as markers;
fixed a line-42 parenthesis bug immediately after it was explained.

**△ Mistakes** — **off-by-one on the Y axis**: set the height to 10, had to
correct it to 9.

Older, still relevant: he is fast, he says *"I think I can do it"* and starts with
no starter code, and he knows `elif`, `and`, and `agent.detect` from the maze
work. **He will finish early — this deck must be long.**

**Today:** a bigger picture, built cleanly — and the off-by-one killed for good.

Slot 5 model: a ruler drawn from 0. Y from 0 to 9 is **ten** blocks, not nine.
Show the counting twice: once by pointing at each block, once by subtracting
(`end − start + 1`). This is the single most important slide in the deck.

Ramp: v1 one filled rectangle · v2 rectangle + a second colour on top · v3 a
recognisable sprite in four fills · v4 the same sprite with an outline, so the
inner fill must shrink by exactly one on each side.

**The outline in v4 is the real assessment** — it forces `end − start + 1`
thinking on all four edges. Do not cut it.

**Debug slides (4+)** — (1) height set to 10 where 9 was meant, his exact error,
with a picture of the sprite one row too tall; (2) a missing comma between
coordinates; (3) a parenthesis closed in the wrong place, echoing his line-42 bug;
(4) two fills overlapping so the later one erases the earlier one; (5) OPTIONAL:
X and Z swapped so the art faces the wrong way.

**Stretch, and make it deep (OPTIONAL, 6+ slides)** — a mirrored second half, a
sprite built from a coordinate list plus a `for` loop (he can handle it), a
hollow frame, and a two-layer 3D version. He beat the last three lessons early.
Give him somewhere to go.

---

## 21:00 KST · 19:00 HCMC · ETHAN — `ethan-for-loops-range.html`

**Track:** Python · **Source:** draft, 2026-08-24 · **This is a rebuild of the
08-24 deck of the same name — `for` loops were promised on 08-10 and still have
not been taught.** Check `lessons/2026-08-24/ethan-for-loops-range.html` for tone,
then write a fresh deck: the recap facts have changed.

**Covered last time (08-24)**
- `input()` for user input
- Storing input in variables — `name`, `age`, `favorite_food`, `favorite_person`
- `print()` to output stored values
- F-string syntax `f"text {variable}"`, several variables in one f-string
- Built a small interactive story

**Before that (08-10)** — `print()`, a list of favourite foods indexed by number,
`if` / `elif` for weather messages. He worked out zero-based indexing himself
after testing `[0]`.

**✓ Wins** — spotted small differences between his code and the shown pattern and
fixed them; repeated the structure for new variables on his own.

**△ Mistakes**
- Needed the *"what goes inside the f-string `{}`"* explanation more than once.
- **Waits for step-by-step guidance instead of applying a pattern he already
  knows.** Same note as Neo — design against it.

**Promised (08-10)** — "`for` loops and `range()` starting next lesson." Goal:
simple games (number guess, times-table quiz) in about three weeks.

**Today:** `for` loops and `range()`, finally.

Slot 2 recap uses the **08-24** facts (input, f-strings, the story) — not the
08-10 list-indexing lesson the old deck assumed.

Bridge from what he owns: he already indexed a list by hand, `foods[0]`,
`foods[1]`, `foods[2]`. A `for` loop is that, without typing every number.

Slot 5 model: a conveyor belt. The list feeds items past one at a time, and the
loop variable is the **label on whatever is passing right now**. Draw three
frames of the belt with the variable's value written on each. Then `range(5)` as
the same belt fed by a number machine that counts 0, 1, 2, 3, 4 — **starts at 0,
stops before 5**. Give the stops-before-5 rule its own slide.

Ramp: v1 `for food in foods:` printing each · v2 `for i in range(5):` counting ·
v3 `range(1, 13)` for a times table · v4 a loop with `input()` inside, so the
program asks five times.

Land on the **times-table quiz**, which is the three-week goal made visible:

```python
number = int(input("Which times table? "))
for i in range(1, 13):
    print(f"{number} x {i} = {number * i}")
```

**Fight the waiting-for-guidance habit.** Put **"ETHAN WRITES THIS ONE ALONE"**
slides before v2 and v4, with the goal stated and no code shown until the next
slide. Add a "you already know this" callback slide pointing at the f-string
pattern he mastered last week.

**Debug slides (4+)** — (1) missing colon after `range(5)`; (2) the loop body not
indented; (3) `range(5)` expected to print 1–5 → the off-by-one, his likeliest
error; (4) the loop variable printed in quotes, `print("i")` vs `print(i)`, which
is the f-string `{}` confusion in a new outfit; (5) OPTIONAL:
`for i in range(1, 13)` written as `range(1, 12)` → the 12× row goes missing.

**Stretch (OPTIONAL)** — a number-guessing game with a fixed number of tries, a
countdown with `range(10, 0, -1)`, and nested loops printing the whole times-table
grid.
