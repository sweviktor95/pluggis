const { build } = require("./mkpptx.js");
build({
  out: "/tmp/kem/out/kemi-2-0-introduktion-till-materia.pptx",
  title: "Introduktion till materia", kicker: "KEMI · KAPITEL 2 · MATERIA OCH PARTIKLAR", sub: "Start: vad är materia och vad säger partikelmodellen?",
  lessons: "Vad är materia? · Allt består av partiklar · Vad ingår i kapitlet?",
  foot: "Kemi · Kapitel 2 · Start Vad är materia?",
  titleNotes: "Presentationen följer grundtexten i kapitel 2, Start. Anteckningarna innehåller handledning. Allt material är utkast (beta).",
  async slides(h) {
    const A = "Vad är materia?";
    h.section(A, "Materia är allt som har massa och tar plats", "Fråga: är luft materia? Låt eleverna motivera. Spara svaren och återvänd till dem efter partikelmodellen.");
    await h.imgText(A, "Materia omkring oss", ["Fasta föremål, vätskor och gaser.", "Allt som har massa och tar plats.", "Luft är materia, även om vi inte ser den.", "Ljus och värme är inte materia."], "v_oversikt.png", { iw: 7.4, imgLeft: false, fs: 22, notes: "Visa att materia finns i tre former. Fråga vilka exempel eleverna kan ge." });
    await h.imgText(A, "Partikelmodellen", ["Allt består av små partiklar.", "Partiklarna rör sig hela tiden.", "Mellan partiklarna är det tomt.", "Det är en modell, en förenkling av verkligheten."], "v_partikel.png", { iw: 7.4, imgLeft: false, fs: 22, notes: "Koppla till kapitel 1: en modell förklarar och förutsäger, men är inte samma sak som verkligheten." });
    h.table(A, "Vad ingår i kapitlet?", ["Delområde", "Du lär dig"], [["2.1 Ämnen, blandningar och partikelmodellen", "Ämnen och material, densitet, partikelmodellen, rena ämnen och blandningar. Labb: densitet."], ["2.2 Separations- och analysmetoder", "Filtrering, avdunstning, destillation, kromatografi, fällning. Labb: separera sand, salt och vatten."]], { colW: [5, 7.2] });
    h.kolla(A, "Kolla dig själv", ["Vad menas med materia?", "Är luft materia? Hur vet du det?", "Vad säger partikelmodellen att allt består av?"]);
  }
}).catch(e => { console.error(e); process.exit(1); });
