# SPEC – ett kemikapitel (Pluggis, åk 7–9)
Du skriver EN pythonfil: /tmp/kemi/chNN.py (NN = kapitelnummer, 01 …). Allt på SVENSKA. Schemat är identiskt med historiekapitlen: läs /tmp/hist/ch03.py som fullständigt exempel (ignorera historiespecifikt, SCEN och bild-block) och /tmp/kemi/ch_template.py. Kör `cd /tmp/kemi && python3 validate.py chNN` tills det står OK.
Skriv aldrig utanför /tmp/kemi/chNN.py.

## Källor och faktagrund (OBLIGATORISKT)
- Utgå från Lgr22 kursplanen i kemi (/mnt/user-data/outputs/pluggis/kursplaner/Kemi-GRGRKEM01.pdf, läs med `pdftotext -layout`) och kapitelplanen /mnt/user-data/outputs/pluggis/planering/kemi.md. Kursplanen ska BEHANDLAS i sak, inte citeras ordagrant: täck centralt innehåll och öva förmågorna (kemins begrepp och förklaringsmodeller; granska information, kommunicera och ta ställning i miljö- och hälsofrågor; genomföra systematiska undersökningar). Kunskapskraven E/C/A gäller åk 9.
- Varje ämne har egna moment: skriv kemin ur kemins vinkel, hänvisa inte till biologiboken.
- Använd WebSearch för att faktakolla (Skolverket, NE.se, Kemikalieinspektionen, Naturvårdsverket, Folkhälsomyndigheten, Livsmedelsverket, SMHI, Nobelprize.org, IUPAC, universitet, Britannica; Wikipedia endast som vägvisare). WebFetch fungerar bara på URL:er som först dykt upp i ett sökresultat. Kopiera aldrig text ur läroböcker eller nationella prov; formulera själv. Nationella provet i kemi (åk 9) är sekretessbelagt: använd bara det publika bedömningsstödet och provets struktur som vägledning för nivå och frågetyper (förklara samband, använda modeller, resonera och ta ställning, planera och värdera undersökningar).
- KALLOR: endast URL:er du själv har sett i sökresultat/öppnat. Minst 6 per kapitel, blandat. Säg i slutrapporten vilka som är verifierade.
- Osäkra siffror: "ungefär/omkring", undvik falsk precision. Skilj fakta från tolkning.
- Säkerhet: inga experiment med farliga ämnen. Laborationer ska vara säkra hemmaexperiment/skolexperiment med vardagsmaterial och tydliga säkerhetsregler (skyddsglasögon, ventilation, hantera hett vatten försiktigt, smaka aldrig, läs varningsmärkning). Inga recept för explosiva, giftiga eller narkotiska ämnen.

## Stil
- Luftigt, lättläst, korta stycken (2–4 meningar), tydliga rubriker, åk 7–9, du-tilltal. Förklara begrepp när de först används. Konkreta vardagsexempel, kemiska symboler/formler där det passar (använd <sub>/<sup> i html, t.ex. H<sub>2</sub>O).
- Varje sektion: `intro` + block. Blanda tabell, ruta (visste/fakta/tank/exempel; typ "historia" används för kemins historia/anekdoter), tidslinje (kemins historia), lista, kolla-dig-själv (3 frågor). Varje kapitel ska ha: förklaringsmodell/begrepp, orsak–samband, ett systematiskt undersökningsresonemang, källkritik/argumentation där det passar kapitlet, och en koppling till miljö/hälsa/samhälle.
- Sektioner: 6–8 st (nr "N.1", "N.2" … där N = kapitelnummer). Ca 200–350 ord per sektion. Fördjupning: 3–4 sektioner "F1".. (sidospår, svårare resonemang).
- UPPG minst 8 (blandade nivåer, facit i femte tupelelementet), TEST_A 8 flervalsfrågor, TEST_B 6 korta svar, KALLA = en text/påstående att granska (egen konstruerad text märkt "Konstruerad källa baserad på …" eller kort fritt citat <25 ord med källa), SKRIV = längre skrivuppgift med E/C/A-stöd.
- LAB = "Kemilabbet": säker praktisk undersökning med syfte, material, utförande (steg), frågor+svar, BONUS för läraren.
- LARAR: koppling till Lgr22 (täckta punkter i syfte/centralt innehåll/kunskapskrav), förslag på upplägg (6–10 lektioner), vanliga missuppfattningar, bedömningsstöd (E/C/A i klartext), tips till Blooket/Jeopardy.
- BLOOKET: minst 24 frågor `[(fråga, rätt, fel1, fel2, fel3)]` (svar max 80 tecken, fråga max 300). JEOPARDY: 5 kategorier × (100–500): `{"kategori":[(poäng, ledtråd, svar)...]}`. Exakt ett rätt svar per fråga.

## Blocktyper (använd exakt dessa)
- ("p", html)  – html får innehålla <strong>, <em>, <br>
- ("tab", [kolumnrubriker], [[cell,...],...])
- ("ruta", typ, rubrik, html) typ ∈ visste | fakta | tank | historia | exempel
- ("list", [html,...])
- ("tidslinje", [("1789","Franska revolutionen börjar"),...])  (4–9 poster)
- ("kalla", "Rubrik/typ av källa", "Källtext (egen formulering, <60 ord)", "Ursprung: vem, när, varför – eller 'Konstruerad källa'")
- (inget "bild"-block i kemi: använd INTE bild)
- ("kolla", [fråga1, fråga2, fråga3])  – sist i varje sektion; facit i sektionens `svar` (lika många)

## Datastruktur (exakta namn)
T, S, UPPG, BEGREPP, SAMMAN, TEST_A, TEST_B, KALLA, SKRIV, LAB, LARAR, KALLOR, F, F_UPPG, F_SAMMAN, F_BEGR, BLOOKET, JEOPARDY, GRUPPER, SCEN
- T = dict(nr=int, namn, under, fil="kemi-NN-slug", arskurs="7–9" (exakt den strängen), nodeid="kemi-<slug>", mal=[6–8 punkter "…"], fundera="Fråga att fundera på innan man läser")
- GRUPPER = [("slug-suffix","Titel på sajtsida","Kort intro",[sektions-id,...]), ...] (3–4 sajtsidor; varje sektion ska ingå i exakt en grupp). Ordna logiskt.
- UPPG = [(rubrik, instruktion, [delfrågor eller []], [alternativ för para-ihop eller None], facit-text), ...]
- TEST_A = [(fråga, [4 alt], index_rätt)]; TEST_B = [(fråga, facit)]
- KALLA = dict(text=..., ursprung=..., fragor=[(fråga, facit),...3–4 st])
- SKRIV = dict(uppgift=..., stod=[ "E: ...", "C: ...", "A: ..." ])
- LAB = dict(titel, syfte, material, utforande=[steg], fragor=[(fråga,facit)], bonus="…")
- F (fördjupning) = lista av sektioner (samma format som S, id "f1"..), F_UPPG = som UPPG men första elementet är nivå "●" "●●" "●●●", F_SAMMAN=[…], F_BEGR=[(term,förklaring)]
- BEGREPP 12–16 st, SAMMAN 6–8 punkter.
- SCEN = None (kemi har ingen tidsresa). (Ignorera resten av SCEN-beskrivningen.) Ignored: dict(titel="…", plats="…", tid="…", sky=("#färg1","#färg2"), mark="#färg", walker=dict(typ=PERSON), etapper=[ dict(x_etikett="Kort", tid="1789", plats="Paris", rubrik="…", fakta=[2–3 stycken à 1–2 meningar], fraga="…", alt=[3 alt], ratt=index, forklaring="…", deko=[("assetnamn", dx, skala)...]) , … 7 etapper ], diskutera="Diskussionsfråga" )
  PERSON: typ ∈ {"bonde","soldat","handlare","arbetare","medborgare","sjoman","resenar"}. Etapperna är i kronologisk ordning; sista etappen = sammanfattning (utan fråga, med "diskutera"). deko-assets ska väljas från /tmp/kemi/ASSETS.txt (lista skapas parallellt av Claude; om du saknar ett: välj närmaste och skriv ett förslag i en kommentar på raden efter).
