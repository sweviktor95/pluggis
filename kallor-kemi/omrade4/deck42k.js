const { build } = require("./mkpptx.js");
build({
  out: "/tmp/kem/out/kemi-4-2-kemiska-reaktioner.pptx",
  title: "Kemiska reaktioner", kicker: "KEMI · KAPITEL 4 · KEMISKA FÖRENINGAR OCH REAKTIONER", sub: "Delområde 4.2: reaktioner, formler, massans bevarande, hastighet och energi, labb: massan bevaras",
  lessons: "Vad är en kemisk reaktion? · Reaktionsformler · Hastighet och energi · Labb 4.2",
  foot: "Kemi · Kapitel 4 · Delområde 4.2 Kemiska reaktioner",
  titleNotes: "Presentationen följer grundtexten i kapitel 4. Anteckningarna innehåller handledning. Allt material är utkast (beta).",
  async slides(h) {
    const A = "Vad är en kemisk reaktion?", B = "Reaktionsformler och oförstörbarhet", Cc = "Hastighet och energi", D = "Labb 4.2 Massan bevaras";
    h.section(A, "Vad är en kemisk reaktion?", "Fråga: hur vet man att något nytt har bildats? Samla förslag.");
    await h.imgText(A, "Från utgångsämnen till produkter", ["Utgångsämnen reagerar och produkter bildas.", "Atomerna byter partner.", "Tecken: gas, temperaturändring, färg, fast ämne, ljus eller lukt."], "v_reaktion.png", { iw: 7.6, imgLeft: false, fs: 21, notes: "Färgändring och fällning som tecken är vanliga i läromedel men ingen säker bevisning ensam." });
    h.kolla(A, "Kolla dig själv", ["Vad är utgångsämnen och produkter?", "Nämn tre tecken på reaktion.", "Vad händer med atomerna?"]);

    h.section(B, "Reaktionsformler och oförstörbarhet", "Fråga: kan massa försvinna? Låt eleverna motivera.");
    await h.imgText(B, "Balansera en formel", ["2 H₂ + O₂ → 2 H₂O", "Lika många atomer av varje sort på båda sidor.", "Ändra bara talen framför, aldrig talen inne i formlerna."], "v_balans.png", { iw: 7.4, imgLeft: false, fs: 22, notes: "Räkna atomer tillsammans på tavlan." });
    h.cards(B, "Massans bevarande", [["Lavoisier", "Visade att massan är lika före och efter i ett slutet system."], ["Öppet system", "Gas kan lämna, så den mätta massan minskar."], ["Slutet system", "Massan är oförändrad bortsett från mätfel."]], { h: 3.3, note: "Koppla till ättika och bikarbonat." });
    h.kolla(B, "Kolla dig själv", ["Balansera H₂ + Cl₂ → HCl.", "Varför minskar massan i en öppen flaska?", "Vad säger massans bevarande?"]);

    h.section(Cc, "Hastighet och energi", "Fråga: varför bevarar vi mat i kyl? Koppla till reaktionshastighet.");
    await h.imgText(Cc, "Vad påverkar hastigheten?", ["Temperatur, koncentration, ytarea och katalysator.", "Fler och hårdare krockar ger snabbare reaktion.", "Katalysatorn förbrukas inte."], "v_hastighet.png", { iw: 7.4, imgLeft: false, fs: 21, notes: "Förklara med partiklar, inte bara ”det går fortare”." });
    await h.imgText(Cc, "Exoterm och endoterm", ["Exoterm: energi avges, omgivningen blir varmare.", "Endoterm: energi tas upp, omgivningen blir kallare.", "Ättika och bikarbonat är endoterm."], "v_energi.png", { iw: 7.4, imgLeft: false, fs: 21, notes: "Mät temperaturen i labben." });
    h.kolla(Cc, "Kolla dig själv", ["Nämn två saker som ökar hastigheten.", "Vad är skillnaden mellan exoterm och endoterm?", "Vad är en katalysator?"]);

    h.section(D, "Labb 4.2: massan bevaras", "Material: ättika, bikarbonat, flaskor, våg, ballong, skyddsglasögon. Använd små mängder och stäng inte hårt. Förväntat: massan minskar i öppet system och är oförändrad i slutet.");
    await h.imgText(D, "Gör så här", ["Väg flaskan med ättika och bikarbonat före.", "Låt reaktionen ske öppet och i slutet system.", "Väg efter och jämför."], "v_labb2.png", { iw: 5.8, imgLeft: false, fs: 21, notes: "Diskutera mätfel och varför ballongen sväller." });
    h.table(D, "Frågor att svara på", ["Fråga", "Tips"], [["Varför minskade massan öppet?", "Vad lämnade flaskan?"], ["Varför oförändrad i slutet system?", "Vart tog gasen vägen?"], ["Hur säker är slutsatsen?", "Upprepa och räkna mätfel."]], { colW: [6, 6.2] });
  }
}).catch(e => { console.error(e); process.exit(1); });
