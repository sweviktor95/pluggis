// Hela Pluggis ämnesträd. Varje nod kan ha "barn" (undernivåer) - hur
// många nivåer djupt som helst. En nod UTAN barn (eller med tom barn-lista)
// blir en innehållssida - då letar mallen efter en matchande post i
// "innehall"-objektet (se t.ex. matematik-tallinjen.js) för text/bild/simulering.
//
// Så här lägger du till mer:
// - Nytt ämne: lägg till ett objekt i toppnivå-listan (med ikon!)
// - Ny nivå/delmoment: lägg till i rätt "barn"-lista
// - Idéer på ikoner: 🧮 📐 🧬 🌱 🧪 ⚗️ ⚡ 🔭 ⚙️ 🔧

var struktur = [
  {
    id: "matematik",
    titel: "Matematik",
    ikon: "🧮",
    barn: [
      {
        id: "matematik-ak7",
        titel: "Årskurs 7",
        barn: [
          {
            id: "matematik-ak7-statistik",
            titel: "Statistik",
            barn: [
              { id: "matematik-ak7-statistik-tabeller", titel: "Tabeller" },
              { id: "matematik-ak7-statistik-diagram", titel: "Diagram" },
              { id: "matematik-ak7-statistik-lagesmatt", titel: "Lägesmått och spridningsmått" },
              { id: "matematik-ak7-statistik-repetition", titel: "Repetition" }
            ]
          },
          {
            id: "matematik-ak7-tal",
            titel: "Tal",
            barn: [
              { id: "matematik-klockan", titel: "Klockan" },
              { id: "matematik-tallinjen", titel: "Tallinjen" },
              { id: "matematik-positionssystem", titel: "Positionssystemet" },
              { id: "matematik-positionssystem-decimaler", titel: "Positionssystemet - Inklusive decimaler" },
              { id: "matematik-ak7-tal-tiobas", titel: "Tiobas (multiplicera/dividera med 10, 100, 1000 osv)" },
              {
                id: "matematik-rakneattt",
                titel: "De fyra räknesätten",
                barn: [
                  { id: "matematik-addition", titel: "Addition" },
                  { id: "matematik-subtraktion", titel: "Subtraktion" },
                  { id: "matematik-multiplikation", titel: "Multiplikation" },
                  { id: "matematik-division", titel: "Division" }
                ]
              },
              { id: "matematik-ak7-tal-decimalberakningar", titel: "Decimalberäkningar (multiplicera/dividera med tal mellan 0 och 1)" },
              { id: "matematik-ak7-tal-primtal", titel: "Primtal" },
              { id: "matematik-ak7-tal-delbarhet", titel: "Delbarhet" },
              { id: "matematik-ak7-tal-avrundning", titel: "Avrundning" },
              { id: "matematik-ak7-tal-overslagsrakning", titel: "Överslagsräkning" },
              { id: "matematik-ak7-tal-repetition", titel: "Repetition" }
            ]
          },
          {
            id: "matematik-ak7-brak",
            titel: "Bråk",
            barn: [
              { id: "matematik-ak7-brak-tallinjen", titel: "Bråkform" },
              { id: "matematik-ak7-brak-jamfora", titel: "Jämföra bråk" },
              { id: "matematik-ak7-brak-forlang-forkorta", titel: "Förlänga och förkorta bråk" },
              { id: "matematik-ak7-brak-add-sub", titel: "Addition och subtraktion av bråk" },
              { id: "matematik-ak7-brak-mult", titel: "Multiplikation av bråk" },
              { id: "matematik-ak7-brak-div", titel: "Division av bråk" },
              { id: "matematik-ak7-brak-repetition", titel: "Repetition" }
            ]
          },
          {
            id: "matematik-ak7-procent",
            titel: "Procent",
            barn: [
              { id: "matematik-ak7-procent-andel", titel: "Andel" },
              { id: "matematik-ak7-procent-forandring", titel: "Förändring" },
              { id: "matematik-ak7-procent-huvudrakning", titel: "Huvudräkning" },
              { id: "matematik-ak7-procent-delen", titel: "Delen" },
              { id: "matematik-ak7-procent-det-hela", titel: "Det hela" },
              { id: "matematik-ak7-procent-repetition", titel: "Repetition" }
            ]
          },
          {
            id: "matematik-ak7-algebra",
            titel: "Algebra",
            barn: [
              { id: "matematik-intro-uttryck", titel: "Algebraiska uttryck" },
              { id: "matematik-forenkla-uttryck", titel: "Förenkla uttryck" },
              { id: "matematik-ak7-algebra-formler", titel: "Formler" },
              { id: "matematik-ak7-algebra-monster", titel: "Mönster" },
              { id: "matematik-intro-ekvationer", titel: "Ekvationer intro" },
              { id: "matematik-ekvationer", titel: "Ekvationslösningar" },
              { id: "matematik-ak7-algebra-problemlosning", titel: "Problemlösning" },
              { id: "matematik-ak7-algebra-repetition", titel: "Repetition" }
            ]
          },
          {
            id: "matematik-ak7-geometri",
            titel: "Geometri",
            barn: [
              { id: "matematik-ak7-geometri-enheter-prefix", titel: "Enheter och prefix" },
              { id: "matematik-ak7-geometri-vinklar", titel: "Vinklar" },
              { id: "matematik-ak7-geometri-vinkelsumma-manghorningar", titel: "Vinkelsumma och månghörningar" },
              { id: "matematik-ak7-geometri-omkrets", titel: "Omkrets" },
              { id: "matematik-ak7-geometri-area-intro", titel: "Area intro" },
              { id: "matematik-ak7-geometri-area-fyrhorningar", titel: "Area fyrhörningar" },
              { id: "matematik-ak7-geometri-area-trianglar", titel: "Area trianglar" },
              { id: "matematik-ak7-geometri-area-cirklar", titel: "Area cirklar" },
              { id: "matematik-ak7-geometri-repetition", titel: "Repetition" }
            ]
          }
        ]
      },
      { id: "matematik-ak8", titel: "Årskurs 8", barn: [] },
      {
        id: "matematik-ak9",
        titel: "Årskurs 9",
        barn: [
          {
            id: "matematik-ak9-brak",
            titel: "Bråk",
            barn: [
              { id: "matematik-ak9-tallinjen", titel: "Tallinjen" },
              { id: "matematik-ak9-brak-forlang-forkorta", titel: "Förlänga och förkorta bråk" },
              { id: "matematik-ak9-brak-add-sub", titel: "Addition och subtraktion av bråk" },
              { id: "matematik-ak9-brak-mult", titel: "Multiplikation av bråk" },
              { id: "matematik-ak9-brak-div", titel: "Division av bråk" },
              { id: "matematik-ak9-brak-repetition", titel: "Jeopardy bråk" },
              { id: "matematik-ak9-brak-repetition-knapp", titel: "Repetition" }
            ]
          },
          {
            id: "matematik-ak9-algebra",
            titel: "Algebra",
            barn: [
              { id: "matematik-ak9-intro-uttryck", titel: "Uttryck intro" },
              { id: "matematik-ak9-forenkla-uttryck", titel: "Förenkla uttryck" },
              { id: "matematik-ak9-algebra-multiplicera-uttryck", titel: "Multiplicera uttryck" },
              { id: "matematik-ak9-algebra-faktorisera-uttryck", titel: "Faktorisera uttryck" },
              { id: "matematik-ak9-intro-ekvationer", titel: "Ekvationer intro" },
              { id: "matematik-ak9-ekvationer", titel: "Ekvationer" },
              { id: "matematik-ak9-algebra-problemlosning", titel: "Problemlösning" },
              { id: "matematik-ak9-algebra-repetition", titel: "Repetition" }
            ]
          },
          {
            id: "matematik-ak9-samband",
            titel: "Samband och förändring",
            barn: [
              { id: "matematik-ak9-samband-funktioner-intro", titel: "Funktioner intro" },
              { id: "matematik-ak9-samband-linjara-funktioner", titel: "Linjära funktioner" },
              { id: "matematik-ak9-samband-rata-linjens-ekvation", titel: "Räta linjens ekvation" },
              { id: "matematik-ak9-samband-procentuell-forandring", titel: "Procentuell förändring" },
              { id: "matematik-ak9-samband-upprepad-procentuell-forandring", titel: "Upprepad procentuell förändring" },
              { id: "matematik-ak9-samband-repetition", titel: "Repetition" }
            ]
          },
          {
            id: "matematik-ak9-geometri",
            titel: "Geometri",
            barn: [
              { id: "matematik-ak9-geometri-symmetri", titel: "Symmetri" },
              { id: "matematik-ak9-geometri-likformighet-kongruens", titel: "Likformighet och kongruens" },
              { id: "matematik-ak9-geometri-langdskala", titel: "Längdskala" },
              { id: "matematik-ak9-geometri-areaskala", titel: "Areaskala" },
              { id: "matematik-ak9-geometri-volymskala", titel: "Volymskala" },
              { id: "matematik-ak9-geometri-likformiga-trianglar-topptriangelsatsen", titel: "Likformiga trianglar och topptriangelsatsen" },
              { id: "matematik-ak9-geometri-pythagoras-sats", titel: "Pythagoras sats" },
              { id: "matematik-ak9-geometri-repetition", titel: "Repetition" }
            ]
          },
          {
            id: "matematik-ak9-repetition-np",
            titel: "Repetition åk 7-9 inför NP",
            barn: [
              {
                id: "matematik-ak9-np-tal",
                titel: "Tal",
                barn: [
                  { id: "matematik-ak9-np-tal-decimalform", titel: "Decimalform" },
                  { id: "matematik-ak9-np-tal-mult-div", titel: "Multiplikation och division" },
                  { id: "matematik-ak9-np-tal-brak", titel: "Bråk" },
                  { id: "matematik-ak9-np-tal-negativa-tal", titel: "Negativa tal" },
                  { id: "matematik-ak9-np-tal-potenser-kvadratrotter", titel: "Potenser och kvadratrötter" },
                  { id: "matematik-ak9-np-tal-prioriteringsregler", titel: "Prioriteringsregler" },
                  { id: "matematik-ak9-np-tal-avrundning-overslag", titel: "Avrundning och överslagsräkning" },
                  { id: "matematik-ak9-np-tal-repetition", titel: "Repetition tal" }
                ]
              },
              {
                id: "matematik-ak9-np-algebra",
                titel: "Algebra",
                barn: [
                  { id: "matematik-ak9-np-algebra-uttryck", titel: "Uttryck" },
                  { id: "matematik-ak9-np-algebra-forenkla-uttryck", titel: "Förenkla uttryck" },
                  { id: "matematik-ak9-np-algebra-ekvationer", titel: "Ekvationer" },
                  { id: "matematik-ak9-np-algebra-monster", titel: "Mönster" },
                  { id: "matematik-ak9-np-algebra-formler", titel: "Formler" },
                  { id: "matematik-ak9-np-algebra-repetition", titel: "Repetition algebra" }
                ]
              },
              {
                id: "matematik-ak9-np-geometri",
                titel: "Geometri",
                barn: [
                  { id: "matematik-ak9-np-geometri-vinklar-manghorningar", titel: "Vinklar och månghörningar" },
                  { id: "matematik-ak9-np-geometri-omkrets-enheter", titel: "Omkrets och enheter" },
                  { id: "matematik-ak9-np-geometri-area-volym", titel: "Area och volym" },
                  { id: "matematik-ak9-np-geometri-symmetri", titel: "Symmetri" },
                  { id: "matematik-ak9-np-geometri-likformiga-figurer", titel: "Likformiga figurer" },
                  { id: "matematik-ak9-np-geometri-skala", titel: "Skala" },
                  { id: "matematik-ak9-np-geometri-pythagoras-sats", titel: "Pythagoras sats" },
                  { id: "matematik-ak9-np-geometri-repetition", titel: "Repetition geometri" }
                ]
              },
              {
                id: "matematik-ak9-np-statistik",
                titel: "Statistik och sannolikhetslära",
                barn: [
                  { id: "matematik-ak9-np-statistik-tolka-diagram", titel: "Tolka diagram" },
                  { id: "matematik-ak9-np-statistik-lagesmatt-spridningsmatt", titel: "Lägesmått och spridningsmått" },
                  { id: "matematik-ak9-np-statistik-kombinatorik", titel: "Kombinatorik" },
                  { id: "matematik-ak9-np-statistik-sannolikhet", titel: "Sannolikhet" },
                  { id: "matematik-ak9-np-statistik-repetition", titel: "Repetition statistik och sannolikhetslära" }
                ]
              },
              {
                id: "matematik-ak9-np-samband",
                titel: "Samband och förändring",
                barn: [
                  { id: "matematik-ak9-np-samband-andel-delen-hela", titel: "Andel, delen, det hela" },
                  { id: "matematik-ak9-np-samband-procentuell-forandring-forandringsfaktor", titel: "Procentuell förändring och förändringsfaktor" },
                  { id: "matematik-ak9-np-samband-procentenheter", titel: "Procentenheter" },
                  { id: "matematik-ak9-np-samband-koordinatsystem-grafer", titel: "Koordinatsystem och tolka grafer" },
                  { id: "matematik-ak9-np-samband-proportionalitet-linjara-samband", titel: "Proportionalitet och linjära samband" },
                  { id: "matematik-ak9-np-samband-rata-linjens-ekvation", titel: "Räta linjens ekvation" },
                  { id: "matematik-ak9-np-samband-repetition", titel: "Repetition samband och förändring" }
                ]
              }
            ]
          }
        ]
      }
    ]
  },
  {
    id: "biologi",
    titel: "Biologi",
    ikon: "🌱",
    barn: [
      {
        id: "biologi-vetenskap",
        titel: "Vetenskap",
        barn: [
          { id: "biologi-vetenskap-vad-ar-biologi", titel: "Vad är biologi?" },
          { id: "biologi-vetenskap-metod", titel: "Vetenskaplig metod" },
          { id: "biologi-vetenskap-hur-utvecklas-kunskap", titel: "Hur utvecklas kunskap?" }
        ]
      },
      {
        id: "biologi-liv",
        titel: "Liv",
        barn: [
          { id: "biologi-cellen", titel: "Celler (växtceller och djurceller)" },
          { id: "biologi-organ", titel: "Organ och organsystem" },
          { id: "biologi-liv-fotosyntes-cellandning", titel: "Fotosyntes och cellandning" }
        ]
      },
      {
        id: "biologi-mangfald",
        titel: "Biologisk mångfald",
        barn: [
          { id: "biologi-mangfald-vad-ar", titel: "Vad är biologisk mångfald?" },
          { id: "biologi-mangfald-varfor-viktig", titel: "Varför är biologisk mångfald viktig?" },
          { id: "biologi-mangfald-hot", titel: "Hot mot den biologiska mångfalden" }
        ]
      },
      {
        id: "biologi-organismvarlden",
        titel: "Organismvärlden",
        barn: [
          { id: "biologi-organismvarlden-alger-sporvaxter-svampar-lavar", titel: "Alger, sporväxter, svampar och lavar" },
          { id: "biologi-organismvarlden-frovaxter", titel: "Fröväxter" },
          { id: "biologi-organismvarlden-ryggradslosa-djur", titel: "Ryggradslösa djur" },
          { id: "biologi-organismvarlden-ryggradsdjur", titel: "Ryggradsdjur" }
        ]
      },
      {
        id: "biologi-ekologi",
        titel: "Ekologi",
        barn: [
          { id: "biologi-ekologi-population-resurser", titel: "Population och resurser" },
          { id: "biologi-ekologi-naringskedjor-naringsvavar", titel: "Näringskedjor och näringsvävar" },
          { id: "biologi-ekologi-liv-i-samspel", titel: "Liv i samspel" },
          { id: "biologi-ekologi-energi-materia", titel: "Energi och materia" },
          { id: "biologi-ekologi-systems-kanslighet", titel: "Ekosystems känslighet" },
          { id: "biologi-ekologi-ekosystem", titel: "Ekosystem" },
          { id: "biologi-ekologi-hallbar-utveckling", titel: "Hållbar utveckling" }
        ]
      },
      {
        id: "biologi-matspjalkning-naringslara",
        titel: "Matspjälkning och näringslära",
        barn: [
          { id: "biologi-matspjalkning-matens-vag", titel: "Matens väg genom kroppen" },
          { id: "biologi-matspjalkning-naringsamnen", titel: "Näringsämnen" },
          { id: "biologi-matspjalkning-energi-kost", titel: "Energi och kost" }
        ]
      },
      {
        id: "biologi-andning-blodomlopp",
        titel: "Andning och blodomlopp",
        barn: [
          { id: "biologi-andning-lungor-hjarta", titel: "Lungor och hjärta" },
          { id: "biologi-andning-blod-syretransport", titel: "Blod och syretransport" }
        ]
      },
      {
        id: "biologi-immunforsvar-sjukdomar",
        titel: "Immunförsvar och sjukdomar",
        barn: [
          { id: "biologi-immunforsvar-bakterier", titel: "Bakterier" },
          { id: "biologi-immunforsvar-virus", titel: "Virus" },
          { id: "biologi-immunforsvar-vaccination", titel: "Vaccination" },
          { id: "biologi-immunforsvar-antibiotika", titel: "Antibiotika" },
          { id: "biologi-immunforsvar-immunforsvar", titel: "Immunförsvar" }
        ]
      },
      {
        id: "biologi-genetik",
        titel: "Genetik",
        barn: [
          { id: "biologi-genetik-dna", titel: "DNA" },
          { id: "biologi-genetik-gener", titel: "Gener" },
          { id: "biologi-genetik-kromosomer", titel: "Kromosomer" },
          { id: "biologi-genetik-nedarvning-arftlighet", titel: "Nedärvning och ärftlighet" },
          { id: "biologi-genetik-dominanta-recessiva-anlag", titel: "Dominanta och recessiva anlag" }
        ]
      },
      {
        id: "biologi-fortplantning-sexualitet-relationer",
        titel: "Fortplantning, sexualitet och relationer",
        barn: [
          { id: "biologi-fortplantning-pubertet", titel: "Pubertet" },
          { id: "biologi-fortplantning-fortplantning", titel: "Fortplantning" },
          { id: "biologi-fortplantning-graviditet", titel: "Graviditet" },
          { id: "biologi-fortplantning-preventivmedel", titel: "Preventivmedel" },
          { id: "biologi-fortplantning-sti", titel: "Sexuellt överförbara infektioner (STI)" },
          { id: "biologi-fortplantning-relationer-samtycke", titel: "Relationer och samtycke" }
        ]
      },
      {
        id: "biologi-psykisk-fysisk-ohalsa",
        titel: "Psykisk och fysisk ohälsa",
        barn: [
          { id: "biologi-ohalsa-stress", titel: "Stress" },
          { id: "biologi-ohalsa-somn", titel: "Sömn" },
          { id: "biologi-ohalsa-motion", titel: "Motion" },
          { id: "biologi-ohalsa-levnadsvanor", titel: "Levnadsvanor" }
        ]
      },
      {
        id: "biologi-evolution",
        titel: "Evolution",
        barn: [
          { id: "biologi-evolution-naturligt-urval", titel: "Naturligt urval" },
          { id: "biologi-evolution-mutationer", titel: "Mutationer" },
          { id: "biologi-evolution-anpassningar", titel: "Anpassningar" },
          { id: "biologi-evolution-artbildning", titel: "Artbildning" }
        ]
      },
      {
        id: "biologi-livets-historia",
        titel: "Livets historia",
        barn: [
          { id: "biologi-livets-historia-fossiler", titel: "Fossiler" },
          { id: "biologi-livets-historia-jordens-utveckling", titel: "Jordens utveckling" },
          { id: "biologi-livets-historia-evolutionens-bevis", titel: "Evolutionens bevis" }
        ]
      },
      {
        id: "biologi-ekologi-fordjupning",
        titel: "Ekologi fördjupning",
        barn: [
          { id: "biologi-ekologi-fordjupning-kretslopp", titel: "Kretslopp" },
          { id: "biologi-ekologi-fordjupning-kolcykel", titel: "Kolcykel" },
          { id: "biologi-ekologi-fordjupning-kvavecykel", titel: "Kvävecykel" },
          { id: "biologi-ekologi-fordjupning-biologisk-mangfald", titel: "Biologisk mångfald" },
          { id: "biologi-ekologi-fordjupning-ekosystemtjanster", titel: "Ekosystemtjänster" }
        ]
      },
      {
        id: "biologi-klimat-hallbar-utveckling",
        titel: "Klimat och hållbar utveckling",
        barn: [
          { id: "biologi-klimat-klimatforandringar", titel: "Klimatförändringar" },
          { id: "biologi-klimat-overgodning", titel: "Övergödning" },
          { id: "biologi-klimat-forsurning", titel: "Försurning" },
          { id: "biologi-klimat-invasiva-arter", titel: "Invasiva arter" },
          { id: "biologi-klimat-naturvard", titel: "Naturvård" }
        ]
      },
      {
        id: "biologi-informationsgranskning-argument",
        titel: "Informationsgranskning och biologiska argument",
        barn: [
          { id: "biologi-informationsgranskning-kallkritik", titel: "Källkritik" },
          { id: "biologi-informationsgranskning-halsopastaenden", titel: "Granskning av hälsopåståenden" },
          { id: "biologi-informationsgranskning-vetenskapliga-argument", titel: "Vetenskapliga argument" },
          { id: "biologi-informationsgranskning-statistik-diagram", titel: "Statistik och diagram" }
        ]
      },
      { id: "biologi-repetition-np", titel: "Repetition inför nationella proven" }
    ]
  },
  {
    id: "kemi",
    titel: "Kemi",
    ikon: "🧪",
    barn: []
  },
  {
    id: "fysik",
    titel: "Fysik",
    ikon: "⚡",
    barn: []
  },
  {
    id: "teknik",
    titel: "Teknik",
    ikon: "⚙️",
    barn: []
  }
];
