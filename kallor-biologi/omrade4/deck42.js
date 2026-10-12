const { build } = require("./mkpptx.js");
build({
  out: "/tmp/bio/out/biologi-4-2-materiens-kretslopp.pptx",
  title: "Materiens kretslopp", kicker: "BIOLOGI · KAPITEL 4 · EKOLOGI", sub: "Delområde 4.2: materia, kolets kretslopp och nedbrytning",
  lessons: "Materia tillverkas inte och försvinner inte · Kolets kretslopp · Nedbrytning · Labb 4.2 Nedbrytning i jord",
  foot: "Biologi · Kapitel 4 · Delområde 4.2 Materiens kretslopp",
  titleNotes: "Presentationen följer grundtexten i kapitel 4, delområde 4.2. Några bilder per moment. Anteckningarna innehåller handledning.",
  async slides(h) {
    const A = "Materia tillverkas inte och försvinner inte";
    h.section(A, "Energi flödar, materia går runt", "Fråga: kan en atom i din kropp ha suttit i en växt? I ett djur? I havet?");
    h.table(A, "Energi och materia", ["", "Energi", "Materia"], [["Vägen", "Flödar genom ekosystemet", "Går runt i ett kretslopp"], ["Behövs nytt?", "Ja, solen ger ny energi", "Nej, atomerna byter plats"], ["Exempel", "Solljus → växt → hare → värme", "Kol: luft → växt → hare → nedbrytare → luft"]], { colW: [2.6, 4.7, 4.83], fs: 20, rowH: 0.9, note: "Energi flödar. Materia går i kretslopp.", notes: "Skillnaden mellan flöde och kretslopp är kärnan i hela delområdet." });
    h.stat(A, "Van Helmonts pilträd", "5 → 169", "pund på fem år. Jorden blev bara cirka 2 uns lättare.", ["Van Helmont trodde att vikten kom från vattnet.", "Vi vet att den mest kommer från koldioxid i luften.", "Växten är mest byggd av luft och vatten.", "Vanligt fel: ”växter blir stora av jord”."], { notes: "Siffrorna enligt Van Helmonts egen skildring. Ett bra exempel på en undersökning med kontroll som ändå gav delvis fel slutsats." });
    h.cards(A, "Vattnets kretslopp", [["Avdunstning", "Solen värmer havet och vattnet avdunstar."], ["Kondensation", "Ångan svalnar och bildar moln."], ["Nederbörd", "Vattnet faller och rinner till sjöar och hav."]], { h: 3.2, note: "Växter tar upp vatten med rötterna och avger vattenånga genom bladen.", notes: "Be eleverna beskriva kretsloppet med egna ord." });
    h.kolla(A, "Kolla dig själv", ["Vad är skillnaden mellan hur energi och materia rör sig?", "Varifrån kom nästan all vikt i van Helmonts pilträd?", "Beskriv vattnets kretslopp i tre steg."]);

    const B = "Kolets kretslopp";
    h.section(B, "Kolet går runt", "Koppla till område 5 (klimat): förbränning släpper ut kol som legat lagrat i miljontals år.");
    await h.imgText(B, "Så går kolet runt", ["Fotosyntes tar koldioxid från luften.", "Näringskedjan för kolet vidare.", "Cellandning släpper ut koldioxid.", "Nedbrytning frigör koldioxid och näring.", "Förbränning släpper ut lagrat kol."], "ekologi-kol.png", { iw: 6.4, imgLeft: false, fs: 22, notes: "Låt eleverna följa en kolatom från luften via en växt och en hare tillbaka till luften." });
    h.kolla(B, "Kolla dig själv", ["Beskriv två processer som tar kol från luften och två som släpper ut kol.", "Vad händer med kolet i ett träd som dör i skogen?", "Varför kallas det ett kretslopp och inte ett flöde?"]);

    const C = "Nedbrytning";
    h.section(C, "De tysta arbetarna", "Utan nedbrytning skulle döda löv och djur ligga kvar för alltid.");
    h.cards(C, "Vem bryter ner?", [["Detritusätare", "Daggmaskar, gråsuggor och hoppstjärtar hackar sönder döda växtdelar."], ["Nedbrytare", "Svampar och bakterier gör cellandning på det döda och frigör koldioxid och näring."], ["Förna", "Döda löv och barr som ligger på marken."]], { h: 3.6, note: "Näringen tas upp av växterna igen.", notes: "En kompost kan bli över 50 grader, värmen kommer från nedbrytarnas cellandning." });
    h.table(C, "Vad påverkar hastigheten?", ["Faktor", "Effekt", "Exempel"], [["Temperatur", "Varmt går fortare", "Södra Sverige mot Norrbotten"], ["Fukt", "Behövs, men inte för mycket", "Torr förna ligger kvar länge"], ["Syre", "De flesta nedbrytare behöver syre", "Syrefri botten: långsamt"], ["Material", "Mjuka löv går fortare än trä", "Björklöv mot grenvirke"]], { colW: [2.6, 4.7, 4.83], fs: 20, rowH: 0.8, note: "Regnskogen: snabb nedbrytning, näringsfattig jord.", notes: "Förklara varför regnskogens jord är näringsfattig trots rik växtlighet." });
    h.kolla(C, "Kolla dig själv", ["Varför är nedbrytare viktiga för kretsloppet?", "Ge två faktorer som påverkar nedbrytningens hastighet.", "Varför är jorden i en regnskog ofta näringsfattig?"]);

    const D = "Labb 4.2 Nedbrytning i jord";
    h.section(D, "Gräv ner tepåsar", "Material: tepåsar, våg, spade, tre jordar. Förväntat: mest viktförlust i fuktig skogsjord, minst i sand.");
    await h.imgText(D, "Så gör ni", ["Märk och väg tepåsarna.", "Gräv ner tre i varje jord, 8 cm djupt.", "Gräv upp, torka och väg igen.", "Räkna ut förlusten i procent."], "ekologi-tepasar.png", { iw: 6.4, imgLeft: false, fs: 22, notes: "Oberoende variabel: typ av jord. Beroende: viktförlust. Lika: sort te, djup, tid. Samla in alla påsar." });
  }
}).catch(e => { console.error(e); process.exit(1); });
