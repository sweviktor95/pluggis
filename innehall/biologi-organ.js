var innehall = window.innehall || {};

innehall["biologi-organ"] = {
  intro: "Celler bygger upp <strong>vävnader</strong>, och vävnader bygger i sin tur upp <strong>organ</strong>. Varje organ har en egen uppgift, men de flesta organ samarbetar tätt med varandra för att hela kroppen ska fungera.",

  sektioner: [
    {
      ikon: "🫀",
      titel: "Vad är ett organ?",
      text: [
        "Ett <strong>organ</strong> är uppbyggt av flera olika typer av <strong>vävnader</strong> som tillsammans utför en eller flera uppgifter i kroppen.",
        "Exempel på organ är hjärtat, lungorna, levern, magsäcken och hjärnan. Varje organ har en tydlig form och plats i kroppen, och en eller flera specifika funktioner."
      ],
      bild: "bilder/kroppens-organ.svg"
    },
    {
      ikon: "🤝",
      titel: "Organ som samarbetar",
      text: [
        "Organ jobbar sällan helt ensamma. När flera organ samarbetar för att utföra en gemensam uppgift kallas det ett <strong>organsystem</strong>.",
        "Ett och samma organ kan dessutom ingå i flera olika organsystem samtidigt. Blodkärlen är till exempel en del av både cirkulationssystemet och immunsystemet."
      ],
      kontrollfraga: "Vad är skillnaden på ett organ och ett organsystem?",
      kontrollsvar: "Ett organ är en enskild kroppsdel uppbyggd av olika vävnader, till exempel hjärtat. Ett organsystem är flera organ som samarbetar för att utföra en gemensam uppgift, till exempel cirkulationssystemet (hjärta + blodkärl)."
    },
    {
      ikon: "🫁",
      titel: "Några viktiga organsystem",
      text: [
        "Andningsorganen (lungorna med luftvägar) försörjer kroppen med syre och tar bort koldioxid.",
        "Matsmältningssystemet (bland annat magsäck och tarmar) bryter ner maten så att kroppen kan ta upp näring ur den.",
        "Cirkulationssystemet (hjärtat och blodkärlen) transporterar syre, näring och andra ämnen runt i hela kroppen.",
        "Nervsystemet (hjärnan, ryggmärgen och nerverna) skickar signaler som styr och samordnar kroppens funktioner.",
        "Rörelseorganen (skelettet och musklerna) ger kroppen dess form, skyddar inre organ och gör att vi kan röra oss."
      ]
    },
    {
      ikon: "🛡️",
      titel: "Kroppens största organ",
      text: [
        "Många tänker inte på det, men huden räknas som kroppens största organ. Den täcker hela kroppens utsida.",
        "Huden skyddar kroppen mot bland annat bakterier, uttorkning och skadlig UV-strålning, och hjälper också till att reglera kroppstemperaturen."
      ]
    }
  ],

  begrepp: [
    { term: "Organ", forklaring: "en kroppsdel uppbyggd av flera vävnader som tillsammans har en tydlig funktion, t.ex. hjärtat" },
    { term: "Vävnad", forklaring: "många celler av samma typ som sitter ihop och bildar en enhet" },
    { term: "Organsystem", forklaring: "flera organ som samarbetar för att utföra en gemensam uppgift" },
    { term: "Cirkulationssystemet", forklaring: "organsystemet som transporterar blod runt i kroppen - hjärta och blodkärl" },
    { term: "Nervsystemet", forklaring: "organsystemet som skickar signaler i kroppen - hjärna, ryggmärg och nerver" }
  ]
};

window.innehall = innehall;
