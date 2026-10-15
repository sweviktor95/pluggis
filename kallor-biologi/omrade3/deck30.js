const { build } = require("./mkpptx.js");
build({
  out: "/tmp/bio/out/biologi-3-0-introduktion-till-biologisk-mangfald.pptx",
  title: "Introduktion till biologisk mångfald", kicker: "BIOLOGI · KAPITEL 3 · BIOLOGISK MÅNGFALD", sub: "Start: hur mycket liv finns det, och vad är mångfald?",
  lessons: "Startlektion före delområde 3.1 · Vad är biologisk mångfald? · Tre nivåer · Kapitlets frågor",
  foot: "Biologi · Kapitel 3 · Introduktion till biologisk mångfald",
  titleNotes: "Kort startlektion som följer avsnittet Start i grundtexten, före delområde 3.1. Anteckningarna innehåller handledning.",
  async slides(h) {
    const S = "Introduktion till biologisk mångfald";
    h.section(S, "Start: hur mycket liv finns det?", "Börja med Fundera-rutan: skriv ner så många arter du kan på två minuter. Jämför och räkna i klassen.");
    h.cards(S, "Biologisk mångfald", [["Gener", "Variation mellan individer inom en art."], ["Arter", "Variation mellan olika arter."], ["Ekosystem", "Variation mellan livsmiljöer."]], { h: 3.2, note: "Mångfald är mer än antalet arter.", notes: "Vanligt fel: att mångfald bara betyder antal arter. Bilden över de tre nivåerna kommer i delområde 3.1." });
    h.stat(S, "Hur många arter finns det?", "2 miljoner+", "arter är beskrivna", ["Ingen vet hur många som finns totalt.", "Uppskattningarna går från några miljoner till betydligt fler.", "De flesta oupptäckta arterna är troligen insekter, svampar och mikroorganismer."], { notes: "Siffran drygt två miljoner är osäker, eftersom en del arter har flera namn. Poängen är att ingen vet totalen." });
    h.cards(S, "Fem frågor i kapitlet", [["Vad är mångfald?", "Gener, arter och ekosystem."], ["Vad gör naturen för oss?", "Ekosystemtjänster."], ["Vad hotar mångfalden?", "Hot och rödlistan."], ["Hur ordnar vi livet?", "Riken och nycklar."], ["Hur anpassar sig arter?", "Naturligt urval."]], { h: 3.4, note: "Delområde 3.1 och 3.2.", notes: "Visa kapitlets två delområden: 3.1 Mångfald, hot och ekosystemtjänster och 3.2 Gruppera och organismvärlden." });
    h.kolla(S, "Kolla dig själv: Start", ["Vad menas med biologisk mångfald?", "Varför räcker det inte att räkna antalet arter?", "Vad vet forskarna om hur många arter som finns?"]);
  }
}).catch(e => { console.error(e); process.exit(1); });
