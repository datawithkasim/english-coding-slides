#!/usr/bin/env python3
"""Build lesson-deck-generator.html from the .src template.

Injects three things the browser tool can't fetch from a file:// origin:
  __HOUSE_CSS__      -> assets/style.css   (so generated decks are self-contained)
  __HOUSE_JS__       -> assets/deck.js
  __DECK_MANIFEST__  -> JSON index of every existing deck (title, path, keywords)

Re-run this whenever you add or rename decks:
    python scripts/build-deck-generator.py
"""
import json, re, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC  = os.path.join(ROOT, "lesson-deck-generator.src.html")
OUT  = os.path.join(ROOT, "lesson-deck-generator.html")

# Folders that contain real teaching decks (relative to repo root).
DECK_DIRS = ["python", "bootcamp", "minecraft", "webdev", "ai-coding"]
# Skip these — not lesson decks, or duplicates/backups.
SKIP_SUBSTR = ["_backup", ".bak", "/roadmap/", "all-slides", "glossary",
               "lesson-deck-generator", "/parent-vocab/", "/assets/"]
SKIP_NAMES = {"index.html"}

TAG = re.compile(r"<[^>]+>")

def text_of(html, pattern, limit=None):
    out = []
    for m in re.finditer(pattern, html, re.I | re.S):
        t = TAG.sub(" ", m.group(1))
        t = re.sub(r"\s+", " ", t).strip()
        if t:
            out.append(t)
        if limit and len(out) >= limit:
            break
    return out

def build_manifest():
    decks = []
    for d in DECK_DIRS:
        base = os.path.join(ROOT, d)
        if not os.path.isdir(base):
            continue
        for dirpath, _, files in os.walk(base):
            for fn in files:
                if not fn.endswith(".html"):
                    continue
                full = os.path.join(dirpath, fn)
                rel = os.path.relpath(full, ROOT).replace("\\", "/")
                low = "/" + rel.lower()
                if fn in SKIP_NAMES or any(s in low for s in SKIP_SUBSTR):
                    continue
                try:
                    html = open(full, encoding="utf-8").read()
                except Exception:
                    continue
                if 'class="slide' not in html:
                    continue  # not a deck
                title = (text_of(html, r"<title>(.*?)</title>", 1) or [fn])[0]
                headings = text_of(html, r"<h[1-3][^>]*>(.*?)</h[1-3]>")
                pills = text_of(html, r'<div class="pill[^"]*">(.*?)</div>')
                footer = (text_of(html, r'class="footer-tag">(.*?)</div>', 1) or [""])[0]
                track = footer or os.path.dirname(rel)
                # keyword blob: headings + pills + footer (topic-rich, compact)
                kw = " ".join(headings[:24] + pills[:12] + [footer])
                kw = re.sub(r"\s+", " ", kw)[:900]
                decks.append({"tt": title, "path": rel, "track": track, "kw": kw})
    decks.sort(key=lambda x: x["path"])
    return decks

def main():
    src = open(SRC, encoding="utf-8").read()
    css = open(os.path.join(ROOT, "assets/style.css"), encoding="utf-8").read()
    js  = open(os.path.join(ROOT, "assets/deck.js"), encoding="utf-8").read()

    for name, txt in (("style.css", css), ("deck.js", js)):
        if "</script" in txt.lower():
            sys.exit("ERROR: %s contains </script — cannot embed safely" % name)

    manifest = build_manifest()
    # escape < so a heading like "a<b" can't terminate the JSON <script> block
    manifest_json = json.dumps(manifest, ensure_ascii=False).replace("<", "\\u003c")

    for ph, val in (("__HOUSE_CSS__", css), ("__HOUSE_JS__", js), ("__DECK_MANIFEST__", manifest_json)):
        if src.count(ph) != 1:
            sys.exit("ERROR: placeholder %s appears %d times (need 1)" % (ph, src.count(ph)))
        src = src.replace(ph, val)

    open(OUT, "w", encoding="utf-8").write(src)
    print("Built %s" % os.path.basename(OUT))
    print("  decks indexed : %d" % len(manifest))
    print("  size          : %.1f KB" % (len(src.encode("utf-8")) / 1024))
    print("  sample decks  :")
    for d in manifest[:6]:
        print("    - %-52s %s" % (d["path"], d["tt"][:44]))

if __name__ == "__main__":
    main()
