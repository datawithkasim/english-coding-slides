# Animated viz snippets — drop-in templates

Each pattern below is one `<div class="slide">` you can paste directly after the slide that introduces the construct. Customise values to match the lesson's example, then leave the markup structure as-is — CSS in `assets/style.css` drives the animation.

Standard wrapper for every viz slide:

```html
<div class="slide"><div class="pill">Watch it!</div><h2>{TITLE}</h2>
  {VIZ-BLOCK}
  <p class="bilingual">{KOREAN-LABEL}</p></div>
```

The `pill` text "Watch it!" tells students the slide is a live demo. Korean bilingual line is optional but recommended for student-facing decks.

---

## 1. For-loop iteration

Already supported via `.viz-3` / `.viz-4` / `.viz-5`. Existing example (see `webdev/web002-javascript/week-06-arrays-loops.html`):

```html
<div class="viz viz-3">
  <div class="iter-row">
    <div class="iter-item">"a"</div>
    <div class="iter-item">"b"</div>
    <div class="iter-item">"c"</div>
  </div>
  <div class="var-row"><span class="label">i = </span><span class="var-vals">
    <span class="var-val">0</span><span class="var-val">1</span><span class="var-val">2</span>
  </span></div>
  <div class="output-box">
    <div class="out-label">▸ Output</div>
    <div class="out-line">a</div>
    <div class="out-line">b</div>
    <div class="out-line">c</div>
  </div>
</div>
```

For 4 items use `viz-4` (one more `iter-item`, `var-val`, and `out-line`). For 5 items use `viz-5`. Don't go beyond 5 — students lose track.

---

## 2. List / array index lookup (NEW)

When the lesson introduces `items[2]` or `quotes[i]` indexing (not iteration), prefer this over viz-N — it shows the pointer moving and the value popping out for a single expression.

```html
<div class="viz viz-index">
  <div class="iter-row">
    <div class="iter-item">"a"</div>
    <div class="iter-item">"b"</div>
    <div class="iter-item">"c"</div>
    <div class="iter-item">"d"</div>
  </div>
  <div class="idx-expr">
    <span class="idx-name">items</span>[<span class="idx-num">
      <span>0</span><span>1</span><span>2</span><span>3</span>
    </span>]
  </div>
  <div class="output-box">
    <div class="out-label">▸ value</div>
    <div class="out-line">"a"</div>
    <div class="out-line">"b"</div>
    <div class="out-line">"c"</div>
    <div class="out-line">"d"</div>
  </div>
</div>
```

---

## 3. If / else branching (NEW)

Cycles two scenarios (true → false) every 8 s so students see both branches taken.

```html
<div class="viz viz-if">
  <div class="if-input">
    <span class="case case-a">age = 14</span>
    <span class="case case-b">age = 9</span>
  </div>
  <div class="if-cond">age &gt;= 13</div>
  <div class="if-branches">
    <div class="if-branch true">print("teen")</div>
    <div class="if-branch false">print("kid")</div>
  </div>
  <div class="if-output">
    <div class="out-label">▸ Output</div>
    <div class="out-line out-a">teen</div>
    <div class="out-line out-b">kid</div>
  </div>
</div>
```

Rules:
- `.case-a` must satisfy the condition; `.case-b` must NOT.
- Branch labels (`✓ true →`, `✗ false →`) are auto-prepended via CSS.
- Output `out-a` shows when scenario A is on; `out-b` when B is on.

---

## 4. While loop (NEW)

Three iterations + exit. 8 s cycle.

```html
<div class="viz viz-while">
  <div class="wh-var">
    <span class="vname">count</span> = <span class="vval">
      <span>0</span><span>1</span><span>2</span><span>3</span>
    </span>
  </div>
  <div class="wh-cond">count &lt; 3</div>
  <div class="wh-body">print(count); count += 1</div>
  <div class="output-box">
    <div class="out-label">▸ Output</div>
    <div class="out-line">0</div>
    <div class="out-line">1</div>
    <div class="out-line">2</div>
    <div class="out-line wh-exit">→ exit loop</div>
  </div>
</div>
```

If the lesson's loop counts down or uses different stops, edit the values but keep exactly 4 `vval` spans + 3 output lines + 1 `wh-exit` line.

---

## 5. Function call + return (NEW)

```html
<div class="viz viz-func">
  <div class="fn-caller">
    <span class="fn-callcode">greet(<span class="arg">"Min"</span>)</span>
    <span class="fn-result">→ <span class="rv">"Hello, Min!"</span></span>
  </div>
  <div class="fn-flow-down">↓ call</div>
  <div class="fn-body">
    <div class="fn-sig">def greet(<span class="param">name</span>):</div>
    <div class="fn-line">return "Hello, " + <span class="param-use">name</span> + "!"</div>
  </div>
  <div class="fn-flow-up">↑ return</div>
</div>
```

For JS, change `def greet(name):` to `function greet(name) {` (and add `}` to a second fn-line). Same structure.

---

## 6. Variable re-assignment timeline (NEW)

For lessons introducing `x = 1; x = x + 4; …`. Code lines highlight in sequence; one big var box on the right updates value.

```html
<div class="viz viz-reassign">
  <div class="ra-code">
    <div class="ra-line">x = 1</div>
    <div class="ra-line">x = x + 4</div>
    <div class="ra-line">x = x * 2</div>
    <div class="ra-line">x = x - 3</div>
  </div>
  <div class="ra-box">
    <span class="ra-name">x</span>
    <span class="ra-vals">
      <span>1</span><span>5</span><span>10</span><span>7</span>
    </span>
  </div>
</div>
```

Exactly 4 lines + 4 values.

---

## 7. Dict / object lookup (NEW)

Two scenarios per 8 s cycle (looks up two different keys).

```html
<div class="viz viz-dict">
  <div class="d-table">
    <div class="d-row"><span class="d-key">"hp"</span><span class="d-sep">:</span><span class="d-val">35</span></div>
    <div class="d-row"><span class="d-key">"type"</span><span class="d-sep">:</span><span class="d-val">"electric"</span></div>
    <div class="d-row"><span class="d-key">"name"</span><span class="d-sep">:</span><span class="d-val">"Pikachu"</span></div>
  </div>
  <div class="d-lookup">pokemon[<span class="d-qs"><span class="d-q d-q1">"hp"</span><span class="d-q d-q2">"name"</span></span>]</div>
  <div class="output-box">
    <div class="out-label">▸ Output</div>
    <div class="out-line d-out d-out1">35</div>
    <div class="out-line d-out d-out2">"Pikachu"</div>
  </div>
</div>
```

First scenario (`d-q1` + `d-out1`) highlights row 1. Second scenario (`d-q2` + `d-out2`) highlights row 3. Row 2 is shown but not selected — that's intentional so students see other keys exist.

If the lesson covers only one lookup, you can still include both scenarios — picking two real keys reinforces the pattern.

---

## 8. Event flow (NEW)

For `addEventListener` lessons. Steps light up in sequence.

```html
<div class="viz viz-event">
  <div class="ev-step ev-click">🖱 click</div>
  <div class="viz-arrow">↓</div>
  <div class="ev-step ev-listen">button.addEventListener("click", run)</div>
  <div class="viz-arrow">↓</div>
  <div class="ev-step ev-run">run() fires</div>
  <div class="viz-arrow">↓</div>
  <div class="ev-step ev-dom">DOM updates ✓</div>
</div>
```

---

## 9. Coordinates / sprite movement (NEW)

For pygame x/y, gravity, key-controlled movement.

```html
<div class="viz viz-coord">
  <div class="cg-grid">
    <div class="cg-axis">x →</div>
    <div class="cg-track"><div class="cg-sprite">🎮</div></div>
  </div>
  <div class="cg-readout">
    <span class="cg-name">x</span> = <span class="cg-val">
      <span>0</span><span>100</span><span>200</span><span>300</span>
    </span>
  </div>
</div>
```

For y-axis / gravity, change `x →` to `y ↓`, sprite glyph as appropriate, and `cg-name` to `y`.

---

# Placement rules

- Insert each "Watch it!" slide **immediately after** the concept slide that introduces the construct.
- Use `<div class="pill">Watch it!</div>` (matches existing decks like web002 W6).
- Don't replace existing concept slides — these are additive.
- Don't add viz to recap / vocab / quiz / "your turn" slides.
- One viz per construct per deck is plenty. Don't double up.
- If a deck genuinely has no applicable construct (e.g. CSS box-model lesson), skip — don't shoehorn.

# Korean labels

For the optional `<p class="bilingual">` under each viz, use the construct's Korean name:
- For loop: 반복문
- While loop: 조건 반복
- If / else: 조건문
- Function: 함수
- Variable reassignment: 변수 재할당
- Dict / lookup: 사전 조회 / 객체 조회 (use 사전 for Python dict, 객체 for JS object)
- Event: 이벤트 흐름
- List index: 리스트 인덱스
- Coordinates: 좌표
