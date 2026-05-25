// English Coding — shared slide deck navigation + helpers

(function () {
  const slides = document.querySelectorAll('.slide');
  const counter = document.getElementById('counter');
  const prev = document.getElementById('prev');
  const next = document.getElementById('next');
  let i = 0;

  function show(n) {
    i = (n + slides.length) % slides.length;
    slides.forEach((s, idx) => s.classList.toggle('active', idx === i));
    if (counter) counter.textContent = `${i + 1} / ${slides.length}`;
  }
  if (next) next.onclick = () => show(i + 1);
  if (prev) prev.onclick = () => show(i - 1);
  document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') { e.preventDefault(); show(i + 1); }
    if (e.key === 'ArrowLeft' || e.key === 'PageUp') { e.preventDefault(); show(i - 1); }
    if (e.key === 'Home') show(0);
    if (e.key === 'End') show(slides.length - 1);
  });

  // === reusable random.choice picker animation ===
  window.startPicker = function (rootId) {
    const root = document.getElementById(rootId);
    if (!root) return;
    const items = root.querySelectorAll('.pkitem');
    const result = root.querySelector('.pkresult .val');
    let spinTimer = null;

    function clearAll() {
      items.forEach(it => { it.classList.remove('spin'); it.classList.remove('win'); });
    }

    function runCycle() {
      clearAll();
      if (result) result.textContent = '';
      let j = 0;
      spinTimer = setInterval(() => {
        items.forEach(it => it.classList.remove('spin'));
        items[j % items.length].classList.add('spin');
        j++;
      }, 110);
      setTimeout(() => {
        clearInterval(spinTimer);
        items.forEach(it => it.classList.remove('spin'));
        const winner = items[Math.floor(Math.random() * items.length)];
        winner.classList.add('win');
        if (result) result.textContent = '"' + winner.dataset.v + '"';
        setTimeout(runCycle, 2200);
      }, 1600);
    }
    runCycle();
  };

  // === reusable dice animation ===
  window.startDice = function (rootId, min, max) {
    const root = document.getElementById(rootId);
    if (!root) return;
    const face = root.querySelector('.face');
    const val = root.querySelector('.dlabel .val');
    let rollTimer = null;
    min = min || 1; max = max || 6;

    function rand() { return min + Math.floor(Math.random() * (max - min + 1)); }

    function runRoll() {
      face.classList.remove('landed');
      face.classList.add('rolling');
      if (val) val.textContent = '?';
      rollTimer = setInterval(() => { face.textContent = rand(); }, 90);
      setTimeout(() => {
        clearInterval(rollTimer);
        const result = rand();
        face.textContent = result;
        face.classList.remove('rolling');
        face.classList.add('landed');
        if (val) val.textContent = result;
        setTimeout(runRoll, 2000);
      }, 1500);
    }
    runRoll();
  };

  // === multi-pick combine viz ===
  window.startCombine = function (rootId) {
    const root = document.getElementById(rootId);
    if (!root) return;
    const items = root.querySelectorAll('.mitem');
    const lines = root.querySelectorAll('.mlog .ln');
    const slots = Array.from(lines).map(ln => ln.querySelector('.rval'));

    function reset() {
      items.forEach(it => it.classList.remove('win'));
      lines.forEach(ln => ln.classList.remove('show'));
      slots.forEach(s => { if (s) s.textContent = ''; });
    }

    function pickOnce(slotIdx, doneCb) {
      let j = 0;
      const spinT = setInterval(() => {
        items.forEach(it => it.classList.remove('win'));
        items[j % items.length].classList.add('win');
        j++;
      }, 90);
      setTimeout(() => {
        clearInterval(spinT);
        items.forEach(it => it.classList.remove('win'));
        const winner = items[Math.floor(Math.random() * items.length)];
        winner.classList.add('win');
        if (slots[slotIdx]) slots[slotIdx].textContent = '"' + winner.dataset.v + '"';
        if (lines[slotIdx]) lines[slotIdx].classList.add('show');
        setTimeout(() => {
          items.forEach(it => it.classList.remove('win'));
          doneCb();
        }, 700);
      }, 900);
    }

    function runCycle() {
      reset();
      pickOnce(0, () => pickOnce(1, () => pickOnce(2, () => setTimeout(runCycle, 1800))));
    }
    runCycle();
  };

  // === MCQ Quiz support ===
  // Each .mcq slide has data-correct="N" + .opt buttons.
  // Score tracked per-deck in window.__quizState.
  window.__quizState = window.__quizState || { score: 0, answered: 0, total: 0 };

  // Fisher-Yates in-place shuffle.
  function shuffle(arr) {
    for (let i = arr.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [arr[i], arr[j]] = [arr[j], arr[i]];
    }
    return arr;
  }

  // Shuffle .opt children inside a single .mcq slide and remap data-correct
  // to the new index of what was previously the correct option. All decks
  // ship with the correct option at index 0; without shuffling, students
  // learn "always pick the first" instead of the concept.
  function shuffleMcq(m) {
    const correct = parseInt(m.dataset.correct, 10);
    if (Number.isNaN(correct)) return;
    const container = m.querySelector('.opts') || (m.querySelector('.opt') && m.querySelector('.opt').parentElement);
    if (!container) return;
    const opts = Array.from(container.querySelectorAll('.opt'));
    if (opts.length < 2) return;
    const correctEl = opts[correct];
    if (!correctEl) return;
    const order = shuffle(opts.map((_, i) => i));
    order.forEach(idx => container.appendChild(opts[idx]));
    m.dataset.correct = String(order.indexOf(correct));
  }

  function initQuiz() {
    const mcqs = document.querySelectorAll('.mcq');
    window.__quizState.total = mcqs.length;
    mcqs.forEach(m => {
      shuffleMcq(m);
      const correct = parseInt(m.dataset.correct, 10);
      const opts = m.querySelectorAll('.opt');
      const feedback = m.querySelector('.qfeedback');
      opts.forEach((opt, idx) => {
        opt.addEventListener('click', () => {
          if (m.dataset.done === '1') return;
          m.dataset.done = '1';
          opts.forEach(o => o.classList.add('disabled'));
          if (idx === correct) {
            opt.classList.add('right');
            window.__quizState.score++;
            if (feedback) {
              feedback.classList.add('show', 'good');
              feedback.innerHTML = '✓ Correct! ' + (m.dataset.explain || '');
            }
          } else {
            opt.classList.add('wrong');
            opts[correct].classList.add('right');
            if (feedback) {
              feedback.classList.add('show', 'bad');
              feedback.innerHTML = '✗ Not quite. ' + (m.dataset.explain || '');
            }
          }
          window.__quizState.answered++;
        });
      });
    });

    // Score slide: refresh on view
    const scoreSlide = document.querySelector('.mcq-score');
    if (scoreSlide) {
      const update = () => {
        const s = window.__quizState;
        const val = scoreSlide.querySelector('.score-val');
        const msg = scoreSlide.querySelector('.score-msg');
        if (val) val.textContent = `${s.score} / ${s.total}`;
        if (msg) {
          const pct = s.total ? Math.round(s.score / s.total * 100) : 0;
          if (pct >= 80)      msg.textContent = '🔥 Mastered it!';
          else if (pct >= 50) msg.textContent = '👍 Good effort. Review the misses.';
          else                msg.textContent = "📖 Re-read the slides. You'll get it.";
        }
      };
      // Update whenever the score slide becomes visible
      const obs = new MutationObserver(() => {
        if (scoreSlide.classList.contains('active')) update();
      });
      obs.observe(scoreSlide, { attributes: true, attributeFilter: ['class'] });
      update();
    }

    // Reset button (any)
    document.querySelectorAll('.quiz-reset').forEach(b => {
      b.addEventListener('click', () => {
        window.__quizState = { score: 0, answered: 0, total: mcqs.length };
        mcqs.forEach(m => {
          delete m.dataset.done;
          m.querySelectorAll('.opt').forEach(o => o.classList.remove('disabled','right','wrong'));
          const fb = m.querySelector('.qfeedback');
          if (fb) { fb.classList.remove('show','good','bad'); fb.innerHTML = ''; }
        });
        if (scoreSlide) {
          const val = scoreSlide.querySelector('.score-val');
          if (val) val.textContent = `0 / ${mcqs.length}`;
        }
      });
    });
  }

  // auto-init: any element with data-picker / data-dice / data-combine
  document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('[data-picker]').forEach(el => window.startPicker(el.id));
    document.querySelectorAll('[data-dice]').forEach(el => {
      const r = el.dataset.range || '1-6';
      const [a, b] = r.split('-').map(Number);
      window.startDice(el.id, a, b);
    });
    document.querySelectorAll('[data-combine]').forEach(el => window.startCombine(el.id));
    initQuiz();
  });
})();
