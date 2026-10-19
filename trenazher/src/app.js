// Движок тренажёра. Всё хранится в браузере (localStorage) + выгрузка в файл.
var LS_KEY = "trenazher_peregovory_v1";
var DAY = 86400000;
var INTERVALS = [0, 1, 3, 7, 14, 30];          // дни до повторения для коробок 0..5
var VERD = {
  b: { l: "✅ Лучший ход", c: "v-b", p: 10 },
  o: { l: "🟡 Неплохо, но можно лучше", c: "v-o", p: 5 },
  x: { l: "🟠 Слабый ход", c: "v-x", p: 1 },
  z: { l: "⛔ Запрещено: блеф, давление, ложь", c: "v-z", p: 0 }
};
var LEVELS = [[0, "Новичок 🌱"], [80, "Слушательница 👂"], [200, "Спокойная в разговоре 🧘"], [400, "Мастер вопроса ❓"], [700, "Цена слова 🏆"]];
var BADGES = {
  first: "🎬 Первый раунд",
  ask5: "❓ Сначала спросила ×5",
  clean: "🕊 Раунд без запрещённых ходов",
  days3: "🔥 3 дня подряд",
  dlg: "💬 Живой разговор пройден",
  own10: "✍️ 10 своих ответов",
  allbooks: "📚 Знаю приёмы всех пяти книг"
};

var memOnly = false;
function blank() { return { pts: 0, cards: {}, answers: [], days: [], badges: [], dialogs: {}, asked: 0, bans: 0, rounds: 0, cleanRound: false }; }
function load() {
  try { var j = localStorage.getItem(LS_KEY); if (j) { var o = JSON.parse(j); return Object.assign(blank(), o); } } catch (e) { memOnly = true; }
  return blank();
}
function save() { try { localStorage.setItem(LS_KEY, JSON.stringify(S)); } catch (e) { memOnly = true; } }
var S = load();

function esc(s) { return String(s == null ? "" : s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;"); }
function shuffle(a) { a = a.slice(); for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
function today() { var d = new Date(); return d.getFullYear() + "-" + ("0" + (d.getMonth() + 1)).slice(-2) + "-" + ("0" + d.getDate()).slice(-2); }
function level() { var l = LEVELS[0][1], nxt = null; for (var i = 0; i < LEVELS.length; i++) { if (S.pts >= LEVELS[i][0]) { l = LEVELS[i][1]; nxt = LEVELS[i + 1] || null; } } return { name: l, next: nxt }; }
function streak() {
  var set = {}; S.days.forEach(function (d) { set[d] = 1; });
  var n = 0, dt = new Date();
  if (!set[today()]) dt = new Date(Date.now() - DAY);
  while (true) {
    var k = dt.getFullYear() + "-" + ("0" + (dt.getMonth() + 1)).slice(-2) + "-" + ("0" + dt.getDate()).slice(-2);
    if (set[k]) { n++; dt = new Date(dt.getTime() - DAY); } else break;
  }
  return n;
}
function byId(id) { for (var i = 0; i < SCEN.length; i++) if (SCEN[i].id === id) return SCEN[i]; return null; }

// ---------- повторения по коробкам (Лейтнер) ----------
function cardState(id) { return S.cards[id] || null; }
function updateBox(id, verdict) {
  var c = S.cards[id] || { box: 0, due: 0, seen: 0 };
  c.seen++;
  if (verdict === "b") c.box = Math.min(5, c.box + 1);
  else if (verdict === "o") c.box = Math.max(c.box, 0);
  else c.box = 0;
  c.due = Date.now() + INTERVALS[c.box] * DAY;
  c.last = verdict;
  S.cards[id] = c;
}
function dueList() { var now = Date.now(); return SCEN.filter(function (s) { var c = S.cards[s.id]; return c && c.due <= now && c.box < 5; }); }

// ---------- выбор раунда: повторения, новое, перемешивание книг ----------
function interleave(list) {
  var out = [], rest = list.slice();
  while (rest.length) {
    var last = out.length ? out[out.length - 1].bk : null, idx = -1;
    for (var i = 0; i < rest.length; i++) { if (rest[i].bk !== last) { idx = i; break; } }
    if (idx < 0) idx = 0;
    out.push(rest.splice(idx, 1)[0]);
  }
  return out;
}
function pickRound(pool, n) {
  var now = Date.now();
  var due = pool.filter(function (s) { var c = S.cards[s.id]; return c && c.due <= now; }).sort(function (a, b) { return S.cards[a.id].box - S.cards[b.id].box; });
  var fresh = shuffle(pool.filter(function (s) { return !S.cards[s.id]; }));
  var rest = shuffle(pool.filter(function (s) { var c = S.cards[s.id]; return c && c.due > now; })).sort(function (a, b) { return S.cards[a.id].box - S.cards[b.id].box; });
  var chosen = due.slice(0, Math.ceil(n / 2)).concat(fresh).concat(due.slice(Math.ceil(n / 2))).concat(rest);
  return interleave(shuffle(chosen.slice(0, n)));
}

// ---------- подсказки по тексту Виты (простая проверка слов, не оценка смысла) ----------
function hints(text, sc) {
  var t = text.toLowerCase(), h = [];
  if (/хотя бы|как получится|чтобы мне приятно|много времени не займ|я только учусь|если можно|извини,? что|просто если/.test(t)) h.push("Есть смягчитель («хотя бы», «как получится», «я только учусь»…) — он снижает твою позицию. Попробуй убрать.");
  if (/иначе|последний шанс|остановлю|или ты|до пятницы|только сегодня/.test(t)) h.push("Похоже на ультиматум или срок. Он допустим, только если ты правда это сделаешь и срок настоящий.");
  if (/другой (поставщик|клиент|завод|студи|заказчик)|у меня много (заказ|клиент)|есть оффер/.test(t)) h.push("Похоже на блеф про «других». Если этого нет — не говори.");
  if (/\d/.test(t) && !/__/.test(text)) h.push("Есть цифра. Откуда она — из часов, расчёта, реальных данных? Если не можешь объяснить, поставь «__».");
  if (sc.q && text.indexOf("?") < 0) h.push("В этой ситуации сначала нужен один уточняющий вопрос. В твоём ответе вопроса нет.");
  if ((text.match(/\?/g) || []).length > 2) h.push("Вопросов много. Лучше один главный, остальные потом.");
  if (text.length > 450) h.push("Длинно. Одна мысль — одно предложение, лучше короче.");
  if (!h.length) h.push("Явных слов-ловушек не нашла. Сравни свой ответ со «лучшим ходом» ниже: совпала ли идея?");
  return h;
}

// ---------- награды ----------
function checkBadges() {
  var newb = [];
  function give(k) { if (S.badges.indexOf(k) < 0) { S.badges.push(k); newb.push(BADGES[k]); } }
  if (S.rounds >= 1) give("first");
  if (S.asked >= 5) give("ask5");
  if (S.cleanRound) give("clean");
  if (streak() >= 3) give("days3");
  if (Object.keys(S.dialogs).length) give("dlg");
  if (S.answers.filter(function (a) { return a.own && a.own.length >= 15; }).length >= 10) give("own10");
  var ok = true;
  ["voss", "weiss", "klaff", "mom", "hall"].forEach(function (b) {
    var any = SCEN.some(function (s) { return s.bk === b && S.cards[s.id] && S.cards[s.id].box >= 2; });
    if (!any) ok = false;
  });
  if (ok) give("allbooks");
  return newb;
}

// ---------- экраны ----------
var R = null, D = null, view = "home";
var app = document.getElementById("app");

function topbar(back, title) {
  var lv = level();
  return '<div class="topbar">' + (back ? '<button class="ghost" data-act="home">← Меню</button>' : '<span></span>') +
    '<div class="tb-mid">' + esc(title || "") + '</div><div class="pts" title="Очки">⭐ ' + S.pts + '</div></div>';
}
function setView(html) { app.innerHTML = html; window.scrollTo(0, 0); }

function bookProgress(bk) {
  var all = SCEN.filter(function (s) { return s.bk === bk; });
  var done = all.filter(function (s) { return S.cards[s.id] && S.cards[s.id].box >= 3; }).length;
  return { n: all.length, done: done };
}

function renderHome() {
  view = "home";
  var lv = level(), due = dueList().length;
  var st = streak();
  var h = '<header class="hero"><div class="hero-t">Тренажёр переговоров</div><div class="hero-s">Ситуации из жизни. Ты отвечаешь — тренажёр показывает приём, запрет и ход лучше.</div></header>';
  if (memOnly) h += '<div class="warn">Браузер не разрешает сохранять здесь. Играть можно; чтобы не потерять — нажми «Журнал» → «Скачать сохранение».</div>';
  h += '<div class="stats"><div class="stat"><b>' + S.pts + '</b><span>очки</span></div><div class="stat"><b>' + st + '</b><span>дней подряд</span></div><div class="stat"><b>' + due + '</b><span>на повторение</span></div></div>';
  h += '<div class="lvl">' + esc(lv.name) + (lv.next ? ' · до «' + esc(lv.next[1]) + '» ещё ' + (lv.next[0] - S.pts) : ' · высший уровень') + '</div>';
  h += '<div class="menu">';
  h += '<button class="big primary" data-act="round" data-mode="mix">▶ Играть: раунд из 8</button>';
  h += '<button class="big" data-act="round" data-mode="due"' + (due ? '' : ' disabled') + '>🔁 Повторить слабое (' + due + ')</button>';
  h += '<button class="big" data-act="dialogs">💬 Живой разговор (3 хода)</button>';
  h += '<button class="big" data-act="round" data-mode="def">🛡 Защита: узнай давление</button>';
  h += '</div>';
  h += '<div class="sec-t">Тренировать одну книгу</div><div class="books">';
  ["voss", "weiss", "klaff", "mom", "hall"].forEach(function (b) {
    var p = bookProgress(b);
    h += '<button class="book" style="--bc:' + BOOKS[b].c + '" data-act="round" data-mode="book" data-book="' + b + '"><span>' + BOOKS[b].e + ' ' + esc(BOOKS[b].s) + '</span><small>освоено ' + p.done + ' из ' + p.n + '</small></button>';
  });
  h += '</div>';
  h += '<div class="menu2"><button class="ghost" data-act="cards">📖 Приёмы</button><button class="ghost" data-act="journal">📓 Журнал</button><button class="ghost" data-act="about">ℹ️ Как это работает</button></div>';
  if (S.badges.length) h += '<div class="sec-t">Награды</div><div class="badges">' + S.badges.map(function (k) { return '<span class="badge">' + esc(BADGES[k]) + '</span>'; }).join("") + '</div>';
  setView(h);
}

function startRound(mode, book) {
  var pool = SCEN, n = 8, title = "Раунд";
  if (mode === "due") { pool = dueList(); title = "Повторение"; }
  else if (mode === "def") { pool = SCEN.filter(function (s) { return s.o.some(function (o) { return o.g.indexOf("DEF") >= 0 || o.g.indexOf("NOBLUFF") >= 0 || o.g.indexOf("SAFE") >= 0; }); }); title = "Защита"; }
  else if (mode === "book") { pool = SCEN.filter(function (s) { return s.bk === book; }); title = BOOKS[book].s; n = Math.min(8, pool.length); }
  var list = pickRound(pool, n);
  if (!list.length) { renderHome(); return; }
  R = { list: list, i: 0, pts: 0, res: [], title: title, mode: mode };
  renderPlay("own");
}

function sceneHTML(sc) {
  var bk = BOOKS[sc.bk];
  return '<div class="scene"><div class="chips"><span class="chip" style="background:' + bk.c + '">' + bk.e + ' ' + esc(bk.s) + '</span><span class="chip ch">' + esc(sc.ch) + '</span></div>' +
    '<div class="ctx">' + esc(sc.ctx) + '</div><div class="bubble"><span class="who">' + sc.em + ' ' + esc(sc.who) + '</span>' + esc(sc.line) + '</div></div>';
}

function renderPlay(phase) {
  view = "play";
  var sc = R.list[R.i];
  var h = topbar(true, R.title + " · " + (R.i + 1) + " из " + R.list.length);
  h += '<div class="prog"><i style="width:' + (R.i / R.list.length * 100) + '%"></i></div>';
  h += sceneHTML(sc);
  if (phase === "own") {
    h += '<div class="box"><div class="lab">Шаг 1. Напиши свой ответ — до подсказок</div>' +
      '<div class="hint">Так мозг запоминает лучше. Спроси себя: <b>чего я здесь не знаю?</b> На телефоне можно надиктовать: значок микрофона на клавиатуре.</div>' +
      '<textarea id="own" rows="4" placeholder="Что ты ответила бы? (можно с «__» вместо цифры)"></textarea>' +
      '<div class="row"><button class="primary" data-act="toopts">Показать варианты</button><button class="ghost" data-act="skipown">Пропустить</button></div></div>';
  } else {
    R.order = R.order && R.orderFor === sc.id ? R.order : shuffle(sc.o.map(function (o, i) { return i; }));
    R.orderFor = sc.id;
    h += '<div class="box"><div class="lab">Шаг 2. Выбери ход</div>';
    R.order.forEach(function (i, k) {
      var o = sc.o[i];
      h += '<button class="opt" data-act="pick" data-i="' + i + '"><b>' + "ABCD".charAt(k) + '</b><span>' + esc(o.t) + '</span></button>';
    });
    h += '</div>';
  }
  setView(h);
}

function tagChips(g) { return g.map(function (k) { var c = CARDS[k]; return c ? '<button class="tag" data-act="card" data-k="' + k + '">' + esc(c.n) + '</button>' : ''; }).join(""); }

function recordAnswer(sc, pickedIdx, own) {
  var o = sc.o[pickedIdx], v = o.v;
  var gained = VERD[v].p + (own && own.length >= 15 ? 3 : 0);
  S.pts += gained; R.pts += gained;
  if (v === "z") S.bans++;
  if (sc.q && v === "b") S.asked++;
  updateBox(sc.id, v);
  S.answers.push({ ts: Date.now(), id: sc.id, own: own || "", pick: o.t, v: v });
  if (S.days.indexOf(today()) < 0) S.days.push(today());
  R.res.push({ id: sc.id, v: v, g: o.g, bk: sc.bk });
  save();
  return gained;
}

function renderReveal(pickedIdx) {
  view = "reveal";
  var sc = R.list[R.i], own = R.own || "";
  var gained = recordAnswer(sc, pickedIdx, own);
  var o = sc.o[pickedIdx], vd = VERD[o.v];
  var h = topbar(true, R.title + " · " + (R.i + 1) + " из " + R.list.length);
  h += '<div class="prog"><i style="width:' + ((R.i + 1) / R.list.length * 100) + '%"></i></div>';
  h += sceneHTML(sc);
  h += '<div class="verdict ' + vd.c + '"><b>' + vd.l + '</b> · +' + gained + ' очков' + (sc.q && o.v === "b" ? ' · спросила сначала 👏' : '') + '</div>';
  if (own) {
    h += '<div class="box"><div class="lab">Твой ответ</div><div class="mine">' + esc(own) + '</div>' +
      '<div class="lab">Подсказки по словам <small>(простая проверка слов, не оценка смысла)</small></div><ul class="hl">' + hints(own, sc).map(function (t) { return '<li>' + esc(t) + '</li>'; }).join("") + '</ul></div>';
  }
  h += '<div class="box"><div class="lab">Разбор всех ходов</div>';
  sc.o.forEach(function (x, i) {
    var xv = VERD[x.v];
    h += '<div class="rv ' + xv.c + (i === pickedIdx ? ' picked' : '') + '"><div class="rv-h">' + xv.l + (i === pickedIdx ? ' · твой выбор' : '') + '</div>' +
      '<div class="rv-t">' + esc(x.t) + '</div>' + (x.r ? '<div class="rv-r">' + esc(x.r) + '</div>' : '') +
      '<div class="rv-w">' + esc(x.w) + '</div><div class="tags">' + tagChips(x.g) + '</div></div>';
  });
  h += '</div>';
  h += '<div class="box better"><div class="lab">Пример лучше</div><div class="bt">' + esc(sc.better) + '</div>' + (sc.rbetter ? '<div class="rv-r">' + esc(sc.rbetter) + '</div>' : '') + '<small>«__» — вставь свои настоящие данные: цифры за тебя я не придумываю.</small></div>';
  if (sc.vn) h += '<div class="note">🎙 ' + esc(sc.vn) + '</div>';
  var last = R.i + 1 >= R.list.length;
  h += '<div class="row"><button class="primary" data-act="next">' + (last ? 'Итоги раунда' : 'Дальше →') + '</button></div>';
  setView(h);
}

function renderEnd() {
  view = "end";
  S.rounds++;
  var zs = R.res.filter(function (r) { return r.v === "z"; }).length;
  var bs = R.res.filter(function (r) { return r.v === "b"; }).length;
  if (zs === 0 && R.res.length >= 6) S.cleanRound = true;
  var nb = checkBadges();
  save();
  var h = topbar(true, "Итоги");
  h += '<header class="hero"><div class="hero-t">Раунд окончен</div></header>';
  h += '<div class="stats"><div class="stat"><b>' + bs + '/' + R.res.length + '</b><span>лучших ходов</span></div><div class="stat"><b>+' + R.pts + '</b><span>очки</span></div><div class="stat"><b>' + zs + '</b><span>запрещённых</span></div></div>';
  if (nb.length) h += '<div class="note">🎉 Новая награда: ' + nb.map(esc).join(", ") + '</div>';
  var miss = {}, missBook = {};
  R.res.forEach(function (r) { if (r.v !== "b") { r.g.forEach(function (k) { miss[k] = 1; }); } });
  var keys = Object.keys(miss);
  if (keys.length) h += '<div class="box"><div class="lab">Повтори эти приёмы</div><div class="tags">' + tagChips(keys) + '</div></div>';
  else h += '<div class="box">Все ходы были лучшими. Завтра вернутся самые слабые для повторения.</div>';
  h += '<div class="box"><div class="lab">Что было</div>';
  R.res.forEach(function (r) { var sc = byId(r.id); h += '<div class="line ' + VERD[r.v].c + '">' + VERD[r.v].l.split(" ")[0] + ' ' + esc(sc.who) + ': «' + esc(sc.line.slice(0, 60)) + (sc.line.length > 60 ? '…' : '') + '»</div>'; });
  h += '</div>';
  h += '<div class="menu"><button class="big primary" data-act="round" data-mode="' + R.mode + '"' + (R.mode === "book" ? ' data-book="' + (R.list[0].bk) + '"' : '') + '>▶ Ещё раунд</button><button class="big" data-act="home">Меню</button></div>';
  setView(h);
}

// ---------- живые разговоры ----------
function renderDialogs() {
  view = "dialogs";
  var h = topbar(true, "Живой разговор");
  h += '<div class="hint pad">Тренажёр играет собеседника. Ты отвечаешь тремя репликами подряд; собеседник реагирует на то, что ты выбрала.</div><div class="menu">';
  DIALOGS.forEach(function (d) {
    var best = S.dialogs[d.id];
    h += '<button class="big" data-act="dlg" data-id="' + d.id + '">' + d.em + ' ' + esc(d.t) + (best != null ? '<small> · лучший счёт ' + best + '/30</small>' : '') + '</button>';
  });
  h += '</div>';
  setView(h);
}
function startDialog(id) {
  var dd = DIALOGS.filter(function (d) { return d.id === id; })[0];
  D = { d: dd, i: 0, pts: 0, partner: dd.turns[0].p, hist: [], phase: "ask" };
  renderDialogTurn();
}
function renderDialogTurn() {
  view = "dlgturn";
  var t = D.d.turns[D.i];
  var h = topbar(true, D.d.t + " · " + (D.i + 1) + " из " + D.d.turns.length);
  h += '<div class="prog"><i style="width:' + (D.i / D.d.turns.length * 100) + '%"></i></div>';
  if (D.i === 0) h += '<div class="note">' + esc(D.d.intro) + '</div>';
  D.hist.forEach(function (x) { h += '<div class="bubble you">' + esc(x.t) + '</div><div class="bubble"><span class="who">' + D.d.em + '</span>' + esc(x.r) + '</div>'; });
  if (D.hist.length === 0) h += '<div class="bubble"><span class="who">' + D.d.em + '</span>' + esc(D.partner) + '</div>';
  h += '<div class="box"><div class="lab">Что ответишь?</div>';
  D.order = D.order && D.orderI === D.i ? D.order : shuffle(t.o.map(function (o, i) { return i; }));
  D.orderI = D.i;
  D.order.forEach(function (i, k) { h += '<button class="opt" data-act="dpick" data-i="' + i + '"><b>' + "ABCD".charAt(k) + '</b><span>' + esc(t.o[i].t) + '</span></button>'; });
  h += '</div>';
  setView(h);
}
function dialogPick(i) {
  var t = D.d.turns[D.i], o = t.o[i], vd = VERD[o.v];
  D.pts += vd.p; S.pts += vd.p; if (o.v === "z") S.bans++;
  D.hist.push({ t: o.t, r: o.r, v: o.v, w: o.w, g: o.g });
  view = "dlgfb";
  var h = topbar(true, D.d.t + " · " + (D.i + 1) + " из " + D.d.turns.length);
  D.hist.slice(0, -1).forEach(function (x) { h += '<div class="bubble you">' + esc(x.t) + '</div><div class="bubble"><span class="who">' + D.d.em + '</span>' + esc(x.r) + '</div>'; });
  h += '<div class="bubble you">' + esc(o.t) + '</div><div class="bubble"><span class="who">' + D.d.em + '</span>' + esc(o.r) + '</div>';
  h += '<div class="verdict ' + vd.c + '"><b>' + vd.l + '</b> · +' + vd.p + '</div><div class="box"><div class="rv-w">' + esc(o.w) + '</div><div class="tags">' + tagChips(o.g) + '</div></div>';
  var last = D.i + 1 >= D.d.turns.length;
  h += '<div class="row"><button class="primary" data-act="dnext">' + (last ? 'Итог разговора' : 'Дальше →') + '</button></div>';
  setView(h);
}
function dialogEnd() {
  var id = D.d.id;
  if (S.dialogs[id] == null || D.pts > S.dialogs[id]) S.dialogs[id] = D.pts;
  if (S.days.indexOf(today()) < 0) S.days.push(today());
  var nb = checkBadges(); save();
  var msg = D.pts >= 25 ? "Условия на одной странице, собеседник услышан. Отличный разговор." : D.pts >= 15 ? "Разговор идёт, но часть приёмов упущена. Сыграй ещё раз." : "Разговор завис или испортился. Посмотри карточки приёмов и сыграй ещё.";
  var h = topbar(true, "Итог разговора") + '<header class="hero"><div class="hero-t">' + D.pts + ' из 30</div><div class="hero-s">' + msg + '</div></header>';
  if (nb.length) h += '<div class="note">🎉 Новая награда: ' + nb.map(esc).join(", ") + '</div>';
  var keys = {}; D.hist.forEach(function (x) { if (x.v !== "b") x.g.forEach(function (k) { keys[k] = 1; }); });
  if (Object.keys(keys).length) h += '<div class="box"><div class="lab">Повтори приёмы</div><div class="tags">' + tagChips(Object.keys(keys)) + '</div></div>';
  h += '<div class="menu"><button class="big primary" data-act="dlg" data-id="' + id + '">Сыграть ещё</button><button class="big" data-act="dialogs">Другие разговоры</button></div>';
  setView(h);
}

// ---------- приёмы, журнал, о тренажёре ----------
function cardHTML(k) {
  var c = CARDS[k], b = BOOKS[c.b];
  return '<div class="card" style="--bc:' + b.c + '"><div class="card-h">' + b.e + ' ' + esc(c.n) + '<small>' + esc(b.n) + '</small></div>' +
    '<p>' + esc(c.s) + '</p><p class="ex"><b>Пример:</b> ' + esc(c.e) + '</p>' + (c.no ? '<p class="no"><b>Не применять / осторожно:</b> ' + esc(c.no) + '</p>' : '') + '</div>';
}
function renderCards(filter) {
  view = "cards";
  var h = topbar(true, "Приёмы") + '<div class="hint pad">Нажми книгу, чтобы отфильтровать. Всё из твоих книг; «Общее» — наши правила, не из книг.</div><div class="tags pad">';
  ["all", "voss", "weiss", "klaff", "mom", "hall", "gen"].forEach(function (b) { h += '<button class="tag' + (filter === b || (!filter && b === "all") ? ' on' : '') + '" data-act="cardf" data-b="' + b + '">' + (b === "all" ? "Все" : esc(BOOKS[b].s)) + '</button>'; });
  h += '</div><div class="cards">';
  Object.keys(CARDS).forEach(function (k) { if (!filter || filter === "all" || CARDS[k].b === filter) h += cardHTML(k); });
  h += '</div>';
  setView(h);
}
function showCardModal(k) {
  var m = document.getElementById("modal");
  m.innerHTML = '<div class="mwrap"><div class="mcard">' + cardHTML(k) + '<button class="primary" data-act="mclose">Закрыть</button></div></div>';
  m.style.display = "block";
}
function renderJournal() {
  view = "journal";
  var n = S.answers.length;
  var h = topbar(true, "Журнал");
  h += '<div class="stats"><div class="stat"><b>' + n + '</b><span>ответов</span></div><div class="stat"><b>' + S.rounds + '</b><span>раундов</span></div><div class="stat"><b>' + S.bans + '</b><span>запрещённых ходов</span></div></div>';
  h += '<div class="box"><div class="lab">Сохранение</div><div class="hint">Очки и ответы лежат в этом браузере. Если сменишь телефон или очистишь историю — потеряются. Скачай файл и держи копию.</div>' +
    '<div class="row"><button class="primary" data-act="exp-json">⬇ Скачать сохранение</button><button class="ghost" data-act="exp-txt">⬇ Мои ответы (текст)</button></div>' +
    '<div class="row"><label class="ghost file">⬆ Загрузить сохранение<input type="file" id="imp" accept=".json,application/json"></label>' +
    '<button class="ghost danger" data-act="reset">Сбросить всё</button></div><div id="msg" class="hint"></div></div>';
  h += '<div class="sec-t">Последние ответы</div>';
  var rec = S.answers.slice(-30).reverse();
  if (!rec.length) h += '<div class="hint pad">Пока пусто — сыграй раунд.</div>';
  rec.forEach(function (a) {
    var sc = byId(a.id), d = new Date(a.ts);
    h += '<div class="jr ' + VERD[a.v].c + '"><div class="jr-h">' + d.toLocaleDateString("ru-RU") + ' · ' + esc(sc ? sc.who : a.id) + ': «' + esc(sc ? sc.line.slice(0, 50) : '') + '»</div>' +
      (a.own ? '<div class="mine">Моя запись: ' + esc(a.own) + '</div>' : '') + '<div class="jr-p">' + VERD[a.v].l + ' — ' + esc(a.pick) + '</div></div>';
  });
  setView(h);
}
function download(name, text, mime) {
  var blob = new Blob([text], { type: mime }), url = URL.createObjectURL(blob);
  var a = document.createElement("a"); a.href = url; a.download = name; document.body.appendChild(a); a.click();
  setTimeout(function () { document.body.removeChild(a); URL.revokeObjectURL(url); }, 500);
}
function exportTxt() {
  var lines = ["Тренажёр переговоров — мои ответы", "Очки: " + S.pts, ""];
  S.answers.forEach(function (a) { var sc = byId(a.id); lines.push(new Date(a.ts).toLocaleString("ru-RU") + " · " + (sc ? sc.who + ": " + sc.line : a.id)); if (a.own) lines.push("  Моя запись: " + a.own); lines.push("  Выбор (" + VERD[a.v].l + "): " + a.pick); lines.push(""); });
  download("moi_otvety_trenazher.txt", lines.join("\n"), "text/plain");
}
function renderAbout() {
  view = "about";
  var h = topbar(true, "Как это работает");
  h += '<div class="box about"><p><b>Идея.</b> Ты не читаешь про приёмы — ты их применяешь. Так запоминается лучше (скилл kak-uchitsya: сначала вспоминай сама, потом сверяйся).</p>' +
    '<p><b>Шаг 1.</b> Пишешь свой ответ до подсказок. <b>Шаг 2.</b> Выбираешь ход. <b>Шаг 3.</b> Видишь, какой это приём из какой книги, что хорошо, что запрещено и пример лучше.</p>' +
    '<p><b>Повторения.</b> Правильно — карточка уходит в следующую коробку и вернётся позже (через 1, 3, 7, 14, 30 дней). Неправильно — вернётся сразу. Это «интервальные повторения».</p>' +
    '<p><b>Перемешивание.</b> Книги в раунде идут вперемешку: так учишься выбирать приём, а не просто повторять один.</p>' +
    '<p><b>Три правила.</b> 1) Если не хватает данных — сначала один вопрос. 2) Без блефа, давления и лжи — они дают ⛔. 3) Цифры за тебя не придумываю: «__» — твоя настоящая.</p>' +
    '<p><b>Голос и чат.</b> Зеркало, пауза, звонок через сутки — приёмы для голоса. В чате они работают иначе: смотри пометку 🎙.</p>' +
    '<p><b>Книги.</b> Восс, Вайс, Клафф, «Тест мамы», Холл (НЛП). Холл — слабая научная база: это инструмент самонаблюдения. Ситуации придуманы для тренировки, это не твои настоящие переписки.</p>' +
    '<p><b>Защита.</b> Ты узнаёшь и манипулятивные приёмы, чтобы не попасть в них, а не чтобы применять.</p></div>';
  setView(h);
}

// ---------- события ----------
document.addEventListener("click", function (ev) {
  var t = ev.target.closest("[data-act]"); if (!t) return;
  var a = t.getAttribute("data-act");
  if (a === "home") { document.getElementById("modal").style.display = "none"; renderHome(); }
  else if (a === "round") startRound(t.getAttribute("data-mode"), t.getAttribute("data-book"));
  else if (a === "toopts") { var ta = document.getElementById("own"); R.own = ta ? ta.value.trim() : ""; renderPlay("opts"); }
  else if (a === "skipown") { R.own = ""; renderPlay("opts"); }
  else if (a === "pick") renderReveal(parseInt(t.getAttribute("data-i"), 10));
  else if (a === "next") { R.i++; R.own = ""; R.order = null; if (R.i >= R.list.length) renderEnd(); else renderPlay("own"); }
  else if (a === "dialogs") renderDialogs();
  else if (a === "dlg") startDialog(t.getAttribute("data-id"));
  else if (a === "dpick") dialogPick(parseInt(t.getAttribute("data-i"), 10));
  else if (a === "dnext") { D.i++; D.order = null; if (D.i >= D.d.turns.length) dialogEnd(); else renderDialogTurn(); }
  else if (a === "cards") renderCards("all");
  else if (a === "cardf") renderCards(t.getAttribute("data-b"));
  else if (a === "card") showCardModal(t.getAttribute("data-k"));
  else if (a === "mclose") document.getElementById("modal").style.display = "none";
  else if (a === "journal") renderJournal();
  else if (a === "about") renderAbout();
  else if (a === "exp-json") download("trenazher_sohranenie.json", JSON.stringify(S, null, 1), "application/json");
  else if (a === "exp-txt") exportTxt();
  else if (a === "reset") {
    if (t.getAttribute("data-sure")) { S = blank(); save(); renderJournal(); }
    else { t.setAttribute("data-sure", "1"); t.textContent = "Точно сбросить? Нажми ещё раз"; }
  }
});
document.addEventListener("change", function (ev) {
  if (ev.target && ev.target.id === "imp") {
    var f = ev.target.files[0]; if (!f) return;
    var fr = new FileReader();
    fr.onload = function () {
      var m = document.getElementById("msg");
      try { var o = JSON.parse(fr.result); if (!o || typeof o.pts !== "number" || !o.cards) throw 0; S = Object.assign(blank(), o); save(); renderJournal(); document.getElementById("msg").textContent = "Сохранение загружено."; }
      catch (e) { if (m) m.textContent = "Это не файл сохранения тренажёра."; }
    };
    fr.readAsText(f);
  }
});
renderHome();
