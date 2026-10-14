const { build } = require("./mkpptx.js");
build({
  out: "/tmp/bio/out/biologi-2-2-fotosyntes-och-cellandning.pptx",
  title: "Fotosyntes och cellandning", kicker: "BIOLOGI · KAPITEL 2 · CELLEN OCH LIVETS PROCESSER", sub: "Delområde 2.2: växten som producent, cellandning, jäsning och hur processerna hör ihop",
  lessons: "Växten som producent · Cellandning · Processerna tillsammans · Labb 2.2",
  foot: "Biologi · Kapitel 2 · Delområde 2.2 Fotosyntes och cellandning",
  titleNotes: "Presentationen följer grundtexten i kapitel 2, delområde 2.2.",
  async slides(h) {
    const A = "Växten som producent";
    h.section(A, "Växter gör sin egen mat", "Fråga: Var kommer en tallens vikt ifrån? Jord, vatten eller luft? Samla gissningar innan ni går vidare.");
    h.cards(A, "In och ut", [["In", "Koldioxid från luften, vatten från jorden och ljusenergi från solen."], ["Ut", "Glukos (druvsocker) och syre."]], { h: 3.4, note: "koldioxid + vatten + ljus → glukos + syre", notes: "Reaktionsformeln: 6 CO₂ + 6 H₂O + ljus → C₆H₁₂O₆ + 6 O₂. Atomerna byter plats men försvinner inte." });
    await h.imgText(A, "Var och hur?", ["Sker i kloroplasterna.", "Klorofyll fångar ljuset.", "Ljusenergin lagras i glukosen.", "Glukos: energi, byggmaterial (cellulosa) eller lager (stärkelse)."], "cellen-fotosyntes.png", { iw: 5.4, imgLeft: false, fs: 22, notes: "Bilden visar både fotosyntes och cellandning. Vi återvänder till den i nästa moment." });
    h.kolla(A, "Kolla dig själv", ["Vilka ämnen behöver växten, och vad bildas?", "Var i cellen sker fotosyntesen, och vilket ämne fångar ljuset?", "Varför kallas växter producenter?", "Vad kan växten göra med glukosen?"]);

    const B = "Cellandning";
    h.section(B, "Energi ur glukos", "Vanligt fel: att cellandning är samma sak som att andas med lungorna.");
    h.stat(B, "Cellandning", "alla", "levande celler gör cellandning, dag och natt", ["glukos + syre → koldioxid + vatten + energi", "Sker i mitokondrierna.", "Energin används, och en del blir värme.", "Skilj från andning med lungorna."], { notes: "Lungorna tar in syre och släpper ut koldioxid. I cellerna används syret och koldioxiden bildas." });
    h.cards(B, "Utan syre: jäsning", [["Jäst", "Koldioxid och alkohol. Får bröd att jäsa."], ["Mycket mindre energi", "Glukosen bryts ner bara delvis."]], { h: 3.2, note: "Labb 2.2 mäter jästens koldioxid.", notes: "Fördjupning: mjölksyrajäsning (muskler, filmjölk), 2 mot ca 30 ATP." });
    h.kolla(B, "Kolla dig själv", ["Skriv cellandningen med ord.", "Var i cellen sker den?", "Vad är skillnaden mellan cellandning och andning med lungorna?", "Vart tar energin vägen när cellen använder den?"]);

    const C = "Processerna tillsammans";
    h.section(C, "Varandras motsatser", "Vanligt fel: växter andas bara på natten. De gör cellandning hela tiden.");
    h.table(C, "Jämförelse", ["", "Fotosyntes", "Cellandning"], [["In", "koldioxid, vatten, ljus", "glukos, syre"], ["Ut", "glukos, syre", "koldioxid, vatten"], ["Energi", "ljusenergi lagras", "energi frigörs"], ["Var", "kloroplaster", "mitokondrier"], ["När", "bara i ljus", "dag och natt"]], { colW: [2.4, 4.9, 4.83], fs: 22, rowH: 0.7, note: "Kol går i kretslopp. Energi gör det inte.", noteY: 6.0 });
    await h.imgText(C, "Dag och natt", ["Dagtid: både fotosyntes och cellandning.", "Oftast mer fotosyntes: syre släpps ut.", "Natt: bara cellandning.", "Då tar växten upp syre och släpper ut koldioxid."], "dagnatt.png", { iw: 6.4, imgLeft: false, fs: 22 });
    h.kolla(C, "Kolla dig själv", ["Hur är processerna varandras motsatser?", "Gör växter cellandning? När?", "Varför går kol i kretslopp men inte energi?", "Varför växer inte en växt som står i mörker?"]);

    const D = "Labb 2.2 Jäst och koldioxid";
    h.section(D, "Temperatur och jäst", "Material: fyra 0,5 l flaskor med ballonger, jäst, socker, termometer, måttband. Resultaten varierar. Ofta mest gas vid ca 35 °C.");
    h.steps(D, "Så gör ni", ["Fyra vattenbad: ca 5, 20, 35 och 50 °C.", "1 tsk jäst, 1 tsk socker och 1 dl ljummet vatten i varje flaska.", "Ballong på varje flaska. Ställ flaskorna i baden.", "Mät omkretsen efter 5, 10 och 15 minuter.", "Rita diagram: temperatur mot omkrets efter 15 minuter."], { notes: "Lika: mängd jäst, socker och vatten, flaskstorlek och tid. Kontrollförsök utan jäst visar att det är jästen som bildar gasen." });
  }
}).catch(e => { console.error(e); process.exit(1); });
