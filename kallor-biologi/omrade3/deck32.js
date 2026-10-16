const { build } = require("./mkpptx.js");
build({
  out: "/tmp/bio/out/biologi-3-2-gruppera-och-organismvarlden.pptx",
  title: "Gruppera och organismvärlden", kicker: "BIOLOGI · KAPITEL 3 · BIOLOGISK MÅNGFALD", sub: "Delområde 3.2: riken, bestämningsnycklar, anpassningar och artbestämning",
  lessons: "Rikena · Bestämningsnycklar · Anpassningar · Labb 3.2",
  foot: "Biologi · Kapitel 3 · Delområde 3.2 Gruppera och organismvärlden",
  titleNotes: "Presentationen följer grundtexten i kapitel 3, delområde 3.2. Några bilder per moment. Anteckningarna innehåller handledning.",
  async slides(h) {
    const A = "Rikena";
    h.section(A, "Fem riken", "Fråga: är en svamp en växt? Vad skulle man titta på för att avgöra det?");
    await h.imgText(A, "Fem riken", ["Djur, växter, svampar, bakterier.", "Encelliga organismer med cellkärna.", "Svampar gör ingen fotosyntes.", "Lav: svamp + alg i symbios."], "rikena.png", { iw: 7.7, imgLeft: false, fs: 20, notes: "Vanligt fel: att svampar är växter. Mycel är svampens nät av trådar." });
    h.cards(A, "Vetenskapligt namn", [["Två ord", "Släkte och art."], ["Tall", "Pinus sylvestris"], ["Gran", "Picea abies"]], { h: 3.0, note: "Systemet infördes av Linné på 1700-talet.", notes: "Första ordet har stor bokstav och namnet skrivs kursivt." });
    h.kolla(A, "Kolla dig själv", ["Nämn de fem rikena.", "Vad skiljer en svamp från en växt?", "Hur skrivs ett vetenskapligt namn?", "Vad är en lav?"]);

    const B = "Bestämningsnycklar";
    h.section(B, "Vad heter trädet?", "Ta fram bild 3.9 och låt eleverna testa nyckeln på ett lövprov eller en bild.");
    await h.imgText(B, "En nyckel för fem träd", ["Två alternativ i varje steg.", "Jämför kännetecken, inte känsla.", "Följ valen tills du får ett namn.", "Kontrollera i bok eller app."], "nyckel.png", { iw: 7.7, imgLeft: false, fs: 20, notes: "Låt eleverna bygga en egen nyckel för tre djur eller tre föremål." });
    h.kolla(B, "Kolla dig själv", ["Vad är en bestämningsnyckel?", "Varför ska nyckeln ha två alternativ i varje steg?", "Hitta på ett första steg för gädda, räv och duva."]);

    const C = "Anpassningar";
    h.section(C, "Passar bäst – överlever", "Fråga: varför ser fjällräv och rödräv olika ut? Koppla till miljön.");
    await h.imgText(C, "Naturligt urval", ["Variation: individer är olika.", "Urval: de som passar bäst överlever.", "Ärftlighet: draget går i arv.", "Draget blir vanligare."], "urval.png", { iw: 7.7, imgLeft: false, fs: 20, notes: "Pepparfjärilen är förenklad. Vanligt fel: att individer anpassar sig medvetet." });
    h.kolla(C, "Kolla dig själv", ["Vad är en anpassning?", "Förklara naturligt urval med tre ord.", "Varför är en anpassning ingen sak en individ bestämmer?"]);

    const D = "Labb 3.2 Artbestämning med nyckel";
    h.section(D, "Träd på skolgården", "Material: nyckeln, mobil, papper. Vissa träd (sälg, al) finns inte i nyckeln, och det är en del av övningen.");
    h.steps(D, "Så gör ni", ["Välj ett träd. Ta bilder på trädet, barken och bladen.", "Följ nyckeln steg för steg och skriv upp valen.", "Skriv svenskt och vetenskapligt namn och kontrollera.", "Gör likadant med minst fyra träd.", "Skriv vilket steg som inte stämmer om trädet saknas i nyckeln."], { notes: "Förväntat: tall, gran, björk, asp, rönn. Plocka bara löv som redan ligger på marken." });
  }
}).catch(e => { console.error(e); process.exit(1); });
