# Today's decks — 2026-08-27 (Thu)

One deck per student, built from the tracker + last week's Notion lesson
transcripts (2026-08-20). Six Thursday slots, 15:00 → 21:50 Korea time.

## Hard rules for every deck

Read first, in this order:
1. `../../TEMPLATE.md` — the 20-slot structure and the per-slide rules
2. `../../PEDAGOGY.md` — why each slot exists
3. `../../assets/style.css` — the only styling allowed; the BC-track section holds
   `.trace-grid`, `.debug-card`, `.err`, `.quiz-card`, `.stretch-list`, `.exit`,
   `.activity-tag`
4. One finished deck in the matching course folder, as the reference for tone

Then:
- Save to `lessons/2026-08-27/<file>.html`. Stylesheet path is
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
- Only reuse existing CSS classes. No new inline component styling.
- Slot 2 (Recap) must recall **that student's own last lesson**, using the facts
  in their brief below — not a generic recap.
- The △ lines in a brief are what the student actually got wrong. Turn each into
  a Common Mistake or Debug slot rather than inventing a bug.
- A deck teaching one growing program ramps v1→v2→v3→v4: new lines hot, old
  lines dim, OLD/NEW markers on changed lines.

## LUCY · Thursday afternoon · IYF speech contest (added 2026-08-27)

Not a coding student — essay/speech coaching for the 2026 IYF National
Children's English Speech Contest. Not in roster.json or the tracker; source is
the Notion transcript "LUCY [ESSAY COMP] @Monday 7:30 AM (GMT+7)" (2026-08-24)
plus her completed homework worksheet (photos, 2026-08-27).

Last session (2026-08-24, Notion transcript):
- Built a 2.5-minute "My Dream" speech (veterinarian): Pom-pom the hamster
  rescued from E-Mart — cardboard box, shivering, excrement, bald patches
- Theme evolved from "eliminate suffering" to "be someone animals can depend on"
- ~340 words (target 300–360); draft sent to mum as double-spaced PDF
- Homework: worksheet exercises 1–6 + final copy rewrite

Homework results (worksheet photos):
- ✓ Timeline fixed — rescue one night, THEN 11 months, then the last morning
- ✓ Opener now starts inside E-Mart ("Imagine you see loads of sick and
  injured animals at E-Mart! Would you want to shop there?")
- ✓ Realisation line in her own mouth: "I thought I could eliminate suffering.
  But now I know I was greedy to feel that" — keep exactly
- ✓ Ending circled: "That reminded me of the memories with Pom Pom!"
- △ "animals take need of other people" → must become "animals depend on people"
- △ Spelling: "obstical" → obstacle, "clumbsy" → clumsy
- △ Final Copy page 2 nearly blank — speech unfinished, word-count box empty

Today: apply the three fixes, finish page 2 (11 months + obstacle-course
memory → last morning → realisation → dream → circled ending), word count,
then contest rules (script = speech exactly; Zoom prelim Sept 19, no
PowerPoint; judging 30/30/25/15).
Topic slug: `lucy-finish-the-speech`. Deck adapts the 12-slot structure to
speech coaching — compare-rows carry her exact draft lines vs fixes.

## ERIC KIM · 15:00 · Minecraft Python functions

Last lesson (2026-08-20, tracker):
- Helper functions calling helper functions: make_cage → make_row → make_cube
- Nested for loops on x, y, z axes, spacing 7
- One call, make_cube(1, 1, 1), builds all 64 cages
- ✓ Built the whole 4x4x4 tower from a single call, no copy-paste
- △ CHICKEN is hardcoded inside make_row, so make_cage's animal parameter is never used
- △ make_cage fills a solid grass cube, so cages are not hollow and animals spawn inside blocks
- △ make_row loops x and y, so it builds a wall, not a row; the name no longer matches the job

Today (promised): pass the animal through make_row and make_cube instead of
hardcoding CHICKEN; bring back the hollow fence cage with a grass floor; one
spacing value in one place instead of three.
Topic slug: `eric-pass-the-parameter`. Tone reference: a deck in
`minecraft/003-functions-games/`.

## JJ snlovelyb · 16:20 · Minecraft agent (MakeCode)

Last lesson (2026-08-20, tracker + transcript):
- `agent.place()` on move; `agent.set_block_or_item()` to choose the block
- Combining `agent.move("forward")` / `("up")` / `("down")` into one sequence
- Agent puts the block at the square it LEFT, not the square it stands on
  (JJ's own words: "the agent doesn't like it in its stomach")
- Bridge shape = up → across → down pattern
- ✓ Asked how long the bridge should be, unprompted; caught teacher's missing
  forward-by-one; first bridge finished after several tries
- △ Mixed up `forward` and `up` when ordering commands; needed repeated explanation
- △ Blocks vs moves counting still unclear
- △ Second bridge: wrong forward/up repeat count and wrong middle forward count

Today (promised): make the blocks-vs-moves difference explicit; review the
second-bridge homework; keep drilling forward/up sequencing patterns.
Topic slug: `jj-count-moves-not-blocks`. Tone reference:
`lessons/2026-08-24/yunho-agent-inspect.html`.

## DANIEL · 19:00 · Python Adventures

Last lesson (2026-08-20, transcript — tracker log 08-13 is one week stale):
- `input()` to receive user input; storing input in variables (name, age, food)
- Variables inside `print()` sentences — self-introduction card
- `int()` to convert string input to a number
- Subtraction with number variables (slippers and gecko purchase calculations)
- String vs integer type errors
- ✓ Built name/age/food card step by step; wrote the int() purchase code himself
- △ Waited for hints instead of reading code himself (missing capital letter)
- △ End of lesson: variable value did not update — reassignment not yet taught

Today (promised): variable reassignment (`money = money - 20`) fixes the
stuck-value bug from last lesson; more hands-on typing; practice explaining
aloud what each line does.
Topic slug: `daniel-money-goes-down`. Tone reference: a deck in
`python/daniel-ask-the-player/`.

## SEOHYEON · 20:00 · Minecraft MakeCode

Last lesson (2026-08-20, transcript — tracker log 08-13 is one week stale):
- `blocks.fill()` with start coordinates, end coordinates, block type
- Cube structures from wood; hollow glass structures via the `hollow` parameter
- Water placed with `replace` mode
- Loops + `mobs.spawn()` to spawn animals
- ✓ Followed on screen, entered coordinates, fixed hollow herself when told
- △ Mistyped coordinate numbers several times, needed multiple corrections
- △ Omitted the `hollow` parameter at first
- △ Waits for teacher to type first instead of trying herself

Today: aquarium build — her own hollow glass tank, water via `replace`, fish
via loop + `mobs.spawn()`. She types the command structures herself. Make the
six-coordinate order explicit and drill it.
Topic slug: `seohyeon-aquarium-build`. Tone reference: a deck in
`minecraft/004-fill-loops/`.

## SERENA · 21:00 · Python → Pygame

Last lesson (2026-08-20, transcript — no tracker row for Serena at all):
- Reviewed monster encyclopedia structure (dictionaries, `.isdigit()`,
  main.py using mythic.py data)
- Pygame setup: `pygame.init()`, `pygame.display.set_mode()`
- Game loop: `while`, event handling, `clock.tick()`
- Constants + RGB colors; `pygame.draw.rect()`; drew first red rectangle
- ✓ Explained encyclopedia structure clearly; remembered `.isdigit()`; got
  "colors never change" constant idea instantly; experimented with colors
- △ Y-axis direction: answered "up" first — needed repeats to accept y grows DOWN
- △ Slow to grasp how x, y, width, height work together; learned by trial

Homework was Super Catio: 4 rectangles (ground, grass, cat, enemy) in the
starter file (screen 600×600, PASTEL_PEACH fill, example red rect at
120, 420, 60, 70). Today: review the homework rectangles, drill the inverted
Y-axis and the 4-number rect anatomy, then first movement — arrow keys move
the cat (`pygame.key.get_pressed()`, cat_x/cat_y variables replacing fixed
numbers).
Topic slug: `serena-move-the-cat`. Tone reference: a deck in
`python/pygame-starter/`.

## IAN · 21:50 · Web dev

Last web-dev lesson (2026-08-13, tracker — the 08-20 slot transcript was Neo's
makeup pygame lesson, not Ian):
- Flexbox review (`display: flex`, `justify-content`, `align-items`, `gap`)
- Grid (`display: grid`, `grid-template-columns: 1fr 1fr 1fr`), nested divs
- Renamed `main.css` → `styles.css`, updated links on every HTML page
- Images: folder + paths (`image/cat.jpg`), `alt`, `width: 100%`,
  `aspect-ratio`, `object-fit: fill/contain/cover`
- Anchor tags `<a href="">` to link images
- ✓ Predicted `width: 100%` fills the screen before typing it
- △ Forgot semicolons at the end of CSS properties several times
- △ Rename broke links — must check every linked file when renaming

Today (promised habits woven in): build a nav bar with Flexbox and link the
site's pages together (`<a href="page.html">`), relative paths, one shared
`styles.css` across pages. Semicolon check + renamed-file link check appear as
Debug slots.
Topic slug: `ian-nav-bar-links`. Tone reference: a deck in
`webdev/web001-css/`.
