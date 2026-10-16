const { build } = require("./mkpptx.js");
build({
  out: "/tmp/kem/out/kemi-1-2-modeller-kallor-argument.pptx",
  title: "Modeller, källor och argument", kicker: "KEMI · KAPITEL 1 · KEMI SOM VETENSKAP", sub: "Delområde 1.2: modeller, kemins historia, källkritik och fläckborttagaren",
  lessons: "Vad är en modell? · Hur kemin vuxit fram · Granska påståenden · Labb 1.2",
  foot: "Kemi · Kapitel 1 · Delområde 1.2 Modeller, källor och argument",
  titleNotes: "Presentationen följer grundtexten i kapitel 1, delområde 1.2. Några bilder per moment. Anteckningarna innehåller handledning. Allt material är utkast (beta).",
  async slides(h) {
    const A = "Vad är en modell i kemi?", B = "Hur kemin vuxit fram", Cc = "Granska kemipåståenden", D = "Labb 1.2 Fungerar fläckborttagaren?";
    h.section(A, "Modeller förenklar", "Partikelmodellen behandlas utförligt i kapitel 2. Här används den som exempel.");
    await h.imgText(A, "Partikelmodellen", ["Fast: partiklarna sitter på fasta platser.", "Flytande: tätt men de glider förbi varandra.", "Gas: stora avstånd, rör sig fritt.", "Partiklarna är i verkligheten mycket mindre än i bilden."], "l_modell.png", { iw: 7.7, imgLeft: false, fs: 20, notes: "Vanligt fel: att modellen är en bild av hur det egentligen ser ut." });
    h.cards(A, "Vad gör en modell?", [["Förklarar", "Varför löser tabletten sig fortare i varmt vatten?"], ["Förutsäger", "Gas kan pressas ihop eftersom avstånden är stora."], ["Har gränser", "Säger inget om ämnets färg."]], { h: 3.4, note: "En modell är en förenkling, inte verkligheten.", notes: "Jämför med en karta: den visar vissa saker, inte allt." });
    h.kolla(A, "Kolla dig själv", ["Vad är en modell i kemi?", "Varför är en modell inte samma sak som verkligheten?", "Vad händer med en modell när nya undersökningar visar något nytt?"]);

    h.section(B, "Från fyra element till atomer", "Årtalen för Empedokles och Aristoteles är runda uppskattningar. Boyle 1661, Lavoisier 1789 och Dalton 1808 är kontrollerade mot öppna källor.");
    await h.imgText(B, "Fem steg", ["Empedokles och Aristoteles: fyra element.", "Boyle 1661: tvivlar och vill ha försök.", "Lavoisier 1789: massan bevaras.", "Dalton 1808: atomteori."], "v_tidslinje.png", { iw: 7.7, imgLeft: false, fs: 20, notes: "Läran om fyra element var inflytelserik i cirka 2 000 år (LibreTexts)." });
    await h.imgText(B, "Lavoisier: massan bevaras", ["En sluten flaska med tablett och vatten.", "Före och efter reaktionen: samma massa.", "Gasen blir kvar i flaskan.", "Ingenting försvinner, ämnena ändrar bara form."], "v_massa.png", { iw: 7.7, imgLeft: false, fs: 20, notes: "Praktiskt: tablett och vatten ska vara åtskilda före (t.ex. i en liten kapsel), annars börjar reaktionen innan flaskan är stängd." });
    await h.imgText(B, "Dalton: atomteorin", ["Allt består av atomer.", "Atomer av samma grundämne är lika.", "Föreningar bildas i enkla förhållanden.", "Atomer skapas inte och försvinner inte i en reaktion."], "v_dalton.png", { iw: 7.7, imgLeft: false, fs: 20, notes: "Idag vet vi att atomer har delar (elektronen upptäcktes 1897) och att atomer av samma ämne kan väga olika (isotoper). Det tas upp i fördjupningen." });
    h.kolla(B, "Kolla dig själv", ["Vad ansåg Empedokles och Aristoteles?", "Vad gjorde Boyle annorlunda?", "Vad visade Lavoisier?", "Vad säger Daltons atomteori?", "Varför är det en styrka att modeller kan ändras?"]);

    h.section(Cc, "Granska påståenden", "Be eleverna återvända till sina gissningar om kemikalier från början av kapitlet.");
    h.steps(Cc, "Fem frågor", ["Vem säger det?", "Varför säger de det? Vill de sälja?", "Vilka belägg finns?", "Hur gammal är informationen?", "Vad säger andra källor?"], { notes: "Källkritik är ett verktyg, inte ett facit." });
    h.table(Cc, "Ord att granska", ["Påstående", "Problem"], [["Kemikaliefritt", "Allt består av kemikalier. Ordet säger inget om faran."], ["100 % naturligt", "Naturliga ämnen kan vara giftiga, till exempel i flugsvamp."], ["9 av 10 var nöjda", "Nöjda jämfört med vad? Hur många? Vem frågade?"]], { colW: [4.2, 7.93], fs: 22, rowH: 0.95, note: "Källa: Svenska Kemisamfundet (Tumregler). Flugsvamp som giftig är allmänt faktum, inte kontrollerat.", notes: "Svenska Kemisamfundet råder att inte använda ordet kemikalier som samlingsord för sådant som är giftigt." });
    h.kolla(Cc, "Kolla dig själv", ["Vilka frågor ställer du för att granska ett påstående?", "Varför är ”kemikaliefri” missvisande?", "Är allt naturligt ofarligt?", "Varför räcker inte en reklam som källa?"]);

    h.section(D, "Labb 1.2: fungerar fläckborttagaren?", "Material: vit bomull, te eller kaffe, glas, vatten, diskmedel, tvättmedel, fläckborttagare, skyddsglasögon, handskar. Förbered fläckarna så att de hinner torka. Blanda aldrig produkter.");
    await h.imgText(D, "Fyra vätskor, lika fläck", ["A: bara vatten (jämförelse).", "B: diskmedel.", "C: fläckborttagare X (påhittad produkt).", "D: tvättmedel."], "v_flack.png", { iw: 7.7, imgLeft: false, fs: 20, notes: "Poängskala 0–3. En kamrat som inte vet vilken som är vilken sätter poäng." });
    h.table(D, "Planera rättvist", ["Vad", "Hur"], [["Ändrar", "Vätskan"], ["Mäter", "Hur ljus fläcken blir (poäng 0–3)"], ["Håller lika", "Tyg, fläck, mängd vätska, tid och sätt att skölja"], ["Opartisk bedömning", "Kamrat som inte vet vilken som är vilken"]], { colW: [4.0, 8.13], fs: 22, rowH: 0.85, note: "Vad kan testet inte säga? Andra fläckar och tyger är inte testade.", notes: "Diskutera slutsatsens räckvidd." });
  }
}).catch(e => { console.error(e); process.exit(1); });
