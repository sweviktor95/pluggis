const { build } = require("./mkpptx.js");
build({
  out: "/tmp/bio/out/biologi-2-1-cellen.pptx",
  title: "Cellen", kicker: "BIOLOGI · KAPITEL 2 · CELLEN OCH LIVETS PROCESSER", sub: "Delområde 2.1: kännetecken på liv, cellteorin, mikroskopet, djur- och växtceller och bakterier",
  lessons: "Start: Vad är liv? · Cellteorin och mikroskopet · Djurcell och växtcell · Bakterier och encelliga organismer · Labb 2.1",
  foot: "Biologi · Kapitel 2 · Delområde 2.1 Cellen",
  titleNotes: "Presentationen följer grundtexten i kapitel 2, delområde 2.1. Några bilder per moment. Anteckningarna innehåller handledning.",
  async slides(h) {
    const A = "Vad är liv?";
    h.section(A, "Start: kännetecken på liv", "Fråga: Är en eld levande? Den växer och förbrukar bränsle. Vilka kännetecken saknas?");
    h.cards(A, "Fem kännetecken", [["Celler", "Allt levande är uppbyggt av celler."], ["Energi", "Tar upp energi och ämnen och omvandlar dem."], ["Växer och förökar sig", "Utvecklas och för vidare sitt DNA."], ["Reagerar", "Svarar på ljus, värme eller beröring."]], { h: 3.4, note: "Allt utgår från en sak: cellen.", notes: "Be eleverna testa bilen, elden och en gran mot listan. Virus är ett gränsfall: de behöver en värdcell." });
    await h.imgText(A, "Från cell till organism", ["Cellen är minsta levande enheten.", "Encellig: en enda cell, till exempel en bakterie.", "Flercellig: miljarder celler som samarbetar.", "Vi återvänder till bilden i 2.3."], "cellen-nivaer.png", { iw: 6.4, imgLeft: false, fs: 22, notes: "Virus räknas oftast inte som levande: de är inte celler och kan inte föröka sig utan en värdcell." });
    h.kolla(A, "Kolla dig själv: Start", ["Nämn tre kännetecken på liv.", "Vilken är den minsta enhet som är levande?", "Varför räknas virus oftast inte som levande?"]);

    const B = "Cellteorin och mikroskopet";
    h.section(B, "Hooke såg celler i kork", "Hooke såg bara tomma väggar eftersom korkcellerna var döda. Han kallade rummen cells.");
    await h.imgText(B, "Hooke och korken, 1665", ["Hooke tittade på kork i ett mikroskop.", "Han såg små kammare som vaxkakor.", "Han kallade dem celler.", "Det var döda celler: bara väggarna syntes."], "kork.png", { iw: 6.4, imgLeft: false, fs: 22, notes: "Bilden är en förenklad återgivning." });
    h.cards(B, "Cellteorin", [["Alla organismer består av celler", "Från bakterier till blåvalar."], ["Cellen är minsta levande enheten", "Delar av en cell kan inte leva själva."], ["Celler kommer från celler", "Nya celler bildas när en cell delar sig."]], { h: 3.4, note: "Schleiden och Schwann på 1830-talet, Virchow på 1850-talet.", notes: "Skolboken anger årtalen 1838, 1839 och 1855. Källan vi kontrollerade anger bara början av 1800-talet och omkring 1850." });
    h.stat(B, "Förstoring", "400×", "okular 10× · objektiv 40×", ["Förstoring = okularets × objektivets förstoring.", "Ljusmikroskop: upp till ungefär 1 000 gånger.", "Virus syns bara i elektronmikroskop."], { notes: "Låt eleverna räkna: okular 10×, objektiv 10× och 40×. Hur många gånger ökar förstoringen?" });
    h.kolla(B, "Kolla dig själv", ["Vad såg Hooke, och vad kallade han det?", "Vad säger cellteorin?", "Beräkna förstoringen med okular 10× och objektiv 40×.", "Varför ser man inte virus i ett ljusmikroskop?"]);

    const C = "Djurcell och växtcell";
    h.section(C, "Organeller: cellens små organ", "Rita en växtcell och en djurcell på tavlan tillsammans. Vanligt fel: att växtceller saknar mitokondrier.");
    await h.imgText(C, "Djurcell", ["Cellmembran, cytoplasma, cellkärna.", "Ribosomer bygger proteiner.", "Mitokondrier gör cellandning.", "Små vakuoler."], "cellen-djurcell.png", { iw: 6.4, imgLeft: false, fs: 22, notes: "Färgerna är påhittade för att delarna ska kunna skiljas åt." });
    await h.imgText(C, "Växtcell", ["Har allt djurcellen har.", "Dessutom: cellvägg, kloroplaster och en stor vakuol.", "Mitokondrier finns också här.", "Alla växtceller har inte kloroplaster. Rötter saknar dem."], "cellen-vaxtcell.png", { iw: 6.4, imgLeft: false, fs: 22, notes: "Alla celler behöver energi, även de som gör fotosyntes." });
    h.table(C, "Jämförelse", ["Del", "Djurcell", "Växtcell"], [["Cellvägg", "–", "✔"], ["Kloroplaster", "–", "✔ (i gröna delar)"], ["Stor vakuol", "små", "✔"], ["Mitokondrier", "✔", "✔"], ["Cellkärna", "✔", "✔"]], { colW: [4.1, 4.0, 4.03], fs: 22, rowH: 0.7, note: "Alla celler har cellmembran, cytoplasma, DNA och ribosomer.", noteY: 6.0 });
    h.kolla(C, "Kolla dig själv", ["Vilka tre delar har växtceller men inte djurceller?", "Varför har även växtceller mitokondrier?", "Vad är skillnaden mellan cellvägg och cellmembran?", "Varför saknar en rotcell kloroplaster?"]);

    const D = "Bakterier och encelliga organismer";
    h.section(D, "Celler utan cellkärna", "Många encelliga organismer är inte bakterier: amöbor, encelliga alger och jäst har cellkärna.");
    await h.imgText(D, "Bakteriecellen", ["DNA ligger fritt i cytoplasman.", "Ingen cellkärna.", "Mycket liten: ca 0,001–0,005 mm.", "Många har cellvägg och spröt (flageller)."], "cellen-bakterie.png", { iw: 6.4, imgLeft: false, fs: 22 });
    h.cards(D, "Bakterier och virus", [["Bakterier", "Celler. De flesta är ofarliga eller nyttiga. Kan ibland behandlas med antibiotika."], ["Virus", "Inte celler. Behöver en värdcell. Antibiotika hjälper inte."]], { h: 3.4, note: "Halsfluss orsakad av bakterier: antibiotika. Förkylning: virus, ingen effekt.", notes: "Fördjupning: mitokondrier och kloroplaster liknar bakterier, vilket ligger bakom endosymbiosteorin." });
    h.kolla(D, "Kolla dig själv", ["Vad är den viktigaste skillnaden mellan bakteriecell och djurcell?", "Varför hjälper antibiotika mot bakteriell halsfluss men inte mot en förkylning?", "Nämn två encelliga organismer som inte är bakterier."]);

    const E = "Labb 2.1 Mikroskopera celler";
    h.section(E, "Lök och jod", "Material: mikroskop, objektglas, täckglas, pincett, pipett, jodlösning, lökbit. Läraren skär. Vanligt fel: preparatet veckas eller har luftbubblor.");
    h.steps(E, "Så gör ni", ["Dra loss ett tunt skinn från insidan av ett lökblad.", "Lägg skinnet plant på objektglaset. Droppa jod.", "Sänk täckglaset långsamt så att inga bubblor fastnar.", "Titta först med lägsta förstoring, sedan högre.", "Rita en cell, märk ut delarna och räkna ut förstoringen."], { notes: "Förväntat: rektangulära celler med tydlig cellvägg och en brunfärgad cellkärna. Inga kloroplaster eftersom löken växer under jord." });
  }
}).catch(e => { console.error(e); process.exit(1); });
