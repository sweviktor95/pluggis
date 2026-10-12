# Biologi åk 7–9 – planering för omarbetningen (Lgr22)

Status: FÖRSLAG, väntar på Vicks beslut (se "Beslut som behövs").
Källa: kursplanen i biologi (`kursplaner/Biologi-GRGRBIO01.pdf`), centralt innehåll och betygskriterier för åk 9.
Innehållet behandlas i sak och citeras inte ordagrant. Kursplanens termer behöver inte nämnas hela tiden.

## 1. Mål

1. Ett sammanhängande biologiläromedel för åk 7–9 som täcker allt centralt innehåll och de tre förmågorna.
2. PDF:erna är mastern. Sajten byggs från samma källa, inte i efterhand.
3. Varje kapitel finns i tre versioner (vanlig, lättläst, fördjupning), var och en med elevversion och lärarversion ("-komplett").
4. Varje kapitel har granskats mot ett fast protokoll (avsnitt 5) innan det kallas klart.
5. Allt är markerat "(beta)" tills Vick har läst igenom det.

## 2. Läget idag

| Kap | Titel | PDF | Granskat | Sajt |
|---|---|---|---|---|
| 1 | Biologi som vetenskap | Ombyggd från egen källa | Ja (`kallor-biologi/granskning-kapitel1.md`) | Gammal, matchar inte PDF:erna |
| 2 | Cellen | Gamla PDF:er, källkod förlorad | Nej | Gammal |
| 3 | Mångfald | Gamla PDF:er, källkod förlorad | Nej | Gammal |
| 4 | Ekologi | Ombyggd från egen källa | Nej (kapitel 1-protokollet är inte körd) | Ny. PDF:erna saknar hållbar utveckling, sajten har det |
| 5– | Övrigt | Finns inte | – | Delvis i `struktur.js`, saknar innehåll |

Byggsystemet är generellt (`CH=NN python3 bbuild.py`, `bbuild_latt.py`, `bbuild_fordj.py`) och nya kapitel läggs till som `chNN.py`, `chNN_latt.py`, `chNN_fordj.py`.

## 3. Föreslagen kapitelstruktur

Kap 1–4 är Vicks redan beslutade kapitel. Kap 5–14 är mitt förslag och kan ändras fritt.

| Kap | Titel | Centralt innehåll som behandlas | Elevlab (förslag) |
|---|---|---|---|
| 1 | Biologi som vetenskap | Undersökningsbara frågor, planering, utförande, värdering, dokumentation; modellernas historiska framväxt; källkritik; ställningstaganden | Reaktionstid som rättvist försök |
| 2 | Cellen och livets processer | Celler, organ och organsystem (översikt); fotosyntes och cellandning | Mikroskopera lök- och elodeaceller; syreproduktion hos vattenpest |
| 3 | Biologisk mångfald | Mångfald; identifiering och systematik; anpassning; ekosystemtjänster (inledning) | Artbestämning med nyckel i närmiljön |
| 4 | Ekologi | Lokala och globala ekosystem; populationer och resurser; kretslopp och energiflöde | Provruteinventering eller nedbrytning i marken |
| 5 | Människan och miljön | Påverkan lokalt och globalt; hållbar utveckling på individ- och samhällsnivå; biologisk mångfald och ekosystemtjänster; klimat, övergödning, invasiva arter | Mätning av övergödningseffekt (alger/vatten) |
| 6 | Mat och matspjälkning | Matspjälkningens organ; näringsämnen; kost och hälsa | Enzymförsök (stärkelse, saliv) |
| 7 | Andning och blodomlopp | Lungor, hjärta, blod; samverkan mellan organsystem; motion | Puls och andning före/efter belastning |
| 8 | Infektioner och immunförsvar | Virus, bakterier, smittspridning, antibiotikaresistens, förebyggande och behandling (hygien, vaccination) | Smittspridningsmodell (leksimulering) och bakterieodling |
| 9 | Arv och genetik | Arvsmassans egenskaper; DNA, gener, kromosomer; nedärvning; förhållandet mellan arv och miljö | DNA-extraktion ur frukt; korsningsövning med kort |
| 10 | Genteknik | Några gentekniska metoder; möjligheter, risker, etiska frågor | Strukturerad diskussion/debatt med underlag |
| 11 | Evolution och livets historia | Livets uppkomst, utveckling och mångfald; evolutionens mekanismer; naturligt urval, mutationer; fossil | Modellförsök naturligt urval |
| 12 | Hälsa och levnadsvanor | Psykisk och fysisk hälsa; kost, sömn, motion, stress, beroendeframkallande medel; åtgärder på individ- och samhällsnivå | Sömn-/stressenkät med diagram |
| 13 | Pubertet, sexualitet och relationer | Reproduktion, sexualitet och identitet; relationer, kärlek, ansvar, samtycke, ömsesidighet; sexuellt överförbara sjukdomar; preventivmedel | Ingen traditionell lab; faktaundersökning och källgranskning |
| 14 | Repetition inför nationella proven | Alla delar, alla tre förmågor | Provlik laboration |

Ordning och årskurs: förslagsvis åk 7 kap 1–4, åk 8 kap 5–9, åk 9 kap 10–14. På sajten visas kapitlen direkt under ämnet i ordning, utan årskursmappar, så att läraren kan ta dem i egen ordning.

## 4. Täckning: centralt innehåll mot kapitel

| Centralt innehåll åk 7–9 (i sak) | Kapitel |
|---|---|
| Livets uppkomst, utveckling och mångfald; evolutionens mekanismer | 3, 11 |
| Arvsmassans egenskaper; arv och miljö | 9 |
| Gentekniska metoder, möjligheter, risker, etik | 10 |
| Lokala och globala ekosystem; populationer och resurser | 4 |
| Fotosyntes, cellandning, materiens kretslopp, energiflöden | 2, 4 |
| Människans påverkan, hållbar utveckling, biologisk mångfald, ekosystemtjänster | 3, 5 |
| Celler, organ och organsystem | 2, 6, 7 |
| Virus, bakterier, infektioner, smittspridning, antibiotikaresistens | 8 |
| Hälsa: levnadsförhållanden, kost, sömn, motion, stress, beroende, åtgärder | 6, 7, 12 |
| Reproduktion, sexualitet, identitet, relationer, samtycke, STI, preventivmedel | 13 |
| Undersökningar: frågor, planering, utförande, värdering, dokumentation (bilder, tabeller, diagram, rapporter) | 1 och en lab i varje kapitel |
| Biologiska undersökningar och begrepp/modeller; modellernas historia, användbarhet, föränderlighet | 1, 3, 9, 11 |
| Informationssökning, kritisk granskning | 1, 5, 12, 13 |
| Argumentation och ställningstaganden i miljö och hälsa | 5, 10, 12, 13 |

Luckor som redan är kända: hållbar utveckling saknas i ekologi-PDF:erna (hamnar i kap 5), och kap 3 behöver en tydlig identifierings- och systematikdel.

## 5. Arbetsflöde per kapitel (samma för alla)

1. **Innehållsspec.** Lista exakt vad kapitlet ska täcka och vilka förmågor det övar. Vicks godkännande innan vi skriver.
2. **Faktaunderlag.** Samla pålitliga källor (myndigheter, universitet, läroböcker med öppna källor). Länkarna samlas bak i lärarversionen.
3. **Skriva vanlig version** med figurer, "Kom ihåg", övningar, test och facit, elevlab och bonuslab i lärarversionen.
4. **Skriva lättläst och fördjupning** från samma underlag.
5. **Lärarmaterial.** Facit, bedömningsstöd mot kriterierna, Blooket-CSV och klassrums-Jeopardy med lag.
6. **Bygga alla sex PDF:er** och kontrollera sidnummer, innehållsförteckning och figurer visuellt.
7. **Granskning** (avsnitt 6).
8. **Sajten byggs från samma källa** med moment, spel och övningar enligt samma innehåll.
9. **Test:** `nav_test.js` måste ge ALL OK. Commit lokalt.
10. **Push endast när Vick skriver "pusha".**

Ett kapitel i taget. Nästa kapitel startar först när föregående är granskat och Vick har sagt till.

## 6. Granskningsprotokoll (lätt, men fast)

För varje kapitel, och dokumenterat i `kallor-biologi/granskning-kapitelN.md`:

- **Centralt innehåll:** varje punkt i avsnitt 4 som kapitlet ska täcka är bockad, med sida.
- **Syftet och förmågorna:** minst en uppgift per förmåga (begrepp/modeller, granska och ta ställning, undersökningar).
- **Betygskriterier åk 9:** fördjupningsuppgifter och test formulerade så att E-, C- och A-nivå går att skilja. Nivåerna ska skilja sig i hur utvecklat resonemanget är, inte i antalet fakta.
- **Nationella prov:** jämförelse med släppta uppgifter som finns tillgängliga, för uppgiftstyper och svårighet.
- **Faktakontroll:** alla siffror, årtal, namn och påståenden mot primärkälla. Osäkert formuleras om eller tas bort.
- **Textgranskning:** en oberoende läsare per kapitel (inte författaren) läser texten, med fokus på fel, otydligheter och ålderspassning.
- **Visuell kontroll:** varje sida öppnas som bild.
- **Försiktiga områden:** kap 8, 10, 12 och 13 (hälsa, genteknik, sexualitet) granskas extra noga och formuleras sakligt, utan skrämsel eller värderingar.

Begränsning som alltid ska stå i granskningsloggen: granskningen är inte en ersättning för att en biologilärare läser kapitlet.

## 7. Gemensamma designregler

- Alla biologikapitel använder samma gröna färg; luftig layout, enkelt språk, många figurer.
- Alla begrepp förklaras där de första gången används. Spel och simuleringar ska vara spelbara fristående.
- Varje kapitel slutar med en elevlab; lärarhandledningen har en bonuslab.
- Ämnet har egna moment. Överlapp med andra ämnen är avsiktligt och behandlas ur biologins vinkel.
- Allt på svenska.

## 8. Beslut som behövs

1. **Struktur:** passar kapitel 5–14 (avsnitt 3), eller vill du slå ihop/dela något, t.ex. genetik och genteknik till ett kapitel?
2. **Ordning/årskurs:** ska evolution (kap 11) komma tidigare?
3. **Befintliga kapitel:** granskar vi kap 4 mot protokollet först, eller bygger vi kap 2–3 först?
4. **Arbetstakt:** ett kapitel i taget (rekommenderas) eller flera parallellt med en granskare per kapitel?
5. **Sajten för kap 1:** uppdatera nu så att den matchar PDF:erna?

## 9. Rekommenderad första vecka

1. Beslut enligt avsnitt 8.
2. Sajten för kap 1 synkas med PDF:erna.
3. Kap 1 körs mot kursplanens kriterier ordagrant (nu tillgängliga i repot) och markeras klart.
4. Kap 2 (Cellen) byggs med hela flödet.
