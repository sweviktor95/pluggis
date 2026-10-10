# SPEC – ett historiekapitel (Pluggis, åk 7–9)
Du skriver EN pythonfil per kapitel: /tmp/hist/chNN.py (NN = 01–15). Allt på SVENSKA. Se /tmp/hist/example_ch.py (spanska, annan typ av ämne men samma schema) och /tmp/hist/ch_template.py.
Kör `python3 /tmp/hist/validate.py chNN` tills det står OK.

## Källor och faktagrund (OBLIGATORISKT)
- Utgå från Lgr22 kursplan Historia åk 7–9 (syfte: kunskaper om händelser/aktörer/förändringsprocesser och begrepp, källkritik, historiebruk; centralt innehåll i tre block: 1) Samhällsomvandlingar: framväxten av civilisationer och industrisamhällen, 2) Imperialism och världskrig ca 1850–1950 inkl. Förintelsen och Gulag, 3) Demokratisering och ökad globalisering ca 1900–nutid). Kunskapskraven E/C/A (kunskaper, orsak/konsekvens, kontinuitet/förändring, källor, historiebruk).
- Använd WebSearch/WebFetch för att faktakolla årtal, siffror, händelser (t.ex. Nationalencyklopedin, Svenskt översättningslexikon ej; Riksarkivet, Statens historiska museer, Forum för levande historia, Britannica, UNESCO, Skolverket, Sveriges riksdag, Arbetarrörelsens arkiv, Wikipedia endast som vägvisare). Skriv ALDRIG av text ur läroböcker eller nationella prov; formulera själv. Gamla nationella prov: använd som vägledning för nivå och frågetyper (källfrågor, orsak–konsekvens, kontinuitet–förändring, historiebruk), kopiera inte uppgifter.
- KALLOR: endast URL:er du själv har öppnat/verifierat. Minst 6 per kapitel, blandade primär- och sekundärkällor.
- Var försiktig med osäkra siffror: skriv "ungefär/omkring", ange tidsintervall, undvik falsk precision. Skilj fakta från tolkning ("forskare är oense om …").
- Sensibla ämnen (krig, slaveri, Förintelsen, folkmord): sakligt, respektfullt, åldersanpassat, inga grafiska detaljer, fokus på människor, orsaker, konsekvenser och motstånd. Inga nazistiska symboler eller hatpropaganda återges; analysera propaganda i ord.
- Balans och flera perspektiv. Lyft svensk koppling där den finns (t.ex. S:t Barthélemy, industrialiseringen i Sverige, folkrörelser, neutralitet, flyktingmottagande).

## Stil
- Luftigt, lättläst, korta stycken (2–4 meningar), tydliga rubriker, åk 7–9. Förklara begrepp när de först används. Ordet "du" till eleven. Ingen tjatig ton.
- Varje sektion: `intro` (1–3 meningar) + block. Blandning av: tidslinje, tabell, ruta (visste/fakta/tank/historia), källa-ruta, bild, lista, kolla-dig-själv (3 frågor). Varje kapitel ska ha: orsak–konsekvens-resonemang, kontinuitet–förändring, källkritik/källanalys, historiebruk (hur historien används idag, av vem och varför), minst en svensk koppling.
- Sektioner: 6–8 st (nr "N.1", "N.2" …, där N = kapitelnumret i boken: kap 1 = 1.x osv). Ca 200–350 ord per sektion. Fördjupning: 3–4 sektioner med nr "F1".. ("sidospår", svårare resonemang, tolkningsfrågor, historiografi, jämförelser).
- Uppgifter (UPPG) minst 8 (blandade nivåer), facit i fjärde elementet (femte i tupeln). Test: TEST_A 8 flervalsfrågor, TEST_B 6 korta svar, KALLA = en källanalys (utdrag du själv skriver eller ett kort, fritt citat <25 ord med tydlig källa; hellre en konstruerad "källa" märkt "Konstruerad källa baserad på …"), SKRIV = längre skrivuppgift med bedömningsstöd (E/C/A).
- LAB = "Historikerns verkstad": praktisk elevövning (källundersökning, tidslinjearbete, rollspel/debatt, kartövning, intervju) med syfte, material, utförande (steg), frågor+svar, och BONUS för läraren (lärarhandledningen).
- LARAR: koppling till Lgr22 (vilka punkter i syfte/centralt innehåll/kunskapskrav kapitlet täcker), förslag på upplägg (6–10 lektioner), vanliga missuppfattningar, bedömningsstöd (E/C/A i klartext), samt tips till Blooket/Jeopardy-frågor (10 bra kategorier + exempel).
- BLOOKET: lista med minst 24 frågor `[(fråga, rätt, fel1, fel2, fel3)]` (svarsalternativ korta, max 80 tecken; fråga max 300 tecken). JEOPARDY: 5 kategorier × 5 poängnivåer (100–500): `{"kategori":[(poäng, ledtråd, svar)...]}` (frågor i Jeopardy-form: ledtråd → svar).
- SCEN = specifikation för kapitlets animerade "tidsresa" (se nedan). SCEN=None för kap 9, 11 (har redan egna kartsimuleringar i /mnt/user-data/outputs/pluggis/simuleringar/ – läs dem för konsekventa fakta) och kap 12 (Förintelsen: ingen tecknad animation av respekt).

## Blocktyper (använd exakt dessa)
- ("p", html)  – html får innehålla <strong>, <em>, <br>
- ("tab", [kolumnrubriker], [[cell,...],...])
- ("ruta", typ, rubrik, html) typ ∈ visste | fakta | tank | historia | exempel
- ("list", [html,...])
- ("tidslinje", [("1789","Franska revolutionen börjar"),...])  (4–9 poster)
- ("kalla", "Rubrik/typ av källa", "Källtext (egen formulering, <60 ord)", "Ursprung: vem, när, varför – eller 'Konstruerad källa'")
- ("bild", "scennyckel", "Bildtext")  – scennyckel ∈ lista i /tmp/hist/SCENES.txt (illustrationer finns/skapas av Claude; välj det som passar, max 1–3 per kapitel; om inget passar hoppa över)
- ("kolla", [fråga1, fråga2, fråga3])  – sist i varje sektion; facit i sektionens `svar` (lika många)

## Datastruktur (exakta namn)
T, S, UPPG, BEGREPP, SAMMAN, TEST_A, TEST_B, KALLA, SKRIV, LAB, LARAR, KALLOR, F, F_UPPG, F_SAMMAN, F_BEGR, BLOOKET, JEOPARDY, GRUPPER, SCEN
- T = dict(nr=int, namn, under, fil="historia-NN-slug", arskurs=7|8|9, nodeid="historia-<slug>", mal=[6–8 punkter "…"], fundera="Fråga att fundera på innan man läser")
- GRUPPER = [("slug-suffix","Titel på sajtsida","Kort intro",[sektions-id,...]), ...] (3–4 sajtsidor; varje sektion ska ingå i exakt en grupp). Ordna logiskt.
- UPPG = [(rubrik, instruktion, [delfrågor eller []], [alternativ för para-ihop eller None], facit-text), ...]
- TEST_A = [(fråga, [4 alt], index_rätt)]; TEST_B = [(fråga, facit)]
- KALLA = dict(text=..., ursprung=..., fragor=[(fråga, facit),...3–4 st])
- SKRIV = dict(uppgift=..., stod=[ "E: ...", "C: ...", "A: ..." ])
- LAB = dict(titel, syfte, material, utforande=[steg], fragor=[(fråga,facit)], bonus="…")
- F (fördjupning) = lista av sektioner (samma format som S, id "f1"..), F_UPPG = som UPPG men första elementet är nivå "●" "●●" "●●●", F_SAMMAN=[…], F_BEGR=[(term,förklaring)]
- BEGREPP 12–16 st, SAMMAN 6–8 punkter.
- SCEN = dict(titel="…", plats="…", tid="…", sky=("#färg1","#färg2"), mark="#färg", walker=dict(typ=PERSON), etapper=[ dict(x_etikett="Kort", tid="1789", plats="Paris", rubrik="…", fakta=[2–3 stycken à 1–2 meningar], fraga="…", alt=[3 alt], ratt=index, forklaring="…", deko=[("assetnamn", dx, skala)...]) , … 7 etapper ], diskutera="Diskussionsfråga" )
  PERSON: typ ∈ {"bonde","soldat","handlare","arbetare","medborgare","sjoman","resenar"}. Etapperna är i kronologisk ordning; sista etappen = sammanfattning (utan fråga, med "diskutera"). deko-assets ska väljas från /tmp/hist/ASSETS.txt (lista skapas parallellt av Claude; om du saknar ett: välj närmaste och skriv ett förslag i en kommentar på raden efter).
