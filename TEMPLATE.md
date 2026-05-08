# Slide Template — 12-Slot Structure

Every deck in this library follows the same 12-slot order. Teachers and students learn the rhythm; consistency lets us focus on content.

Total time per deck: **~10 minutes**.

## The 12 slots

| # | Slot | Time | Required? |
|---|------|------|-----------|
| 1 | **Title + Objective** | 30s | Yes |
| 2 | **Recap & Retrieve** | 60s | Yes (week 2+) |
| 3 | **Predict (Hook)** | 60s | Yes |
| 4 | **Vocab Preview** | 60s | Yes |
| 5 | **Concept (Notional Machine)** | 60s | Yes |
| 6 | **Run (Worked Example)** | 60s | Yes |
| 7 | **Investigate (Animated Trace)** | 90s | When applicable |
| 8 | **Common Mistake** | 45s | Yes |
| 9 | **Modify (Faded)** | 60s | Yes |
| 10 | **Code Talk Frame** | 45s | Yes |
| 11 | **Make / Your Turn** | 30s | Yes |
| 12 | **Close & Bridge** | 30s | Yes |

## Per-slide rules

1. **≤ 40 English words + ≤ 15 Korean words** per slide. Hard cap. ESL learners read ~30% slower than natives.
2. **Code adjacent to output.** Output box directly below or beside the code block. Never split with paragraphs.
3. **Active voice + SVO order.** "The variable stores the value" — not "The value is stored."
4. **One Tier 3 (domain-specific) term per 2–3 slides max.** Surround with familiar context.
5. **Korean glosses only on Tier 3 vocab + concept hooks + bridges.** Not on every line — translanguaging, not subtitling.
6. **Color-coded syntax**: `--kw` keywords (pink), `--str` strings (yellow), `--num` numbers (purple), `--fn` functions (green).
7. **Signaling**: highlight the line/word being explained with `var(--accent)` background pill.
8. **Reuse animation classes**: `.viz-3 / .viz-4 / .viz-5 / .picker / .dice / .monsters` already implement step-through. Don't reinvent.
9. **Common Mistake** uses `.compare-row` (red broken vs green fixed).
10. **Sentence Frame** uses `.frame-card` with visible `___` blanks.

## Skeleton HTML for new decks

Copy-paste, fill in the slots. Save under the right course folder.

```html
<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>COURSE WN — TITLE</title><link rel="stylesheet" href="../../assets/style.css"></head><body>
<div class="stage"><div class="footer-tag">COURSE · TRACK · Week N</div>

<!-- Slot 1: Title + Objective -->
<div class="slide active center-all">
  <span class="slot-badge">SLOT 1</span>
  <div class="pill">Week N</div>
  <div class="emoji">🎯</div>
  <h1>Lesson<br>Title</h1>
  <p class="big" style="margin-top:.6em;color:var(--accent-2);">By the end you'll <span class="sub">verb</span> + <span class="sub">verb</span></p>
  <p class="bilingual">한 줄 학습 목표</p>
</div>

<!-- Slot 2: Recap & Retrieve -->
<div class="slide">
  <span class="slot-badge">SLOT 2</span>
  <div class="pill purple">Recap</div>
  <h2>Last week you learned…</h2>
  <div class="recap-q">
    <div class="label">Quick check</div>
    <div class="q">Question that recalls last week's concept</div>
    <details><summary>Show answer</summary><div class="ans">The answer in one line.</div></details>
  </div>
</div>

<!-- Slot 3: Predict -->
<div class="slide">
  <span class="slot-badge">SLOT 3</span>
  <div class="pill">Predict 🤔</div>
  <h2>What will print?</h2>
  <div class="predict-card">
    <div class="label">Predict</div>
    <pre>code goes here</pre>
    <details><summary>Reveal output</summary><div class="ans">expected output</div></details>
  </div>
</div>

<!-- Slot 4: Vocab Preview -->
<div class="slide">
  <span class="slot-badge">SLOT 4</span>
  <div class="pill">Vocab</div>
  <h2>New words today</h2>
  <div class="vocab-table">
    <span class="term">term</span>
    <span class="gloss">English meaning</span>
    <span class="ko">한국어</span>
    <!-- repeat 1-3 times -->
  </div>
</div>

<!-- Slot 5: Concept (Notional Machine) -->
<div class="slide">
  <span class="slot-badge">SLOT 5</span>
  <div class="pill">Concept</div>
  <h2>The mental model</h2>
  <!-- visual analogy: varbox-row, bubble-card, etc. — NO code here -->
</div>

<!-- Slot 6: Run (Worked Example) -->
<div class="slide">
  <span class="slot-badge">SLOT 6</span>
  <div class="pill">Code</div>
  <h2>Run it</h2>
<pre>full code here</pre>
  <div class="output-box" style="margin-top:.5em">
    <div class="out-label">▸ Output</div>
    <div style="opacity:1">expected output</div>
  </div>
</div>

<!-- Slot 7: Investigate (Animated Trace) — optional if no iteration -->
<div class="slide">
  <span class="slot-badge">SLOT 7</span>
  <div class="pill">Watch it!</div>
  <h2>Step through</h2>
  <!-- use .viz-3, .picker, .dice, etc. -->
</div>

<!-- Slot 8: Common Mistake -->
<div class="slide">
  <span class="slot-badge">SLOT 8</span>
  <div class="pill">⚠️ Watch out</div>
  <h2>Common mistake</h2>
  <div class="compare-row">
    <div class="col bad"><span class="tag">✗ broken</span><pre>broken code</pre></div>
    <div class="col good"><span class="tag">✓ fixed</span><pre>correct code</pre></div>
  </div>
</div>

<!-- Slot 9: Modify (Faded) -->
<div class="slide">
  <span class="slot-badge">SLOT 9</span>
  <div class="pill">Try it</div>
  <h2>Fill in the blank</h2>
<pre>code with ___ blanks</pre>
  <p style="margin-top:.6em">Hint or constraint.</p>
</div>

<!-- Slot 10: Code Talk Frame -->
<div class="slide">
  <span class="slot-badge">SLOT 10</span>
  <div class="pill purple">Code Talk</div>
  <h2>Tell a partner</h2>
  <div class="frame-card">
    <div class="label">Sentence frame</div>
    <div class="frame">"<code>this code</code> does <span class="blank"></span> because <span class="blank"></span>."</div>
    <div class="pair-prompt">한국어로 먼저, 그다음 영어로 / Korean first, then English.</div>
  </div>
</div>

<!-- Slot 11: Make / Your Turn -->
<div class="slide">
  <span class="slot-badge">SLOT 11</span>
  <div class="pill">Your turn!</div>
  <h2>Build it 🚀</h2>
  <ul class="check-list">
    <li>Step 1</li>
    <li>Step 2</li>
    <li>Step 3</li>
  </ul>
</div>

<!-- Slot 12: Close & Bridge -->
<div class="slide center-all">
  <span class="slot-badge">SLOT 12</span>
  <div class="emoji">🌉</div>
  <h1 style="font-size:clamp(36px,6vmin,56px)">Big idea today</h1>
  <p class="big" style="margin-top:.5em;color:var(--accent-2);">Next week: tease</p>
  <p class="bilingual">다음 주 미리보기</p>
</div>

<div class="nav">
  <button id="prev">‹</button><span class="counter" id="counter">1 / 12</span><button id="next">›</button>
</div>
</div><script src="../../assets/deck.js"></script></body></html>
```

## Workflow checklist for a new deck

- [ ] Identify the week's main concept and 1–3 Tier 3 vocab terms
- [ ] Write a one-sentence retrieval question for slot 2 (about previous week)
- [ ] Write the predict scenario for slot 3 (output that requires the new concept)
- [ ] Look up the Tier 3 terms in `glossary.html` for consistent Korean glosses
- [ ] Build slot 5 with NO code — just visual mental model
- [ ] Build slot 6 with the simplest possible worked example
- [ ] Pick the right animation class for slot 7 if applicable
- [ ] Find the most common bug at this stage for slot 8
- [ ] Write a sentence frame matching the slot's concept (slot 10)
- [ ] Word-count slides — no slide over 40 EN + 15 KO
- [ ] Walkthrough timing should be 9–11 min

See `PEDAGOGY.md` for the research behind each slot.
