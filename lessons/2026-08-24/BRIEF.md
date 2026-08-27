# Today's decks — 2026-08-24 (Mon)

One deck per student, built from what the tracker says they last did and what was
promised for next time. Seven Monday slots, 15:10 → 21:00 Korea time.

## Hard rules for every deck

Read first, in this order:
1. `../../TEMPLATE.md` — the 20-slot structure and the per-slide rules
2. `../../PEDAGOGY.md` — why each slot exists
3. `../../assets/style.css` — the only styling allowed; the BC-track section holds
   `.trace-grid`, `.debug-card`, `.err`, `.quiz-card`, `.stretch-list`, `.exit`,
   `.activity-tag`
4. One finished deck in the matching course folder, as the reference for tone

Then:
- Save to `lessons/2026-08-24/<file>.html`. Stylesheet path is
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
