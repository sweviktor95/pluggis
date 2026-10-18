# -*- coding: utf-8 -*-
"""Kapitel 2 Cellen – fördjupning (nya ramverket, per moment)."""
import sys
sys.path.insert(0, '/tmp/bio')
from bstyle import *
import fordj_common as C
from fordj_common import roww
FIG = '/tmp/bio/fig02n/'
NR = 2
SLUG = "cellen"
TAB = "2+"
NAMN = "Cellen och livets processer"
UNDER = "Hur kommer ämnen in i cellen – och varför ser livet ut som det gör?"
INTRO = ("Varför blir en vissen sallad fräsch av kallt vatten? Hur kan en växtrot ta upp näring som det redan finns mer av inne i cellen än utanför? "
         "Och varför har dina celler små ”bakterier” inuti sig? I den här fördjupningen resonerar du om hur celler tar upp ämnen, om hur bladet är byggt, "
         "om vad som begränsar fotosyntesen och om hur växten transporterar vatten och socker. Namn och mätvärden i uppgifterna är påhittade exempel.")
MAL = ["Resonera i flera led: visa hur en sak leder till nästa, med ”eftersom … därför … vilket leder till …”.", "Använd begreppen korrekt och förklara dem i sammanhanget.",
       "Koppla byggnad till funktion: förklara varför något är format som det är.", "Var nyanserad: visa vad som är säkert, vad som är en teori och vad man mer skulle behöva veta.",
       "Planera en enkel undersökning och värdera hur säker slutsatsen blir."]
MAL_RUBRIK = "SÅ NÅR DU HÖGSTA NIVÅN"
FUNDERA = "Läs först grundtexten i kapitel 2. Fördjupningen bygger på begreppen cellmembran, cellvägg, vakuol, mitokondrie, kloroplast, fotosyntes, cellandning och organsystem."
D = {"2.1": "Cellen", "2.2": "Fotosyntes och cellandning", "2.3": "Organ och organsystem"}

S = []; FOOTS = []
def add(nr, t, delomr, inner):
    S.append((nr, t, inner)); FOOTS.append(f"Fördjupning {NR} · Delområde {delomr} {D[delomr]} · {t}")

add("F2.1.2", "Transport över cellmembranet", "2.1",
 "<p>Cellen måste hela tiden ta upp ämnen som den behöver och göra sig av med sådant den inte vill ha. Det sker genom cellmembranet, som släpper igenom vissa ämnen lättare än andra. Det finns tre huvudsakliga sätt för ämnen att ta sig över.</p>"
 + fig(FIG+"f_osmos.png", "<b>Bild F2.1</b> Tre sätt att ta sig över ett membran. Den streckade linjen är membranet.", "76%")
 + row("<p><strong class='green'>Diffusion.</strong> Alla ämnen i vätska och gas rör sig på måfå. Därför sprids de så småningom ut jämnt: nettorörelsen går från ett ställe där det finns mycket till ett där det finns lite. Det kräver ingen energi. Så tar sig till exempel syre in i cellen och koldioxid ut ur den.</p>"
       "<p><strong class='green'>Osmos.</strong> Osmos är diffusion av vatten genom ett membran som släpper igenom vatten men inte de lösta ämnena. Vattnet rör sig mot sidan där det finns mest löst ämne. Det kräver ingen energi.</p>"
       "<p><strong class='green'>Aktiv transport.</strong> Ibland behöver cellen ta in ett ämne <em>fastän</em> det redan finns mer av det inne i cellen. Då måste cellen pumpa mot strömmen, med hjälp av särskilda proteiner i membranet. Det kostar energi från cellandningen.</p>",
       [begrepp([("Diffusion", "Ämnen sprids från högre till lägre halt. Kräver ingen energi."), ("Osmos", "Vatten rör sig genom ett membran mot den sida där det finns mer löst ämne."), ("Aktiv transport", "Ämnen flyttas mot haltskillnaden. Kräver energi."), ("Turgor", "Trycket från vätskan i en växtcell mot cellväggen.")]),
        box("tank", "Tänk efter", "<p>Du la potatisbitar i kranvatten och saltlösning i labbarna. Vilken typ av transport flyttade vatten in i och ut ur potatiscellerna?</p>")])
 + "<h3>Varför växter blir stinna – och slokar</h3>"
 + row("<p>I en växtcell fyller den stora vakuolen mycket av cellen. När det finns mycket vatten tar cellen upp vatten med osmos, vakuolen sväller och trycker cellens innehåll mot den stela cellväggen. Cellen blir fast, och trycket kallas <strong>turgor</strong>. Många fasta celler tillsammans håller upp bladen och mjuka stjälkar. När växten får för lite vatten sjunker turgorn och växten slokar.</p>"
       "<p>Cellväggen gör att växtceller inte spricker i rent vatten. Djurceller har ingen cellvägg och kan svälla så mycket att de spricker, eller krympa i saltlösning. Därför måste kroppsvätskan hos djur hålla rätt halt av salter.</p>",
       [box("visste", "Visste du?", "<p>Rotens celler tar upp mineralämnen som nitrat med aktiv transport. Därför kan en rot som översvämmas och får brist på syre få svårt att ta upp näring: utan cellandning finns ingen energi till pumparna.</p>")]))

add("F2.1.4", "Mitokondrier och kloroplaster – en gammal historia", "2.1",
 "<p>Mitokondrier och kloroplaster har något märkligt gemensamt: de är nästan som små celler inne i cellen. Det har fått forskare att föreslå att de en gång var egna bakterier.</p>"
 + fig(FIG+"f_endo.png", "<b>Bild F2.2</b> Så tänker man sig att mitokondrier (överst) och kloroplaster (nederst) uppstod.", "96%")
 + roww("<p>Idén kallas <strong class='green'>endosymbiosteorin</strong> och drevs på 1960-talet bland andra av biologen Lynn Margulis. För över en miljard år sedan skulle en större cell ha tagit in en liten bakterie utan att bryta ner den. Bakterien fick skydd och näring, och cellen fick tillgång till bakteriens förmåga: att göra cellandning (mitokondrien) eller fotosyntes (kloroplasten). Efter många generationer kunde varken cellen eller bakterien leva utan den andra.</p>"
        "<h3>Vad talar för teorin?</h3>"
        + bullets(["Båda har <strong>egen DNA</strong>, och den är ringformad som hos bakterier.", "Båda har <strong>egna ribosomer</strong> som liknar bakteriernas.", "Båda är omgivna av <strong>dubbla membran</strong>, vilket passar med att de en gång tagits in i en blåsa.", "Båda <strong>delar sig själva</strong> inne i cellen, som bakterier gör, och är ungefär lika stora som bakterier."])
        + "<p>Teorin är mycket väl understödd, och de flesta forskare anser att den stämmer för mitokondrier och kloroplaster. Men den beskriver något som hände för mycket länge sedan, så ingen har sett det ske. Man drar slutsatser av spår som finns kvar, och detaljerna är fortfarande under utredning.</p>",
        [begrepp([("Endosymbios", "Ett samliv där en organism lever inuti en annan, till nytta för båda."), ("Teori", "En förklaring som stöds av många oberoende observationer, och som ständigt prövas.")]),
         box("fundera", "Fundera", "<p>Varför har inte djurceller kloroplaster, om teorin stämmer? Använd bildens ordning: vad måste ha hänt först?</p>")]))

add("F2.2.1", "Bladet – en fabrik för fotosyntes", "2.2",
 "<p>Ett blad är nästan en optimerad fabrik. Det är tunt och platt, så att ljuset når alla celler och så att koldioxid snabbt kan nå in. Titta på ett tvärsnitt genom ett blad och du ser att det är uppbyggt av lager, där varje lager har sin uppgift.</p>"
 + fig(FIG+"f_blad.png", "<b>Bild F2.3</b> Tvärsnitt genom ett blad (förenklad bild).", "100%")
 + row("<p><strong class='green'>Kutikulan</strong> är ett vaxartat lager som minskar att vatten avdunstar. <strong class='green'>Epidermis</strong> är ytterlagret, ett tunt skyddande skikt av celler. Det är nästan genomskinligt så att ljuset kan komma igenom.</p>"
       "<p><strong class='green'>Palisadvävnaden</strong> består av avlånga celler tätt packade under ovansidan. De har många kloroplaster och sitter där det är mest ljus. <strong class='green'>Svampvävnaden</strong> har rundare celler med luftrum mellan sig, så att gaserna kan sprida sig inne i bladet.</p>"
       "<p>På undersidan finns många <strong class='green'>klyvöppningar</strong>. Varje öppning omges av två <strong>slutceller</strong> som öppnar och stänger den. Koldioxid kommer in och syre och vattenånga kommer ut. I <strong class='green'>ledningssträngarna</strong>, bladets nerver, transporteras vatten in och socker ut.</p>",
       [box("tank", "Resonera", "<p>Varför sitter de flesta kloroplaster högst upp i bladet, medan de flesta klyvöppningar sitter på undersidan? Vad skulle hända med bladets vattenförlust om de satt på ovansidan i solen?</p>"),
        box("klimat", "Dilemmat", "<p>När klyvöppningarna är öppna kommer koldioxid in, men vatten avdunstar. När de är stängda sparas vatten, men fotosyntesen minskar. Växten måste hela tiden balansera dem. Många växter stänger dem vid torka.</p>")]))

add("F2.2.2", "Vad begränsar fotosyntesen?", "2.2",
 "<p>Fotosyntesen behöver ljus, koldioxid och vatten, och den fungerar bara vid lagom temperatur. Hur snabbt den går bestäms inte av allt som finns i överflöd, utan av det som finns <em>minst</em> av i förhållande till behovet. Det kallas den <strong class='green'>begränsande faktorn</strong>.</p>"
 + fig(FIG+"f_begr.png", "<b>Bild F2.4</b> Fotosyntesens hastighet vid ökande ljus, med lite eller mycket koldioxid (schematisk bild, inga riktiga mätvärden).", "86%")
 + row("<p>Läs bilden från vänster. Vid svagt ljus ökar fotosyntesen när ljuset ökar: då är ljuset den begränsande faktorn. Men längre till höger händer inget mer, hur mycket ljus man än tillför. Då är något annat begränsande, här koldioxid. Det syns på att kurvan med mer koldioxid fortsätter högre upp.</p>"
       "<p><strong>Temperatur.</strong> Fotosyntesen styrs av enzymer. Vid låga temperaturer går reaktionerna långsamt. När temperaturen stiger går de fortare, men vid för hög temperatur (ofta över 40 °C) skadas enzymerna och fotosyntesen avtar kraftigt.</p>"
       "<p><strong>Koldioxid.</strong> Luften innehåller bara ungefär 0,04 procent koldioxid, så den kan ofta vara begränsande på ljusa, varma dagar. Det är därför vissa odlare i växthus tillsätter extra koldioxid, utöver ljus och värme.</p>",
       [box("varning", "Obs!", "<p>En faktor som är begränsande vid ett tillfälle kan vara det en annan dag. Det kan också vara flera faktorer samtidigt. Därför ändrar man bara en sak i taget när man undersöker.</p>"),
        box("tank", "Tänk efter", "<p>Du fördubblar ljuset till en växt som står i ett mörkt hörn, och fotosyntesen går mycket fortare. Vilken faktor var begränsande?</p>")]))

add("F2.2.4", "Jäsning – energi utan syre", "2.2",
 "<p>I grundtexten såg du att jäst kan få energi även utan syre. Det kallas <strong class='green'>jäsning</strong>. Glukosen bryts då ner bara delvis. Det går att leva på, men man får betydligt mindre energi än i cellandningen, ungefär 2 energibärande molekyler (ATP) per glukos i stället för ungefär 30. Det finns två vanliga sorters jäsning.</p>"
 + table(["", "Alkoholjäsning", "Mjölksyrajäsning"],
         [["Sker i", "jästsvampar", "mjölksyrabakterier och våra muskelceller"],
          ["Glukos blir", "etanol (alkohol) och koldioxid", "mjölksyra"],
          ["Energi", "lite", "lite"],
          ["Används till", "bröd, öl och vin", "filmjölk, yoghurt, surkål"]], "tbl")
 + row("<p><strong>Bröd.</strong> När jästen jäser sockret i degen bildas koldioxid. Gasen bildar bubblor som får degen att jäsa upp och bli luftig. Alkoholen avdunstar när brödet gräddas.</p>"
       "<p><strong>Filmjölk.</strong> Mjölksyrabakterier jäser mjölksockret. Mjölksyran gör mjölken sur, och den hindrar andra bakterier från att växa. Därför håller sig fil länge, jämfört med mjölk.</p>"
       "<p><strong>Muskler.</strong> Vid mycket hårt arbete räcker inte syretillförseln alltid till. Musklerna kan då under kort tid få extra energi genom mjölksyrajäsning. När du vilar och andas lugnt kan mjölksyran användas igen.</p>",
       [box("tank", "Resonera", "<p>Varför kan inte musklerna leva på jäsning hela tiden? Tänk på hur mycket energi man får.</p>"),
        box("visste", "Visste du?", "<p>Cellandning och jäsning börjar på samma sätt: glukosen delas i cytoplasman. Skillnaden är vad som händer sedan, med eller utan syre.</p>")]))

add("F2.3.3", "Växtens organ och transport", "2.3",
 "<p>En växt är, precis som ett djur, uppbyggd av celler som bildar vävnader och organ. De viktigaste organen är roten, stjälken och bladet, och de samarbetar som ett organsystem.</p>"
 + fig(FIG+"f_vaxt.png", "<b>Bild F2.5</b> Växtens organ och dess två transportsystem.", "100%")
 + row("<p><strong>Roten</strong> fäster växten och tar upp vatten och mineralämnen. Rothåren gör ytan stor. <strong>Stjälken</strong> bär upp bladen mot ljuset och innehåller transportrören. <strong>Bladet</strong> gör fotosyntes. Blomman har en annan uppgift: förökning.</p>"
       "<p><strong class='green'>Xylem</strong> (vattenledningen) transporterar vatten och mineralämnen från roten upp till bladen, åt ett håll. Rören består av döda, ihåliga celler med förstärkta väggar. När vatten avdunstar från bladen genom klyvöppningarna, dras nytt vatten upp efter, ungefär som när man dricker med sugrör.</p>"
       "<p><strong class='green'>Floem</strong> (sockerledningen) transporterar socker från bladen till de delar som behöver det, till exempel rötter, frukter och växande skott, eller dit växten lagrar det, som i potatisknölen. Floemets celler är levande. Transporten kan gå åt olika håll beroende på var sockret behövs.</p>",
       [begrepp([("Xylem", "Rör som leder vatten och mineraler uppåt."), ("Floem", "Rör som leder socker dit det behövs.")]),
        box("tank", "Tänk efter", "<p>På våren, när trädet skjuter nya blad, kommer sockret från rötterna och stammen. På sommaren kommer det från bladen. Vad säger det om floemets riktning?</p>")]))

UPG = [
 ("En morot delas i två stavar. Den ena läggs i kranvatten och den andra i mycket salt vatten. Efter en timme är den ena stinn och den andra mjuk. a) Vilken är vilken? Förklara med osmos och turgor. b) Förklara varför en vissen sallad blir fräsch av kallt vatten. c) Varför är saltvatten dåligt som vatten till krukväxter?", 3),
 ("Rotceller kan ta upp nitrat från jorden fastän halten i cellen redan är högre än utanför. a) Förklara varför det inte kan vara diffusion. b) Hur tar cellen upp nitratet, och vad kostar det? c) Förklara varför växter i översvämmad jord kan få näringsbrist trots att det finns gott om vatten.", 3),
 ("Mitokondrier och kloroplaster tros komma från bakterier. a) Beskriv två iakttagelser som stöder teorin. b) Förklara varför man kallar det en teori och inte säker kunskap. c) Vad innebär teorin för hur man ser på cellens uppbyggnad: är en cell med mitokondrier ”en” organism? Argumentera.", 3),
 ("En tomatodlare ökar belysningen i växthuset kraftigt, men fotosyntesen ökar knappt. a) Förklara med begreppet begränsande faktor varför. b) Föreslå två andra faktorer som kan begränsa och hur odlaren kan undersöka vilken det är. c) Värdera: är det en bra idé att tillsätta extra koldioxid? Ta hänsyn till både nytta och kostnad.", 3),
 ("En bagare gör degen och låter den jäsa varmt. a) Förklara vad som händer i jästcellerna och varför degen blir luftig. b) Varför ger jäsning mindre energi än cellandning? c) Jämför bagarens jäst med en muskelcell vid hårt arbete.", 3),
 ("Man tar bort en ring av bark runt hela en trädstam, ner till veden. Trädet lever först kvar men dör efter något år. Förklara varför det inte dör genast och varför det ändå dör till slut. Använd begreppen xylem, floem och fotosyntes. Förklara också vilket av transportsystemen som skadas först.", 3),
]
def uppg_html(): return C.uppg_html(UPG, 4)
SVAR = [
 "a) Staven i kranvatten är stinn: vatten rörde sig med osmos in i cellerna eftersom halten löst ämne är högre inuti, vakuolerna svällde och cellväggen gav turgor. Staven i saltvatten är mjuk: vatten rörde sig ut ur cellerna mot den saltrikare sidan, och turgorn sjönk. b) Vattnet tas upp med osmos och turgorn byggs upp igen. c) Salt vatten runt rötterna kan dra vatten ut ur rotcellerna, så växten får torka trots att det finns vatten.",
 "a) Diffusion går från hög till låg halt, här skulle nitratet i så fall röra sig ut. b) Med aktiv transport: proteiner i membranet pumpar in nitratet mot haltskillnaden, och det kostar energi från cellandningen. c) I översvämmad jord är syret slut, så rötternas cellandning minskar och därmed energin till pumparna. Upptaget av mineraler minskar.",
 "a) T.ex. egen ringformad DNA, egna ribosomer, dubbla membran, delar sig själva. b) Man har inte kunnat se det ske, utan drar slutsatser från spår. Det finns stark men indirekt evidens, och en teori kan förbättras när man får nya fynd. c) Öppet svar. Ett välutvecklat svar nämner att mitokondrien delar sig själv och har eget DNA, men är så beroende av cellen att den inte kan leva fritt, så gränsen är oskarp.",
 "a) Ljuset var inte längre begränsande, och något annat, till exempel koldioxid eller temperatur, satte tak. b) Koldioxid och temperatur. Ändra en faktor i taget och mät fotosyntesens hastighet (t.ex. syrebildning), med kontrollgrupp. c) Extra koldioxid kan ge större skörd om koldioxid är begränsande, men det kostar pengar och är bara värt det om ljus och värme redan är tillräckliga. Ett välutvecklat svar väger kostnad mot nytta.",
 "a) Jästen jäser sockret och bildar koldioxid och etanol. Koldioxidgasen bildar bubblor i degen. b) Glukosen bryts bara ner delvis (etanolen innehåller kvar energi) och ingen syre används, så färre energibärande molekyler bildas. c) Muskelcellen kan också jäsa glukos utan syre, men bildar mjölksyra, inte etanol och koldioxid.",
 "Barken innehåller floemet, medan xylemet ligger inne i veden. När barken tas bort bryts floemet, men xylemet fungerar så att vatten och mineraler fortsätter upp till bladen. Bladen gör fortfarande fotosyntes. Men sockret kan inte transporteras ner till rötterna, som först lever på lagrad näring och sedan svälter. När rötterna dör kan trädet inte ta upp vatten, och hela trädet dör. Ett välutvecklat svar förklarar kedjan i flera led.",
]
RUTOR = [("Tänk efter (Transport över cellmembranet):", "Osmos: vatten rörde sig genom cellmembranet in i bitarna i kranvatten och ut ur bitarna i saltlösning."),
         ("Fundera (Mitokondrier och kloroplaster):", "Kloroplasten kom från en fotosyntetiserande bakterie som togs upp av en cell som redan hade mitokondrier. Djurcellernas förfäder tog aldrig in en sådan bakterie, eller den försvann."),
         ("Resonera (Bladet):", "Ljuset kommer uppifrån, så fotosyntesen sker där. Klyvöppningar på undersidan förlorar mindre vatten än om de satt i solen på ovansidan."),
         ("Tänk efter (Vad begränsar fotosyntesen?):", "Ljuset var begränsande."),
         ("Resonera (Jäsning):", "Jäsning ger bara en femtondel av energin och bildar mjölksyra som ansamlas, så man kan bara göra det en kort stund."),
         ("Tänk efter (Växtens organ och transport):", "Floemet kan transportera åt olika håll, beroende på var sockret finns och var det behövs.")]
def teacher_html():
    return C.teacher_html("Fördjupningen riktar sig till elever som är klara tidigt eller som behöver mer utmaning mot de högre kriterierna. Den fördjupar transport över cellmembranet, endosymbiosteorin, bladets byggnad, begränsande faktorer, jäsning och växtens transportsystem, och tränar det resonemang som krävs på högsta nivå.",
      SVAR, RUTOR,
      "Källstatus (kontrollerat 2026-10-14 mot öppnade sidor, se lärarversionens källförteckning): bladets byggnad, jäsning, begränsande faktorer, endosymbiosens belägg, xylem och floem samt diffusion, osmos, aktiv transport och turgor är kontrollerade mot minst en öppnad källa. Delvis kontrollerat: att palisadvävnaden har flest kloroplaster (källan säger bara 'många' i mesofyllet), temperaturen 40 °C, koldioxidhalten 0,04 %, rotens aktiva upptag av nitrat, Margulis och tidsangivelsen för endosymbiosen. Ej källkontrollerat: att floemet ligger i innerbarken (uppgift 6, ringbarkning). Energiutbytet 2 mot ca 30 ATP är ett avrundat modernt läroboksvärde (en källa anger upp till 36). Figurerna är schematiska. Allt är utkast som läraren bör granska. Källor: Skolverket, Lgr22 kursplan i biologi. · Illustrationer: egenritade.")
