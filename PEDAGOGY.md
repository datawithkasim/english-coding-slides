# Why this template works — research backing

Each of the 12 slots in `TEMPLATE.md` maps to evidence-based teaching practice. This file is a quick reference so future contributors understand the **why** behind the structure.

## Two pedagogies, woven together

The template combines:

- **Programming pedagogy** — how to teach kids to read and write code.
- **ESL pedagogy** — how to teach content in a second language.

Korean students at English Coding learn both *at the same time*. The template treats this as a feature, not a constraint.

## Slot-by-slot rationale

### Slot 1 — Title + Objective
- **SIOP §1 (Lesson Preparation)**: clear, posted objectives improve ESL comprehension. Students know what success looks like.
- **CLIL Cognition**: framing learning around a verb ("you'll *predict*, *trace*, and *modify* loops") names the cognitive skill, not just the topic.

### Slot 2 — Recap & Retrieve
- **Spaced repetition / retrieval practice**: revisiting previous concepts at expanding intervals strengthens long-term memory more than re-explaining (Roediger & Karpicke, 2006).
- **SIOP §2 (Building Background)**: connecting to prior knowledge is essential for ESL learners.
- The `<details>` reveal pattern lets students *try* before they see the answer — that's retrieval, not recognition.

### Slot 3 — Predict (Hook)
- **PRIMM-P (Sue Sentance)**: prediction *before* execution forces engagement with the notional machine. Students who only watch code run learn less.
- **Krashen's i+1**: the prediction stage exposes learners to language slightly above their level in a context they care about (the answer).
- **Curiosity gap**: an unresolved question primes attention for the rest of the lesson.

### Slot 4 — Vocab Preview
- **Beck/McKeown Tier 1/2/3 model**: pre-teaching Tier 3 (domain-specific) vocab unlocks the rest of the deck. Without the word "loop" defined, every other slide is harder.
- **Translanguaging (García)**: a Korean gloss is a *bridge*, not a crutch. Strategic L1 use deepens English acquisition.
- **Konglish flag**: false friends (e.g., 'function' ≠ 함수 in casual usage) sabotage comprehension if not surfaced.

### Slot 5 — Concept (Notional Machine)
- **Sorva on notional machines**: students need an explicit, shared mental model of how code executes. Without it, misconceptions persist.
- **CS Unplugged (Bell et al.)**: visual / kinesthetic analogies before syntax reduce intrinsic cognitive load.
- **Mayer's Dual Coding**: pairing visual model with text uses two cognitive channels — better retention than either alone.
- **No code on this slide on purpose**: keeps focus on concept, not syntax.

### Slot 6 — Run (Worked Example)
- **Sweller's Worked-Example Effect**: 22+ controlled studies show novices learn faster from complete worked examples than from solving problems unaided.
- **Mayer's Spatial Contiguity**: code and its output must be adjacent. Splitting them across the screen forces the learner to hold one in working memory while reading the other — added cost, no benefit.
- **PRIMM-R**: the "Run" stage cements what the prediction set up.

### Slot 7 — Investigate (Animated Trace)
- **PRIMM-I**: tracing variable values frame-by-frame is how kids build the notional machine.
- **Python Tutor (Guo)**: 25M+ users; adopted at MIT, Harvard, Berkeley. The animated trace is the gold standard for procedural concepts.
- We reuse `.viz-3` / `.viz-4` / `.viz-5` (CSS animations) and `.picker` / `.dice` / `.monsters` (JS animations) so this is *one prebuilt component* per concept, not 64 hand-built diagrams.

### Slot 8 — Common Mistake
- **Misconception research (Sorva, Lopez et al.)**: novice bugs are predictable (`=` vs `==`, off-by-one, scope confusion, indent errors). Preempting them in instruction beats fixing them in homework.
- **Two-column compare** (red broken vs green fixed) leverages **contrast** — a high-effect-size principle in concept teaching.

### Slot 9 — Modify (Faded)
- **Use-Modify-Create progression**: after seeing a worked example, students gain agency by changing one piece — but with the structure intact.
- **Faded scaffolding (Renkl et al.)**: removing one step at a time is faster than asking for a full solution. The blank guides the learner toward the concept being practiced.

### Slot 10 — Code Talk Frame
- **Sentence frames (Colorín Colorado)**: ESL learners need scaffolds to *speak* about content, not just understand it. Frames give a syntactic skeleton.
- **CLIL Communication**: language practice is part of every content lesson, not a separate skill.
- **Translanguaging in pairs**: students discuss in Korean first, then encode in English. This deepens both.

### Slot 11 — Make / Your Turn
- **UMC-Create**: open-ended challenge ties to the course's final project. Motivation is highest when the lesson contributes to a real artifact.
- **Authentic task (Wiggins & McTighe)**: learners do what real programmers do — apply the concept to their own code.

### Slot 12 — Close & Bridge
- **Spaced repetition prompt**: a one-line tease keeps the concept alive between sessions.
- **Narrative arc**: each lesson is a chapter; each course is a story. Keeps engagement across 8 weeks.

## The hard limits

| Rule | Why |
|---|---|
| ≤ 40 EN + ≤ 15 KO words/slide | ESL reads ~30% slower; cognitive load already high from code. |
| Code adjacent to output | Mayer Spatial Contiguity — effect size 1.10 across 22 studies. |
| Active voice, SVO order | Matches Korean particle-stripped action order; reduces transfer error. |
| Color-coded syntax | Mayer Signaling — points working memory at what matters. |
| One Tier 3 term per 2–3 slides | Pre-teach surface area limit; avoids vocab overload. |

## Sources

- Sentance, S. *Computing Education Research Centre, Cambridge*. PRIMM model. https://primmportal.com
- Lee, I. et al. *Use-Modify-Create*. ACM SIGCSE.
- Sweller, J. *Cognitive Load Theory*; Sweller & Cooper, *Worked Example Effect*.
- Mayer, R.E. *Multimedia Learning* (3rd ed.), 2014.
- Sorva, J. *Notional Machines and Introductory Programming Education*.
- Bell, T. et al. *CS Unplugged*. https://csunplugged.org
- Beck, McKeown, Kucan. *Bringing Words to Life* (Tier 1/2/3 vocabulary).
- García, O. *Translanguaging in Bilingual Education*.
- Krashen, S. *Comprehensible Input* (i+1).
- Echevarria, Vogt, Short. *SIOP Model* (8 components).
- Roediger & Karpicke. *Test-Enhanced Learning* (retrieval practice).
- Colorín Colorado. *Sentence Frames for ELLs*.

This template is a synthesis. Refine as we learn what actually works in our classrooms.
