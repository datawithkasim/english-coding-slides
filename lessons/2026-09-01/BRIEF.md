# Today's decks — 2026-09-01 (Tue)

Single requested deck: Ryan, built from his live IDE code (`student_ide` schema)
plus the 2026-08-20 tracker draft.

## Hard rules for every deck

Read first, in this order:
1. `../../TEMPLATE.md` — the slot structures and the per-slide rules
2. `../../PEDAGOGY.md` — why each slot exists
3. `../../assets/style.css` — the only styling allowed; the BC-track section holds
   `.trace-grid`, `.debug-card`, `.err`, `.quiz-card`, `.stretch-list`, `.exit`,
   `.activity-tag`
4. One finished deck in the matching course folder, as the reference for tone
   (here: `../2026-08-24/neo-boss-shoots-back.html` and the STEP format in
   `../2026-08-25/jason-finish-the-game.html`)

Then:
- Save to `lessons/2026-09-01/<file>.html`. Stylesheet `../../assets/style.css`,
  script `../../assets/deck.js`.
- **Overshoot on purpose.** Target 26–30 slides; overflow marked
  `<span class="activity-tag">OPTIONAL</span>`.
- Per-slide caps: **≤ 40 English words, ≤ 15 Korean words**.
- Korean glosses only on Tier-3 vocab, concept hooks, bridges.
- Slot 2 Recap uses the student's own facts below — never generic.
- △ lines are what the student actually got wrong — they become Common Mistake
  / Debug slides, never invented bugs.
- Big program change → progressive versions v1→v2→v3→v4, one STEP slide per
  change: 🔍 FIND (exact Ctrl+F string), full OLD/NEW blocks (no `...` inside a
  changed region), 📍 placement + indent, one-line why, one-line check.

## Ryan · Tue 09:00 · PyGame space shooter ("My Awesome Game")

Source: IDE `shooter.py` (2026-08-21) + Homework `main.py` Star Catcher
(2026-08-24, all 6 tasks correct) + tracker draft 2026-08-20.

Covered (2026-08-20 draft):
- Enemy-type variable blocks: scout / tank / fleet (width, height, speed, colour)
- `enemies.append()` per type — but all appends are plain `[x, y]`
- RGB colours, blit overlap fix (solo), balance talk
- Started "unique identifier" idea to tell enemy types apart in one list

Promised (2026-08-20 draft):
- Implement unique identifier to distinguish enemy types when drawing
- Practice extending existing code patterns instead of separate structures

What his code shows now:
- ✓ bullet-enemy `colliderect` + score, done by him (old 08-11 promise cleared)
- ✓ bullets loop over `bullets[:]` copy — he knows the trick
- Dead code: scout/tank/fleet stat blocks never used; every spawn appends 4
  identical `[x, y]` enemies, all drawn BLACK at 20×20, all move `enemy_speed`

△ facts (real, from code + drafts):
- △ `for enemy in enemies:` + `enemies.remove(enemy)` inside — no `[:]` copy
  (he used `[:]` for bullets but not enemies) → Debug 1
- △ `if enemy[:]:` no-op guard line in draw loop → dies in STEP 5 rewrite
- △ his own comment `# why is this here?` above `now = pygame.time.get_ticks()`
  → answered in Recap + OPTIONAL tidy slide
- △ (07-07) forgot quotes make a string → Common Mistake (bare `scout` NameError)
- △ (08-20) made separate scouts/tanks lists instead of one `enemies` list →
  reinforce single-list message in Concept slide

Deck: `ryan-enemy-name-tags.html` — topic **enemy name tags**: `[x, y, tag]`
as list item 3, then draw / move / score branch on `enemy[2]`. v1 tags,
v2 draw colours, v3 speeds, v4 per-type score. Bridge: enemies shoot back.
