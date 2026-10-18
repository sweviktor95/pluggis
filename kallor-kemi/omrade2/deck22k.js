const { build } = require("./mkpptx.js");
build({
  out: "/tmp/kem/out/kemi-2-2-separation-och-analys.pptx",
  title: "Separations- och analysmetoder", kicker: "KEMI · KAPITEL 2 · MATERIA OCH PARTIKLAR", sub: "Delområde 2.2: filtrering, avdunstning, destillation, kromatografi, fällning, labb om att separera sand, salt och vatten",
  lessons: "Filtrering och avdunstning · Destillation och kromatografi · Identifiera ämnen och fällning · Labb 2.2",
  foot: "Kemi · Kapitel 2 · Delområde 2.2 Separations- och analysmetoder",
  titleNotes: "Presentationen följer grundtexten i kapitel 2, delområde 2.2. Anteckningarna innehåller handledning. Allt material är utkast (beta).",
  async slides(h) {
    const A = "Filtrering, avdunstning och sedimentering", B = "Destillation och kromatografi", Cc = "Identifiera ämnen och fällning", D = "Labb 2.2 Separera sand, salt och vatten";
    h.section(A, "Skilja ämnen åt", "Fråga: hur skulle ni få bort sand ur vatten? Och salt ur saltvatten?");
    await h.imgText(A, "Filtrering", ["Skiljer fasta partiklar från vätska.", "Sanden stannar i filtret, vattnet går igenom.", "Löst salt går igenom, partiklarna är för små.", "Filtratet är det som rinner igenom."], "v_filtrering.png", { iw: 7.0, imgLeft: false, fs: 21, notes: "Visa gärna med riktigt kaffefilter." });
    h.cards(A, "Avdunstning och sedimentering", [["Avdunstning", "Vätskan förångas, det lösta ämnet blir kvar. Så får man salt ur saltvatten."], ["Sedimentering", "Tunga partiklar sjunker till botten när blandningen får stå."], ["Dekantering", "Man häller försiktigt av vätskan ovanför."]], { h: 3.2, note: "Metoderna kan kombineras." });
    h.kolla(A, "Kolla dig själv", ["Vilken metod skiljer sand från vatten?", "Hur får du tillbaka salt ur saltvatten?", "Varför går inte löst salt att filtrera bort?"]);

    h.section(B, "Destillation och kromatografi", "Fråga: hur kan man få dricksvatten ur havsvatten?");
    await h.imgText(B, "Destillation", ["Bygger på att ämnen har olika kokpunkter.", "Vätskan som kokar först förångas.", "Ångan kyls och kondenseras igen.", "Vatten ur saltvatten: saltet blir kvar."], "v_destillation.png", { iw: 7.4, imgLeft: false, fs: 21, notes: "Kokpunkter: vatten 100 °C, etanol ca 78 °C." });
    await h.imgText(B, "Kromatografi", ["Skiljer ämnen som löser sig olika bra.", "Lösningsmedlet vandrar uppför papperet.", "Olika ämnen vandrar olika långt.", "Kända prover används för jämförelse."], "v_kromatografi.png", { iw: 7.0, imgLeft: false, fs: 21, notes: "Pennfärg på kaffefilter är ett enkelt försök." });
    h.kolla(B, "Kolla dig själv", ["På vad bygger destillation?", "Varför vandrar olika färger olika långt?", "Vad används kända prover till?"]);

    h.section(Cc, "Identifiera ämnen och fällning", "Fråga: hur kan man veta vad ett okänt ämne är?");
    h.cards(Cc, "Identifiera ett okänt ämne", [["Mät flera egenskaper", "Smältpunkt, densitet, löslighet."], ["Jämför", "Med kända prover och tabellvärden."], ["Var försiktig", "Flera ämnen kan ha samma värde på en egenskap."]], { h: 3.2, note: "Därför behövs mer än en egenskap." });
    await h.imgText(Cc, "Fällning", ["Två klara lösningar blandas.", "Ett fast ämne bildas: en fällning.", "Används i vattenrening.", "Fällningen kan filtreras bort."], "v_felling.png", { iw: 7.0, imgLeft: false, fs: 21, notes: "Visa gärna ett enkelt försök om skolan har lämpliga ämnen." });
    await h.imgText(Cc, "Flödesschema för separation", ["Planera i vilken ordning metoderna används.", "Först sand ur blandningen: filtrering.", "Sedan salt ur vatten: avdunstning."], "v_flode.png", { iw: 7.0, imgLeft: false, fs: 21, notes: "Låt eleverna skapa egna flödesscheman." });
    h.kolla(Cc, "Kolla dig själv", ["Varför behövs fler egenskaper än en?", "Vad är en fällning?", "Planera: sand, salt och vatten."]);

    h.section(D, "Labb 2.2: separera sand, salt och vatten", "Material: sand, salt, vatten, bägare, tratt, filtrerpapper, värmekälla, skyddsglasögon. Varning vid upphettning: stå upp och sprutskydd. Utbyte = fått / väntat × 100.");
    await h.imgText(D, "Gör så här", ["Väg upp sand och salt, blanda med vatten.", "Filtrera: sanden blir kvar.", "Indunsta filtratet: saltet blir kvar.", "Väg och räkna utbytet."], "v_labb2.png", { iw: 5.8, imgLeft: false, fs: 21, notes: "Understryk säkerheten vid upphettning." });
    h.table(D, "Frågor att svara på", ["Fråga", "Tips"], [["Vad blev utbytet?", "Fått / väntat × 100. Värdet ska vara under 100 %."], ["Var kan du ha förlorat material?", "Filter, bägare, sprut."], ["Hur kan du förbättra försöket?", "Skölj, torka längre, väg om."]], { colW: [5, 7.2] });
  }
}).catch(e => { console.error(e); process.exit(1); });
