/* The one script of the reading site. Without it every page still reads (the Lean text, the steps, the links); the
   script adds the formulas (KaTeX), wrapping and copying of Lean text, the keyboard tree of a structured proof, and the
   reading mode: the note's pages drawn by PDF.js, its statements chosen on the pages, their proofs and Lean text beside. */
(function () {
  'use strict';
  const doc = document;
  doc.documentElement.classList.add('js');
  const $ = (s, el) => (el || doc).querySelector(s);
  const $$ = (s, el) => Array.from((el || doc).querySelectorAll(s));
  const store = {
    get(k) { try { return window.localStorage.getItem(k); } catch (e) { return null; } },
    set(k, v) { try { window.localStorage.setItem(k, v); } catch (e) { /* a private window keeps nothing */ } }
  };
  const calm = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const narrow = () => window.matchMedia('(max-width: 62rem)').matches;
  const typing = (e) => { const t = e.target; return !!t && (t.isContentEditable || /^(INPUT|TEXTAREA|SELECT)$/.test(t.tagName)); };
  const ASSETS = (doc.currentScript && doc.currentScript.src) ? doc.currentScript.src.replace(/[^/]*$/, '') : new URL('assets/', doc.baseURI).href;
  function within(pane, el, part, atOnce) {               // move a pane, and only the pane, until el stands at `part` of its height
    if (!pane || !el) { return; }
    const top = pane.scrollTop + el.getBoundingClientRect().top - pane.getBoundingClientRect().top - pane.clientHeight * part;
    pane.scrollTo({ top: Math.max(0, top), behavior: calm || atOnce ? 'auto' : 'smooth' });
  }
  function seen(el, pane) {                               // is el wholly inside the visible part of its pane (or of the window)?
    const r = el.getBoundingClientRect(), p = pane ? pane.getBoundingClientRect() : { top: 0, bottom: window.innerHeight };
    return r.top >= p.top && r.bottom <= p.bottom;
  }

  // ---------------------------------------------------------------- formulas
  const K = window.katex;
  function glue(m) {                                      // a formula stays on one line with what touches it: (x), x;, x-adic
    const parent = m.parentNode;
    if (!parent || m.classList.contains('d') || (parent.classList && parent.classList.contains('nw'))) { return; }
    const before = [], after = [];
    const p = m.previousSibling, n = m.nextSibling;
    if (p && p.nodeType === 3) { const r = /\S+$/.exec(p.data); if (r) { before.push(p.splitText(p.data.length - r[0].length)); } }
    else if (p && p.nodeType === 1 && p.tagName === 'CODE') { before.push(p); }
    if (n && n.nodeType === 3) { const r = /^\S+/.exec(n.data); if (r) { if (r[0].length < n.data.length) { n.splitText(r[0].length); } after.push(n); } }
    else if (n && n.nodeType === 1 && n.tagName === 'CODE') { after.push(n); }
    if (!before.length && !after.length) { return; }
    const w = doc.createElement('span');
    w.className = 'nw';
    parent.insertBefore(w, before[0] || m);
    before.forEach((x) => w.appendChild(x)); w.appendChild(m); after.forEach((x) => w.appendChild(x));
  }
  function renderMath(el) {
    if (!K || !el) { return; }
    $$('.m:not([data-k])', el).forEach((m) => {
      const tex = m.textContent;
      m.setAttribute('data-k', '');
      try { K.render(tex, m, { displayMode: m.classList.contains('d'), throwOnError: false, strict: 'ignore', output: 'htmlAndMathml' }); glue(m); }
      catch (e) { m.textContent = tex; m.classList.add('m-err'); }
    });
  }
  const mathIO = ('IntersectionObserver' in window) ? new IntersectionObserver((es) => {
    es.forEach((e) => { if (e.isIntersecting) { mathIO.unobserve(e.target); renderMath(e.target); } });
  }, { rootMargin: '700px 0px' }) : null;
  function mathSoon(el) {                                 // now when there is little of it, else as it comes near the view
    const blocks = $$('.tex', el).filter((b) => b.querySelector('.m'));
    if (!mathIO || blocks.length < 60) { renderMath(el); } else { blocks.forEach((b) => mathIO.observe(b)); }
  }

  // ---------------------------------------------------------------- Lean text: wrapping and copying
  let wrapOn = store.get('readback-wrap') === '1';
  function applyWrap(el) {
    $$('pre.lean', el).forEach((p) => {
      if (wrapOn && !p.hasAttribute('data-ind')) {         // the hanging indent of a wrapped line follows its own indent
        $$('code > span', p).forEach((l) => { const n = /^ */.exec(l.textContent)[0].length; if (n) { l.style.setProperty('--ind', n); } });
        p.setAttribute('data-ind', '');
      }
      p.classList.toggle('wrap', wrapOn);
    });
    $$('[data-wrap]', el).forEach((b) => b.setAttribute('aria-pressed', wrapOn ? 'true' : 'false'));
  }
  function copy(button) {
    const pre = button.closest('figure').querySelector('pre');
    const text = $$('code > span', pre).map((l) => l.textContent).join('\n') + '\n';
    const say = (ok) => { const old = button.textContent; button.textContent = ok ? 'Copied' : 'Could not copy'; setTimeout(() => { button.textContent = old; }, 1400); };
    const byHand = () => {
      const t = doc.createElement('textarea'); let ok = false;
      t.value = text; t.setAttribute('readonly', ''); t.style.position = 'fixed'; t.style.opacity = '0';
      doc.body.appendChild(t); t.select();
      try { ok = doc.execCommand('copy'); } catch (e) { ok = false; }
      t.remove(); say(ok);
    };
    if (navigator.clipboard && navigator.clipboard.writeText) { navigator.clipboard.writeText(text).then(() => say(true), byHand); } else { byHand(); }
  }
  function boxButtons(el) {                               // Wrap and Copy on every Lean box (made here, not sent with each box)
    $$('figure.code > figcaption', el).forEach((f) => {
      if (f.querySelector('.acts')) { return; }
      const cap = doc.createElement('span'); cap.className = 'cap';
      while (f.firstChild) { cap.appendChild(f.firstChild); }
      const acts = doc.createElement('span'); acts.className = 'acts';
      acts.innerHTML = '<button type="button" data-wrap aria-pressed="' + wrapOn + '" title="Wrap long lines">Wrap</button><button type="button" data-copy title="Copy the Lean text">Copy</button>';
      f.appendChild(cap); f.appendChild(acts);
    });
  }
  doc.addEventListener('click', (e) => {
    const w = e.target.closest('[data-wrap]'), c = e.target.closest('[data-copy]');
    if (w) { wrapOn = w.getAttribute('aria-pressed') !== 'true'; store.set('readback-wrap', wrapOn ? '1' : '0'); applyWrap(doc); }
    if (c) { copy(c); }
  });

  // lines of a Lean box: mark ranges [[a, b, cls]], return the first marked line
  function markLines(box, ranges) {
    if (!box) { return null; }
    const code = $('code', box), start = +box.getAttribute('data-a');
    $$(':scope > .hl, :scope > .hh', code).forEach((l) => l.classList.remove('hl', 'hh'));
    let first = null;
    ranges.forEach(([a, b, cls]) => {
      for (let n = a; n <= b; n++) { const l = code.children[n - start]; if (l) { l.classList.add(cls); first = first || l; } }
    });
    return first;
  }
  function excerpt(box, a, b) {                            // a copy of lines a..b of a Lean box, for beside a step
    const start = +box.getAttribute('data-a'), code = $('code', box);
    const fig = doc.createElement('figure'), pre = doc.createElement('pre'), c = doc.createElement('code');
    fig.className = 'code excerpt'; pre.className = 'lean'; pre.tabIndex = 0;
    pre.setAttribute('aria-label', 'Its Lean ' + (b > a ? 'lines ' + a + '–' + b : 'line ' + a));
    c.style.counterReset = 'ln ' + (a - 1);
    for (let n = a; n <= b; n++) {
      const l = code.children[n - start];
      if (l) { const k = l.cloneNode(true); k.removeAttribute('id'); k.classList.remove('hl', 'hh', 's'); c.appendChild(k); }
    }
    pre.appendChild(c); fig.appendChild(pre);
    applyWrap(fig);
    return fig;
  }
  const range = (s) => { const m = /^(\d+)-(\d+)$/.exec(s || ''); return m ? [+m[1], +m[2]] : null; };

  // ---------------------------------------------------------------- the tree of a structured proof
  function Tree(ol, opt) {
    const items = $$('li[role="treeitem"]', ol);
    if (!items.length) { return null; }
    const parentOf = (li) => { const p = li.parentElement.closest('li[role="treeitem"]'); return p && ol.contains(p) ? p : null; };
    const kidsOf = (li) => { const g = $(':scope > ol[role="group"]', li); return g ? Array.from(g.children) : []; };
    const shown = (li) => { for (let p = parentOf(li); p; p = parentOf(p)) { if (p.getAttribute('aria-expanded') === 'false') { return false; } } return true; };
    let current = null;
    items.forEach((li) => { li.tabIndex = -1; });
    items[0].tabIndex = 0;
    function focus(li) {
      items.forEach((x) => { x.tabIndex = -1; });
      li.tabIndex = 0;
      li.focus({ preventScroll: true });
      const node = $(':scope > .node', li);
      if (!seen(node, opt.pane && opt.pane())) { node.scrollIntoView({ block: 'nearest', behavior: calm ? 'auto' : 'smooth' }); }
    }
    function toggle(li, open) {
      if (!li.hasAttribute('aria-expanded')) { return; }
      li.setAttribute('aria-expanded', open === undefined ? (li.getAttribute('aria-expanded') !== 'true' ? 'true' : 'false') : (open ? 'true' : 'false'));
    }
    function select(li, how) {
      if (!li) { return; }
      for (let p = parentOf(li); p; p = parentOf(p)) { toggle(p, true); }
      items.forEach((x) => x.removeAttribute('aria-selected'));
      li.setAttribute('aria-selected', 'true');
      current = li;
      const lines = range(li.getAttribute('data-lines')), head = range(li.getAttribute('data-head'));
      const box = opt.box && opt.box();
      const first = lines && markLines(box, [[lines[0], lines[1], 'hl']].concat(head ? [[head[0], head[1], 'hh']] : []));
      $$('.excerpt', ol).forEach((x) => x.remove());
      if (box && lines && opt.inline && opt.inline()) { $(':scope > .node > .sb', li).appendChild(excerpt(box, lines[0], lines[1])); }
      else if (first && box) { within($('pre', box), first, 0.18, how === 'load'); }
      if (how !== 'quiet') { focus(li); }
      if (opt.onSelect) { opt.onSelect(li, how); }
    }
    const visibleItems = () => items.filter(shown);
    ol.addEventListener('click', (e) => {
      const li = e.target.closest('li[role="treeitem"]');
      if (!li || !ol.contains(li)) { return; }
      const step = e.target.closest('a[data-step]');
      if (step) {
        e.preventDefault();
        const t = items.find((x) => (x.id || x.getAttribute('data-id')) === step.getAttribute('href').slice(1));
        if (t) { select(t, 'click'); }
        return;
      }
      if (e.target.closest('.tw')) { toggle(li); if (!shown(current || li)) { select(li, 'click'); } return; }
      if (e.target.closest('a.ll')) { e.preventDefault(); select(li, 'click'); return; }
      if (e.target.closest('a, button, summary, pre, code.select')) { return; }
      if (window.getSelection && String(window.getSelection()).trim()) { return; }   // a selection of text, not a choice
      if (e.target.closest('.node')) { select(li, 'click'); }
    });
    ol.addEventListener('keydown', (e) => {
      const li = e.target.closest('li[role="treeitem"]');
      if (!li || e.target !== li || e.altKey || e.ctrlKey || e.metaKey) { return; }
      const vis = visibleItems(), i = vis.indexOf(li);
      let to = null;
      switch (e.key) {
        case 'ArrowDown': case 'j': to = vis[i + 1]; break;
        case 'ArrowUp': case 'k': to = vis[i - 1]; break;
        case 'Home': to = vis[0]; break;
        case 'End': to = vis[vis.length - 1]; break;
        case 'ArrowRight': case 'l':
          if (li.getAttribute('aria-expanded') === 'false') { toggle(li, true); } else if (kidsOf(li).length) { to = kidsOf(li)[0]; }
          break;
        case 'ArrowLeft': case 'h':
          if (li.getAttribute('aria-expanded') === 'true') { toggle(li, false); } else { to = parentOf(li); }
          break;
        case 'Enter': case ' ': select(li, 'key'); break;
        case '*': (parentOf(li) ? kidsOf(parentOf(li)) : Array.from(ol.children)).forEach((x) => toggle(x, true)); break;
        default: return;
      }
      e.preventDefault();
      if (to) { select(to, 'key'); }
    });
    return {
      items: items,
      select: select,
      current: () => current,
      all: (open) => { items.forEach((x) => toggle(x, open)); if (!open && current && !shown(current)) { let p = current; while (parentOf(p)) { p = parentOf(p); } select(p, 'quiet'); } },
      find: (id) => items.find((x) => (x.id || x.getAttribute('data-id')) === id)
    };
  }
  function treeButtons(bar, T) {
    if (!bar || !T) { return; }
    bar.addEventListener('click', (e) => { const b = e.target.closest('[data-all]'); if (b) { T.all(b.getAttribute('data-all') === 'open'); } });
  }

  // ---------------------------------------------------------------- proof mode
  const pm = $('.proofmode');
  if (pm) {
    const box = $('.leanpane figure.code', pm);
    const T = Tree($('ol.tree', pm), {
      box: () => box, inline: narrow,
      onSelect: (li, how) => { if (how !== 'load' && li.id) { history.replaceState(null, '', '#' + li.id); } }
    });
    treeButtons($('.treebar', pm), T);
    const h = decodeURIComponent(location.hash.slice(1));
    if (T && h.indexOf('s-') === 0 && T.find(h)) {
      const li = T.find(h);
      T.select(li, 'load');
      $(':scope > .node', li).scrollIntoView({ block: 'center' });
    }
  }

  // ---------------------------------------------------------------- lists: find by name
  $$('[data-filter]').forEach((inp) => {
    const list = inp.closest('section').querySelector('ul.decls');
    inp.addEventListener('input', () => {
      const q = inp.value.trim().toLowerCase();
      $$(':scope > li', list).forEach((li) => { li.hidden = !!q && (li.getAttribute('data-name') || '').indexOf(q) < 0; });
    });
  });
  $$('[data-filter-rows]').forEach((inp) => {
    inp.addEventListener('input', () => {
      const q = inp.value.trim().toLowerCase();
      $$('main tbody tr').forEach((tr) => { tr.hidden = !!q && tr.textContent.toLowerCase().indexOf(q) < 0; });
      if (q) { $$('main details').forEach((d) => { d.open = true; }); }
    });
  });
  const lib = $('#library details');
  if (lib && location.hash === '#library') { lib.open = true; }
  window.addEventListener('hashchange', () => { if (lib && location.hash === '#library') { lib.open = true; } });

  // ---------------------------------------------------------------- reading mode
  const RD = $('.reading');
  if (RD) { reader(RD); }

  function reader(RD) {
    const data = JSON.parse($('#note-data').textContent);
    const side = $('.side', RD), body = $('.side-body', side), sel = $('.sel', side), chips = $('.dchips', side);
    const list = $('#stmts', side), cur = $('.picker .cur', side);
    const arts = {};
    $$('article.decl', side).forEach((a) => { arts[a.getAttribute('data-key')] = a; });
    const by = {};
    data.items.forEach((x) => { by[x.at] = x; });
    data.lean.forEach((x) => { by[x.at] = x; });
    const order = data.items.map((x) => x.at);
    const keyOfPlace = {};
    Object.keys(data.decls).forEach((k) => { const d = data.decls[k]; keyOfPlace[d.file + '#' + d.a + '-' + d.b] = k; });
    let now = null, key = null;
    const pdfName = 'readback-pos-' + data.note;

    const label = (x) => x.title || ('LEAN line, page ' + x.page);
    const keysOf = (x) => (x.keys || []).filter((k) => arts[k]);
    function choose(at, k, how) {
      const x = by[at];
      if (!x) { return false; }
      now = at;
      const keys = keysOf(x);
      key = k && keys.indexOf(k) >= 0 ? k : (keys[0] || null);
      sel.textContent = '';
      const h = doc.createElement('h2'); h.textContent = label(x);
      const m = doc.createElement('p'); m.className = 'meta';
      m.textContent = 'Page ' + x.page + ' · ' + (keys.length === 1 ? '1 declaration' : keys.length + ' declarations') + (x.at.indexOf('l-') === 0 ? ' named on this LEAN line' : '');
      sel.appendChild(h); sel.appendChild(m);
      chips.textContent = '';
      chips.hidden = keys.length < 2;
      keys.forEach((kk) => {
        const d = data.decls[kk], b = doc.createElement('button'), a = arts[kk];
        b.type = 'button'; b.setAttribute('data-key', kk);
        const kind = a ? ($('.kind', a) || {}).textContent : '';
        b.innerHTML = '<span class="k"></span><span class="n"></span>';
        b.firstChild.textContent = kind || ''; b.lastChild.textContent = (d && d.name ? d.name.split('.').pop() : kk);
        b.title = d && d.name ? d.name : kk;
        chips.appendChild(b);
      });
      if (!keys.length) { const p = doc.createElement('p'); p.className = 'hint'; p.textContent = 'The note names no declaration of the concordance here.'; sel.appendChild(p); }
      showKey(key);
      $$('a', list).forEach((a) => a.classList.toggle('on', a.getAttribute('data-at') === at));
      const pos = order.indexOf(at);
      cur.querySelector('b').textContent = label(x);
      cur.querySelector('small').textContent = pos >= 0 ? 'p. ' + x.page + ' · ' + (pos + 1) + ' of ' + order.length : 'p. ' + x.page;
      V.mark(at, x, key);
      if (how !== 'page' && how !== 'start') { V.show(x, how === 'load'); }
      history.replaceState(null, '', '#at=' + encodeURIComponent(at) + (key ? '&k=' + encodeURIComponent(key) : ''));
      body.scrollTop = 0;
      if (how === 'page' && narrow()) { side.scrollIntoView({ block: 'start', behavior: calm ? 'auto' : 'smooth' }); }
      return true;
    }
    function showKey(k) {
      key = k;
      Object.keys(arts).forEach((kk) => { arts[kk].hidden = kk !== k; });
      $$('button', chips).forEach((b) => b.setAttribute('aria-pressed', b.getAttribute('data-key') === k ? 'true' : 'false'));
      const a = arts[k];
      if (!a) { return; }
      tabs(a);
      const want = store.get('readback-tab') || 'proof';
      tab(a, want === 'proof' && a.hasAttribute('data-proof') ? 'proof' : 'lean', false);
      renderMath(a);
      const says = $(':scope > .says', a);                // a long reading is folded, so that the tabs stay in view
      if (says && !says.hasAttribute('data-fold') && says.scrollHeight > 300) {
        says.setAttribute('data-fold', '');
        says.classList.add('clamped');
        const more = doc.createElement('button');
        more.type = 'button'; more.className = 'more'; more.textContent = 'The whole reading';
        more.setAttribute('aria-expanded', 'false');
        more.addEventListener('click', () => {
          const open = says.classList.toggle('clamped') === false;
          more.textContent = open ? 'Fold the reading' : 'The whole reading';
          more.setAttribute('aria-expanded', open ? 'true' : 'false');
        });
        says.after(more);
      }
      if (now) { history.replaceState(null, '', '#at=' + encodeURIComponent(now) + '&k=' + encodeURIComponent(k)); }
    }
    const WHY = {
      def: () => 'A definition has no proof to structure; its Lean text is under <b>Lean</b>.',
      lib: (u) => 'This declaration belongs to unit ' + u + ' of the background library, which has not been read.',
      none: (u) => 'The reading of unit ' + u + ' has no structured proof of this declaration; its Lean text is under <b>Lean</b>.',
      nounit: () => 'This declaration belongs to no unit of the ledger.'
    };
    function tabs(a) {                                     // the two tabs of a declaration, made when it is first shown
      if (a.querySelector('.tabs')) { return; }
      const proof = a.getAttribute('data-proof'), n = +a.getAttribute('data-b') - +a.getAttribute('data-a') + 1;
      const bar = doc.createElement('div');
      bar.className = 'tabs'; bar.setAttribute('role', 'tablist'); bar.setAttribute('aria-label', 'Its proof and its Lean text');
      bar.innerHTML = '<button type="button" role="tab" data-tab="proof"' + (proof ? '' : ' data-none') + '>Structured proof' + (proof ? ' <small>' + a.getAttribute('data-steps') + ' steps</small>' : '') + '</button>'
        + '<button type="button" role="tab" data-tab="lean">Lean <small>' + n + (n === 1 ? ' line' : ' lines') + '</small></button>'
        + (proof ? '<a class="open" href="' + proof + '" title="The structured proof beside its whole declaration, on a page of its own">Proof mode →</a>' : '');
      const pp = doc.createElement('div'), lp = doc.createElement('div');
      [pp, lp].forEach((p, i) => { p.className = 'panel'; p.setAttribute('role', 'tabpanel'); p.setAttribute('data-panel', i ? 'lean' : 'proof'); p.hidden = true; });
      pp.innerHTML = proof ? '<p class="dim">Reading the structured proof…</p>' : '<p class="dim">' + (WHY[a.getAttribute('data-why')] || WHY.nounit)(a.getAttribute('data-unit') || '') + '</p>';
      const l0 = a.querySelector('.lean0');
      while (l0 && l0.firstChild) { lp.appendChild(l0.firstChild); }
      if (l0) { l0.remove(); }
      a.appendChild(bar); a.appendChild(pp); a.appendChild(lp);
    }
    function tab(a, which, remember) {
      $$('[role="tab"]', a).forEach((t) => t.setAttribute('aria-selected', t.getAttribute('data-tab') === which ? 'true' : 'false'));
      $$('[role="tabpanel"]', a).forEach((p) => { p.hidden = p.getAttribute('data-panel') !== which; });
      if (remember) { store.set('readback-tab', which); }
      if (which === 'proof') { loadProof(a); } else { loadWhole(a); }
      applyWrap($('[data-panel="' + which + '"]', a));
    }
    const docs = {};
    function page(href) {                                  // another page of the site, read once
      href = href.split('#')[0];
      return (docs[href] = docs[href] || fetch(href).then((r) => { if (!r.ok) { throw new Error(String(r.status)); } return r.text(); })
        .then((txt) => new DOMParser().parseFromString(txt, 'text/html')));
    }
    function wholeFrom(d, a) {                             // the declaration's lines, taken from a page that has them with their addresses
      const lo = +a.getAttribute('data-a'), hi = +a.getAttribute('data-b'), sa = +a.getAttribute('data-sa'), sb = +a.getAttribute('data-sb');
      const fig = doc.createElement('figure'), cap = doc.createElement('figcaption'), pre = doc.createElement('pre'), code = doc.createElement('code');
      fig.className = 'code'; fig.setAttribute('data-a', lo); fig.setAttribute('data-b', hi);
      cap.textContent = a.getAttribute('data-file') + ' · ' + (hi > lo ? 'lines ' + lo + '–' + hi : 'line ' + lo) + ' · the statement marked in the margin';
      pre.className = 'lean'; pre.tabIndex = 0; code.style.counterReset = 'ln ' + (lo - 1);
      for (let n = lo; n <= hi; n++) {
        const l = d.getElementById('L' + n);
        if (!l) { return null; }
        const k = doc.importNode(l, true);
        k.removeAttribute('id'); k.className = n >= sa && n <= sb ? 's' : '';
        code.appendChild(k);
      }
      pre.appendChild(code); fig.appendChild(cap); fig.appendChild(pre);
      return fig;
    }
    function putWhole(a, fig) {
      const lp = $('[data-panel="lean"]', a);
      if (!fig || !lp || a.hasAttribute('data-full')) { return; }
      a.setAttribute('data-full', '');
      lp.textContent = '';
      lp.appendChild(fig);
      boxButtons(lp); applyWrap(lp);
      const T = a._tree, li = T && T.current();
      if (li) { T.select(li, 'quiet'); }
    }
    function loadWhole(a) {
      if (a.hasAttribute('data-whole') || a.hasAttribute('data-full') || a.hasAttribute('data-asked')) { return; }
      a.setAttribute('data-asked', '');
      page(a.getAttribute('data-proof') || a.getAttribute('data-src')).then((d) => putWhole(a, wholeFrom(d, a))).catch(() => {
        const lp = $('[data-panel="lean"]', a), p = doc.createElement('p');
        p.className = 'dim';
        p.innerHTML = 'Above is the statement. The whole declaration could not be read here (a page opened as a file cannot read another): <a href="' + a.getAttribute('data-src') + '#L' + a.getAttribute('data-a') + '">it is in its file</a>.';
        if (lp) { lp.appendChild(p); }
      });
    }
    function loadProof(a) {
      const href = a.getAttribute('data-proof'), panel = $('[data-panel="proof"]', a);
      if (!href || !panel || panel.hasAttribute('data-loaded')) { return; }
      panel.setAttribute('data-loaded', '');
      page(href).then((d) => {
        const tree = d.querySelector('ol.tree'), sum = d.querySelector('.proof-head .summary');
        if (!tree) { throw new Error('no tree'); }
        if (!a.hasAttribute('data-whole')) { putWhole(a, wholeFrom(d, a)); }
        panel.textContent = '';
        if (sum) { panel.appendChild(doc.importNode(sum, true)); }
        const bar = doc.createElement('div');
        bar.className = 'treebar';
        bar.innerHTML = '<button type="button" data-all="open">Expand all</button><button type="button" data-all="shut">Collapse all</button><span class="keys">↑ ↓ ← → in the tree</span>';
        panel.appendChild(bar);
        const t = doc.importNode(tree, true);
        $$('[id]', t).forEach((el) => { el.setAttribute('data-id', el.id); el.removeAttribute('id'); });
        $$('a.ll', t).forEach((l) => { l.setAttribute('href', href + '#' + l.closest('li').getAttribute('data-id')); });
        panel.appendChild(t);
        renderMath(panel);
        a._tree = Tree(t, { box: () => $('[data-panel="lean"] figure.code', a), inline: () => true, pane: () => body });
        treeButtons(bar, a._tree);
        const more = doc.createElement('p'); more.className = 'dim';
        more.innerHTML = 'Choose a step to see its Lean lines; they are marked under <b>Lean</b> too. <a href="' + href + '">The proof beside its whole declaration</a>.';
        panel.appendChild(more);
      }).catch(() => {
        panel.innerHTML = '<p class="dim">The structured proof could not be read from its page here (a page opened as a file cannot read another; see the README of the site). <a href="' + href + '">Open the structured proof</a>.</p>';
      });
    }
    side.addEventListener('click', (e) => {
      const t = e.target.closest('[role="tab"]');
      if (t) { tab(t.closest('article'), t.getAttribute('data-tab'), true); return; }
      const c = e.target.closest('.dchips button');
      if (c) { showKey(c.getAttribute('data-key')); V.mark(now, by[now], key); return; }
      const mv = e.target.closest('[data-move]');
      if (mv) { move(+mv.getAttribute('data-move')); return; }
      if (e.target.closest('.picker .cur')) { openList(list.hidden); return; }
      const s = e.target.closest('#stmts a[data-at]');
      if (s) { e.preventDefault(); openList(false); choose(s.getAttribute('data-at'), null, 'list'); }
    });
    side.addEventListener('keydown', (e) => {
      const t = e.target.closest('[role="tab"]');
      if (t && (e.key === 'ArrowRight' || e.key === 'ArrowLeft')) {
        const tabs = $$('[role="tab"]', t.parentElement), i = tabs.indexOf(t), n = tabs[(i + (e.key === 'ArrowRight' ? 1 : tabs.length - 1)) % tabs.length];
        tab(t.closest('article'), n.getAttribute('data-tab'), true); n.focus(); e.preventDefault();
      }
    });
    function openList(open) {
      list.hidden = !open;
      cur.setAttribute('aria-expanded', open ? 'true' : 'false');
      if (open) { const on = $('a.on', list) || $('a', list); if (on) { on.scrollIntoView({ block: 'nearest' }); on.focus({ preventScroll: true }); } }
    }
    function move(step) {
      const i = order.indexOf(now);
      const base = i >= 0 ? i : (by[now] && by[now].item ? order.indexOf(by[now].item) : -1);
      const to = order[Math.max(0, Math.min(order.length - 1, base < 0 ? 0 : base + step))];
      if (to) { choose(to, null, 'list'); }
    }
    doc.addEventListener('keydown', (e) => {
      if (typing(e) || e.altKey || e.ctrlKey || e.metaKey) { return; }
      if (e.target.closest && e.target.closest('ol.tree, [role="tab"]')) { return; }
      if (e.key === 'j' || e.key === 'n') { move(1); e.preventDefault(); }
      else if (e.key === 'k' || e.key === 'p') { move(-1); e.preventDefault(); }
      else if (e.key === 'Escape' && !list.hidden) { openList(false); cur.focus(); }
      else if (e.key === '+' || e.key === '=') { V.zoom(1); e.preventDefault(); }
      else if (e.key === '-') { V.zoom(-1); e.preventDefault(); }
      else if (e.key === '0') { V.zoom(0); e.preventDefault(); }
    });

    // a Lean name in the note is a link to the artifact's lines: it chooses that declaration here
    function keyOfUrl(u) {
      let url;
      try { url = new URL(u); } catch (e) { return null; }
      const m = /^#L(\d+)(?:-L(\d+))?$/.exec(url.hash);
      if (!m) { return null; }
      let path;
      try { path = decodeURIComponent(url.pathname); } catch (e) { return null; }
      const a = +m[1], b = +(m[2] || m[1]);
      for (const k of Object.keys(data.decls)) {
        const d = data.decls[k];
        if (d.a === a && d.b === b && path.endsWith('/' + d.file)) { return k; }
      }
      return null;
    }
    function pickKey(k, page, fy) {
      const hit = data.items.find((x) => x.rg.some((r) => r[0] === page && fy >= r[2] - 0.004 && fy <= r[4] + 0.004) && x.keys.indexOf(k) >= 0)
        || data.lean.find((b) => b.page === page && fy >= b.box[1] - 0.004 && fy <= b.box[3] + 0.004 && b.keys.indexOf(k) >= 0)
        || data.items.find((x) => x.keys.indexOf(k) >= 0);
      if (hit) { choose(hit.at, k, 'page'); }
    }

    const V = Viewer($('.viewer', RD), data, {
      pick: (at) => choose(at, null, 'page'),
      pickKey: pickKey,
      keyOfUrl: keyOfUrl,
      dest: (name) => { const x = data.items.find((it) => it.dest === name); if (x) { choose(x.at, null, 'link'); return true; } return false; },
      store: pdfName
    });

    // where to begin: the address, else the first statement (the pages stay where the reader left them)
    let h = location.hash.slice(1);
    try { h = decodeURIComponent(h); } catch (e) { /* read it as it stands */ }
    const q = {};
    h.split('&').forEach((p) => { const i = p.indexOf('='); if (i > 0) { q[p.slice(0, i)] = p.slice(i + 1); } });
    if (!(q.at && choose(q.at, q.k || null, 'load'))) {
      if (h.indexOf('d-') === 0) { const kk = h.slice(2), x = data.items.find((it) => it.keys.indexOf(kk) >= 0); if (x) { choose(x.at, kk, 'load'); return; } }
      if (order.length) {                                 // resume where the reader left this note; choose the first statement from there on
        const n = V.restore(), x = data.items.find((it) => it.page >= n) || data.items[0];
        choose(x.at, null, 'start');
      }
    }
  }

  // ---------------------------------------------------------------- the pages of a note, drawn by PDF.js
  function Viewer(el, data, hooks) {
    const scroll = $('.pdfscroll', el), pagesEl = $('.pages', el), bar = $('.vbar', el);
    const pgs = $$('.pg', pagesEl), input = $('.pageno input', bar), zoomval = $('.zoomval', bar);
    const ZOOMS = [0.5, 0.67, 0.8, 0.9, 1, 1.1, 1.25, 1.5, 1.75, 2, 2.5, 3];
    let zoom = +(store.get('readback-zoom') || 1);
    if (!(zoom >= 0.5 && zoom <= 3)) { zoom = 1; }
    const maxW = Math.max.apply(null, data.pages.map((p) => p[0]));
    pagesEl.style.setProperty('--pwmax', maxW);
    let pdf = null, lib = null, failed = false, fit = 0;
    const st = pgs.map(() => ({ w: 0, busy: false, text: false, links: false, near: false }));

    // the marks: statements (their regions) and LEAN lines, as fractions of a page
    const regions = pgs.map(() => []);
    const layer = pgs.map((pg) => { const m = doc.createElement('div'); m.className = 'marks'; pg.appendChild(m); return m; });
    function put(n, cls, at, box, extra) {
      const d = doc.createElement('div');
      d.className = cls; d.setAttribute('data-at', at);
      if (extra) { d.setAttribute('data-item', extra); }
      d.style.left = (box[0] * 100).toFixed(3) + '%'; d.style.top = (box[1] * 100).toFixed(3) + '%';
      d.style.width = ((box[2] - box[0]) * 100).toFixed(3) + '%'; d.style.height = ((box[3] - box[1]) * 100).toFixed(3) + '%';
      layer[n - 1].appendChild(d);
      return d;
    }
    data.items.forEach((x) => x.rg.forEach((r) => {
      if (r[0] < 1 || r[0] > pgs.length) { return; }
      const box = r.slice(1);
      regions[r[0] - 1].push({ at: x.at, box: box, el: put(r[0], 'rg', x.at, box) });
    }));
    data.lean.forEach((b) => {
      if (b.page < 1 || b.page > pgs.length) { return; }
      const d = put(b.page, 'band' + (b.item ? '' : ' free'), b.at, b.box, b.item);
      if (!b.item && b.keys.length) { regions[b.page - 1].push({ at: b.at, box: b.box, el: d }); }
    });
    const area = (b) => (b[2] - b[0]) * (b[3] - b[1]);
    function hit(e) {
      const pg = e.target.closest && e.target.closest('.pg');
      if (!pg) { return null; }
      const r = pg.getBoundingClientRect(), fx = (e.clientX - r.left) / r.width, fy = (e.clientY - r.top) / r.height;
      let best = null;
      regions[+pg.getAttribute('data-n') - 1].forEach((g) => {
        if (fx >= g.box[0] && fx <= g.box[2] && fy >= g.box[1] && fy <= g.box[3] && (!best || area(g.box) < area(best.box))) { best = g; }
      });
      return best;
    }
    let hovered = null, hoverPg = null;
    pagesEl.addEventListener('pointermove', (e) => {
      if (e.pointerType === 'touch') { return; }
      const g = e.target.closest('.plink') ? null : hit(e), pg = e.target.closest('.pg');
      if (hovered && hovered !== g) { hovered.el.classList.remove('hover'); }
      if (g) { g.el.classList.add('hover'); }
      hovered = g;
      if (hoverPg && hoverPg !== pg) { hoverPg.classList.remove('pointing'); }
      if (pg) { pg.classList.toggle('pointing', !!g); }
      hoverPg = pg;
    });
    pagesEl.addEventListener('pointerleave', () => { if (hovered) { hovered.el.classList.remove('hover'); hovered = null; } if (hoverPg) { hoverPg.classList.remove('pointing'); } });
    pagesEl.addEventListener('click', (e) => {
      if (e.target.closest('.plink')) { return; }
      if (window.getSelection && String(window.getSelection()).trim()) { return; }       // a selection of text, not a choice
      const g = hit(e);
      if (g) { hooks.pick(g.at); }
    });

    function mark(at, x, key) {
      layer.forEach((m) => $$('.on', m).forEach((d) => d.classList.remove('on')));
      $$('.plink.lean.on', pagesEl).forEach((d) => d.classList.remove('on'));
      if (!x) { return; }
      layer.forEach((m) => $$('[data-at="' + CSS.escape(at) + '"], .band[data-item="' + CSS.escape(at) + '"]', m).forEach((d) => d.classList.add('on')));
      if (key) { $$('.plink.lean[data-key="' + CSS.escape(key) + '"]', pagesEl).forEach((d) => d.classList.add('on')); }
    }
    function place(x) {                                    // [page, top fraction] of a statement or a LEAN line
      if (x.rg && x.rg.length) { return [x.rg[0][0], x.rg[0][2]]; }
      if (x.box) { return [x.page, x.box[1]]; }
      return [x.page || 1, 0];
    }
    function goTo(n, fy, atOnce, part) {
      if (failed) { frame(n); return; }
      const pg = pgs[n - 1];
      if (!pg) { return; }
      const top = scroll.scrollTop + pg.getBoundingClientRect().top - scroll.getBoundingClientRect().top + fy * pg.clientHeight - scroll.clientHeight * (part === undefined ? 0.14 : part);
      scroll.scrollTo({ top: Math.max(0, top), behavior: calm || atOnce ? 'auto' : 'smooth' });
    }
    function show(x, atOnce) {
      const [n, fy] = place(x);
      if (failed) { frame(n); return; }
      const pg = pgs[n - 1];
      if (!pg) { return; }
      const r = pg.getBoundingClientRect(), s = scroll.getBoundingClientRect(), y = r.top + fy * r.height;
      if (!atOnce && y > s.top + 30 && y < s.top + s.height * 0.72) { return; }   // already in view: do not move the page
      goTo(n, fy, atOnce);
    }

    // zoom and size
    function layout(keep) {
      const pad = parseFloat(getComputedStyle(scroll).paddingLeft) || 0;
      const anchor = keep ? (scroll.scrollTop + scroll.clientHeight / 2) / Math.max(1, pagesEl.scrollHeight) : null;
      const anchorX = keep ? (scroll.scrollLeft + scroll.clientWidth / 2) / Math.max(1, pagesEl.scrollWidth) : null;
      fit = Math.max(240, Math.min(scroll.clientWidth - 2 * pad, 1100));
      pagesEl.style.setProperty('--fit', fit + 'px');
      pagesEl.style.setProperty('--zoom', zoom);
      pagesEl.style.setProperty('--total-scale-factor', (fit * zoom / maxW).toFixed(6));
      zoomval.textContent = Math.round(zoom * 100) + '%';
      if (keep) {
        scroll.scrollTop = anchor * pagesEl.scrollHeight - scroll.clientHeight / 2;
        scroll.scrollLeft = anchorX * pagesEl.scrollWidth - scroll.clientWidth / 2;
      }
      drawSoon();
    }
    function setZoom(z) {
      z = Math.max(0.5, Math.min(3, z));
      if (Math.abs(z - zoom) < 0.001) { return; }
      zoom = z; store.set('readback-zoom', String(zoom));
      layout(true);
    }
    function zoomStep(dir) {
      if (dir === 0) { setZoom(1); return; }
      const next = dir > 0 ? ZOOMS.find((z) => z > zoom + 0.001) : ZOOMS.slice().reverse().find((z) => z < zoom - 0.001);
      setZoom(next || zoom);
    }
    bar.addEventListener('click', (e) => { const b = e.target.closest('[data-zoom]'); if (b) { zoomStep(+b.getAttribute('data-zoom')); } });
    scroll.addEventListener('wheel', (e) => {                // a pinch, or ctrl and the wheel: zoom about the pointer's page
      if (!e.ctrlKey) { return; }
      e.preventDefault();
      setZoom(zoom * Math.exp(-e.deltaY * 0.01));
    }, { passive: false });
    let resizeTimer = 0;
    if ('ResizeObserver' in window) { new ResizeObserver(() => { clearTimeout(resizeTimer); resizeTimer = setTimeout(() => layout(true), 90); }).observe(scroll); }

    // the page number
    function pageNow() {
      const s = scroll.getBoundingClientRect(), y = s.top + s.height * 0.35;
      let lo = 0, hi = pgs.length - 1;
      while (lo < hi) { const mid = (lo + hi + 1) >> 1; if (pgs[mid].getBoundingClientRect().top <= y) { lo = mid; } else { hi = mid - 1; } }
      return lo + 1;
    }
    let ticking = false, saveTimer = 0;
    scroll.addEventListener('scroll', () => {
      if (ticking) { return; }
      ticking = true;
      requestAnimationFrame(() => {
        ticking = false;
        if (doc.activeElement !== input) { input.value = pageNow(); }
        clearTimeout(saveTimer);
        saveTimer = setTimeout(() => { const n = pageNow(), pg = pgs[n - 1]; const f = (scroll.getBoundingClientRect().top - pg.getBoundingClientRect().top) / pg.clientHeight; store.set(hooks.store, n + ':' + f.toFixed(4)); }, 400);
      });
    }, { passive: true });
    input.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') { const n = Math.max(1, Math.min(pgs.length, parseInt(input.value, 10) || 1)); input.value = n; goTo(n, 0, false, 0.02); input.blur(); }
    });

    // drawing
    const MAX_PIXELS = 16e6;
    function drawSoon() { requestAnimationFrame(() => st.forEach((s, i) => { if (s.near) { draw(i); } })); }
    function draw(i) {
      if (!pdf) { return; }
      const pg = pgs[i], s = st[i];
      const w = pg.clientWidth;
      if (!w) { return; }
      const dpr = Math.min(window.devicePixelRatio || 1, 3);
      const target = Math.round(w * dpr);
      if (s.busy || s.w === target) { return; }
      s.busy = true;
      pdf.getPage(i + 1).then((page) => {
        const base = page.getViewport({ scale: 1 });
        let scale = target / base.width;
        if (base.width * base.height * scale * scale > MAX_PIXELS) { scale = Math.sqrt(MAX_PIXELS / (base.width * base.height)); }
        const vp = page.getViewport({ scale: scale });
        const c = doc.createElement('canvas');
        c.width = Math.floor(vp.width); c.height = Math.floor(vp.height);
        c.setAttribute('aria-hidden', 'true');
        return page.render({ canvas: c, viewport: vp }).promise.then(() => {
          const old = $(':scope > canvas', pg);
          if (old) { old.replaceWith(c); old.width = 0; old.height = 0; } else { pg.insertBefore(c, pg.firstChild); }
          pg.classList.add('drawn');
          s.w = target; s.busy = false;
          if (!s.text) { textLayer(page, pg, s); }
          if (!s.links) { links(page, pg, s, i + 1); }
          if (!s.near) { release(i); } else if (Math.round(pg.clientWidth * dpr) !== s.w) { draw(i); }
        });
      }).catch(() => { s.busy = false; });
    }
    function release(i) {                                  // a page far from the view gives its pixels back
      const c = $(':scope > canvas', pgs[i]), s = st[i];
      if (c && !s.busy) { c.width = 0; c.height = 0; c.remove(); pgs[i].classList.remove('drawn'); s.w = 0; }
    }
    function textLayer(page, pg, s) {
      s.text = true;
      if (!lib.TextLayer) { return; }
      const div = doc.createElement('div');
      div.className = 'textLayer';
      pg.insertBefore(div, pg.querySelector('.marks'));
      try {
        new lib.TextLayer({ textContentSource: page.streamTextContent(), container: div, viewport: page.getViewport({ scale: 1 }) }).render().catch(() => {});
      } catch (e) { div.remove(); }
    }
    function links(page, pg, s, n) {
      s.links = true;
      page.getAnnotations({ intent: 'display' }).then((anns) => {
        const v = page.view, W = v[2] - v[0], H = v[3] - v[1];
        const m = pg.querySelector('.marks');
        anns.forEach((a) => {
          if (a.subtype !== 'Link' || !a.rect || (!a.url && !a.dest)) { return; }
          const x0 = (Math.min(a.rect[0], a.rect[2]) - v[0]) / W, x1 = (Math.max(a.rect[0], a.rect[2]) - v[0]) / W;
          const y0 = (v[3] - Math.max(a.rect[1], a.rect[3])) / H, y1 = (v[3] - Math.min(a.rect[1], a.rect[3])) / H;
          const l = doc.createElement('a');
          l.className = 'plink';
          Object.assign(l.style, { left: (x0 * 100) + '%', top: (y0 * 100) + '%', width: ((x1 - x0) * 100) + '%', height: ((y1 - y0) * 100) + '%' });
          if (a.url) {
            const k = hooks.keyOfUrl(a.url);
            if (k) {
              const d = data.decls[k];
              l.classList.add('lean'); l.href = a.url; l.setAttribute('data-key', k);
              l.title = (d && d.name ? d.name : k) + ': show it beside the note (with ⌘ or Ctrl: open the artifact on GitHub)';
              l.addEventListener('click', (e) => {
                if (e.metaKey || e.ctrlKey || e.shiftKey) { return; }
                e.preventDefault(); hooks.pickKey(k, n, (y0 + y1) / 2);
              });
            } else { l.href = a.url; l.target = '_blank'; l.rel = 'noopener'; l.title = a.url; }
          } else {
            l.href = '#'; l.title = 'Go to the place it refers to';
            l.addEventListener('click', (e) => { e.preventDefault(); toDest(a.dest); });
          }
          l.setAttribute('aria-label', l.title);
          m.appendChild(l);
        });
        if (now0) { mark0(); }
      }).catch(() => {});
    }
    let now0 = null;
    function mark0() { if (now0) { mark(now0[0], now0[1], now0[2]); } }
    function toDest(dest) {
      if (typeof dest === 'string' && hooks.dest(dest)) { return; }
      const p = typeof dest === 'string' ? pdf.getDestination(dest) : Promise.resolve(dest);
      p.then((d) => {
        if (!Array.isArray(d)) { return; }
        return (typeof d[0] === 'object' && d[0] !== null ? pdf.getPageIndex(d[0]) : Promise.resolve(d[0])).then((idx) => {
          const n = idx + 1, pg = pgs[n - 1];
          if (!pg) { return; }
          let fy = 0;
          if (d[1] && d[1].name === 'XYZ' && typeof d[3] === 'number') { fy = 1 - d[3] / data.pages[n - 1][1]; }
          goTo(n, Math.max(0, fy), false, 0.12);
          const f = doc.createElement('div'); f.className = 'flash'; f.style.top = (Math.max(0, fy) * 100) + '%';
          pg.querySelector('.marks').appendChild(f); setTimeout(() => f.remove(), 1800);
        });
      }).catch(() => {});
    }

    // only the pages near the view are drawn; pages far from it give their pixels back
    const nearIO = new IntersectionObserver((es) => {
      es.forEach((e) => { const i = pgs.indexOf(e.target); st[i].near = e.isIntersecting; if (e.isIntersecting) { draw(i); } });
    }, { root: scroll, rootMargin: '120% 0px' });
    const farIO = new IntersectionObserver((es) => {
      es.forEach((e) => { if (!e.isIntersecting) { release(pgs.indexOf(e.target)); } });
    }, { root: scroll, rootMargin: '400% 0px' });
    pgs.forEach((p) => { nearIO.observe(p); farIO.observe(p); });

    // without PDF.js (a page opened as a file, an old browser): the browser's own viewer
    function frame(n) {
      const f = $('iframe.pdfframe', el);
      if (!f) { return; }
      const fresh = f.cloneNode(false);                    // a frame does not follow a changed fragment: put a new one
      fresh.src = data.pdf + '#page=' + n;
      f.replaceWith(fresh);
    }
    function fallback(why) {
      if (failed) { return; }
      failed = true;
      bar.classList.add('fallback');
      const note = doc.createElement('p');
      note.className = 'fallnote';
      note.textContent = why;
      const f = doc.createElement('iframe');
      f.className = 'pdfframe'; f.title = 'The note as a PDF'; f.src = data.pdf;
      scroll.replaceWith(f);
      f.parentNode.insertBefore(note, f);
    }
    layout(false);
    if (location.protocol === 'file:') {
      fallback('Opened as a file, this page cannot run PDF.js; the browser\'s own viewer shows the note instead, without marks on the pages. Serve the site over http (serve.sh) for the full reader.');
    } else {
      import(ASSETS + 'vendor/pdfjs/pdf.min.mjs').then((m) => {
        lib = m;
        lib.GlobalWorkerOptions.workerSrc = ASSETS + 'vendor/pdfjs/pdf.worker.min.mjs';
        return lib.getDocument({ url: new URL(data.pdf, doc.baseURI).href, isEvalSupported: false }).promise;
      }).then((d) => {
        pdf = d;
        drawSoon();
      }).catch((e) => fallback('PDF.js could not open the note (' + (e && e.message ? e.message : e) + '); the browser\'s own viewer shows it instead.'));
    }
    return {
      mark: (at, x, key) => { now0 = [at, x, key]; mark(at, x, key); },
      show: show,
      zoom: zoomStep,
      restore: () => {
        const v = store.get(hooks.store), m = /^(\d+):(-?[\d.]+)$/.exec(v || '');
        if (m && +m[1] <= pgs.length) { goTo(+m[1], Math.max(0, +m[2]), true, 0); return +m[1]; }
        return 1;
      }
    };
  }

  // formulas last: the reading mode has shown what it shows first
  boxButtons(doc);
  mathSoon(doc.body);
  applyWrap(doc);
})();
