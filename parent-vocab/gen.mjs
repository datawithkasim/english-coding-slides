// Build one print-ready HTML per curriculum from data.mjs.
// Run: node gen.mjs   → writes parent-vocab/html/<code>.html and prints the list.
import { CURRICULA } from "./data.mjs";
import { writeFileSync, mkdirSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

const here = dirname(fileURLToPath(import.meta.url));
const outDir = join(here, "html");
mkdirSync(outDir, { recursive: true });

const esc = (s) =>
  String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");

function weekGroups(terms) {
  const map = new Map();
  for (const t of terms) {
    if (!map.has(t.w)) map.set(t.w, []);
    map.get(t.w).push(t);
  }
  return [...map.entries()];
}

function page(c) {
  const groups = weekGroups(c.terms)
    .map(
      ([w, items]) => `
    <section class="week">
      <h2><span class="wk">${esc(w)}</span></h2>
      <table>
        <colgroup><col class="c1"><col class="c2"><col class="c3"></colgroup>
        <thead><tr><th>단어</th><th>의미</th><th>간단한 예시</th></tr></thead>
        <tbody>
        ${items
          .map(
            (t) => `<tr>
            <td><span class="term">${esc(t.t)}</span></td>
            <td class="def">${esc(t.d)}</td>
            <td><pre class="ex">${esc(t.ex)}</pre></td>
          </tr>`
          )
          .join("\n")}
        </tbody>
      </table>
    </section>`
    )
    .join("\n");

  return `<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<title>${esc(c.code)} 어휘 — 영어코딩</title>
<style>
  @page { size: A4; margin: 20mm 18mm 22mm; }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  html { font-family: "Inter", "Segoe UI", system-ui, sans-serif; color: #1a1a2e; }
  body { font-size: 11px; line-height: 1.45; }
  .cover {
    border-bottom: 3px solid #ff7849; padding-bottom: 16px; margin-bottom: 22px;
  }
  .brand { font-size: 13px; font-weight: 800; color: #ff7849; letter-spacing: .04em; }
  .cover h1 { font-size: 26px; color: #6b4ee6; margin: 8px 0 6px; }
  .cover .blurb { font-size: 12px; color: #555; }
  .cover .note {
    margin-top: 14px; background: #fff6ef; border: 1px solid #ffd9c2;
    border-radius: 8px; padding: 12px 16px; font-size: 11px; color: #8a4b22;
    line-height: 1.6;
  }
  .week { break-inside: avoid; margin-bottom: 18px; }
  .week h2 { margin-bottom: 8px; }
  .wk {
    display: inline-block; background: #6b4ee6; color: #fff; font-weight: 800;
    font-size: 11px; padding: 3px 10px; border-radius: 999px; letter-spacing: .06em;
  }
  table { width: 100%; border-collapse: collapse; table-layout: fixed; }
  th, td { text-align: left; vertical-align: top; padding: 8px 12px; border-bottom: 1px solid #eee; }
  th { font-size: 9px; text-transform: uppercase; letter-spacing: .1em; color: #999; font-weight: 800; padding-bottom: 6px; }
  col.c1 { width: 24%; } col.c2 { width: 40%; } col.c3 { width: 36%; }
  .term {
    font-family: "JetBrains Mono", "Consolas", monospace; font-weight: 800;
    color: #ff7849; background: #fff1e8; padding: 2px 6px; border-radius: 5px;
    display: inline-block; word-break: break-word;
  }
  .def { color: #333; }
  pre.ex {
    font-family: "JetBrains Mono", "Consolas", monospace; font-size: 10px;
    background: #1e1e2e; color: #b9f6ca; padding: 8px 12px; border-radius: 6px;
    white-space: pre-wrap; word-break: break-word;
  }
  footer {
    position: fixed; bottom: 10mm; left: 18mm; right: 18mm; text-align: center;
    font-size: 9px; color: #aaa;
  }
  footer b { color: #ff7849; }
</style>
</head>
<body>
  <div class="cover">
    <div class="brand">📚 영어코딩</div>
    <h1>${esc(c.code)} · ${esc(c.title)}</h1>
    <div class="blurb">${esc(c.track)} — ${esc(c.blurb)}</div>
    <div class="note">
      <b>학부모님께:</b> 자녀가 이 과정에서 매주 만나는 핵심 영어 코딩 단어들입니다.
      직접 코딩하실 필요는 없습니다 — 단어를 함께 읽어 보시고, 자녀에게 자기 말로
      다시 설명해 달라고 해 주세요. 옆의 짧은 예시는 실제 코드에서의 모습입니다.
    </div>
  </div>
  ${groups}
  <footer>영어코딩 · <b>english-coding.co.uk</b> · ${esc(c.code)} 어휘 목록</footer>
</body>
</html>`;
}

const list = [];
for (const c of CURRICULA) {
  const f = join(outDir, `${c.code}.html`);
  writeFileSync(f, page(c), "utf8");
  list.push({ code: c.code, file: f, terms: c.terms.length });
}
console.log(JSON.stringify(list));
console.error(`Wrote ${list.length} HTML files to ${outDir}`);
