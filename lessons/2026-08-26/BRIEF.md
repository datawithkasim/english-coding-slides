# Today's decks — 2026-08-26 (Wed)

Single-deck day: Kasim asked for NEO only, built from his live IDE state.
Other Wednesday students (SEOHOO 15:00, RIHAN 16:00, JADEN 18:00, YUNA 19:00,
DANIEL LEE 20:00, ihyeon 21:00) intentionally not built.

## Hard rules for every deck

Read first, in this order:
1. `../../TEMPLATE.md` — the 20-slot structure and the per-slide rules
2. `../../PEDAGOGY.md` — why each slot exists
3. `../../assets/style.css` — the only styling allowed; the BC-track section holds
   `.trace-grid`, `.debug-card`, `.err`, `.quiz-card`, `.stretch-list`, `.exit`,
   `.activity-tag`
4. One finished deck in the matching course folder, as the reference for tone

Then:
- Save to `lessons/2026-08-26/<file>.html`. Stylesheet `../../assets/style.css`,
  script `../../assets/deck.js`.
- Overshoot: base 20-slot + 4–8 OPTIONAL slots, target 26–30 slides.
- Per-slide caps: ≤ 40 English words, ≤ 15 Korean words.
- Korean glosses only on Tier-3 vocab, concept hooks, bridges.
- Only existing CSS classes. Slot 2 recaps that student's own last lesson.
- △ lines = what the student got wrong → Common Mistake / Debug slots.

## NEO · Wed 17:00 · Pygame Turret Shooter (RS003)

Source: live IDE (student_ide homework `main.py`, updated 2026-08-25 18:26 KST;
opened again 2026-08-26 14:18 KST). Tracker stops at 08-12 — stale, ignored.

Covered (Mon 08-24 lesson + homework since):
- Boss shoots back: cooldown, spread, boss_bullets, player lives.
- Formations started live in lesson. Lesson ended on the crash
  `TypeError: 'function' object is not subscriptable`.
- Homework done Tue evening: TASK 1 fixed (append parens), TASK 3 done
  (anchor enters top-middle: `anchor_x = CENTER_X`), TASK 4 done — he wrote
  the v-shape math himself: `dx = (i - count // 2) * 25`,
  `dy = abs(i - count // 2) * -15`.
- Circle pattern works (cos/sin, radius 70).

△ (real mistakes, used in deck):
- △ `formations.append(make_formation)` — no parens → the Monday crash.
- △ Skipped homework TASK 2 (force one pattern while testing) — testing was
  slow, so square/hexagon/pizza never got attempted.

Still empty in his file — dx, dy = 0, 0 with his own design comments:
- pizza: "count/3 per straight edge, rest covering the top arc"
- square: "3~4 per side, walk one side then turn 90"
- hexagon: "120 degrees, 3 per side, turn and continue"

Today (deck: `neo-formation-shapes.html`): implement his three empty patterns
with one tool — the walker (walk `gap` px, after `side` ships turn). Square
first, hexagon = same block with 2 numbers changed (6, 60; his 120° is the
inside angle, walker turns 180−120=60), pizza = two cos/sin edges + arc crust.
Test lab first (force pattern, count=12, timer 400→60 — closes TASK 2 △).
OPTIONAL: escape plans from his own comments (age timer flips vx/vy),
360/sides any-shape table, crust angle trace.
