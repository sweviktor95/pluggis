// Flashcards som eget moment efter "Testa dig själv" (biologi och kemi, kapitel 1–4).
// Korten byggs av begreppen och sammanfattningen i kapitlets moment "Sammanfattning och begrepp".
(function () {
  if (typeof innehall === "undefined") { return; }
  ["biologi", "kemi"].forEach(function (amne) {
    for (var n = 1; n <= 4; n++) {
      var s = innehall[amne + "-m-" + n + "-s"];
      if (!s || !s.nivaer) { continue; }
      var f = { nivaer: {}, nivaStandard: s.nivaStandard || "vanlig" };
      Object.keys(s.nivaer).forEach(function (k) { f.nivaer[k] = { sektioner: [], flash: s.nivaer[k] }; });
      innehall[amne + "-m-" + n + "-f"] = f;
    }
  });
})();
