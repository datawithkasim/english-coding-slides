# Today's decks — 2026-08-29 (Sat)

Two decks today. Kasim cut the day down to **ANDY (20:45)** and **Dewy (22:00)**.
MASON 10:00, JOY 13:00 and YUNGUN 20:00 were skipped on his instruction — no
decks built for them.

## Hard rules for every deck

Read first, in this order:
1. `../../TEMPLATE.md` — the 20-slot structure and the per-slide rules
2. `../../PEDAGOGY.md` — why each slot exists
3. `../../assets/style.css` — the only styling allowed; the BC-track section holds
   `.trace-grid`, `.debug-card`, `.err`, `.quiz-card`, `.stretch-list`, `.exit`,
   `.activity-tag`
4. One finished deck in the matching course folder, as the reference for tone

Then:
- Save to `lessons/2026-08-29/<file>.html`. Stylesheet path is
  `../../assets/style.css` and the script is `../../assets/deck.js` — this folder
  sits two levels deep, same as every course folder.
- **Overshoot on purpose.** Base is the 20-slot structure, then add 4–8 extra
  slots: more debug cards, a harder modify, extra stretch challenges. Target
  **26–30 slides**. A lesson must never run out of material. Mark the overflow
  slots with `<span class="activity-tag">OPTIONAL</span>` so the ones that must
  be taught stay obvious.
- Update the `counter` span to `1 / <total>` and check `deck.js` for how it
  counts, so navigation and the counter agree.
- Per-slide caps hold everywhere: **≤ 40 English words, ≤ 15 Korean words**.
- Korean glosses only on Tier-3 vocab, concept hooks, and bridges.
- Only reuse existing CSS classes. A per-deck `<style>` block at the top of the
  file is allowed **only** for the step-walkthrough components already used in
  `lessons/2026-09-01/ryan-enemy-name-tags.html` (`.find`, `.steptag`, `.was`,
  `.now`, `.tag-old`, `.tag-new`, `pre .hot`, `pre .dim`, `.vstep`, `.chip`) —
  lift them verbatim, invent nothing new.
- Slot 2 (Recap) must recall **that student's own last lesson**, using the facts
  in their brief below — not a generic recap.
- The △ lines in a brief are what the student actually got wrong. Turn each into
  a Common Mistake or Debug slot rather than inventing a bug.
- A deck teaching one growing program ramps v1→v2→v3→v4: new lines hot, old
  lines dim, OLD/NEW markers on changed lines.

## ANDY · 20:45 · Manim lesson 1 of 16 (매스 모션 16)

**Kasim's directive for this deck, overrides the default slot mix:**
"Andy is doing lesson 1 of Manim but we can move forward quite quick. Should be
more of a guided walkthrough than anything. 0 thinking required."

So: model this deck on `lessons/2026-09-01/ryan-enemy-name-tags.html` — a
STEP 1/N walkthrough, not the vanilla 20-slot mix. Every step slide gives the
code, where it goes, why, and a ✅ run-check. Predict / fill-in-the-blank /
quiz slots get cut or tagged `OPTIONAL`. Common Mistake slides stay — reading
an error message is part of the walkthrough. "Move quick" means more steps
covered, not fewer slides: still 26–30.

Course framing (from the public site): **매스 모션 16** — Python · Manim ·
수학 애니메이션 · 16회. Today is lesson 1 of 16.

Last lesson (2026-08-15, tracker) was the **old JavaScript track** — he
finished a calculator and started a weekly task tracker:
- Added a `reset` button, met `NaN`, refactored repeat event-listener code into
  one `updateCount(event)` function, `event.target.checked` with `if`/`else`,
  HTML table with checkboxes
- ✓ Proposed the reset button himself and coded it unaided; spotted the need to
  refactor ("if there were 100 checkboxes it would be quite hard to code")
- △ Needed step-by-step guidance on function syntax and waited for me to type
- △ iPad copy-paste failed, so Kasim typed much of it
- Promised: break the work into short chunks so Andy types the syntax himself;
  leave more wait time before stepping in

Recap slot therefore = a short JS bridge, not a Manim recap: he already knows
what a function is and what "call the function" means — Manim's `construct` and
`self.play()` land on that. Then flip to the new chapter.

**The two △ lines set the format of this deck**: he types every line himself,
in short chunks, so no step may contain more than one or two lines of new code.
No slide may need copy-paste.

**Where the code runs — exact, no guessing:**
- `app.english-coding.co.uk` — our own IDE, in the browser. Works on his iPad.
- He writes Python in the editor and presses **Run**. There is no terminal,
  no install, no `manim -pql` command, no scene name to type.
- The server finds the Scene class by itself and renders **the last Scene class
  in the file**, so a second scene added at the bottom is the one that plays.
- The finished animation comes back as a video in the app. A render takes about
  10–60 seconds and one student renders at a time, so "queued" for a moment is
  normal, not a bug. Video is 480p15 — small on purpose.
- Errors come back as a cleaned-up manim log: his own error lines, not the
  library's banner spam.

Today's content — one file, growing:
- v1: `from manim import *`, `class ... (Scene)`, `def construct(self):`, one
  `Circle()`, `self.play(Create(circle))` → first video
- v2: colour and size — `Circle(color=BLUE, radius=2)`, `.set_fill(BLUE, opacity=0.5)`
- v3: `Square()` + `Transform(circle, square)` — the shape morph, the "wow"
- v4: `Text("...")` and `.animate.shift(UP)` / `.animate.scale(2)` — motion
- Common Mistakes to cover: forgot `self.` in `self.play(...)`; the body of
  `construct` not indented; `play(circle)` instead of `play(Create(circle))`
  (you animate an *animation*, not an object); nothing appears because
  `self.play` was never called.

**No LaTeX on the render box.** `code-executor/manim_setup.sh` installs cairo,
pango and fonts only — no texlive — so `MathTex` / `Tex` will fail. Write maths
as `Text("x² + y² = r²")` instead. Bare `Axes()` and `NumberPlane()` are fine;
anything that draws tick numbers is not.

Topic slug: `andy-manim-first-animation`. Tone reference:
`lessons/2026-09-01/ryan-enemy-name-tags.html` (structure + the step CSS).

## Dewy · 22:00 · Minecraft agent, typed Python

Last lesson (2026-08-08, tracker draft):
- `agent.teleport()` to bring the agent to the player
- `agent.move("forward", n)`, `agent.turn("left")` / `agent.turn("right")`
- `agent.move("up", n)` for vertical movement
- `agent.place_on_move(on)` / `agent.place_on_move(off)` toggle
- L-shaped paths and stepped structures; skipping a no-placement section
- ✓ Solved the L-path first try: move forward 7, turn left, move forward 10
- ✓ Didn't give up on errors — debugged step by step until it finished
- △ Miscounted blocks: confused start and end point, counted the agent's own square
- △ Slow to grasp that the agent places its block at the square it *leaves*,
  not the square it arrives at

Today: **`for` loops with the agent**. He can already chain move → turn → move
by hand; today the repeated lines collapse into
`for i in range(4): agent.move("forward", 5); agent.turn("left")` — a square
wall built by a loop instead of eight typed lines. Then `range` with a variable
for staircases (`agent.move("up", 1)` inside the loop).

Both △ lines become their own slides:
- The counting one → Common Mistake + a count-ritual slide (point, count aloud,
  start square does not count as a move) — and `range(4)` gives four turns for
  four walls, the same off-by-one trap in a new costume.
- The place-on-departure one → its own trace slide: step the agent one square
  at a time and shade the block it just left, so he sees the block appears
  behind it, never under it.

He types Python, not MakeCode blocks — show real code.
Topic slug: `dewy-agent-loops`. Tone reference:
`lessons/2026-08-24/yunho-agent-inspect.html`, plus
`lessons/2026-08-28/ian-agent-square-walls.html` for the four-walls sequence.
