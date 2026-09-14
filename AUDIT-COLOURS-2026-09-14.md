# Colour audit — SVG text on the cream background

Date: 2026-09-14. Scanned: `lessons/*/*.html` (144 decks).
Tool: WCAG relative-luminance contrast check on every `<svg><text>` fill,
resolved against the topmost `<rect>/<circle>/<ellipse>` painted under it,
falling back to the page background `--bg: #faf6f0`.

## Headline

- **4,055** SVG text elements across **56 decks** are Dracula/dark-theme colours sitting directly on cream. They fail 4.5:1; most are near-invisible (1.0–2.9:1).
- **130** more are dark-on-dark inside code boxes. Many of those are the deliberate "old line dimmed" style (#4a5670 on #1e1e2e = 2.23:1) — leave them.
- Root cause 1: the 2026-09-09 flip to the light cream palette changed `assets/style.css` only. Inline SVG `fill="..."` values in the decks were never flipped.
- Root cause 2 — **still live**: decks written *after* the flip carry the same fills (seohyeon 09-10 = 121, andy 09-12 = 110, amy 09-14 = 151, yunho 09-14 = 347). Each morning's deck is hand-authored by copying an older deck, so the dark palette keeps being carried forward. `lesson-deck-generator.html` is **not** the leak — its `--str/--com/--fn` tokens live inside dark `<pre>` boxes and are correct there.
- Not a problem: purple `h2` (`--accent-2` #6b4ee6 = 5.06:1), orange pill, red box border. Those are the deck's own tokens.


## Fix applied 2026-09-14

`python scripts/svgcontrast.py "<glob>" --fix --apply` rewrote **5,210** text fills in
**53** decks under `lessons/`, and **5,099** in **51** decks under
`../english-coding-students/students/*/slides/`. Nothing is committed or pushed.

Guarantees, all machine-checked after the run:

- Zero SVG text is left failing on cream in either repo.
- Only `<text>` tags changed. Every file was compared to its `HEAD` version with all
  `<text ...>` tags blanked out: 0 of 104 files differ anywhere else. Block fills,
  strokes, rects, code boxes and `<pre>` syntax colours are byte-identical.
- Re-running the fixer rewrites nothing (idempotent).

Left alone on purpose:

- **460** (lessons) / **458** (students) texts that are dim *inside* dark code boxes -
  the deliberate "old line faded" style. None of them sit on cream.
- **199** light texts in **14** decks whose SVG has a gradient or a dark
  `<path>`/`<polygon>` backdrop. The flat containment test cannot tell whether those
  sit on the dark shape (correct) or on cream (broken), so the fixer skips the whole
  SVG. These need an eyeball:

- `lessons/2026-09-09/eunwoo-one-loop-two-lists.html` - 77
- `lessons/2026-09-03/eric-trees-that-take-orders.html` - 30
- `lessons/2026-09-04/ian-kim-the-square-that-grows.html` - 14
- `lessons/2026-09-03/ian-one-file-styles-them-all.html` - 13
- `lessons/2026-09-10/jj-the-spiral-staircase.html` - 11
- `lessons/2026-09-13/logan-the-wall-you-cannot-cross.html` - 11
- `lessons/2026-09-07/yunho-let-the-loop-build.html` - 8
- `lessons/2026-09-10/ian-name-the-colour-once.html` - 8
- `lessons/2026-09-06/logan-keyboard-control.html` - 7
- `lessons/2026-08-31/amy-player-card-solo.html` - 5
- `lessons/2026-08-31/jaden-my-own-command.html` - 5
- `lessons/2026-09-11/junwoo-the-floor-fills-itself.html` - 5
- `lessons/2026-09-09/seohoo-two-numbers-one-tower.html` - 3
- `lessons/2026-09-03/jj-the-growing-staircase.html` - 2

`<g transform="translate(...)">` **is** handled - all 234 groups in the decks are
translate-only, and the checker composes the offsets.

## Offending fills, by how often they appear on cream

| fill | count | on cream | role | replace with |
|---|---|---|---|---|
| `#8a97b8` | 2152 | 2.71:1 | muted label / caption | `#4a5268` (7.2:1) |
| `#38d0e0` | 483 | 1.73:1 | cyan code / question | `#0b6b78` (5.8:1) |
| `#50fa7b` | 321 | 1.27:1 | green yes / success | `#17693a` (6.3:1) |
| `#f1fa8c` | 215 | 1.04:1 | yellow key caption | `#1f2233` ink (14.6:1) |
| `#8b5cf6` | 209 | 3.93:1 | purple axis label | `#764BCC` (5.4:1) |
| `#e8eef6` | 189 | 1.08:1 | near-white code | `#1f2233` ink (14.6:1) |
| `#ff5555` | 102 | 2.92:1 | red warning | `#c2261c` (5.4:1) |
| `#ff79c6` | 86 | 2.22:1 | pink accent | `#a8236e` (6.2:1) |
| `#ffb86c` | 47 | 1.58:1 | orange accent | `#b45309` (4.7:1) |
| `#bd93f9` | 46 | 2.24:1 | light purple | `#764BCC` (5.4:1) |
| `#ff9a9a` `#ff5f56` `#ff8fa3` | 83 | 2.8:1 | reds | `#c2261c` (5.4:1) |
| `#3cdc78` `#7bffa8` | 34 | 1.67:1 | greens | `#17693a` (6.3:1) |

Warning on greens: every green already in `style.css` fails on cream
(#28a745 = 3.0, #569138 = 3.5, #2bb673 = 2.4). Use `#17693a` or ink.

## The slide in the screenshot

`lessons/2026-09-14/amy-the-fight-that-repeats.html` slide 25, lines 439–440:

```
<text x="10" y="164" fill="#f1fa8c" ...>Five hits means five copies of the same line.</text>   1.04:1
<text x="10" y="186" fill="#3cdc78" ...>A loop writes them for you.</text>                      1.67:1
```

Both sit **below** the dark rect (y 14→134), so they land on cream. The #8a97b8
code lines and #ff5555 line above them are inside the box and are fine.

## Decks, worst first

- lessons\2026-08-24\eunwoo-shape-first.html                   31 bad
- lessons\2026-08-30\logan-pygame-window.html                   2 bad
- lessons\2026-08-31\amy-player-card-solo.html                  3 bad
- lessons\2026-08-31\eunwoo-see-the-numbers.html               14 bad
- lessons\2026-08-31\jaden-my-own-command.html                  7 bad
- lessons\2026-08-31\neo-formation-trig-solo.html              17 bad
- lessons\2026-08-31\siyun-maze-and-or.html                    13 bad
- lessons\2026-08-31\yunho-pixel-art-bigger.html              267 bad
- lessons\2026-09-01\eunwoo-see-the-numbers.html               14 bad
- lessons\2026-09-01\eunwoo-two-strands.html                    8 bad
- lessons\2026-09-01\jiyu-pixel-art-with-loops.html           132 bad
- lessons\2026-09-02\eunwoo-see-the-numbers.html               14 bad
- lessons\2026-09-02\ihyeon-maze-first-turn.html               68 bad
- lessons\2026-09-02\neo-bullets-that-hurt.html                65 bad
- lessons\2026-09-02\seohoo-pixels-with-a-loop.html            49 bad
- lessons\2026-09-03\eric-trees-that-take-orders.html          50 bad
- lessons\2026-09-03\ian-one-file-styles-them-all.html         11 bad
- lessons\2026-09-03\jj-the-growing-staircase.html             25 bad
- lessons\2026-09-03\seohyeon-loop-inside-a-loop.html          59 bad
- lessons\2026-09-03\serena-make-the-cat-jump.html            240 bad
- lessons\2026-09-04\ian-kim-the-square-that-grows.html        16 bad
- lessons\2026-09-04\junwoo-one-repeat-many-rows.html         226 bad
- lessons\2026-09-04\nellie-the-agent-does-the-placing.html    25 bad
- lessons\2026-09-05\andy-many-things-at-once.html             51 bad
- lessons\2026-09-05\dewy-the-loop-turns-the-corner.html       42 bad
- lessons\2026-09-05\joy-lesson-1-the-agent-obeys.html         57 bad
- lessons\2026-09-05\suho-one-repeat-every-layer.html          78 bad
- lessons\2026-09-05\yura-one-repeat-many-steps.html            6 bad
- lessons\2026-09-06\claire-hp-bar.html                       155 bad
- lessons\2026-09-06\david-p-inverted-pyramid.html             23 bad
- lessons\2026-09-06\logan-keyboard-control.html               27 bad
- lessons\2026-09-07\amy-keep-going-until.html                108 bad
- lessons\2026-09-07\neo-name-your-own-command.html           108 bad
- lessons\2026-09-07\yunho-let-the-loop-build.html            393 bad
- lessons\2026-09-09\eunwoo-one-loop-two-lists.html           451 bad
- lessons\2026-09-09\ihyeon-agent-feels-the-wall.html         152 bad
- lessons\2026-09-09\neo-a-box-that-answers.html               76 bad
- lessons\2026-09-09\seohoo-two-numbers-one-tower.html        101 bad
- lessons\2026-09-09\yoojun-first-square.html                  37 bad
- lessons\2026-09-10\ian-name-the-colour-once.html             17 bad
- lessons\2026-09-10\jiyu-one-fill-many-times.html             68 bad
- lessons\2026-09-10\jj-the-spiral-staircase.html              17 bad
- lessons\2026-09-10\seohyeon-loop-inside-a-loop.html          79 bad
- lessons\2026-09-10\serena-three-ledges-one-list.html          6 bad
- lessons\2026-09-11\ian-the-box-reads-itself.html             32 bad
- lessons\2026-09-11\nellie-the-agent-does-the-placing.html    41 bad
- lessons\2026-09-12\andy-andy-sets-the-clock.html             68 bad
- lessons\2026-09-12\dewy-a-loop-inside-a-loop.html            35 bad
- lessons\2026-09-12\joy-one-repeat-walks-the-square.html      51 bad
- lessons\2026-09-12\yura-the-square-unrolls.html              13 bad
- lessons\2026-09-13\claire-damage-then-the-bar.html            9 bad
- lessons\2026-09-13\david-p-upside-down-pyramid.html           5 bad
- lessons\2026-09-13\logan-the-wall-you-cannot-cross.html      16 bad
- lessons\2026-09-14\amy-the-fight-that-repeats.html          151 bad
- lessons\2026-09-14\neo-a-table-that-answers.html              9 bad
- lessons\2026-09-14\yunho-maths-on-the-counter.html          347 bad

## How the fix must be done

**Do not run a global find-and-replace on these hexes.** `#8a97b8` is *correct* inside a
dark code box (5.62:1 on `#1e1e2e`) and broken on cream — the same hex appears hundreds of
times in each context. Any fix has to reuse the checker's containment test and rewrite only
the elements it flags.

## Caveats

- 15 decks use `<g transform>`; the checker ignores transforms, so a handful of their flags may be false positives.
- Text placed over a `<path>` or `<polygon>` backdrop is also scored against cream. Spot-check before a blind replace.
- `english-coding-students/students/*/slides/` holds copies of these decks. Same faults, same fix.

## Reproduce

`python scripts/svgcontrast.py "lessons/*/*.html" -v` to check;
add `--fix` for a dry run and `--fix --apply` to write.
