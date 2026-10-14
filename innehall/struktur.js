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
  // BIOLOGI START (genereras av planering/biologi_plan25.py)
  {
    id: "biologi",
    titel: "Biologi (beta)",
    ikon: "🌱",
    ramverk: true,
    barn: [
      {
        id: "biologi-vetenskap",
        titel: "1. Biologi som vetenskap",
        ramverk: true,
        barn: [
          {
            id: "biologi-d-1-1",
            titel: "1.1 Undersöka systematiskt",
            ramverk: true,
            barn: [
              { id: "biologi-m-1-1-1", titel: "Från fråga till plan" },
              { id: "biologi-m-1-1-2", titel: "Dokumentera: tabell, diagram, rapport" },
              { id: "biologi-m-1-1-3", titel: "Värdera: slump, felkällor, slutsats" },
              { id: "biologi-m-1-1-l", titel: "Labb: Reaktionstid som rättvist försök" }
            ]
          },
          {
            id: "biologi-d-1-2",
            titel: "1.2 Modeller, källor och argument",
            ramverk: true,
            barn: [
              { id: "biologi-m-1-2-1", titel: "Vad kan vetenskap pröva?" },
              { id: "biologi-m-1-2-2", titel: "När forskare ändrat sig" },
              { id: "biologi-m-1-2-3", titel: "Söka information och bedöma källor" },
              { id: "biologi-m-1-2-l", titel: "Labb: Granska ett påstående" }
            ]
          },
          { id: "biologi-m-1-s", titel: "Sammanfattning och begrepp" },
          { id: "biologi-m-1-t", titel: "Testa dig själv" }
        ]
      },
      {
        id: "biologi-omrade-2",
        titel: "2. Cellen och livets processer",
        ramverk: true,
        barn: [
          {
            id: "biologi-d-2-1",
            titel: "2.1 Cellen",
            ramverk: true,
            barn: [
              { id: "biologi-m-2-1-1", titel: "Vad är liv? Cellteorin och mikroskopet" },
              { id: "biologi-m-2-1-2", titel: "Djurcell och växtcell" },
              { id: "biologi-m-2-1-3", titel: "Bakterier och encelliga organismer" },
              { id: "biologi-m-2-1-l", titel: "Labb: Mikroskopera celler" }
            ]
          },
          {
            id: "biologi-d-2-2",
            titel: "2.2 Fotosyntes och cellandning",
            ramverk: true,
            barn: [
              { id: "biologi-m-2-2-1", titel: "Växten som producent" },
              { id: "biologi-m-2-2-2", titel: "Cellandning" },
              { id: "biologi-m-2-2-3", titel: "Processerna tillsammans" },
              { id: "biologi-m-2-2-l", titel: "Labb: Jäst och koldioxid" }
            ]
          },
          {
            id: "biologi-d-2-3",
            titel: "2.3 Organ och organsystem",
            ramverk: true,
            barn: [
              { id: "biologi-m-2-3-1", titel: "Specialiserade celler och vävnader" },
              { id: "biologi-m-2-3-2", titel: "Kroppens organsystem – översikt" }
            ]
          },
          { id: "biologi-m-2-s", titel: "Sammanfattning och begrepp" },
          { id: "biologi-m-2-t", titel: "Testa dig själv" }
        ]
      },
      {
        id: "biologi-omrade-3",
        titel: "3. Biologisk mångfald",
        ramverk: true,
        barn: [
          {
            id: "biologi-d-3-1",
            titel: "3.1 Mångfald, hot och ekosystemtjänster",
            ramverk: true,
            barn: [
              { id: "biologi-m-3-1-1", titel: "Gener, arter och ekosystem" },
              { id: "biologi-m-3-1-2", titel: "Ekosystemtjänster" },
              { id: "biologi-m-3-1-3", titel: "Hoten mot mångfalden" },
              { id: "biologi-m-3-1-l", titel: "Labb: Artinventering i en provruta" }
            ]
          },
          {
            id: "biologi-d-3-2",
            titel: "3.2 Gruppera och organismvärlden",
            ramverk: true,
            barn: [
              { id: "biologi-m-3-2-1", titel: "Rikena" },
              { id: "biologi-m-3-2-2", titel: "Bestämningsnycklar" },
              { id: "biologi-m-3-2-3", titel: "Anpassningar" },
              { id: "biologi-m-3-2-l", titel: "Labb: Artbestämning med nyckel" }
            ]
          }
        ]
      },
      {
        id: "biologi-ekologi",
        titel: "4. Ekologi",
        ramverk: true,
        barn: [
          {
            id: "biologi-d-4-1",
            titel: "4.1 Ekosystem och energi",
            ramverk: true,
            barn: [
              { id: "biologi-m-4-1-1", titel: "Vad är ett ekosystem?" },
              { id: "biologi-m-4-1-2", titel: "Producenter, konsumenter och näringsvävar" },
              { id: "biologi-m-4-1-3", titel: "Energiflöde och biomassa" },
              { id: "biologi-m-4-1-l", titel: "Labb: Energi i en näringskedja – modellspel" }
            ]
          },
          {
            id: "biologi-d-4-2",
            titel: "4.2 Materiens kretslopp",
            ramverk: true,
            barn: [
              { id: "biologi-m-4-2-1", titel: "Materia tillverkas inte och försvinner inte" },
              { id: "biologi-m-4-2-2", titel: "Kolets kretslopp" },
              { id: "biologi-m-4-2-3", titel: "Nedbrytning" },
              { id: "biologi-m-4-2-l", titel: "Labb: Nedbrytning i jord" }
            ]
          },
          {
            id: "biologi-d-4-3",
            titel: "4.3 Populationer och samspel",
            ramverk: true,
            barn: [
              { id: "biologi-m-4-3-1", titel: "Populationer och förändring" },
              { id: "biologi-m-4-3-2", titel: "Begränsande faktorer" },
              { id: "biologi-m-4-3-3", titel: "Konkurrens, jakt och samarbete" },
              { id: "biologi-m-4-3-l", titel: "Labb: Rovdjur–bytesmodell" }
            ]
          },
          { id: "biologi-m-4-s", titel: "Sammanfattning och begrepp" },
          { id: "biologi-m-4-t", titel: "Testa dig själv" }
        ]
      },
      {
        id: "biologi-omrade-5",
        titel: "5. Människan och miljön",
        ramverk: true,
        barn: [
          {
            id: "biologi-d-5-1",
            titel: "5.1 Påverkan på naturen och klimat",
            ramverk: true,
            barn: [
              { id: "biologi-m-5-1-1", titel: "Övergödning" },
              { id: "biologi-m-5-1-2", titel: "Växthuseffekten" },
              { id: "biologi-m-5-1-3", titel: "Följder för arter och ekosystem" },
              { id: "biologi-m-5-1-l", titel: "Labb: Växthuseffekten – modell" }
            ]
          },
          {
            id: "biologi-d-5-2",
            titel: "5.2 Hållbar utveckling och ställningstagande",
            ramverk: true,
            barn: [
              { id: "biologi-m-5-2-1", titel: "Vad är hållbar utveckling?" },
              { id: "biologi-m-5-2-2", titel: "Naturresurser och ekosystemtjänster" },
              { id: "biologi-m-5-2-3", titel: "Vad kan jag och samhället göra?" },
              { id: "biologi-m-5-2-l", titel: "Labb: Argumentera i en miljöfråga" }
            ]
          }
        ]
      },
      {
        id: "biologi-omrade-6",
        titel: "6. Kroppens system: mat, andning och blod",
        ramverk: true,
        barn: [
          {
            id: "biologi-d-6-1",
            titel: "6.1 Mat och matspjälkning",
            ramverk: true,
            barn: [
              { id: "biologi-m-6-1-1", titel: "Kolhydrater, proteiner och fetter" },
              { id: "biologi-m-6-1-2", titel: "Matens väg och spjälkning" },
              { id: "biologi-m-6-1-3", titel: "Kostråd och energibalans" },
              { id: "biologi-m-6-1-l", titel: "Labb: Enzymförsök" }
            ]
          },
          {
            id: "biologi-d-6-2",
            titel: "6.2 Andning, blod och samverkan",
            ramverk: true,
            barn: [
              { id: "biologi-m-6-2-1", titel: "Luftvägar och lungor" },
              { id: "biologi-m-6-2-2", titel: "Hjärta och blodkärl" },
              { id: "biologi-m-6-2-3", titel: "Blodomloppet och syretransport" },
              { id: "biologi-m-6-2-l", titel: "Labb: Puls och andning vid belastning" }
            ]
          }
        ]
      },
      {
        id: "biologi-omrade-7",
        titel: "7. Infektioner och immunförsvar",
        ramverk: true,
        barn: [
          {
            id: "biologi-d-7-1",
            titel: "7.1 Bakterier, virus och smitta",
            ramverk: true,
            barn: [
              { id: "biologi-m-7-1-1", titel: "Bakterier och virus" },
              { id: "biologi-m-7-1-2", titel: "Smittvägar" },
              { id: "biologi-m-7-1-3", titel: "Förebygga smitta" },
              { id: "biologi-m-7-1-l", titel: "Labb: Smittspridningsmodell med handtvätt" }
            ]
          },
          {
            id: "biologi-d-7-2",
            titel: "7.2 Immunförsvar, vaccin och antibiotika",
            ramverk: true,
            barn: [
              { id: "biologi-m-7-2-1", titel: "Vita blodkroppar och antikroppar" },
              { id: "biologi-m-7-2-2", titel: "Vaccination" },
              { id: "biologi-m-7-2-3", titel: "Antibiotika och resistens" },
              { id: "biologi-m-7-2-l", titel: "Labb: Granska ett vaccinpåstående" }
            ]
          }
        ]
      },
      {
        id: "biologi-omrade-8",
        titel: "8. Arv, genetik och genteknik",
        ramverk: true,
        barn: [
          {
            id: "biologi-d-8-1",
            titel: "8.1 DNA och nedärvning",
            ramverk: true,
            barn: [
              { id: "biologi-m-8-1-1", titel: "DNA, gener och kromosomer" },
              { id: "biologi-m-8-1-2", titel: "Anlag och alleler" },
              { id: "biologi-m-8-1-3", titel: "Korsningsschema" },
              { id: "biologi-m-8-1-l", titel: "Labb: DNA ur frukt" }
            ]
          },
          {
            id: "biologi-d-8-2",
            titel: "8.2 Arv och miljö, mutationer och genteknik",
            ramverk: true,
            barn: [
              { id: "biologi-m-8-2-1", titel: "Arv och miljö" },
              { id: "biologi-m-8-2-2", titel: "Gensax, GMO och kloning" },
              { id: "biologi-m-8-2-3", titel: "Etiska frågor" },
              { id: "biologi-m-8-2-l", titel: "Labb: Etisk bedömning av genteknik" }
            ]
          }
        ]
      },
      {
        id: "biologi-omrade-9",
        titel: "9. Evolution och livets historia",
        ramverk: true,
        barn: [
          {
            id: "biologi-d-9-1",
            titel: "9.1 Livets historia och bevis",
            ramverk: true,
            barn: [
              { id: "biologi-m-9-1-1", titel: "Jordens och livets tidslinje" },
              { id: "biologi-m-9-1-2", titel: "Fossil och massutdöenden" },
              { id: "biologi-m-9-1-3", titel: "Fossil och jämförande anatomi" },
              { id: "biologi-m-9-1-l", titel: "Labb: Jämför skelett och bygg släktträd" }
            ]
          },
          {
            id: "biologi-d-9-2",
            titel: "9.2 Evolutionens mekanismer",
            ramverk: true,
            barn: [
              { id: "biologi-m-9-2-1", titel: "Variation och naturligt urval" },
              { id: "biologi-m-9-2-2", titel: "Artbildning" },
              { id: "biologi-m-9-2-3", titel: "Naturvetenskap och andra sätt att förklara" },
              { id: "biologi-m-9-2-l", titel: "Labb: Modellförsök om urval" }
            ]
          }
        ]
      },
      {
        id: "biologi-omrade-10",
        titel: "10. Hälsa och levnadsvanor",
        ramverk: true,
        barn: [
          {
            id: "biologi-d-10-1",
            titel: "10.1 Stress, sömn och psykisk hälsa",
            ramverk: true,
            barn: [
              { id: "biologi-m-10-1-1", titel: "Stress i kroppen" },
              { id: "biologi-m-10-1-2", titel: "Sömn och motion" },
              { id: "biologi-m-10-1-3", titel: "Psykisk ohälsa och stöd" },
              { id: "biologi-m-10-1-l", titel: "Labb: Sömn och vanor: statistik" }
            ]
          },
          {
            id: "biologi-d-10-2",
            titel: "10.2 Beroendeframkallande medel",
            ramverk: true,
            barn: [
              { id: "biologi-m-10-2-1", titel: "Alkohol, tobak, nikotin och droger" },
              { id: "biologi-m-10-2-2", titel: "Hjärnan och beroende" },
              { id: "biologi-m-10-2-3", titel: "Förebyggande och stöd" },
              { id: "biologi-m-10-2-l", titel: "Labb: Läs och tolka statistik om tobak och alkohol" }
            ]
          }
        ]
      },
      {
        id: "biologi-omrade-11",
        titel: "11. Pubertet, sexualitet och relationer",
        ramverk: true,
        barn: [
          {
            id: "biologi-d-11-1",
            titel: "11.1 Pubertet, reproduktion, preventivmedel och STI",
            ramverk: true,
            barn: [
              { id: "biologi-m-11-1-1", titel: "Pubertet och könsorgan" },
              { id: "biologi-m-11-1-2", titel: "Befruktning och graviditet" },
              { id: "biologi-m-11-1-3", titel: "Preventivmedel och STI" },
              { id: "biologi-m-11-1-l", titel: "Labb: Faktagranska information om skydd" }
            ]
          },
          {
            id: "biologi-d-11-2",
            titel: "11.2 Relationer, identitet och samtycke",
            ramverk: true,
            barn: [
              { id: "biologi-m-11-2-1", titel: "Sexualitet och identitet" },
              { id: "biologi-m-11-2-2", titel: "Relationer, kärlek och ansvar" },
              { id: "biologi-m-11-2-3", titel: "Samtycke och gränser" },
              { id: "biologi-m-11-2-l", titel: "Labb: Samtycke – fallövning" }
            ]
          }
        ]
      },
      {
        id: "biologi-omrade-12",
        titel: "12. Repetition inför nationella proven",
        ramverk: true,
        barn: [
          {
            id: "biologi-d-12-1",
            titel: "12.1 Repetition inför nationella proven",
            ramverk: true,
            barn: [
              { id: "biologi-m-12-1-1", titel: "Röda trådar" },
              { id: "biologi-m-12-1-2", titel: "Planera och värdera en undersökning" },
              { id: "biologi-m-12-1-3", titel: "Argumentera i miljö- och hälsofrågor" },
              { id: "biologi-m-12-1-l", titel: "Labb: Provlik mini-undersökning" }
            ]
          }
        ]
      }
    ]
  },
  // BIOLOGI END
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
  },
  {
    id: "historia",
    titel: "Historia (beta)",
    ikon: "🏛️",
    barn: [
      {
        id: "historia-hogkulturer",
        titel: "Kapitel 2 – Högkulturer",
        barn: [
          { id: "historia-hogkulturer-vad-ar-hogkultur", titel: "Vad är en högkultur?" },
          { id: "historia-hogkulturer-mesopotamien-egypten", titel: "Mesopotamien och Egypten" },
          { id: "historia-hogkulturer-indus-kina", titel: "Indusdalen och Kina" },
          { id: "historia-hogkulturer-amerika", titel: "Högkulturer i Amerika" },
          { id: "historia-hogkulturer-tidsresa", titel: "Tidsresa (spel)" }
        ]
      }
    ]
  },
  {
    id: "bild",
    titel: "Bild",
    ikon: "🎨",
    barn: []
  },
  {
    id: "engelska",
    titel: "Engelska",
    ikon: "🇬🇧",
    barn: []
  },
  {
    id: "geografi",
    titel: "Geografi",
    ikon: "🌍",
    barn: []
  },
  {
    id: "hem-konsumentkunskap",
    titel: "Hem- och konsumentkunskap",
    ikon: "🍳",
    barn: []
  },
  {
    id: "idrott-halsa",
    titel: "Idrott och hälsa",
    ikon: "🏃",
    barn: []
  },
  {
    id: "moderna-sprak",
    titel: "Moderna språk",
    ikon: "🗣️",
    barn: []
  },
  {
    id: "musik",
    titel: "Musik",
    ikon: "🎵",
    barn: []
  },
  {
    id: "religionskunskap",
    titel: "Religionskunskap",
    ikon: "🕊️",
    barn: []
  },
  {
    id: "samhallskunskap",
    titel: "Samhällskunskap",
    ikon: "🗳️",
    barn: []
  },
  {
    id: "slojd",
    titel: "Slöjd",
    ikon: "🧵",
    barn: [
      { id: "slojd-textil", titel: "Textilslöjd" },
      { id: "slojd-tra-metall", titel: "Trä- och metallslöjd" }
    ]
  },
  {
    id: "svenska",
    titel: "Svenska",
    ikon: "📖",
    barn: []
  }
];

