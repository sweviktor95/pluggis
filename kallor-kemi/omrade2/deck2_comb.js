// Kemi kapitel 2: samlad PowerPoint optimerad för Cornell-anteckningar:
// rubriker som frågor (ledtrådar), Tänk tillbaka först i varje avsnitt, paus för ledtrådar före Kolla dig själv, sammanfattning sist.
const mk = require("./mkpptx.js");
const caps = [];
const realBuild = mk.build;
mk.build = cfg => { caps.push(cfg); return Promise.resolve(); };
require("./deck20k.js"); require("./deck21k.js"); require("./deck22k.js");
mk.build = realBuild;
const KQ = JSON.parse(require("fs").readFileSync("/tmp/kem/kq02.json", "utf8"));
const TB = { // avsnitt -> frågor från föregående moment
  "Ämnen och material": KQ["Start"], "Partikelmodellen": KQ["2.1.1"], "Rena ämnen och blandningar": KQ["2.1.2"],
  "Filtrering, avdunstning och sedimentering": KQ["2.1.3"], "Destillation och kromatografi": KQ["2.2.1"], "Identifiera ämnen och fällning": KQ["2.2.2"] };
const T = { "Materia omkring oss": "Vad är materia?", "Partikelmodellen": "Vad säger partikelmodellen?", "Densitet": "Hur räknar man ut densitet?", "Mäta volym med vattenförskjutning": "Hur mäter man volym med vattenförskjutning?",
  "Flyta eller sjunka": "När flyter något och när sjunker det?", "Tre tillstånd": "Hur ligger partiklarna i fast, flytande och gas?", "Diffusion": "Vad är diffusion och vad bevisar den?",
  "Modellens gränser": "Vad visar partikelmodellen och vad visar den inte?", "Lösningar": "Vad är lösning, löst ämne och lösningsmedel?", "Filtrering": "Hur fungerar filtrering?",
  "Avdunstning och sedimentering": "Vad är avdunstning, sedimentering och dekantering?", "Destillation": "Hur fungerar destillation?", "Kromatografi": "Hur fungerar kromatografi?",
  "Identifiera ett okänt ämne": "Hur identifierar man ett okänt ämne?", "Fällning": "Vad är en fällning?", "Flödesschema för separation": "Hur planerar man en separation i flera steg?" };
const [c0, c1, c2] = caps;
mk.build({
  out: "/tmp/kem/out/kemi-2-materia-och-partiklar.pptx",
  title: "Materia och partiklar", kicker: "KEMI · KAPITEL 2", sub: "Allt består av partiklar", cover: "cover_vanlig.png",
  lessons: "", labels: { "Vad är materia?": "KAPITEL 2 · VAD ÄR MATERIA?", "Ämnen och material": "KAPITEL 2 · ÄMNEN OCH MATERIAL", "Partikelmodellen": "KAPITEL 2 · PARTIKELMODELLEN", "Rena ämnen och blandningar": "KAPITEL 2 · RENA ÄMNEN OCH BLANDNINGAR", "Labb 2.1 Densitet och flyta eller sjunka": "KAPITEL 2 · LABB: DENSITET OCH FLYTA ELLER SJUNKA", "Filtrering, avdunstning och sedimentering": "KAPITEL 2 · FILTRERING, AVDUNSTNING OCH SEDIMENTERING", "Destillation och kromatografi": "KAPITEL 2 · DESTILLATION OCH KROMATOGRAFI", "Identifiera ämnen och fällning": "KAPITEL 2 · IDENTIFIERA ÄMNEN OCH FÄLLNING", "Labb 2.2 Separera sand, salt och vatten": "KAPITEL 2 · LABB: SEPARERA SAND, SALT OCH VATTEN" },
  foot: "Kemi · Kapitel 2 · Materia och partiklar",
  titleNotes: "Presentationen är gjord för Cornell-anteckningar: rubrikerna är frågor som eleverna kan skriva som ledtrådar, varje avsnitt börjar med Tänk tillbaka och har en paus för ledtrådar, och sist kommer en sammanfattning med egna ord. Anteckningarna innehåller handledning. Allt material är utkast (beta).",
  async slides(h) {
    const seen = {};
    const wrap = {
      ...h,
      section(n, sub, notes) { h.skipSection(n, sub, notes); if (TB[n]) { h.tank(n, TB[n].slice(0, 2).map(q => q[0])); } },
      async imgText(sect, title, b, img, o) { return h.imgText(sect, T[title] || title, b, img, o); },
      cards(sect, title, items, o) { return h.cards(sect, T[title] || title, items, o); },
      table(sect, title, head, rows, o) { return h.table(sect, T[title] || title, head, rows, o); },
      kolla(sect, title, qs, o) { if (!/^Labb/.test(sect)) { h.cornell(sect); } return h.kolla(sect, title, qs, o); },
    };
    for (const c of [c0, c1, c2]) { await c.slides(wrap); }
    h.cornell("Labb 2.2 Separera sand, salt och vatten", { final: true });
  }
}).catch(e => { console.error(e); process.exit(1); });
