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
            id: "matematik-ak7-tal",
            titel: "Tal",
            barn: [
              { id: "matematik-klockan", titel: "Klockan" },
              { id: "matematik-tallinjen", titel: "Tallinjen" },
              { id: "matematik-positionssystem", titel: "Positionssystemet" },
              {
                id: "matematik-rakneattt",
                titel: "De fyra räknesätten",
                barn: [
                  { id: "matematik-addition", titel: "Addition" },
                  { id: "matematik-subtraktion", titel: "Subtraktion" },
                  { id: "matematik-multiplikation", titel: "Multiplikation" },
                  { id: "matematik-division", titel: "Division" }
                ]
              }
            ]
          },
          {
            id: "matematik-ak7-brak",
            titel: "Bråk",
            barn: [
              { id: "matematik-ak7-brak-tallinjen", titel: "Tallinjen" }
            ]
          },
          { id: "matematik-ak7-procent", titel: "Procent" },
          {
            id: "matematik-ak7-algebra",
            titel: "Algebra",
            barn: [
              { id: "matematik-intro-uttryck", titel: "Intro uttryck" },
              { id: "matematik-forenkla-uttryck", titel: "Förenkla uttryck" },
              { id: "matematik-intro-ekvationer", titel: "Intro ekvationer" },
              { id: "matematik-ekvationer", titel: "Ekvationer" }
            ]
          },
          { id: "matematik-ak7-geometri", titel: "Geometri" }
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
              { id: "matematik-ak9-brak-repetition", titel: "Repetition bråk" }
            ]
          },
          {
            id: "matematik-ak9-algebra",
            titel: "Algebra",
            barn: [
              { id: "matematik-ak9-intro-uttryck", titel: "Intro uttryck" },
              { id: "matematik-ak9-forenkla-uttryck", titel: "Förenkla uttryck" },
              { id: "matematik-ak9-intro-ekvationer", titel: "Intro ekvationer" },
              { id: "matematik-ak9-ekvationer", titel: "Ekvationer" }
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
      { id: "biologi-vetenskap", titel: "Vetenskap" },
      {
        id: "biologi-liv",
        titel: "Liv",
        barn: [
          { id: "biologi-cellen", titel: "Cellen" },
          { id: "biologi-organ", titel: "Organ" }
        ]
      },
      { id: "biologi-mangfald", titel: "Biologisk mångfald" },
      { id: "biologi-ekologi", titel: "Ekologi" }
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
