const { build } = require("./mkpptx.js");
build({
  out: "/tmp/kem/out/kemi-2-1-amnen-blandningar-partikelmodellen.pptx",
  title: "Ämnen, blandningar och partikelmodellen", kicker: "KEMI · KAPITEL 2 · MATERIA OCH PARTIKLAR", sub: "Delområde 2.1: ämnen och material, partikelmodellen, rena ämnen och blandningar, labb om densitet",
  lessons: "Ämnen och material · Partikelmodellen · Rena ämnen och blandningar · Labb 2.1",
  foot: "Kemi · Kapitel 2 · Delområde 2.1 Ämnen, blandningar och partikelmodellen",
  titleNotes: "Presentationen följer grundtexten i kapitel 2, delområde 2.1. Anteckningarna innehåller handledning. Allt material är utkast (beta).",
  async slides(h) {
    const A = "Ämnen och material", B = "Partikelmodellen", Cc = "Rena ämnen och blandningar", D = "Labb 2.1 Densitet och flyta eller sjunka";
    h.section(A, "Ämnen och deras egenskaper", "Fråga: hur kan man skilja två vita pulver åt? Sinnena räcker inte alltid, därför mäter vi.");
    h.cards(A, "Ämne eller material?", [["Ämne", "En sorts materia med bestämda egenskaper: vatten, järn, socker."], ["Material", "Det något är gjort av: trä, glas, tyg. Kan vara flera ämnen."], ["Egenskap", "Något som kännetecknar ett ämne: färg, hårdhet, smältpunkt, densitet."]], { h: 3.2, note: "Gränsen mellan ämne och material är inte skarp i vardagsspråket. Be eleverna sortera exempel." });
    h.cards(A, "Densitet", [["Formel", "densitet = massa / volym"], ["Enhet", "g/cm³ (1 ml = 1 cm³)"], ["Exempel", "54 g / 20 cm³ = 2,7 g/cm³ (aluminium)"]], { h: 3.2, note: "Låt eleverna räkna ett par exempel själva." });
    await h.imgText(A, "Mäta volym med vattenförskjutning", ["Läs av vattnet före: 50 ml.", "Lägg i föremålet och läs av igen: 70 ml.", "Volymen är skillnaden: 20 ml = 20 cm³.", "Värdena är påhittade."], "v_vattenforskj.png", { iw: 7.2, imgLeft: false, fs: 22, notes: "Påminn om att läsa av menisken (kapitel 1)." });
    await h.imgText(A, "Flyta eller sjunka", ["Lägre densitet än vatten: föremålet flyter.", "Högre densitet än vatten: föremålet sjunker.", "Is (0,92 g/cm³) flyter på vatten (ca 1,0 g/cm³).", "Densitet är en egenskap hos ämnet, inte hos formen."], "v_flyta.png", { iw: 7.2, imgLeft: false, fs: 21, notes: "Vatten är ovanligt: det fasta tillståndet är lättare än vätskan. Det kommer i fördjupningen." });
    h.kolla(A, "Kolla dig själv", ["Ämne eller material?", "Hur räknar du ut densitet?", "Hur mäter du volymen hos en sten?", "Varför flyter is?"]);

    h.section(B, "Partikelmodellen", "Tre tillstånd, samma partiklar. Fråga: vad skiljer ett fast ämne från en gas?");
    await h.imgText(B, "Tre tillstånd", ["Fast: partiklarna ligger tätt i ett mönster och vibrerar.", "Vätska: tätt, men de glider förbi varandra.", "Gas: långt isär och rör sig snabbt åt alla håll."], "v_tillstand.png", { iw: 7.8, imgLeft: false, fs: 21, notes: "Visa gärna en animation eller låt eleverna spela partiklar." });
    await h.imgText(B, "Diffusion", ["Partiklar rör sig och blandar sig av sig själva.", "Doft sprids i ett rum.", "Färg sprids i vatten, snabbare i varmt vatten."], "v_diffusion.png", { iw: 7.2, imgLeft: false, fs: 22, notes: "Diffusion är ett bevis för att partiklarna rör sig." });
    h.cards(B, "Modellens gränser", [["Den visar", "Hur partiklar är ordnade och rör sig i tre tillstånd."], ["Den visar inte", "Krafterna mellan partiklarna, hur partiklarna egentligen ser ut."], ["Därför", "Modellen är bra men måste ibland kompletteras, till exempel för is."]], { h: 3.2, note: "Koppla till modellbegreppet från kapitel 1." });
    h.kolla(B, "Kolla dig själv", ["Beskriv partiklarna i fast form, vätska och gas.", "Vad bevisar diffusion?", "Nämn en begränsning hos partikelmodellen."]);

    h.section(Cc, "Rena ämnen och blandningar", "Fråga: är luft ett rent ämne? Vad består den av?");
    await h.imgText(Cc, "Rent ämne eller blandning", ["Rent ämne: bara en sorts partiklar.", "Blandning: flera sorters partiklar.", "Homogen: delarna syns inte (saltvatten).", "Heterogen: delarna syns (sand i vatten)."], "v_blandning.png", { iw: 7.4, imgLeft: false, fs: 21, notes: "Låt eleverna sortera vardagliga exempel: luft, mjölk, helium, luft, juice, granit." });
    h.table(Cc, "Lösningar", ["Begrepp", "Betyder"], [["Lösning", "Homogen blandning där ett ämne är utspritt i ett annat."], ["Löst ämne", "Det som löses, till exempel salt."], ["Lösningsmedel", "Det som löser, ofta vatten."], ["Löslighet", "Hur mycket som kan lösas i en viss mängd lösningsmedel."]], { colW: [3.5, 8.7] });
    h.kolla(Cc, "Kolla dig själv", ["Rent ämne eller blandning: saltvatten, järn, luft?", "Homogen eller heterogen: sand i vatten?", "Vad är ett lösningsmedel?"]);

    h.section(D, "Labb 2.1: densitet och flyta eller sjunka", "Material: våg, mätcylinder, vatten, föremål av olika material, skyddsglasögon. Förväntat: lägre densitet än 1,0 g/cm³ flyter.");
    await h.imgText(D, "Gör så här", ["Väg varje föremål och skriv massan.", "Mät volymen med vattenförskjutning.", "Räkna ut densiteten.", "Förutsäg först: flyter eller sjunker? Pröva sedan."], "v_labb1.png", { iw: 6.2, imgLeft: false, fs: 21, notes: "Låt eleverna skriva förutsägelsen innan de provar." });
    h.table(D, "Frågor att svara på", ["Fråga", "Tips"], [["Stämde dina förutsägelser?", "Jämför med densiteten."], ["Vilka felkällor fanns?", "Luftbubblor, avläsning av menisken, våta föremål."], ["Hur kan du förbättra försöket?", "Upprepa och ta medelvärde."]], { colW: [5, 7.2] });
  }
}).catch(e => { console.error(e); process.exit(1); });
