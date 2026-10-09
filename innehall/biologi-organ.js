// Från cell till organism, kroppens organsystem – sajtsidor utifrån Kapitel 2 (häftet), avsnitt 2.8–2.10.
// Följer häftet, med rättelserna från faktakollen. Bilderna är utklippta ur häftet.

var innehall = window.innehall || {};

var RUTA = function(typ, rubrik, text) {
  return '<div class="ruta ruta-' + typ + '"><span class="ruta-rubrik">' + rubrik + '</span>' + text + '</div>';
};

innehall["biologi-organ"] = {
  intro: "I en flercellig organism är cellerna organiserade i flera nivåer. Celler av samma sort samarbetar och bildar större enheter. Tänk på det som bokstäver, ord, meningar, kapitel och en hel bok.",
  sektioner: [
    {
      ikon: "🧱",
      titel: "Från cell till organism",
      text: [
        "<strong>Cell:</strong> den minsta levande enheten, till exempel en muskelcell.<br><strong>Vävnad:</strong> många celler av samma sort som gör samma jobb, till exempel muskelvävnad.<br><strong>Organ:</strong> en kroppsdel som består av flera vävnader med en viss uppgift. Hjärtat består till exempel av muskel-, nerv- och bindväv.<br><strong>Organsystem:</strong> flera organ som samarbetar, till exempel hjärtat och blodkärlen.<br><strong>Organism:</strong> en hel levande varelse, där alla organsystem fungerar tillsammans.",
        "<strong>Fyra viktiga vävnader.</strong><br><strong>Muskelvävnad</strong> kan dra ihop sig och ger rörelse. Den finns i armar och ben, men också i hjärtat och tarmarna.<br><strong>Nervvävnad</strong> leder signaler. Den bygger upp hjärnan, ryggmärgen och nerverna.<br><strong>Epitelvävnad</strong> (täckande vävnad) täcker ytor, till exempel huden och insidan av tarmen.<br><strong>Stödjevävnad</strong> (bindväv) håller ihop och stöttar kroppen. Ben, brosk, senor och fett är exempel. Blodet räknas ofta också hit.",
        "<strong>Även växter har organ.</strong> En växts organ är rot, stam, blad och blomma. Bladet är byggt av flera vävnader: en skyddande yta, vävnad med kloroplaster som gör fotosyntes och ledningsvävnad (transportvävnad) som transporterar vatten och socker."
      ],
      bild: "bilder/cellen-nivaer.png",
      bildText: "Bild 2.9 Organisationsnivåer i kroppen, med hjärtat som exempel. Varje nivå består av många delar från nivån före.",
      kontrollfraga: "Ordna från minst till störst: organ, cell, organism, vävnad, organsystem. Ge ett exempel på ett organ hos en växt.",
      kontrollsvar: "Cell – vävnad – organ – organsystem – organism. Ett organ hos en växt är till exempel rot, stam, blad eller blomma."
    },
    {
      ikon: "🫀",
      titel: "Kroppens organsystem",
      text: [
        "Människokroppen har ett tiotal organsystem. Varje system har sin uppgift, men inget av dem klarar sig ensamt. Du kommer att lära dig mer om flera av dem i senare kapitel.",
        "<strong>Matsmältning</strong> (mun, magsäck, tarmar, lever): bryter ner maten så att näringen kan tas upp i blodet.<br><strong>Andning</strong> (luftstrupe, lungor): tar in syre och gör sig av med koldioxid.<br><strong>Cirkulation</strong> (hjärta, blodkärl, blod): transporterar syre, näring och avfall till och från cellerna.<br><strong>Utsöndring</strong> (njurar, urinblåsa): renar blodet och gör sig av med avfall via urinen.<br><strong>Nervsystemet</strong> (hjärna, ryggmärg, nerver, sinnesorgan): tar emot information och styr kroppen med snabba signaler.<br><strong>Hormonsystemet</strong> (hormonkörtlar): styr kroppen med signalämnen i blodet, till exempel adrenalin.<br><strong>Immunförsvar</strong> (vita blodkroppar, lymfkörtlar): skyddar mot bakterier, virus och andra främlingar.<br><strong>Rörelseapparat</strong> (skelett, leder, muskler): ger stöd, skydd och rörelse.<br><strong>Fortplantning</strong> (äggstockar, livmoder, testiklar): bildar könsceller och gör det möjligt att få barn.<br><strong>Huden</strong> (hud, hår, svettkörtlar): skyddar kroppen och hjälper till att hålla rätt temperatur.",
        RUTA("tank", "Tänk efter", "En person dricker mycket alkohol under många år. Levern bryter ner alkoholen och kan skadas. Vilka andra organsystem kan påverkas om levern inte fungerar som den ska?")
      ],
      bild: "bilder/cellen-organ.png",
      bildText: "Bild 2.10 Några av kroppens viktigaste organ.",
      kontrollfraga: "Vilket organsystem tar upp syre? Vad är skillnaden mellan hur nervsystemet och hormonsystemet styr kroppen?",
      kontrollsvar: "Andningssystemet tar upp syre. Nervsystemet styr med snabba signaler i nerverna, hormonsystemet med signalämnen (hormoner) i blodet."
    },
    {
      ikon: "🤝",
      titel: "Organsystemen samarbetar",
      text: [
        "Varför har vi lungor, hjärta och tarmar? Svaret finns i cellerna. Nästan varje cell i kroppen behöver energi, och den får den genom cellandning i mitokondrierna. För det behövs glukos och syre. Cellandningen ger också avfall: koldioxid. Organsystemen samarbetar för att alla celler – även de längst ut i tårna – ska få det de behöver.",
        "<strong>Steg för steg</strong><br>1. <strong>Andningssystemet:</strong> i lungorna går syre från luften över till blodet. Koldioxid går åt andra hållet och andas ut.<br>2. <strong>Matsmältningssystemet:</strong> maten bryts ner. I tunntarmen tas näringen, till exempel glukos, upp i blodet.<br>3. <strong>Cirkulationssystemet:</strong> hjärtat pumpar blodet genom kroppen. Blodet lämnar syre och glukos till cellerna och hämtar koldioxid och avfall.<br>4. <strong>Utsöndringssystemet:</strong> njurarna filtrerar blodet och gör sig av med avfall via urinen.",
        "Nervsystemet och hormonsystemet styr alltihop – till exempel hur fort hjärtat slår och hur snabbt du andas.",
        RUTA("fakta", "Exempel: du springer", "Musklerna i benen arbetar hårt och behöver mycket energi. Då behöver muskelcellerna mer syre och glukos. Du andas snabbare och djupare, och hjärtat slår snabbare så att mer blod når musklerna. När du blir rädd kan hormonet adrenalin göra samma sak på några sekunder.")
      ],
      bild: "bilder/cellen-samarbete.png",
      bildText: "Bild 2.11 Så samarbetar fyra organsystem för att kroppens celler ska få syre och näring och bli av med avfall.",
      kontrollfraga: "Förklara hur syre från luften når en muskelcell i benet. Varför ökar pulsen när du springer?",
      kontrollsvar: "Syre tas upp i lungorna och går över till blodet. Hjärtat pumpar blodet till muskelcellen, som tar upp syret. Pulsen ökar för att musklerna behöver mer syre och glukos, och hjärtat måste då pumpa mer blod."
    }
  ],
  begrepp: [
    { term: "Vävnad", forklaring: "En grupp celler (oftast likadana) som samarbetar och gör samma jobb." },
    { term: "Organ", forklaring: "En kroppsdel som består av flera vävnader med en viss uppgift." },
    { term: "Organsystem", forklaring: "Flera organ som samarbetar." },
    { term: "Organism", forklaring: "En hel levande varelse." }
  ],
  exitTicket: [
    { fraga: "Vilket alternativ visar ordningen från minst till störst? A vävnad–cell–organ–organsystem, B cell–organ–vävnad–organsystem, C cell–vävnad–organ–organsystem, D organ–cell–vävnad–organsystem.", svar: "C – cell, vävnad, organ, organsystem." },
    { fraga: "Vilka två ämnen behöver cellerna för cellandningen?", svar: "Glukos och syre." }
  ]
};
