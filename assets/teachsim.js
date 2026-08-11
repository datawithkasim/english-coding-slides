/* teachsim.js — reusable, slide-aware canvas teaching sims for English-Coding decks.
   A deck adds  <canvas class="tsim" data-sim="NAME"></canvas>  inside a .slide,
   plus <script src="…/assets/teachsim.js"></script> after deck.js.
   Only the canvas on the *active* slide animates (paused otherwise), so a deck can
   hold several sims cheaply. Colours match the dark theme in style.css. */
(function () {
  var dpr = Math.min(window.devicePixelRatio || 1, 2);
  var TAU = Math.PI * 2;
  var C = {
    bg: '#0b111a', panel: '#141b27', line: '#2a3444', ink: '#e8eef6', dim: '#93a1b5',
    cyan: '#38d0e0', violet: '#a78bfa', green: '#5ee6a0', red: '#ff6b6b',
    gold: '#ffcf5c', amber: '#f2c078', pink: '#ff8bd0'
  };
  var MONO = '600 15px "JetBrains Mono", "Fira Code", monospace';

  // ---- inject styles once ----
  var css = '' +
    '.tsim-wrap{display:flex;flex-direction:column;gap:.9rem;align-items:center;width:100%;margin:.4em 0}' +
    'canvas.tsim{width:min(860px,94%);aspect-ratio:16/9;display:block;background:#0b111a;' +
    'border:1px solid #2a3444;border-radius:12px;box-shadow:0 12px 34px rgba(0,0,0,.45)}' +
    '.tsim-ctl{display:flex;gap:1.3rem;align-items:center;flex-wrap:wrap;justify-content:center;' +
    'font-family:"JetBrains Mono",monospace;font-size:clamp(13px,1.5vw,18px);color:#93a1b5}' +
    '.tsim-ctl label{display:flex;gap:.5em;align-items:center;color:#e8eef6}' +
    '.tsim-ctl output{color:#38d0e0;min-width:2em;display:inline-block;text-align:right}' +
    '.tsim-ctl input[type=range]{accent-color:#38d0e0;width:clamp(120px,18vw,220px)}' +
    '.tsim-note{color:#93a1b5;font-family:"JetBrains Mono",monospace;font-size:clamp(12px,1.4vw,16px)}';
  var st = document.createElement('style'); st.textContent = css; document.head.appendChild(st);

  // ---- engine ----
  var current = null, raf = null, last = 0;
  function fit(cv) {
    var w = cv.clientWidth || 800, h = cv.clientHeight || 450;
    cv.width = Math.round(w * dpr); cv.height = Math.round(h * dpr);
    var ctx = cv.getContext('2d'); ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    return { ctx: ctx, w: w, h: h };
  }
  function frame(ts) {
    if (!current) { raf = null; return; }
    var dt = last ? Math.min((ts - last) / 16.667, 3) : 1;
    last = ts;
    current.api.step(dt);
    current.api.draw(current.ctx, current.w, current.h);
    raf = requestAnimationFrame(frame);
  }
  function stop() { if (raf) { cancelAnimationFrame(raf); raf = null; } current = null; last = 0; }
  function start(cv) {
    stop();
    var f = FAC[cv.getAttribute('data-sim')]; if (!f) return;
    var s = fit(cv);
    var api = f(cv, s.w, s.h); api.reset();
    current = { cv: cv, ctx: s.ctx, w: s.w, h: s.h, api: api };
    last = 0; raf = requestAnimationFrame(frame);
  }
  function activeCanvas() {
    var sl = document.querySelector('.slide.active');
    return sl ? sl.querySelector('canvas.tsim') : null;
  }
  function sync() {
    var cv = activeCanvas();
    if (cv) { if (!current || current.cv !== cv) start(cv); }
    else stop();
  }

  // ---- small draw helpers ----
  function roundRect(ctx, x, y, w, h, r) {
    ctx.beginPath();
    ctx.moveTo(x + r, y); ctx.arcTo(x + w, y, x + w, y + h, r);
    ctx.arcTo(x + w, y + h, x, y + h, r); ctx.arcTo(x, y + h, x, y, r);
    ctx.arcTo(x, y, x + w, y, r); ctx.closePath();
  }
  function txt(ctx, s, x, y, color, font, align) {
    ctx.fillStyle = color; ctx.font = font || MONO;
    ctx.textAlign = align || 'left'; ctx.textBaseline = 'middle';
    ctx.fillText(s, x, y);
  }

  // ==========================================================
  //  SIM: recursion call stack — factorial(n)
  //  Frames push while descending, base case hit, values return up.
  // ==========================================================
  function recursionSim(cv, W, H) {
    var n = 4, frames = [], t = 0, phase = 'descend', idx = 0, timer = 0, retVal = 1, done = 0;
    function getN() { var el = document.getElementById('tsimRecN'); return el ? parseInt(el.value, 10) : 4; }
    function reset() {
      n = getN(); frames = []; phase = 'descend'; idx = n; timer = 0; retVal = 1; done = 0;
    }
    function step(dt) {
      timer += dt;
      if (timer < 34) return; timer = 0;
      if (phase === 'descend') {
        if (idx >= 1) { frames.push({ k: idx, ret: null }); idx -= 1; }
        else { phase = 'base'; }
      } else if (phase === 'base') {
        retVal = 1; phase = 'ascend';
      } else if (phase === 'ascend') {
        var open = -1;
        for (var i = 0; i < frames.length; i++) if (frames[i].ret === null) open = i;
        if (open === -1) { phase = 'hold'; done = 0; return; }
        retVal = retVal * frames[open].k;
        frames[open].ret = retVal;
      } else if (phase === 'hold') {
        done += 34; // linger on the finished result then loop
        if (done > 520) reset();
      }
    }
    function draw(ctx, W, H) {
      ctx.fillStyle = C.bg; ctx.fillRect(0, 0, W, H);
      txt(ctx, 'def fact(k): return 1 if k <= 1 else k * fact(k - 1)', 18, 26, C.dim, '500 14px "JetBrains Mono",monospace');
      var fw = Math.min(W * 0.7, 520), fh = 34, gap = 8;
      var x = (W - fw) / 2, y0 = 58;
      for (var i = 0; i < frames.length; i++) {
        var fr = frames[i], y = y0 + i * (fh + gap);
        var returning = fr.ret !== null;
        ctx.fillStyle = returning ? 'rgba(94,230,160,.14)' : 'rgba(56,208,224,.12)';
        roundRect(ctx, x, y, fw, fh, 8); ctx.fill();
        ctx.strokeStyle = returning ? C.green : C.cyan; ctx.lineWidth = 1.5;
        roundRect(ctx, x, y, fw, fh, 8); ctx.stroke();
        txt(ctx, 'fact(' + fr.k + ')', x + 14, y + fh / 2, C.ink);
        if (returning) txt(ctx, '→ returns ' + fr.ret, x + fw - 14, y + fh / 2, C.green, MONO, 'right');
        else txt(ctx, 'waiting for fact(' + (fr.k - 1) + ')', x + fw - 14, y + fh / 2, C.dim, '500 13px "JetBrains Mono",monospace', 'right');
      }
      if (phase === 'base' || (phase === 'descend' && idx < 1)) {
        var by = y0 + frames.length * (fh + gap);
        txt(ctx, 'fact(1) = 1  ← base case, stop recursing', x + 14, by + 16, C.gold);
      }
      var label = phase === 'descend' ? 'CALLING DOWN — each call waits for the next'
        : phase === 'ascend' ? 'RETURNING UP — values multiply back'
          : phase === 'base' ? 'BASE CASE reached'
            : 'fact(' + n + ') = ' + retVal;
      txt(ctx, label, W / 2, H - 18, phase === 'hold' ? C.green : C.cyan, MONO, 'center');
    }
    return { reset: reset, step: step, draw: draw };
  }

  // ==========================================================
  //  SIM: coordinate movement — move the sprite (arrow keys / WASD),
  //  clamps to the window, shows live x,y. Pygame mental model.
  // ==========================================================
  function coordSim(cv, W, H) {
    var pad = 46, gw, gh, sx, sy, sz = 30, speed = 6, keys = {}, auto = 0, autodir = 1;
    function onKey(e, down) {
      var k = e.key.toLowerCase(); var m = { arrowleft: 'l', a: 'l', arrowright: 'r', d: 'r', arrowup: 'u', w: 'u', arrowdown: 'd', s: 'd' }[k];
      if (m) { keys[m] = down; if (down) { auto = 0; e.preventDefault(); } }
    }
    var kd = function (e) { onKey(e, true); }, ku = function (e) { onKey(e, false); };
    function reset() {
      gw = W - pad * 2; gh = H - pad * 2 - 30; sx = gw / 2 - sz / 2; sy = gh / 2 - sz / 2;
      keys = {}; auto = 1; autodir = 1;
      window.removeEventListener('keydown', kd); window.removeEventListener('keyup', ku);
      window.addEventListener('keydown', kd); window.addEventListener('keyup', ku);
    }
    function step(dt) {
      var moved = false;
      if (keys.l) { sx -= speed * dt; moved = true; }
      if (keys.r) { sx += speed * dt; moved = true; }
      if (keys.u) { sy -= speed * dt; moved = true; }
      if (keys.d) { sy += speed * dt; moved = true; }
      if (!moved && auto) { sx += speed * 0.6 * dt * autodir; if (sx <= 0 || sx >= gw - sz) autodir *= -1; }
      if (sx < 0) sx = 0; if (sx > gw - sz) sx = gw - sz;
      if (sy < 0) sy = 0; if (sy > gh - sz) sy = gh - sz;
    }
    function draw(ctx, W, H) {
      ctx.fillStyle = C.bg; ctx.fillRect(0, 0, W, H);
      var ox = pad, oy = pad;
      ctx.strokeStyle = C.line; ctx.lineWidth = 1;
      for (var gx = 0; gx <= gw; gx += 40) { ctx.beginPath(); ctx.moveTo(ox + gx, oy); ctx.lineTo(ox + gx, oy + gh); ctx.stroke(); }
      for (var gy = 0; gy <= gh; gy += 40) { ctx.beginPath(); ctx.moveTo(ox, oy + gy); ctx.lineTo(ox + gw, oy + gy); ctx.stroke(); }
      // axes
      txt(ctx, '(0,0)', ox + 2, oy - 12, C.dim, '500 13px "JetBrains Mono",monospace');
      txt(ctx, 'x →', ox + gw - 30, oy - 12, C.dim, '500 13px "JetBrains Mono",monospace');
      txt(ctx, 'y ↓', ox - 34, oy + 14, C.dim, '500 13px "JetBrains Mono",monospace');
      // sprite
      ctx.fillStyle = C.cyan; roundRect(ctx, ox + sx, oy + sy, sz, sz, 6); ctx.fill();
      // readout
      txt(ctx, 'player["x"] = ' + Math.round(sx) + '    player["y"] = ' + Math.round(sy),
        W / 2, H - 16, C.ink, '700 16px "JetBrains Mono",monospace', 'center');
    }
    return { reset: reset, step: step, draw: draw };
  }

  // ==========================================================
  //  SIM: AABB collision — drag box A onto box B; shows the four
  //  overlap comparisons and the combined verdict.
  // ==========================================================
  function collisionSim(cv, W, H) {
    var A, B, drag = false, off = { x: 0, y: 0 };
    function evPos(e) {
      var r = cv.getBoundingClientRect();
      return { x: (e.clientX - r.left) * (W / r.width), y: (e.clientY - r.top) * (H / r.height) };
    }
    function reset() {
      A = { x: W * 0.18, y: H * 0.45, w: 90, h: 70 };
      B = { x: W * 0.58, y: H * 0.3, w: 120, h: 90 };
      cv.style.cursor = 'grab';
      cv.onmousedown = function (e) {
        var p = evPos(e);
        if (p.x >= A.x && p.x <= A.x + A.w && p.y >= A.y && p.y <= A.y + A.h) { drag = true; off.x = p.x - A.x; off.y = p.y - A.y; cv.style.cursor = 'grabbing'; }
      };
      cv.onmousemove = function (e) { if (!drag) return; var p = evPos(e); A.x = p.x - off.x; A.y = p.y - off.y; };
      window.onmouseup = function () { drag = false; cv.style.cursor = 'grab'; };
    }
    function overlap() {
      return { c1: A.x < B.x + B.w, c2: A.x + A.w > B.x, c3: A.y < B.y + B.h, c4: A.y + A.h > B.y };
    }
    function step() { }
    function draw(ctx, W, H) {
      ctx.fillStyle = C.bg; ctx.fillRect(0, 0, W, H);
      var o = overlap(); var hit = o.c1 && o.c2 && o.c3 && o.c4;
      // B (target)
      ctx.fillStyle = 'rgba(139,92,246,.16)'; roundRect(ctx, B.x, B.y, B.w, B.h, 8); ctx.fill();
      ctx.strokeStyle = C.violet; ctx.lineWidth = 2; roundRect(ctx, B.x, B.y, B.w, B.h, 8); ctx.stroke();
      txt(ctx, 'B', B.x + B.w / 2, B.y + B.h / 2, C.violet, '700 18px "JetBrains Mono",monospace', 'center');
      // A (drag)
      ctx.fillStyle = hit ? 'rgba(94,230,160,.20)' : 'rgba(56,208,224,.16)';
      roundRect(ctx, A.x, A.y, A.w, A.h, 8); ctx.fill();
      ctx.strokeStyle = hit ? C.green : C.cyan; ctx.lineWidth = 2; roundRect(ctx, A.x, A.y, A.w, A.h, 8); ctx.stroke();
      txt(ctx, 'A', A.x + A.w / 2, A.y + A.h / 2, hit ? C.green : C.cyan, '700 18px "JetBrains Mono",monospace', 'center');
      // comparison panel
      var lines = [
        ['A.x < B.x + B.w', o.c1], ['A.x + A.w > B.x', o.c2],
        ['A.y < B.y + B.h', o.c3], ['A.y + A.h > B.y', o.c4]
      ];
      var px = 16, py = 14;
      for (var i = 0; i < lines.length; i++) {
        txt(ctx, (lines[i][1] ? '✓ ' : '✗ ') + lines[i][0], px, py + i * 20 + 8,
          lines[i][1] ? C.green : C.dim, '600 14px "JetBrains Mono",monospace');
      }
      txt(ctx, hit ? 'ALL true → COLLISION' : 'not all true → no hit',
        W / 2, H - 16, hit ? C.green : C.dim, '700 16px "JetBrains Mono",monospace', 'center');
      txt(ctx, 'drag A →', A.x + A.w / 2, A.y - 12, C.dim, '500 12px "JetBrains Mono",monospace', 'center');
    }
    return { reset: reset, step: step, draw: draw };
  }

  var FAC = { recursion: recursionSim, coord: coordSim, collision: collisionSim };

  // ---- range → output wiring (re-run each sim on control change via reset) ----
  document.addEventListener('input', function (e) {
    if (e.target && e.target.matches && e.target.matches('.tsim-ctl input[type=range]')) {
      var out = e.target.parentElement.querySelector('output');
      if (out) out.textContent = e.target.value;
      if (current) current.api.reset();
    }
  });

  // ---- boot: observe slide activation ----
  function init() {
    var obs = new MutationObserver(function (muts) {
      for (var i = 0; i < muts.length; i++) if (muts[i].attributeName === 'class') { sync(); return; }
    });
    document.querySelectorAll('.slide').forEach(function (s) { obs.observe(s, { attributes: true, attributeFilter: ['class'] }); });
    document.querySelectorAll('.tsim-ctl output').forEach(function (o) {
      var r = o.parentElement.querySelector('input[type=range]'); if (r) o.textContent = r.value;
    });
    window.addEventListener('resize', function () { if (current) start(current.cv); });
    sync();
  }
  if (document.readyState !== 'loading') init();
  else document.addEventListener('DOMContentLoaded', init);
})();
