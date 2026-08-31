# Today's decks — 2026-08-30 (Sun)

One deck per student, built from what the tracker says they last did and what was
promised for next time. Five Sunday slots, 08:10 → 21:00 Korea time (06:10 → 19:00 Ho Chi Minh, KST−2).

## Hard rules for every deck

Read first, in this order:
1. `../../TEMPLATE.md` — the slot structures and the per-slide rules
2. `../../PEDAGOGY.md` — why each slot exists
3. `../../assets/style.css` — the only styling allowed; the BC-track section holds
   `.trace-grid`, `.debug-card`, `.err`, `.quiz-card`, `.stretch-list`, `.exit`,
   `.activity-tag`
4. One finished deck in the matching course folder, as the reference for tone

Then:
- Save to `lessons/2026-08-30/<file>.html`. Stylesheet path is
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
- Big programs ramp **v1 → v2 → v3 → v4**: new lines hot, old lines dimmed, and
  changed lines carry OLD / NEW markers.

---

## 08:10 KST · 06:10 HCMC · YUNGUN — `yungun-snake-moves.html`

**Track:** RS001 · **Source:** draft, 2026-08-29 (fresher than the 08-16 log)

**Covered last time**
- `def` functions called with params (`name`, `age`, `favorite_food`)
- f-strings with `{}` to print variables; built lists (foods, animals)
- `for` loop over a list
- Pygame window + `pygame.draw.rect()`
- Snake position through `snake_pos[0]` / `snake_pos[1]` indexing, colour constants

**✓ Wins** — fixed a missing-argument error himself by adding `say_hello("James")`.

**△ Mistakes** — cannot explain in a full sentence what a for-loop variable holds.
Earlier: put `a_counter` inside quotes and printed the name instead of the value.

**Today:** make the snake **move**. `snake_pos[0] = snake_pos[0] + 10` inside the
game loop, then the same for `[1]`, then keyboard keys choosing which one changes.

Slot 5 must give him a physical model for `snake_pos[0]` vs `snake_pos[1]` —
a box with two numbered slots, across then down. The Code Talk Frame should force
the sentence he could not say: "`snake_pos[0]` holds ___, so adding 10 moves the
snake ___." Common Mistake = the quotes bug: `print("snake_pos[0]")` vs
`print(snake_pos[0])`.

---

## 10:00 KST · 08:00 HCMC · DIS — `dis-rainbow-tower.html` · **GROUP PREP CLASS, 50 MINUTES**

**Track:** MS002 · Group of three — **Leia, Danny, Shian** · **Source:** log, 2026-08-16

**This deck is different from the other four. Read this section twice.**

Kasim teaches a part, the students build it, then the next part. Three cycles in
fifty minutes. The deck must be shaped around that rhythm, not around a lecture.

**The algorithm — deliberately tiny.** Build a **rainbow tower** in Minecraft
Education with Python. One idea per stage, and each stage is the previous stage
plus one line.

| Stage | Teach | They build | The one new idea |
|---|---|---|---|
| **1** | one coloured slab with `blocks.fill()` | a single red layer | coordinates make a rectangle |
| **2** | wrap it in `for i in range(6):` and add `y = y + 1` | a six-layer tower, all red | a loop repeats, a variable changes |
| **3** | a `colours` list, `colours[i]` inside the loop | the tower turns rainbow | the counter can pick from a list |

Stage 3 is where the algorithm lands: **repeat, change the height, change the
colour, using the same counter for both.**

**Deck shape** — mark the three teach blocks unmistakably:
- A **STAGE 1 / STAGE 2 / STAGE 3** divider slide before each block, with a
  "Now you build it" slide closing each one. Kasim needs to see at a glance where
  to stop talking.
- Each stage: Predict → Concept → Run (worked example) → the build slide.
- Version ramp across the whole deck: **v1** single fill, **v2** loop, **v3**
  changing colour, **v4** stretch. New lines hot, old lines dimmed, OLD/NEW on
  changed lines.
- **Way more than fifty minutes of material.** Target the top of the range,
  30 slides, and tag everything past the third build `OPTIONAL`. Extra stretch
  ideas: a hollow tower, two towers side by side, a colour that repeats with
  `i % 3`.

**Covered last time** — 3D coordinates (X, Y, Z), counting block distance from
the origin, `blocks.fill()` for 3D structures, working coordinates out from the
agent's position, the panda pixel-art project, switching between Python and
JavaScript modes.

**✓ Wins** — Danny: strong focus, fixed a Z-axis error himself, finished the head
and ears. Leia: switched to JavaScript by accident and still finished the second
paw in JS. Shian: settled and counted coordinates carefully after an early
classroom problem.

**△ Mistakes — one Debug slide each, named to no one**
- Leia miscounted the Z origin and entered 10–11 → Debug: a fill whose Z is
  counted from the wrong place, so the slab lands behind the builder.
- Danny set the body Z range too wide → Debug: a slab far thicker than intended.
- Shian deleted another student's structure → this is the shared-world rule, not
  a code bug. Make it a short **house rules** slide near the front: build only on
  your own marker, never break someone else's blocks.

**Promised** — always start counting where the axes meet; double-check
coordinates before entering them, and respect other builds in the shared world.
Both belong in the deck: the first as the Slot 5 concept, the second as the house
rules slide.

---

## 18:00 KST · 16:00 HCMC · LEO KIM — `leo-loop-that-changes.html`

**Track:** MS002 · **Source:** log, 2026-08-23

**Covered last time**
- `for` loops with `range()`
- Coordinate variables (x, y, z) and change variables (`x_change`, `y_change`, `z_change`)
- `blocks.fill()` for several structures
- Updating a variable inside the loop (`x = x + 1`, `z = z + 1`)
- A multiplier variable to change the spacing

**✓ Wins** — spotted the pattern in the coordinate changes himself (2→4, 4→7,
7→11). Stayed with a hard task and finished by following the demo instead of
quitting.

**△ Mistakes**
- Tried writing 30 separate lines instead of a loop; needed the demo to get it.
- Says only "I don't know" when stuck, so it is hard to find the problem.
- Waits for the teacher to type first instead of trying.

**Today:** the same loop, but he types first. Topic is **one loop, many
structures** — a row of pillars whose spacing comes from a multiplier.

Two things this deck must do that the others do not:
- **Sentence frames for being stuck.** Slot 10 gives him three to read aloud
  instead of "I don't know": "It breaks on line ___.", "I expected ___ but I got
  ___.", "I don't know what ___ means." Put this early as well as late.
- **Type-first prompts.** Every Make slide starts with him typing one line before
  any demo. Mark them so Kasim waits.

Common Mistake = the 30-lines-instead-of-a-loop habit: show the wall of repeated
`blocks.fill()` next to the four-line loop that replaces it.

---

## 19:00 KST · 17:00 HCMC · LOGAN — `logan-pygame-window.html`

> **OVERRIDE (30 Aug):** Kasim switched Logan to **Intro to Pygame** for this
> lesson. The deck to teach is `logan-pygame-window.html`.
> `logan-nested-pokedex.html` stays in the folder unused — the section below is
> the original plan, kept because its recap facts and △ mistakes feed the new deck.

**Track:** RS002 · **Source:** log, 2026-08-16

**Covered last time**
- Reading Pokemon data out of dictionary keys
- f-strings for user prompts
- The escape character for line breaks
- Printing the whole moves list with `for i in range(8)`
- Reaching `search["moves"]` in a nested dictionary
- Using the user's input value (`search`) as the lookup key

**✓ Wins** — had already tried running Python in the Mac terminal at home and
found out how by himself. Understood the string-key rule immediately. Explained
the line-break escape in his own words: "It just made the word into another line."

**△ Mistakes**
- Left the `for` loop body empty at first.
- Reached for `pokedex[search]["moves"]` instead of `search["moves"]` — he had
  already stored the inner dictionary and forgot.
- Fifteen minutes lost to a password reset.

**Promised** — check what a variable already holds before writing code against
it. Log in before class starts.

**Today:** **What is inside this variable?** Continue the Pokedex. Add a second
level — each move carries its own type and power — so he has to look one layer
deeper and keep track of what each name holds.

Slot 5 = nested boxes, a box inside a box, with the variable names written on the
lids. The trace activity should be a table where he writes what `search`,
`search["moves"]`, and `search["moves"][0]` each hold at one moment. Debug 1 is
his own double-lookup bug. Debug 2 is the empty loop body (`IndentationError`).

---

## 21:00 KST · 19:00 HCMC · CLAIRE — `claire-keys-vs-attributes.html`

**Track:** RS003 · **Source:** log, 2026-08-16

**Covered last time**
- A different score per enemy colour, reading `color` from the enemy dictionary
- Resetting `score` and `frames` when the game restarts
- Frame-based automatic score increase (`frames % 300 == 0`)
- A spark effect using a `hits` list and `pygame.draw.circle()`
- Counting a spark's lifetime down and removing it from the list
- A `moving` variable that changes the player's colour

**✓ Wins** — found the collision code on line 149 before Kasim did. Chose 12
frames for the spark after trying 8 and 16: "fast but still visible enough."
Caught her own "saprock" typo.

**△ Mistakes**
- Took several tries to reach `enemy["color"]`.
- Mixed up attribute access (`enemyRect.color`) with dictionary keys.
- Needed prompting to declare `moving`.

**Promised** — leave more wait time before hinting. Practise dictionary-key
access against attribute access.

**Today:** **Square brackets or a dot?** Add power-ups to the game — each is a
dictionary (`{"kind": "shield", "frames": 180}`) that also owns a pygame `Rect`.
The lesson is choosing the right access for the right thing, every single line.

Slot 5 = two pictures side by side: a labelled drawer you open with `["color"]`,
and a machine part you name with `.centerx`. The Code Talk Frame is the rule in
her own words: "`enemy` is a ___, so I use ___. `enemyRect` is a ___, so I use ___."

**Kasim's own note applies here** — leave more wait time before hinting. Put a
visible WAIT marker on every Make slide.
