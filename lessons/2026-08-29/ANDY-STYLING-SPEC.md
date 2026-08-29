# ANDY · 2026-08-29 · Finish the styling (replaces the Manim deck for today)

Kasim: "we are not doing manim today we are going to finish styling his site.
tell me exactly what to do. no room for ambiguity."

The Manim deck (`andy-manim-first-animation.html`) stays in this folder for a
later lesson. Today's deck is this one.

## Where he works

`app.english-coding.co.uk` → his Workspace. Three files, exactly these names:
`index.html`, `main.css`, `scripts.js`. Today he edits **`main.css`** for every
step except the last two, which touch `scripts.js`.

Preview: open the `index.html` tab and press **Run** once — the page appears in
the preview panel. After that the preview re-draws by itself about half a
second after he stops typing, in whichever file he is editing. So: press Run
once at the start, then just watch the panel.

No terminal, no install, no build step.

## His site right now (verified against the live IDE, files unchanged since 22 Aug)

`index.html` — h1 "Daily Planner", five buttons (increase / decrease / square /
square root / reset), a `#clicksCounter` p, two intro lists, a to-do block of
four `.todo-item` rows (each = a `.content-gen` text input + a checkbox
`#chk1`–`#chk4`), then a 7-day timetable `<table>` inside `.container-hori`
with `th` ids `th-mon`…`th-sun` and each cell holding a `.plan-for-day` text
input plus a `data-day` checkbox.

`scripts.js` — the five button listeners, `updateCount(event)` on the four
to-do checkboxes, and a `days.forEach` block that toggles `day-complete` on a
day's `th` when all of that day's checkboxes are ticked.

`main.css` — 112 lines. What is actually wrong with it:
- `font-family: 'cursive'` — quoted, so the browser looks for a font *named*
  "cursive", does not find one, and falls back. The whole site is not styled
  the way he thinks it is.
- `h1` colour `#8fcc77` sits on a `rgb(218, 222, 192)` page — pale green on
  pale green. Barely readable. `padding: 60px` shoves the page down.
- `p` colour `rgb(59, 9, 243)` — hard blue, hurts to read.
- `button { border: 15px }` — a width with no style, so the browser throws the
  whole line away. Same bug in `.plan-for-day { border: 10px }`.
- `tr { min-width: none }` — `none` is not a legal `min-width`. Dead line.
- `.todo-container` sets `flex-direction` inside a `display: grid` box. Dead line.
- `th.day-complete` uses the **same** background as a normal `th`, so finishing
  a day changes almost nothing on screen.
- `.done` is written in the CSS but nothing ever puts that class on an element.

## The lesson — 16 steps, in this order

Each step below is literal. `FIND` = the text he searches for (Ctrl+F) in the
named file. `OLD` = what is there now, `NEW` = what it becomes. Do not reword
the code. Do not merge steps. Every step ends with a one-line ✅ check that
names what changes on screen.

### v1 — foundations (steps 1–3)

**STEP 1 · main.css · fix the font**
FIND: `font-family: 'cursive'`
OLD:
```
* {
    font-family: 'cursive'
}
```
NEW:
```
* {
    box-sizing: border-box;
    font-family: "Comic Sans MS", "Segoe UI", cursive;
}
```
WHY: quotes turned `cursive` into a font *name*. Without quotes it is a
keyword the browser understands. `box-sizing` stops padding from making boxes
wider than you asked.
✅ The whole page changes font.

**STEP 2 · main.css · centre the page**
FIND: `background-color: rgb(218, 222, 192)`
OLD:
```
body {
    background-color: rgb(218, 222, 192);
    font-family: 'cursive';
}
```
NEW:
```
body {
    background-color: rgb(218, 222, 192);
    max-width: 900px;
    margin: 0 auto;
    padding: 24px;
}
```
WHY: `margin: 0 auto` puts equal space left and right — the page sits in the
middle. The font line goes because the `*` rule above already covers it.
✅ Content pulls into a centred column.

**STEP 3 · main.css · make the title readable**
FIND: `color: #8fcc77;`
OLD:
```
h1 {
    color: #8fcc77;
    font-size: 32px;
    font-style: italic;
    font-weight: 600;
    text-align: center;
    padding: 60px;
    margin: 20px;
}
```
NEW:
```
h1 {
    color: #3c6b2c;
    font-size: 40px;
    font-style: italic;
    font-weight: 700;
    text-align: center;
    padding: 24px;
    margin: 0 0 16px;
}
```
WHY: same green, darker, so it stands off the pale page. 60px of padding was
pushing everything down a whole screen.
✅ Title is dark green and the page starts higher up.

### v2 — text (steps 4–5)

**STEP 4 · main.css · calm the paragraph colour**
FIND: `color:rgb(59, 9, 243);`
OLD:
```
p {
    line-height: 1.6;
    max-width: 600px;
    
    color:rgb(59, 9, 243);
}
```
NEW:
```
p {
    line-height: 1.6;
    max-width: 600px;
    color: #2b2233;
}
```
WHY: bright blue on pale green fights the eye. Near-black reads easily.
✅ Paragraphs turn dark grey.

**STEP 5 · main.css · style the two h2 headings**
WHERE: a brand new rule. Put it straight after the closing `}` of the `h1` rule.
NEW:
```
h2 {
    color: #3c6b2c;
    border-bottom: 3px solid #8fcc77;
    padding-bottom: 6px;
    margin-top: 32px;
}
```
WHY: `border-bottom` draws one line under the heading — it splits the page into
sections.
✅ "mathematical buttons" and "My To-Do List:" each get a green underline.

### v3 — buttons (steps 6–8)

**STEP 6 · main.css · give the buttons a real shape**
FIND: `background-color: #722F37;`
OLD:
```
button {
    padding: 5px;
    background-color: #722F37;
    color: #FFFFFF;
    border:15px
}
```
NEW:
```
button {
    padding: 10px 18px;
    background-color: #722F37;
    color: #FFFFFF;
    border: none;
    border-radius: 8px;
    cursor: pointer;
}
```
WHY: `border: 15px` is a width with no style, so the browser dropped it —
that line never did anything. `border-radius` rounds the corners. `cursor`
makes the mouse turn into a hand.
✅ Buttons get bigger, rounded, and the mouse becomes a hand over them.

**STEP 7 · main.css · make the hover fade**
FIND: `border-radius: 8px;`
OLD:
```
    border-radius: 8px;
    cursor: pointer;
```
NEW:
```
    border-radius: 8px;
    cursor: pointer;
    transition: background-color 0.2s;
```
WHY: `transition` slides between the two colours over 0.2 seconds instead of
snapping.
✅ Hover a button — the colour fades in, not jumps.

**STEP 8 · main.css · space the buttons out**
WHERE: a new rule, straight after the `button:hover` rule.
NEW:
```
button + button {
    margin-left: 8px;
}
```
WHY: `button + button` means "a button that comes right after another button".
The first one gets no gap; every one after it does.
✅ The five buttons stop touching.

### v4 — the timetable (steps 9–12)

**STEP 9 · main.css · delete a line that does nothing**
FIND: `min-width: none`
DELETE these four lines:
```
tr {
    min-width: none;
}
```
WHY: `none` is not a legal value for `min-width`, so the browser ignores the
whole rule. Dead code — take it out.
✅ Nothing changes on screen. That is the point.

**STEP 10 · main.css · fix the timetable inputs**
FIND: `padding-top: 30px;`
OLD:
```
.plan-for-day {
    margin: 8px 8px 8px 25px;
    padding-top: 30px;
    border: 10px
}
```
NEW:
```
.plan-for-day {
    width: 110px;
    margin: 4px;
    padding: 6px;
    border: 2px solid #8fcc77;
    border-radius: 6px;
}
```
WHY: `border: 10px` was the same broken bug as the button — no style, so no
border. `padding-top: 30px` made every box tall and empty at the top.
✅ Timetable boxes become neat, even, and the same width.

**STEP 11 · main.css · stripe the rows**
WHERE: a new rule, straight after the `th` rule.
NEW:
```
tbody tr:nth-child(even) {
    background-color: #eef0e0;
}
```
WHY: `:nth-child(even)` picks rows 2, 4, 6… Stripes make a wide table easy to
follow across.
✅ Every other row of the timetable goes slightly lighter.

**STEP 12 · main.css · make "day complete" obvious**
FIND: `th.day-complete`
OLD:
```
th.day-complete {
    background-color: #8fcc77;
    color: #A7002A
}
```
NEW:
```
th.day-complete {
    background-color: #2f5d22;
    color: #ffffff;
}
```
WHY: the old background was the *same colour* a `th` already has, so finishing
a day did almost nothing. Dark green plus white text is unmissable.
✅ Tick every checkbox in one day column — that day's header goes dark green.

### v5 — the to-do list (steps 13–16)

**STEP 13 · main.css · delete another dead line**
FIND: `flex-direction: column;`
OLD:
```
.todo-container {
    display: grid;
    flex-direction: column;
    gap: 10px;
    margin-top: 30px;
    margin-bottom: 30px;
}
```
NEW:
```
.todo-container {
    display: grid;
    gap: 10px;
    margin-top: 30px;
    margin-bottom: 30px;
}
```
WHY: `flex-direction` only works in a `display: flex` box. This box is `grid`,
so the line was ignored.
✅ Nothing changes on screen — the file just got honest.

**STEP 14 · main.css · turn each task into a card**
FIND: `.todo-item {`
OLD:
```
.todo-item {
    display: flex;
    align-items: center;
}
```
NEW:
```
.todo-item {
    display: flex;
    align-items: center;
    gap: 10px;
    background-color: #ffffff;
    border-radius: 8px;
    padding: 8px;
}
```
WHY: `gap` puts space between the text box and the checkbox without touching
either one.
✅ Each task sits on its own white rounded card.

**STEP 15 · main.css · bigger checkboxes**
WHERE: a new rule, straight after the `input` rule.
NEW:
```
input[type="checkbox"] {
    width: 20px;
    height: 20px;
    accent-color: #722F37;
    cursor: pointer;
}
```
WHY: `input[type="checkbox"]` picks only the checkboxes, not the text boxes.
`accent-color` recolours the tick itself.
✅ Checkboxes get bigger and tick in dark red.

**STEP 16 · scripts.js · finally use the `.done` class**
FIND: `statusText.textContent = "TASKS DONE: " + tasksDone;`
OLD:
```
function updateCount(event) {
    if (event.target.checked) {
        tasksDone = tasksDone + 1;
    } else {
        tasksDone = tasksDone - 1;
    }
    statusText.textContent = "TASKS DONE: " + tasksDone;
};
```
NEW:
```
function updateCount(event) {
    if (event.target.checked) {
        tasksDone = tasksDone + 1;
    } else {
        tasksDone = tasksDone - 1;
    }
    statusText.textContent = "TASKS DONE: " + tasksDone;
    event.target.parentElement.classList.toggle("done", event.target.checked);
};
```
WHY: `.done` has been sitting in his CSS since day one with nothing ever
wearing it. `parentElement` is the `.todo-item` card the checkbox sits in.
`toggle` with a true/false second argument means: add the class when ticked,
remove it when unticked — the same `event.target.checked` he already knows.
✅ Tick a task — the whole card fades to 40%.

**STEP 17 · main.css · strike the finished task out** (do this right after 16)
WHERE: a new rule, straight after the `.done` rule at the bottom.
NEW:
```
.todo-item.done .content-gen {
    text-decoration: line-through;
    color: #7a7a7a;
}
```
WHY: `text-decoration` on the card does not reach *inside* a text box, so the
line has to be aimed at `.content-gen` directly. `.todo-item.done` with no
space means "an element that has BOTH classes".
✅ Tick a task — the typed text now has a line through it as well.

## OPTIONAL bonus steps (only if there is time — tag every one OPTIONAL)

- `input:focus { outline: 3px solid #722F37; }` — show which box is selected
- `tbody tr:hover { background-color: #dfe4c8; }` — highlight the row under the mouse
- `.container-hori { display: flex; max-width: max-content; overflow-x: auto; }`
  — lets the wide table scroll sideways on an iPad instead of squashing
- `th { position: sticky; top: 0; }` — day names stay put while scrolling
- `#statusText` and `#count` as pills: `background-color: #722F37; color: #fff;
  display: inline-block; padding: 6px 14px; border-radius: 999px;`
- `box-shadow: 0 2px 6px rgba(0,0,0,.15);` on `.todo-item` and on `table`
- CSS variables: `:root { --leaf: #8fcc77; --leaf-dark: #3c6b2c; --wine: #722F37; }`
  then `color: var(--leaf-dark);` — change one line, the whole site changes
- `@media (max-width: 700px) { body { padding: 12px; } h1 { font-size: 28px; } }`
- `ol, ul { line-height: 1.8; }` — the two intro lists are still unstyled
- A colour-swap challenge: pick a new palette and change only the `:root` block

## Deck rules

Same as the ANDY Manim deck: a guided walkthrough, zero ambiguity, `.steptag`
STEP n / 17, `.find` for the Ctrl+F line, OLD/NEW via `.was` / `.now` /
`.tag-old` / `.tag-new`, a `.why` line, a `.chk` ✅ line naming what he should
see. He types every line himself — never say copy-paste.

Recap slot: his own last session — he built the weekly task tracker: the
`updateCount(event)` function, `event.target.checked`, and the `days.forEach`
block that turns a day header green. Today finishes the look of that page.

Topic slug: `andy-finish-the-styling`.
