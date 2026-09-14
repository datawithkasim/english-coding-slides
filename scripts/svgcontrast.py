"""Check (and optionally fix) SVG <text> colours in the lesson decks.

Decks run on the cream page background (--bg #faf6f0) but their inline SVGs are
hand-written, so dark-theme fills leak in. A fill is only judged - and only ever
rewritten - against the shape actually painted under it: the topmost rect,
circle or ellipse containing the anchor point, else the cream page.

  python scripts/svgcontrast.py "lessons/*/*.html" -v          list failures
  python scripts/svgcontrast.py "lessons/*/*.html" --fix        dry run
  python scripts/svgcontrast.py "lessons/*/*.html" --fix --apply write
"""
import io, sys, re, glob, colorsys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

BG = '#faf6f0'
TARGET = 4.5
HEX = re.compile(r'^#[0-9a-fA-F]{6}$')

MAP = {
    '#f1fa8c': '#1f2233', '#e8eef6': '#1f2233', '#f5f5f5': '#1f2233',
    '#f2f2f2': '#1f2233', '#8a97b8': '#4a5268', '#6b7790': '#4a5268',
    '#38d0e0': '#0b6b78', '#50fa7b': '#17693a', '#3cdc78': '#17693a',
    '#7bffa8': '#17693a', '#7ee0b0': '#17693a', '#ff5555': '#c2261c',
    '#ff5f56': '#c2261c', '#ff9a9a': '#c2261c', '#ff8fa3': '#c2261c',
    '#ff4646': '#c2261c', '#ffb86c': '#b45309', '#ff9c5b': '#b45309',
    '#bd93f9': '#764BCC', '#8b5cf6': '#764BCC', '#c4a8ff': '#764BCC',
    '#ff79c6': '#a8236e',
}

def rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def lum(h):
    def f(v):
        v /= 255
        return v/12.92 if v <= 0.03928 else ((v+0.055)/1.055) ** 2.4
    r, g, b = (f(x) for x in rgb(h))
    return 0.2126*r + 0.7152*g + 0.0722*b

def cr(a, b):
    la, lb = lum(a), lum(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi+0.05)/(lo+0.05)

def darken(h):
    """Walk lightness down, hue and saturation kept, until it clears TARGET."""
    r, g, b = (v/255 for v in rgb(h))
    hh, ll, ss = colorsys.rgb_to_hls(r, g, b)
    while ll > 0.02:
        ll -= 0.02
        out = '#%02x%02x%02x' % tuple(round(v*255) for v in colorsys.hls_to_rgb(hh, ll, ss))
        if cr(out, BG) >= TARGET:
            return out
    return '#1f2233'

def swap(h):
    out = MAP.get(h.lower()) or darken(h)
    return out if cr(out, BG) >= TARGET else darken(h)

def attr(n, s):
    m = re.search(r'\b%s="([^"]*)"' % n, s)
    return m.group(1) if m else None

def num(n, s):
    try: return float(attr(n, s))
    except (TypeError, ValueError): return None

TOKEN = re.compile(r'<g\b[^>]*>|</g>|<(rect|circle|ellipse|text)\b([^>]*?)/?>')
TRANSLATE = re.compile(r'translate\(\s*(-?[\d.]+)[ ,]+(-?[\d.]+)')
DARKSHAPE = re.compile(r'<(?:path|polygon|polyline) [^>]*?fill="(#[0-9a-fA-F]{6})"')

def walk(block):
    """Yield (kind, attrs, x, y, span) with group translates already applied."""
    stack = [(0.0, 0.0)]
    for m in TOKEN.finditer(block):
        tok = m.group(0)
        if tok.startswith('</g'):
            if len(stack) > 1: stack.pop()
            continue
        if tok.startswith('<g'):
            t = TRANSLATE.search(tok)
            dx, dy = (float(t.group(1)), float(t.group(2))) if t else (0.0, 0.0)
            stack.append((stack[-1][0] + dx, stack[-1][1] + dy))
            continue
        yield m.group(1), m.group(2), stack[-1], m

def analyse(block, edits, flags, base, off):
    # A gradient or a dark <path>/<polygon> backdrop cannot be resolved by the
    # rect/circle containment test, so the whole SVG is left alone.
    if 'fill="url(' in block:
        return len(re.findall(r'<text[ >]', block))
    if any(lum(f) < 0.25 for f in DARKSHAPE.findall(block)):
        return len(re.findall(r'<text[ >]', block))
    shapes = []
    for kind, a, (dx, dy), m in walk(block):
        fill = attr('fill', a)
        if not fill or not HEX.match(fill):
            continue
        if kind == 'text':
            x, y = num('x', a), num('y', a)
            if x is None or y is None: continue
            x, y = x + dx, y + dy
            bgc = BG
            for k, g, f in shapes:
                if k == 'rect':
                    rx, ry, w, h = g
                    hit = rx <= x <= rx+w and ry <= y <= ry+h
                else:
                    cx, cy, ex, ey = g
                    hit = ((x-cx)/ex)**2 + ((y-cy)/ey)**2 <= 1
                if hit: bgc = f
            ratio = cr(fill, bgc)
            if ratio >= TARGET:
                continue
            flags.append((base + block[:m.start()].count('\n'), fill,
                          'cream' if bgc == BG else bgc, round(ratio, 2)))
            if bgc == BG:
                fm = re.search(r'\bfill="([^"]*)"', a)
                s0 = off + m.start(2)
                edits.append((s0 + fm.start(1), s0 + fm.end(1), swap(fill)))
        else:
            if kind == 'rect':
                g = tuple(num(k, a) for k in ('x', 'y', 'width', 'height'))
            elif kind == 'circle':
                g = (num('cx', a), num('cy', a), num('r', a), num('r', a))
            else:
                g = (num('cx', a), num('cy', a), num('rx', a), num('ry', a))
            if any(v is None for v in g): continue
            g = (g[0]+dx, g[1]+dy, g[2], g[3])
            shapes.append(('rect' if kind == 'rect' else 'ell', g, fill))
    return 0

def run(path, apply):
    src = io.open(path, encoding='utf-8', newline='').read()
    edits, flags, skipped = [], [], 0
    for sv in re.finditer(r'<svg\b.*?</svg>', src, re.S):
        skipped += analyse(sv.group(0), edits, flags,
                           src[:sv.start()].count('\n') + 1, sv.start())
    if edits and apply:
        out, prev = [], 0
        for a, b, new in sorted(edits):
            out.append(src[prev:a]); out.append(new); prev = b
        out.append(src[prev:])
        io.open(path, 'w', encoding='utf-8', newline='').write(''.join(out))
    return edits, flags, skipped

fixmode = '--fix' in sys.argv
apply = '--apply' in sys.argv
verbose = '-v' in sys.argv
files = []
for p in sys.argv[1:]:
    if not p.startswith('-'): files += sorted(glob.glob(p))

tot = badtot = skiptot = 0
for p in files:
    edits, flags, sk = run(p, fixmode and apply)
    tot += len(edits); badtot += len(flags); skiptot += sk
    if flags or sk:
        print('%-70s %4d bad  %4d fixable  %4d unresolvable' % (p, len(flags), len(edits), sk))
        if verbose:
            for ln, fill, bg, ratio in flags:
                print('   L%-5d %s on %-9s %.2f:1' % (ln, fill, bg, ratio))
print('\n%s: %d bad, %d %s, %d texts in unresolvable SVGs, %d files' % (
    'APPLIED' if (fixmode and apply) else 'DRY RUN' if fixmode else 'CHECK',
    badtot, tot, 'rewritten' if apply else 'fixable', skiptot, len(files)))
