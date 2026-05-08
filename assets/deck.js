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

  // auto-init: any element with data-picker / data-dice / data-combine
  document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('[data-picker]').forEach(el => window.startPicker(el.id));
    document.querySelectorAll('[data-dice]').forEach(el => {
      const r = el.dataset.range || '1-6';
      const [a, b] = r.split('-').map(Number);
      window.startDice(el.id, a, b);
    });
    document.querySelectorAll('[data-combine]').forEach(el => window.startCombine(el.id));
  });
})();
