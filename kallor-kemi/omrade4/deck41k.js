const { build } = require("./mkpptx.js");
build({
  out: "/tmp/kem/out/kemi-4-1-molekyler-och-joner.pptx",
  title: "Molekyler och joner", kicker: "KEMI · KAPITEL 4 · KEMISKA FÖRENINGAR OCH REAKTIONER", sub: "Delområde 4.1: kovalent bindning, joner, egenskaper, labb: leder lösningar ström?",
  lessons: "Molekyler och kovalent bindning · Joner och jonföreningar · Egenskaper hos föreningar · Labb 4.1",
  foot: "Kemi · Kapitel 4 · Delområde 4.1 Molekyler och joner",
  titleNotes: "Presentationen följer grundtexten i kapitel 4. Anteckningarna innehåller handledning. Allt material är utkast (beta).",
  async slides(h) {
    const A = "Molekyler och kovalent bindning", B = "Joner och jonföreningar", Cc = "Egenskaper hos föreningar", D = "Labb 4.1 Leder lösningar elektrisk ström?";
    h.section(A, "Molekyler och kovalent bindning", "Fråga: hur kan två atomer hålla ihop utan att vara laddade? Samla förslag.");
    await h.imgText(A, "Atomer som delar elektroner", ["Kovalent bindning: atomerna delar elektronpar.", "Förekommer mellan icke-metaller.", "Vatten, H₂O: syre delar med två väte.", "Metan, CH₄: kol delar med fyra väte."], "v_kovalent.png", { iw: 7.6, imgLeft: false, fs: 21, notes: "Låt eleverna räkna elektroner i yttersta skalet i bilden." });
    h.cards(A, "Molekylföreningar", [["Smält- och kokpunkt", "Låga. Många är gaser eller vätskor."], ["Ström", "Leder inte, eftersom det saknas fria laddade partiklar."], ["Lösligt", "Varierar. Socker löser sig men leder ändå inte."]], { h: 3.2, note: "O₂ har en dubbelbindning, två delade elektronpar." });
    h.kolla(A, "Kolla dig själv", ["Vad är en kovalent bindning?", "Hur många väteatomer binder kol i metan?", "Varför leder molekylföreningar inte ström?"]);

    h.section(B, "Joner och jonföreningar", "Fråga: kan en atom vara laddad? Hur skulle det gå till?");
    await h.imgText(B, "Natrium och klor blir joner", ["Na avger en elektron och blir Na⁺ (2, 8).", "Cl tar upp en elektron och blir Cl⁻ (2, 8, 8).", "Motsatta laddningar attraherar varandra: jonbindning."], "v_jon.png", { iw: 7.8, imgLeft: false, fs: 21, notes: "Koppla till valenselektroner och ädelgasernas fulla skal från kapitel 3." });
    await h.imgText(B, "Jonkristall", ["Varje positiv jon omges av negativa och tvärtom.", "Mönstret kallas gitter.", "Bordssalt, NaCl, är en jonförening."], "v_kristall.png", { iw: 7.2, imgLeft: false, fs: 22, notes: "Bilden är en förenkling. Verkliga kristaller har många fler joner." });
    h.kolla(B, "Kolla dig själv", ["Hur blir en natriumatom en jon?", "Vad är en jonbindning?", "Hur ser ett jongitter ut?"]);

    h.section(Cc, "Egenskaper hos föreningar", "Fråga: varför smälter salt först vid cirka 800 °C medan socker smälter tidigt?");
    h.table(Cc, "Jämförelse", ["Egenskap", "Jonförening", "Molekylförening"], [["Smältpunkt", "Hög (NaCl 801 °C)", "Låg"], ["Fast ämne leder ström", "Nej", "Nej"], ["Löst i vatten leder ström", "Ja", "Oftast nej"], ["Hårdhet", "Hård men spröd", "Ofta mjuk"]], { colW: [4, 4, 4.2], note: "Metaller leder som fasta ämnen eftersom de yttersta elektronerna är rörliga." });
    await h.imgText(Cc, "Varför leder saltlösning ström?", ["I fast salt sitter jonerna fast.", "I vatten kan jonerna röra sig fritt.", "Rörliga laddade partiklar bär strömmen."], "v_ledning.png", { iw: 7.4, imgLeft: false, fs: 22, notes: "Förbered labben." });
    h.kolla(Cc, "Kolla dig själv", ["Varför är jonföreningar spröda?", "Leder fast salt ström?", "Vad leder ström i en saltlösning?"]);

    h.section(D, "Labb 4.1: leder lösningar elektrisk ström?", "Material: batteri eller lågspänningskälla, lampa, elektroder, bägare, vatten, salt, socker. Förväntat: saltlösning leder, sockerlösning och rent vatten leder dåligt. Använd skyddsglasögon.");
    await h.imgText(D, "Gör så här", ["Bygg kretsen med lampa och elektroder.", "Testa destillerat vatten, saltlösning och sockerlösning.", "Anteckna om lampan lyser.", "Förklara resultaten med joner och molekyler."], "v_labb1.png", { iw: 5.8, imgLeft: false, fs: 21, notes: "Skölj elektroderna mellan varje prov." });
    h.table(D, "Frågor att svara på", ["Fråga", "Tips"], [["Vilka lösningar ledde ström?", "Titta på lampan."], ["Varför ledde saltlösningen?", "Vad finns i den?"], ["Hur säker är din slutsats?", "Upprepa och jämför."]], { colW: [6, 6.2] });
  }
}).catch(e => { console.error(e); process.exit(1); });
