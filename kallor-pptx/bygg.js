// Bygger en PowerPoint per kapitel (biologi och kemi, kapitel 1–4) av delområdenas presentationer.
// Kör: node kallor-pptx/bygg.js [biologi|kemi] [kapitelnummer]   Resultat: planering/<ämne>-omrade<N>/<ämne>-<N>-<kapitel>.pptx
const fs = require("fs"), path = require("path");
const { buildChapter } = require("./mkkapitel.js");
const ROOT = path.join(__dirname, "..");
const FIGROOT = process.env.BIO_FIG || "/tmp/bio";
const K = {
  biologi: [
    { nr: 1, titel: "Biologi som vetenskap", slug: "biologi-som-vetenskap", filer: ["deck10", "deck11", "deck12"] },
    { nr: 2, titel: "Cellen och livets processer", slug: "cellen-och-livets-processer", filer: ["deck21", "deck22", "deck23"] },
    { nr: 3, titel: "Biologisk mångfald", slug: "biologisk-mangfald", filer: ["deck30", "deck31", "deck32"] },
    { nr: 4, titel: "Ekologi", slug: "ekologi", filer: ["deck41", "deck42", "deck43"] }],
  kemi: [
    { nr: 1, titel: "Kemi som vetenskap", slug: "kemi-som-vetenskap", filer: ["deck10k", "deck11k", "deck12k"] },
    { nr: 2, titel: "Materia och partiklar", slug: "materia-och-partiklar", filer: ["deck20k", "deck21k", "deck22k"] },
    { nr: 3, titel: "Atomer och grundämnen", slug: "atomer-och-grundamnen", filer: ["deck30k", "deck31k", "deck32k"] },
    { nr: 4, titel: "Kemiska föreningar och reaktioner", slug: "kemiska-foreningar-och-reaktioner", filer: ["deck40k", "deck41k", "deck42k"] }]
};
function samla(file) {
  const samlat = [];
  const kod = fs.readFileSync(file, "utf8").replace('const { build } = require("./mkpptx.js");', "const build = (c) => { COLLECT.push(c); return Promise.resolve(); };");
  new Function("COLLECT", kod)(samlat);
  return samlat[0];
}
(async () => {
  const bara = process.argv[2], barakap = process.argv[3] && +process.argv[3];
  for (const amne of Object.keys(K)) {
    if (bara && bara !== amne) continue;
    for (const kap of K[amne]) {
      if (barakap && barakap !== kap.nr) continue;
      const dir = path.join(ROOT, amne === "biologi" ? "kallor-biologi" : "kallor-kemi", "omrade" + kap.nr);
      const cfgs = kap.filer.map(f => {
        const c = samla(path.join(dir, f + ".js"));
        const m = c.out.match(/-(\d)-(\d)-/);
        c.delnr = m[1] + "." + m[2];
        c.fig = amne === "biologi" ? `${FIGROOT}/fig0${kap.nr}n/` : path.join(dir, `fig0${kap.nr}k`) + "/";
        return c;
      });
      const utDir = path.join(ROOT, "planering", `${amne}-omrade${kap.nr}`);
      const out = path.join(utDir, `${amne}-${kap.nr}-${kap.slug}.pptx`);
      const K0 = amne === "biologi" ? "BIOLOGI" : "KEMI";
      await buildChapter({
        amne, title: kap.titel, out,
        kicker: `${K0} · KAPITEL ${kap.nr}`,
        notes: `Hela kapitel ${kap.nr} i en presentation. Varje delområde börjar med en egen titelbild, och varje moment har en avsnittsbild. Använd avsnittsvyn i PowerPoint för att hoppa mellan delområdena.`
      }, cfgs);
    }
  }
})().catch(e => { console.error(e); process.exit(1); });
