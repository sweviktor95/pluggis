const { build } = require("./mkpptx.js");
build({
  out: "/tmp/bio/out/biologi-2-3-organ-och-organsystem.pptx",
  title: "Organ och organsystem", kicker: "BIOLOGI · KAPITEL 2 · CELLEN OCH LIVETS PROCESSER", sub: "Delområde 2.3: specialiserade celler, vävnader, organ och organsystem",
  lessons: "Specialiserade celler och vävnader · Kroppens organsystem – översikt",
  foot: "Biologi · Kapitel 2 · Delområde 2.3 Organ och organsystem",
  titleNotes: "Presentationen följer grundtexten i kapitel 2, delområde 2.3.",
  async slides(h) {
    const A = "Specialiserade celler och vävnader";
    h.section(A, "När cellerna får olika jobb", "Fråga: Din muskelcell och din hudcell har samma DNA. Varför ser de olika ut?");
    await h.imgText(A, "Fem specialiserade celler", ["Muskelcell: drar ihop sig.", "Nervcell: lång och grenad, skickar signaler.", "Röd blodkropp: transporterar syre, saknar cellkärna.", "Rothårscell: stor yta för vattenupptag. Palisadcell: många kloroplaster."], "spec-celler.png", { iw: 7.2, imgLeft: false, fs: 20, notes: "Bilden är förenklad och inte skalenlig. Nästan alla celler har samma DNA, men olika delar används i olika celltyper." });
    h.cards(A, "Fyra vävnader", [["Epitel", "Täcker ytor och kläder insidan, till exempel huden."], ["Bindväv", "Binder ihop och stödjer: senor, fett, brosk, blod."], ["Muskel", "Drar ihop sig och ger rörelse."], ["Nerv", "Leder nervsignaler."]], { h: 3.6, note: "Flera vävnader som samarbetar bildar ett organ.", notes: "Exempel: hjärtat består mest av muskelvävnad, men också av bindväv, nervvävnad och epitel." });
    h.kolla(A, "Kolla dig själv", ["Vad är en specialiserad cell? Ge två exempel.", "Skilj på cell, vävnad och organ.", "Nämn de fyra vävnadstyperna.", "Varför kan inte hjärtat bestå av bara muskelvävnad?"]);

    const B = "Kroppens organsystem – översikt";
    h.section(B, "Allt hjälper cellerna", "Detta är kapitlets viktiga sammanhang. Kapitel 6 och 7 går djupare in på matsmältning, andning, blod och immunförsvar.");
    await h.imgText(B, "Kroppens nivåer", ["Cell → vävnad → organ → organsystem → organism.", "Organsystem är organ som samarbetar.", "Hela kroppen är organismen.", "Några organ syns här."], "cellen-organ.png", { iw: 5.4, imgLeft: false, fs: 22 });
    await h.imgText(B, "System som försörjer cellerna", ["Matsmältningen tar upp glukos.", "Andningen tar in syre och släpper ut koldioxid.", "Cirkulationen transporterar ämnena.", "Utsöndringen renar blodet."], "cellen-samarbete.png", { iw: 6.8, imgLeft: false, fs: 22, notes: "Koppla tillbaka till cellandningen i 2.2: varje cell behöver glukos och syre och måste bli av med koldioxid." });
    h.table(B, "Några organsystem", ["Organsystem", "Uppgift", "Organ"], [["Matsmältning", "Bryter ner maten och tar upp näring", "magsäck, tunntarm, lever"], ["Andning", "Tar in syre, släpper ut koldioxid", "lungor, luftrör"], ["Cirkulation", "Transporterar med blodet", "hjärta, blodkärl"], ["Nervsystem", "Tar emot och skickar signaler", "hjärna, ryggmärg"], ["Utsöndring", "Renar blodet", "njurar, urinblåsa"]], { colW: [3.1, 5.2, 3.83], fs: 20, rowH: 0.7 });
    h.kolla(B, "Kolla dig själv", ["Vad är ett organsystem? Ge ett exempel.", "Vilka tre organsystem hjälps åt att förse cellerna med glukos och syre?", "Förklara hur ett organsystem hjälper kroppens celler.", "Vad händer med cellerna om cirkulationen slutar fungera?"]);
  }
}).catch(e => { console.error(e); process.exit(1); });
