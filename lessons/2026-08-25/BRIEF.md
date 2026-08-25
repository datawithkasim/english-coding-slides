# Today's decks — 2026-08-25 (Tue)

One deck per student, built from what the tracker says they last did and what was
promised for next time. Requested slots: JASON 17:00, HWON 18:00 Korea time.

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
