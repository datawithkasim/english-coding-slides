# Today's decks — 2026-08-28 (Fri)

One deck per student, built from the tracker drafts — each student's LAST lesson
where real coding happened (busted/no-progress sessions skipped). Four slots:
Junwoo 16:00, Nellie 18:00, Ian 19:00, Jihun (experience lesson, time TBC).

## Hard rules for every deck

Read first, in this order:
1. `../../TEMPLATE.md` — the 20-slot structure and the per-slide rules
2. `../../PEDAGOGY.md` — why each slot exists
3. `../../assets/style.css` — the only styling allowed; the BC-track section holds
   `.trace-grid`, `.debug-card`, `.err`, `.quiz-card`, `.stretch-list`, `.exit`,
   `.activity-tag`
4. One finished deck in the matching course folder, as the reference for tone

Then:
- Save to `lessons/2026-08-28/<file>.html`. Stylesheet path is
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

## JUNWOO · 16:00 · Minecraft MakeCode (M002)

Last real lesson (2026-08-07, tracker draft — the 08-14 session was lost to
Minecraft Education multiplayer connection failures, zero coding, so recap
reaches back to 08-07):
- 3D coordinate system (X, Y, Z axes)
- `blocks.fill` command with start/end coordinate ranges
- Counting blocks to find start and end coordinates
- Built pixel art in parts: legs, body, tail, neck, head, beak
- ✓ Corrected X/Y/Z axis mix-up right after explanation, on first try
- △ Miscounted coordinates several times; wrong Y-range on beak needed fixes
- Note: 08-14 promise was "check the multiplayer connection before class, then
  run the planned lesson from the top" — today restarts that plan

Today: finish the pixel art with `blocks.fill` — rebuild momentum after two
weeks away, then drill the two weak spots: counting a coordinate range
correctly (start block and end block both count) and saying WHICH axis before
counting. Coordinate-counting mistakes become Debug slots; add a
count-check ritual (point, count aloud, then type).
Topic slug: `junwoo-finish-the-pixel-art`. Tone reference:
`lessons/2026-08-25/jiyu-3d-pixel-art.html`.

## NELLIE · 18:00 · Minecraft MakeCode (MS)

Last lesson (2026-08-21, tracker draft):
- Cherry blossom tree structure: oak log, cherry leaves, animal spawns
- Creating hollow structures using the `fill` command
- Decorating interior spaces (torches, block patterns)
- ✓ Understood hollow instruction immediately, applied it directly to second
  tree section
- △ First cherry blossom tree ran in opposite direction, had to rebuild

Today (promised, carried over from 08-21 — ran out of time): the **rainbow
tower coding challenge**. Stacked `fill` layers, one color per layer, hollow
option for the upper floors she already knows. Direction bug from last week
(build ran the opposite way) becomes the Common Mistake slot; build the
"double-check position + direction BEFORE running" habit into a pre-run
checklist slide.
Topic slug: `nellie-rainbow-tower`. Tone reference:
`lessons/2026-08-27/seohyeon-aquarium-build.html`.

## IAN (tracker `_loha2018`) · 19:00 · Minecraft agent (MakeCode blocks)

Last real lesson (2026-08-07, tracker draft):
- RL command: teleport agent to player
- R/L funcs: `agent.turn("right")` / `agent.turn("left")`
- `agent.move("forward", n)` then place-on-move while moving
- Counting blocks to target; pattern: move → turn → move
- ✓ Built 7- and 8-block walls solo: counted, coded, ran RL + run commands
- △ Miscounted blocks (said 8/5 for 7); mixed up letter L with number 1
- Promised: pause and double-check block counts before entering; watch the
  screen together for L vs 1

He codes with MakeCode blocks (OnChat Command blocks), not typed Python —
show commands the way the blocks read. Today: close the square. He can build
one straight wall; now chain move → turn → move → turn to wrap four walls
into a complete enclosure, place-on-move doing the building. Both △ lines
become Debug slots (a miscounted wall that overshoots the corner; an L/1
mix-up in a command name). Count-then-type ritual on its own slide.
Topic slug: `ian-agent-square-walls`. Tone reference:
`lessons/2026-08-27/jj-count-moves-not-blocks.html` and
`lessons/2026-08-24/yunho-agent-inspect.html`.

## JIHUN · experience lesson (trial — first ever lesson)

No tracker row, no student folder, no history. Slot 2 becomes a course/lesson
intro instead of a recap (W1 rule in TEMPLATE.md).

Today: **first Minecraft code** — the wow lesson. Arc: meet the agent
(teleport it to you), make it move (`agent move forward`), turn it, then the
payoff — one chat command that builds something big instantly (a `fill`
rainbow wall or tower) to land the "code does in one second what hands do in
ten minutes" moment. Keep every step tiny: one block/command per step. No
assumed Minecraft fluency — controls explained as they come up. Finish with
"what you could build in this course" bridge aimed at a trial student deciding
to join.
Topic slug: `jihun-first-minecraft-code`. Tone reference:
`lessons/2026-08-27/jj-count-moves-not-blocks.html` for agent slides plus
`lessons/2026-08-27/seohyeon-aquarium-build.html` for the fill payoff.
