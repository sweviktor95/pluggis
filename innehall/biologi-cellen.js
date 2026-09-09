var innehall = window.innehall || {};

innehall["biologi-cellen"] = {
  intro: "Allt levande är uppbyggt av celler - de är livets minsta byggstenar. En bakterie består bara av en enda cell, medan en människa har biljontals celler som samarbetar.",

  sektioner: [
    {
      ikon: "🔬",
      titel: "Cellen - livets minsta byggsten",
      text: [
        "En cell är den minsta enhet som kan räknas som levande. Alla <strong>organismer</strong> - växter, djur, svampar och bakterier - är uppbyggda av en eller flera celler.",
        "Celler är väldigt små och går oftast inte att se med blotta ögat. För att studera dem behöver man ett <strong>mikroskop</strong>."
      ]
    },
    {
      ikon: "🧫",
      titel: "Vad finns inne i en cell?",
      text: [
        "Inne i cellen finns flera olika smådelar som var och en har sin egen uppgift - de kallas <strong>organeller</strong>. Cellen omges av ett <strong>cellmembran</strong> som håller ihop cellen och bestämmer vad som får komma in och ut.",
        "I cellen finns <strong>cellkärnan</strong>, som innehåller cellens <strong>DNA</strong> - ritningen för hur cellen och hela organismen ska byggas och fungera.",
        "Alla celler har dock inte en cellkärna. Celler hos till exempel människor, djur och växter har en cellkärna och kallas <strong>eukaryota</strong> celler. Bakteriers celler saknar däremot cellkärna och kallas istället <strong>prokaryota</strong> celler - deras DNA flyter fritt i cellen istället.",
        "<strong>Mitokondrier</strong> bryter ner näring och frigör energi som cellen behöver för att fungera - därför kallas de ibland cellens 'kraftverk'.",
        "<strong>Ribosomer</strong> är cellens fabriker för att bygga protein, något cellen behöver för nästan allt den gör.",
        "<strong>Lysosomer</strong> fungerar som en återvinningscentral - de bryter ner skräp och gamla delar av cellen så att byggstenarna kan användas igen.",
        "En <strong>vakuol</strong> är ett förvaringsutrymme inne i cellen som kan innehålla vatten, näring eller avfall. I växtceller är vakuolen ofta mycket stor."
      ],
      bild: "bilder/cell-jamforelse.svg",
      kontrollfraga: "Vad är skillnaden mellan en prokaryot och en eukaryot cell?",
      kontrollsvar: "En eukaryot cell har en cellkärna där DNA:t förvaras - det har till exempel människo-, djur- och växtceller. En prokaryot cell, som en bakteries cell, saknar cellkärna och har DNA:t flytande fritt i cellen istället."
    },
    {
      ikon: "🌱",
      titel: "Växtceller har några extra delar",
      text: [
        "Växtceller har ett par organeller som djurceller saknar. En <strong>cellvägg</strong> ligger utanför cellmembranet och gör cellen stadig och stark, ungefär som ett skyddande skal.",
        "Växtceller innehåller också <strong>kloroplaster</strong>, som fångar upp energi från solljus och använder den för att tillverka näring - det kallas fotosyntes."
      ],
      kontrollfraga: "Vilka två organeller finns i växtceller men saknas i djurceller?",
      kontrollsvar: "Cellvägg och kloroplast. Cellväggen ger stadga, och kloroplasten används för fotosyntes."
    },
    {
      ikon: "🧩",
      titel: "Olika celler, olika jobb",
      text: [
        "Inte alla celler i kroppen ser likadana ut eller gör samma sak. En människa har ungefär 200 olika celltyper, som var och en är specialiserad för en viss uppgift.",
        "Nervceller är byggda för att skicka signaler snabbt genom kroppen. Muskelceller kan dra ihop sig för att skapa rörelse. Röda blodceller transporterar syre runt i kroppen."
      ],
      kontrollfraga: "Varför behöver kroppen många olika typer av celler istället för bara en sorts cell?",
      kontrollsvar: "Olika uppgifter i kroppen kräver olika egenskaper - att skicka nervsignaler, skapa rörelse eller transportera syre är helt olika jobb. Specialiserade celler kan göra sin uppgift mycket effektivare än en generell cell skulle kunna."
    },
    {
      ikon: "🧵",
      titel: "Från cell till vävnad till organ",
      text: [
        "När många celler av samma typ sitter tillsammans bildar de en <strong>vävnad</strong>. Muskelceller bygger till exempel upp muskelvävnad, och nervceller bygger upp nervvävnad.",
        "Flera olika vävnader tillsammans bygger i sin tur upp ett organ - som hjärtat eller lungorna. Det tar du reda på mer om i nästa avsnitt."
      ]
    }
  ],

  begrepp: [
    { term: "Organism", forklaring: "en levande varelse, t.ex. en växt, ett djur, en svamp eller en bakterie" },
    { term: "Mikroskop", forklaring: "ett instrument som förstorar väldigt små saker, som celler, så att man kan se dem" },
    { term: "Cell", forklaring: "den minsta levande byggstenen som alla organismer är uppbyggda av" },
    { term: "Cellmembran", forklaring: "det yttre lagret som håller ihop cellen och styr vad som kommer in och ut" },
    { term: "Cellkärna", forklaring: "delen av cellen som innehåller DNA:t, cellens ritning" },
    { term: "DNA", forklaring: "cellens ritning - informationen för hur organismen ska byggas och fungera" },
    { term: "Organeller", forklaring: "de olika smådelarna inne i en cell, t.ex. cellkärna och mitokondrier, som var och en har sin egen uppgift" },
    { term: "Eukaryot cell", forklaring: "en cell som har en cellkärna - t.ex. celler hos människor, djur och växter" },
    { term: "Prokaryot cell", forklaring: "en cell som saknar cellkärna - t.ex. en bakteries cell" },
    { term: "Mitokondrie", forklaring: "organellen som frigör energi ur näring - cellens 'kraftverk'" },
    { term: "Ribosom", forklaring: "organellen som bygger protein i cellen" },
    { term: "Lysosom", forklaring: "organellen som bryter ner skräp och gamla delar i cellen" },
    { term: "Vakuol", forklaring: "ett förvaringsutrymme i cellen, ofta stort i växtceller" },
    { term: "Cellvägg", forklaring: "ett stadigt skal utanför cellmembranet som finns i växtceller men inte i djurceller" },
    { term: "Kloroplast", forklaring: "organellen i växtceller som fångar solljus och används vid fotosyntes" },
    { term: "Vävnad", forklaring: "många celler av samma typ som sitter ihop och bildar en enhet" }
  ]
};

window.innehall = innehall;
