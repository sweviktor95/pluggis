// Slår på flashcard-övning i repetitionsmomenten ("Sammanfattning och begrepp") för biologi och kemi, kapitel 1–4.
(function () {
  if (typeof innehall === "undefined") { return; }
  ["biologi", "kemi"].forEach(function (amne) {
    for (var n = 1; n <= 4; n++) {
      var d = innehall[amne + "-m-" + n + "-s"];
      if (!d || !d.nivaer) { continue; }
      Object.keys(d.nivaer).forEach(function (k) { d.nivaer[k].flash = true; });
    }
  });
})();
