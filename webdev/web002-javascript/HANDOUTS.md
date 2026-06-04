# 📎 WEB002 — Concept Handouts

Standalone one-concept reference decks. Each exports to a self-contained **PDF** you can send a student alongside homework (open/print anywhere, no folder needed).

| Handout | Concept | 🖥️ Deck | 📄 PDF |
|---|---|---|---|
| The id Connection | one `id` links HTML · CSS · JS | [open](./id-connection.html) | [PDF](./id-connection.pdf) |
| Events (onclick) | a click runs your code | [open](./events-onclick.html) | [PDF](./events-onclick.pdf) |
| querySelector vs getElementById | two ways to grab an element | [open](./queryselector-vs-getelementbyid.html) | [PDF](./queryselector-vs-getelementbyid.pdf) |
| if / else | run code only when true | [open](./if-else.html) | [PDF](./if-else.pdf) |
| Variables (let / const) | boxes that hold a value | [open](./variables-let-const.html) | [PDF](./variables-let-const.pdf) |

---

## ➕ Add a new handout

1. Copy an existing deck `.html` in this folder, rewrite the slides (keep the brand classes + KO glosses).
2. Build the PDF:
   ```
   python scripts/build-deck-pdf.py webdev/web002-javascript/<name>.html
   ```
   (Print layout comes from the shared `@media print` block in `assets/style.css` — no per-file setup.)
3. Add a row to the table above.

> 핸드아웃은 학생에게 숙제와 함께 보내는 단일 개념 자료입니다. PDF만 보내면 됩니다.
