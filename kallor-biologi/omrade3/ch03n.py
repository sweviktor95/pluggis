# -*- coding: utf-8 -*-
"""Område 3 Biologisk mångfald – grundtext (nya ramverket, per moment). Samma format som område 1, 2 och 4."""
import sys
sys.path.insert(0, '/tmp/bio')
from bstyle import *
FIG = '/tmp/bio/fig03n/'
NR = 3
SLUG = "mangfald"
TAB = "3"
NAMN = "Biologisk mångfald"
UNDER = "Livets variation – och varför vi behöver den"
INTRO = ("Ställ dig i en skog i Norrbotten en stilla morgon. Du ser tallar, granar och blåbärsris. Men det mesta av livet ser du inte. I marken under dina fötter finns svamptrådar, maskar, kvalster och miljarder bakterier. "
         "I trädkronorna sitter lavar, insekter och fåglar. Allt hänger ihop, och människan är en del av samma nät. I det här kapitlet lär du dig vad biologisk mångfald är, vad naturen gör för oss och vad som hotar den. "
         "Du lär dig också hur forskare ordnar livet i grupper, hur du bestämmer en art med en nyckel och hur arter anpassar sig till sin miljö. Namn och mätvärden i uppgifterna är påhittade, om inget annat står.")
MAL = ["vad biologisk mångfald är och vilka tre nivåer den har", "vilka ekosystemtjänster naturen ger oss och varför mångfald gör dem säkrare",
       "vad som hotar mångfalden, vad rödlistan visar och vad som kan göras", "hur man undersöker artrikedom med en enkel fältstudie",
       "hur organismer delas in i riken och hur man bestämmer en art med en nyckel", "vad en anpassning är och hur naturligt urval fungerar"]
FUNDERA = "Vilka vilda djur, växter och svampar kan du namnge från din närmaste skog eller strand? Skriv ner så många du kan på två minuter. Räkna sedan: hur många olika sorter blev det?"
DELOMR = {"3.1": "Mångfald, hot och ekosystemtjänster", "3.2": "Gruppera och organismvärlden"}

def roww(m, side):
    return row(m, side).replace('class="row"', 'class="row w"', 1)
def cards4(items):
    return '<div class="cards" style="grid-template-columns:repeat(%d,1fr)">' % len(items) + "".join(f'<div class="card"><b class="h">{h}</b>{t}</div>' for h, t in items) + '</div>'

# Kontrollfrågor med facit (samma källa för häftet och lärarhandledningen)
KQ = {
 "Start": [("Vad menas med biologisk mångfald?", "Variationen av liv på jorden: gener, arter och ekosystem."),
           ("Varför räcker det inte att bara räkna antalet arter?", "Mångfald finns också inom arter (genetisk variation) och mellan livsmiljöer (ekosystem). Dessutom säger antalet inte hur arterna hänger ihop."),
           ("Vad vet forskarna om hur många arter det finns?", "Bara drygt två miljoner är beskrivna. Hur många som finns totalt vet ingen, men det är betydligt fler.")],
 "3.1.1": [("Vilka är de tre nivåerna av biologisk mångfald? Ge ett exempel på varje.", "Genetisk mångfald (tallar med olika gener), artmångfald (gran, räv, flugsvamp) och ekosystemmångfald (fjäll, skog, myr, älv)."),
           ("Förklara med egna ord vad en art är.", "Individer som kan få fortplantningsdugliga ungar med varandra."),
           ("Varför kan stor genetisk variation hjälpa en art att överleva när klimatet blir varmare?", "Individerna har olika gener och tål olika saker. När klimatet ändras överlever de som har gener som passar, och de får ungar. Arten kan därför anpassa sig."),
           ("Förklara varför ett artrikt ekosystem klarar störningar bättre än ett artfattigt.", "Det finns fler arter som kan ta över en uppgift, till exempel fler arter som räven kan äta när sorken blir färre. Det är fler reservdelar.")],
 "3.1.2": [("Ge ett exempel på varje typ av ekosystemtjänst.", "Försörjande: bär, fisk, virke. Reglerande: pollinering, vattenrening. Stödjande: bördig jord, fotosyntes. Kulturella: friluftsliv, jakt, fiske."),
           ("Hur kan en myr minska risken för översvämningar?", "Den suger upp vatten vid kraftiga regn som en svamp och släpper ut det långsamt."),
           ("Förklara varför många olika arter av pollinerare är bättre än en enda.", "Om en art får ett dåligt år kan de andra fortfarande pollinera. Många arter gör tjänsten säkrare."),
           ("Vad är skillnaden mellan en försörjande och en reglerande ekosystemtjänst?", "Försörjande tjänster är saker vi tar från naturen (mat, virke). Reglerande tjänster är sådant naturen styr eller renar (pollinering, vattenrening, koldioxid).")],
 "3.1.3": [("Nämn tre hot mot den biologiska mångfalden och ge ett exempel på varje.", "T.ex. ändrad markanvändning (avverkad skog), överuttag (överfiske), klimatförändringar, föroreningar (plast, miljögifter) och invasiva arter (blomsterlupin)."),
           ("Vad är en rödlista?", "En förteckning över arter och hur stor risken är att de försvinner, som forskare vid SLU Artdatabanken uppdaterar."),
           ("Ge två orsaker till att fjällräven har haft svårt att öka.", "T.ex. jakt förr, brist på lämlar och att rödräven konkurrerar om mat och lyor."),
           ("Vad är en signalart? Ge ett exempel.", "En art som visar att en miljö har höga naturvärden, t.ex. garnlav som visar gammal skog."),
           ("Ge ett argument för och ett emot att avverka en gammal skog.", "För: jobb och virke. Emot: livsmiljöer för många arter försvinner och tar hundratals år att återskapa.")],
 "3.2.1": [("Nämn de fem rikena.", "Djur, växter, svampar, bakterier och encelliga organismer med cellkärna."),
           ("Vad skiljer en svamp från en växt?", "Svampen gör ingen fotosyntes utan tar upp näring från död eller levande materia. Den har cellvägg av annat material än växten."),
           ("Hur skrivs en arts vetenskapliga namn, och vad står de två orden för?", "Två latinska ord, släktnamn och artnamn, t.ex. Pinus sylvestris (tall). Första ordet har stor bokstav."),
           ("Vad är en lav?", "En samlevnad mellan en svamp och en alg eller bakterie som gör fotosyntes. De hjälper varandra.")],
 "3.2.2": [("Vad är en bestämningsnyckel?", "En serie val med två alternativ där varje val leder till nästa tills man kommer fram till arten."),
           ("Använd nyckeln på bild 3.9. Vilket träd har barr som sitter ensamma runt kvisten?", "Gran."),
           ("Varför ska nyckeln bara ha två alternativ i varje steg?", "Det gör valet tydligt: antingen stämmer det ena eller det andra."),
           ("Hitta på ett eget första steg i en nyckel för tre djur: gädda, räv och duva.", "T.ex. Har djuret fjädrar? Ja: duva. Nej: gå vidare. Lever det i vatten? Ja: gädda. Nej: räv.")],
 "3.2.3": [("Vad är en anpassning? Ge ett exempel.", "Ett drag hos en art som gör att den klarar sin miljö, t.ex. fjällrävens tjocka päls och små öron."),
           ("Varför överlever de ljusa pepparfjärilarna oftare i en skog med ljus bark?", "De är svåra för fåglar att se. De mörka syns lättare och blir uppätna oftare."),
           ("Förklara med variation, urval och ärftlighet hur en art kan ändras över generationer.", "Individerna är olika (variation). De med de mest passande dragen överlever och får fler ungar (urval). Dragen går i arv, så de blir vanligare."),
           ("Varför är en anpassning ingen sak som en individ bestämmer sig för?", "Anpassningar uppstår genom att gener som passar blir vanligare över generationer, inte genom att en individ väljer.")],
}
def kq(key):
    return kolla(key if key != "Start" else "Start", [q for q, a in KQ[key]])

S = []
FOOTS = []
def add(nr, t, foot, inner):
    S.append((nr, t, inner)); FOOTS.append(foot)

# ------------------------------------------------------------------ Start
add("Start", "Hur mycket liv finns det?", f"Kapitel {NR} · {NAMN} · Start",
 row("<p><strong class='green'>Biologisk mångfald</strong> betyder variationen av liv på jorden. Ordet används ofta om hur många arter som finns, men det är bara en del av sanningen. Forskare delar in mångfalden i <strong class='green'>tre nivåer</strong> som hänger ihop: gener, arter och ekosystem. Du lär dig dem i det första momentet.</p>"
     "<p>Forskare har hittills beskrivit drygt två miljoner arter, men hur många som finns totalt vet ingen. Uppskattningarna varierar från några miljoner till långt fler, och de flesta oupptäckta arterna är troligen insekter, svampar och mikroorganismer.</p>"
     "<p>I det här kapitlet svarar vi på fem frågor:</p>"
     + bullets(["Vad är biologisk mångfald, och på vilka nivåer finns den?", "Vad gör naturen för oss, och varför är mångfalden viktig för det?", "Vad hotar mångfalden, och vad kan vi göra?",
                "Hur ordnar forskare allt levande i grupper, och hur kan du själv bestämma en art?", "Hur har arterna anpassat sig till sin miljö?"]),
   [begrepp([("Biologisk mångfald", "Variationen av liv: genetisk mångfald, artmångfald och ekosystemmångfald."), ("Art", "Individer som kan få fortplantningsdugliga ungar med varandra."),
             ("Ekosystem", "Alla organismer i ett område och den miljö de lever i.")]),
    box("tank", "Tänk efter", "<p>Vad är artrikast: en blåbärsskog eller en gräsmatta? Hur kan du ta reda på det?</p>")])
 + table(["Delområde", "Du lär dig"],
         [["<b>3.1</b> Mångfald, hot och ekosystemtjänster", "Mångfaldens nivåer, vad naturen gör för oss, hoten mot mångfalden och vad vi kan göra. Labb: artinventering i en provruta."],
          ["<b>3.2</b> Gruppera och organismvärlden", "De fem rikena, bestämningsnycklar och hur arter anpassar sig. Labb: artbestämning med nyckel."]])
 + kq("Start"))

# ------------------------------------------------------------------ 3.1.1
add("3.1.1", "Gener, arter och ekosystem", f"Kapitel {NR} · Delområde 3.1 {DELOMR['3.1']} · Gener, arter och ekosystem",
 "<p>Biologisk mångfald finns på tre nivåer: <strong class='green'>inom arter</strong>, <strong class='green'>mellan arter</strong> och <strong class='green'>mellan ekosystem</strong>. Alla tre är viktiga, och de påverkar varandra.</p>"
 + fig(FIG+"mangfald-tre-nivaer.png", "<b>Bild 3.1</b> Biologisk mångfald finns på tre nivåer: inom arter, mellan arter och mellan ekosystem.", "96%")
 + row("<h3 style='margin-top:0'>1. Genetisk mångfald: variation inom en art</h3><p>Alla tallar tillhör samma art, men ingen tall är exakt lik en annan. Deras <strong class='green'>gener</strong> skiljer sig lite åt. En tall kanske tål torka bättre, en annan klarar kyla eller en viss svampsjukdom. När miljön förändras är det de individer som har ”rätt” gener som överlever och får ungar. Därför gör stor genetisk variation att en art kan anpassa sig.</p>"
       "<h3>2. Artmångfald: variation mellan arter</h3><p><strong class='green'>Artmångfald</strong> handlar om variationen mellan arter. Ett vanligt mått är <strong class='green'>artrikedom</strong>: antalet olika arter i ett område. En <strong class='green'>art</strong> är en grupp individer som kan para sig med varandra och få ungar som också kan få ungar. En blåbärsskog med hundratals arter av insekter, svampar och mossor har större artrikedom än en gräsmatta. Alla individer av en art i ett område kallas en <strong class='green'>population</strong>.</p>"
       "<h3>3. Ekosystemmångfald: variation mellan livsmiljöer</h3><p>Fjäll, myr, gammal skog, älv och skärgård är olika ekosystem. Varje ekosystem har sina egna arter och sitt eget samspel. Om ett landskap bara har en typ av miljö, till exempel planterad skog i samma ålder, försvinner arter som behöver något annat.</p>",
       [begrepp([("Gen", "En del av arvsmassan (DNA) som styr en egenskap."), ("Population", "Alla individer av en art inom ett område."), ("Artrikedom", "Antalet olika arter i ett område.")]),
        box("visste", "Visste du?", "<p>Forskare har hittills beskrivit drygt två miljoner arter. Siffran är osäker, eftersom en del arter har fått flera namn. Hur många som finns totalt vet ingen: uppskattningarna går från några miljoner till betydligt fler.</p>"),
        box("tank", "Tänk efter", "<p>Varför räcker det inte att räkna antalet arter för att veta hur rik naturen är i ett område?</p>")])
 + "<h3>Mångfald ger starka ekosystem</h3>"
 + roww("<p>I ett ekosystem är alla arter beroende av varandra. Gröna växter är <strong class='green'>producenter</strong>: med hjälp av solljus bygger de upp socker med fotosyntes. Djur är <strong class='green'>konsumenter</strong> som får sin energi genom att äta växter eller andra djur. <strong class='green'>Nedbrytare</strong> som svampar och bakterier bryter ner döda växter och djur så att näringen kan användas igen. I naturen äter de flesta djur flera olika saker, så man ritar en <strong class='green'>näringsväv</strong> med många sammanflätade kedjor. Du får lära dig mer om detta i kapitel 4.</p>"
        "<p>Ett ekosystem med många arter är oftast mer motståndskraftigt. Vissa år blir det ont om sork. Då kan räven äta mer skogshare eller tjäder i stället. I ett artfattigt system finns det färre ”reservdelar”. Man kan jämföra med ett nät: du kan klippa av några trådar utan att det går sönder, men klipper du av för många rasar det.</p>",
        [box("visste", "Ett exempel från historien", "<p>På 1840-talet odlade man nästan bara en sorts potatis på Irland. Alla plantor var genetiskt mycket lika. När sjukdomen potatisbladmögel kom fanns inga plantor som tålde den. Skördarna slogs ut och omkring en miljon människor dog av svält.</p>")])
 + fig(FIG+"mangfald-naringsvav.png", "<b>Bild 3.2</b> En förenklad näringsväv i en norrländsk barrskog. Pilarna visar åt vilket håll energin går: från den som blir äten till den som äter.", "86%")
 + box("tank", "Tänk efter", "<p>Titta på bild 3.2. Vad händer med räven om skogssorkarna blir färre? Vilken annan föda kan räven välja?</p>")
 + kq("3.1.1"))

# ------------------------------------------------------------------ 3.1.2
add("3.1.2", "Ekosystemtjänster", f"Kapitel {NR} · Delområde 3.1 {DELOMR['3.1']} · Ekosystemtjänster",
 row("<p>Allt vi äter, luften vi andas och vattnet vi dricker är beroende av andra arter. Det naturen gör för oss kallas <strong class='green'>ekosystemtjänster</strong>. De är gratis, och därför märker vi dem ofta inte förrän de slutar fungera. Man brukar dela in dem i fyra grupper.</p>",
     [begrepp([("Ekosystemtjänst", "Något som naturen gör och som människan har nytta av."), ("Pollinering", "När pollen förs från en blomma till en annan så att den kan bilda frön.")])])
 + fig(FIG+"ekotjanster.png", "<b>Bild 3.3</b> De fyra typerna av ekosystemtjänster.", "96%")
 + table(["Typ", "Vad naturen gör", "Exempel"],
         [["<b>Försörjande</b>", "Ger oss saker vi kan ta från naturen.", "mat, fisk, bär, virke, rent vatten, ämnen till läkemedel"],
          ["<b>Reglerande</b>", "Styr och renar.", "bin och humlor pollinerar, våtmarker renar vatten, skog tar upp koldioxid"],
          ["<b>Stödjande</b>", "Är grunden för allt annat.", "nedbrytare gör jorden bördig, växter bildar syre med fotosyntes"],
          ["<b>Kulturella</b>", "Ger oss upplevelser och värden.", "friluftsliv, jakt, fiske, vila, inspiration, kulturarv"]])
 + "<h3>Pollinering: en tjänst värd miljarder</h3>"
 + roww("<p>När en humla flyger mellan blommor för att samla nektar för den med sig pollen. Då blir blommorna befruktade och kan bilda frön och bär. Utan pollinerare skulle det bli mycket mindre blåbär, lingon, äpplen och raps. Ungefär tre av fyra av de grödor vi odlar är beroende av pollinatörer i någon grad, och omkring en tredjedel av världens matproduktion (räknat i vikt) kommer från sådana grödor. Utan pollinatörer skulle den totala produktionen ändå minska med bara några procent, men frukt, bär och nötter skulle drabbas hårdast.</p>"
        "<h3>Våtmarker och skog</h3><p>En myr fungerar som en svamp: den suger upp vatten vid kraftiga regn och släpper ut det långsamt. Det minskar risken för översvämningar. Samtidigt fastnar näringsämnen och partiklar, så att vattnet som rinner vidare blir renare. Skogen tar upp koldioxid när träden växer och lagrar kol i stammar och i marken.</p>"
        "<h3>Mångfald ger säkrare tjänster</h3><p>Om det finns många olika arter som pollinerar spelar det mindre roll om en av dem får ett dåligt år. Därför är biologisk mångfald en sorts försäkring för ekosystemtjänsterna.</p>",
        [box("visste", "Visste du?", "<p>I vissa fruktodlingar i Kina har det funnits så få bin att människor har fått pollinera blommorna för hand med små penslar. Det tar lång tid och kostar mycket pengar.</p>"),
         box("tank", "Tänk efter", "<p>Vilken typ av ekosystemtjänst är en vandring i fjällen? Och bär som du plockar?</p>")])
 + kq("3.1.2"))

# ------------------------------------------------------------------ 3.1.3
add("3.1.3", "Hoten mot mångfalden", f"Kapitel {NR} · Delområde 3.1 {DELOMR['3.1']} · Hoten mot mångfalden",
 row("<p>Arter har alltid dött ut och nya har utvecklats. Men i dag försvinner arter mycket snabbare än vad som är naturligt. FN:s expertpanel för biologisk mångfald, IPBES, bedömde 2019 att omkring en miljon djur- och växtarter är hotade av utrotning, många inom några årtionden. Nästan alla hot har samma grundorsak: människans aktiviteter. De fem största hoten, i den ordning IPBES rangordnar dem, är:</p>"
     + table(["Hot", "Vad det innebär", "Exempel"],
             [["<b>1. Ändrad mark- och havsanvändning</b>", "Livsmiljöer försvinner eller delas upp.", "skog avverkas, myrar dikas, ängar växer igen"],
              ["<b>2. Överuttag</b>", "Vi fiskar, jagar eller skördar mer än vad som hinner växa till.", "överfiske, tjuvjakt"],
              ["<b>3. Klimatförändringar</b>", "Arter måste flytta norrut eller uppåt.", "fjällens arter har ingenstans att ta vägen"],
              ["<b>4. Föroreningar</b>", "Miljögifter, plast och övergödning skadar liv i mark och vatten.", "övergödda sjöar, plast i havet"],
              ["<b>5. Invasiva arter</b>", "Främmande arter som människan fört in tränger undan de inhemska.", "blomsterlupin"]]),
   [begrepp([("Överuttag", "När människan tar mer ur naturen än vad som hinner växa till."), ("Invasiv art", "En art som människan fört in och som sprider sig och skadar inhemska arter."),
             ("Livsmiljö", "Den plats där en art kan leva och föröka sig.")])])
 + "<h3>Rödlistan: Sveriges hälsokontroll</h3>"
 + roww("<p>Ungefär vart femte år bedömer forskare vid SLU Artdatabanken hur stor risken är att olika arter försvinner från Sverige. Resultatet kallas <strong class='green'>rödlistan</strong>. I den senaste rödlistan, Rödlistan 2025, bedömdes 23 103 arter. Av dem var 5 217 rödlistade, och 2 373 räknades som hotade. Arter i kategorierna VU (sårbar), EN (starkt hotad) och CR (akut hotad) räknas som hotade. DD betyder att forskarna vet för lite om arten för att kunna bedöma den.</p>"
        "<p>Enligt Naturvårdsverket är igenväxning och avverkning de viktigaste negativa påverkansfaktorerna för rödlistade arter i Sverige, och jordbruks- och skogslandskapen hyser tillsammans över 75 procent av de rödlistade arterna. Bland de rödlistade finns också djur som många känner till, till exempel ålen. Men det finns goda nyheter: uttern och havsörnen har blivit så många igen att de inte längre är rödlistade.</p>",
        [box("klimat", "Granska kritiskt", "<p>Mellan år 2000 och 2025 ökade också antalet arter som forskarna bedömde, från cirka 19 000 till drygt 23 000. Betyder det att alla nya rödlistade arter i diagrammet har fått det sämre? Vilken annan förklaring kan finnas?</p>")])
 + fig(FIG+"mangfald-rodlista-diagram.png", "<b>Bild 3.4</b> Antal rödlistade arter i Sverige. Källa: SLU Artdatabanken.", "70%")
 + "<h3>Mångfald i Norrbotten</h3>"
 + row("<p><strong class='green'>Fjällräven</strong> jagades hårt för sin vackra vinterpäls. Den blev fridlyst 1928, men stammen återhämtade sig inte. Runt år 2000 uppskattade forskare att det bara fanns cirka 35–50 vuxna fjällrävar i hela Skandinavien. Fjällräven lever mest av lämlar, och lämmelåren har blivit ovanligare. Dessutom tar sig rödräven allt högre upp på fjället. Den är större och konkurrerar om både mat och lyor. Med stödutfodring och jakt på rödräv har fjällräven ökat igen, men den är fortfarande hotad.</p>"
       "<p><strong class='green'>Gammal skog</strong> som aldrig har kalavverkats har gamla träd, död ved och hängande lavar. Många arter kan bara leva där. Ett exempel är <strong class='green'>garnlaven</strong>, som hänger i långa grågröna trådar från granar. Den kallas en <strong class='green'>signalart</strong>: hittar man den är skogen troligen gammal och artrik. Hänglavar är också viktig vinterföda för renarna.</p>"
       "<p>Torne älv, Kalix älv, Pite älv och Vindelälven är Sveriges fyra nationalälvar. De skyddas av lag mot nya vattenkraftsutbyggnader.</p>",
       [fig(FIG+"mangfald-fjallrav-rodrav.png", "<b>Bild 3.5</b> Fjällräven (till vänster) är mindre och har kort nos och små öron. Rödräven har längre ben och stora öron.", "100%"),
        fig(FIG+"mangfald-garnlav.png", "<b>Bild 3.6</b> Garnlav, en signalart.", "70%"),
        begrepp([("Rödlista", "Förteckning över arter och deras risk att dö ut."), ("Signalart", "Art som visar att en miljö har höga naturvärden.")])])
 + "<div style='break-inside:avoid'><h3>Samhällsfrågan: vad ska skogen användas till?</h3>"
 + "<p>Skogen i Norrbotten ger jobb, virke och biobränsle. Den är också hem för tusentals arter och betesmark för renar. Olika grupper ser olika saker i samma skog.</p>"
 + cards4([("Skogsbolaget", "”Skogsbruket ger jobb i hela länet och virke som kan ersätta plast och betong. Vi lämnar kvar gamla träd och skyddar värdefulla områden.”"),
           ("Naturskyddsförening", "”Det finns för lite gammal skog kvar. Kalhyggen förstör livsmiljöer som tar hundratals år att bygga upp igen.”"),
           ("Renskötaren", "”När gammal skog avverkas försvinner hänglaven. Då har renarna mindre att äta på vintern.”"),
           ("Kommunen", "”Vi behöver både arbetstillfällen och natur som lockar turister och gör det skönt att bo här.”")])
 + "<p class='note'>Citaten är konstruerade för att visa olika perspektiv och är inte ordagranna uttalanden.</p></div>"
 + "<h3>Vad kan vi göra?</h3>"
 + roww("<p>Det viktigaste för att skydda den biologiska mångfalden är att bevara och återskapa livsmiljöer. Det sker på flera nivåer samtidigt. År 2022 kom världens länder överens om att skydda och bevara minst 30 procent av jordens land, sötvatten och hav till år 2030. I Sverige skyddar nationalparker och naturreservat natur, och lagar styr skogsbruk, jakt och fiske. I Norrbotten finns världsarvet Laponia med bland annat Sarek och Padjelanta.</p>"
        "<p>Ibland behöver naturen hjälp att återhämta sig. Man kan till exempel dämma igen diken så att en myr blir blöt igen, låta kor beta igenvuxna ängar eller bränna skog under kontroll, eftersom många arter är anpassade till skogsbränder. Du själv kan låta en bit gräsmatta bli äng, välja hållbart fiskad mat, rapportera arter du ser i Artportalen och aldrig slänga trädgårdsväxter i naturen.</p>",
        [box("tank", "Tänk efter", "<p>Vilka tre saker kan du göra själv för att gynna mångfalden där du bor?</p>")])
 + kq("3.1.3"))

# ------------------------------------------------------------------ Labb 3.1
add("Labb", "3.1 Artinventering i en provruta", f"Kapitel {NR} · Delområde 3.1 {DELOMR['3.1']} · Labb 3.1 Artinventering i en provruta",
 "<p>Du ska undersöka artrikedom med en enkel fältstudie: hur många olika växtsorter finns det i en kvadratmeter på två olika platser?</p>"
 + roww("<p><strong class='green'>Frågeställning:</strong> Finns det fler växtarter på en ängsmark än på en klippt gräsmatta?</p><p><strong class='green'>Hypotes:</strong> Skriv vad du tror och varför innan du börjar.</p>"
        "<p><strong class='green'>Material:</strong> fyra pinnar, snöre (ca 5 m), tumstock, mobilkamera eller artbok/app, papper och penna.</p><h3>Gör så här</h3>"
        + steps(["Märk ut en ruta på 1 × 1 meter med pinnar och snöre på ängen.",
                 "Räkna hur många olika växtarter som finns i rutan. Du behöver inte veta vad de heter: ta en bild och ge dem nummer.",
                 "Gör likadant på gräsmattan.",
                 "Upprepa med minst tre rutor på varje plats. Varför är det viktigt?",
                 "Skriv in resultatet i en tabell och räkna ut medelvärdet för varje plats."]),
        [fig(FIG+"mangfald-provruta.png", "<b>Bild 3.7</b> En provruta på 1 m².", "100%"),
         box("begrepp", "Begrepp", "<b class='t'>Provruta</b><p>Ett avgränsat område där man räknar.</p><b class='t'>Inventering</b><p>Att räkna och notera vilka arter som finns.</p><b class='t'>Medelvärde</b><p>Summan delat med antalet.</p>")])
 + table(["Plats", "Ruta 1", "Ruta 2", "Ruta 3", "Medelvärde"], [["Äng", "", "", "", ""], ["Gräsmatta", "", "", "", ""]], "tbl num")
 + "<h3>Utvärdera</h3>"
 + steps(["Stämde din hypotes?", "Vad kan ha påverkat resultatet, till exempel tid på året, var du lade rutan eller om du kunde skilja arterna åt?", "Hur skulle du göra undersökningen mer tillförlitlig, alltså så att man kan lita på resultatet?"], True)
 + '<p class="note">Säkerhet: Smaka aldrig på växter eller svampar. Följ allemansrätten och lämna platsen som du fann den. Tvätta händerna efteråt.</p>')

# ------------------------------------------------------------------ 3.2.1
add("3.2.1", "Rikena", f"Kapitel {NR} · Delområde 3.2 {DELOMR['3.2']} · Rikena",
 row("<p>Med över två miljoner kända arter behövs ordning. Forskare delar in organismerna i grupper efter hur de är byggda och hur de är släkt med varandra. De största grupperna kallas <strong class='green'>riken</strong>. Här använder vi fem: <strong class='green'>djur</strong>, <strong class='green'>växter</strong>, <strong class='green'>svampar</strong>, <strong class='green'>bakterier</strong> och <strong class='green'>encelliga organismer med cellkärna</strong>, som amöbor och encelliga alger. Du känner redan igen skillnaden mellan celler med och utan kärna från kapitel 2.</p>",
     [begrepp([("Rike", "En av de största grupperna som organismer delas in i."), ("Vetenskapligt namn", "Artens namn på latin, med två ord."), ("Lav", "En samlevnad mellan en svamp och en alg eller bakterie som gör fotosyntes.")])])
 + fig(FIG+"rikena.png", "<b>Bild 3.8</b> De fem rikena. Bilderna är förenklade.", "96%")
 + table(["Rike", "Cell", "Hur får de näring?", "Exempel"],
         [["<b>Djur</b>", "med cellkärna, utan cellvägg", "äter andra organismer", "räv, älg, gädda, myra"],
          ["<b>Växter</b>", "med cellkärna, cellvägg, kloroplaster", "fotosyntes", "tall, blåbär, björk, mossa"],
          ["<b>Svampar</b>", "med cellkärna och cellvägg, utan kloroplaster", "tar upp näring från död eller levande materia", "flugsvamp, mögel, jäst"],
          ["<b>Bakterier</b>", "utan cellkärna", "olika sätt: några bryter ner, några gör fotosyntes", "mjölksyrabakterier, tarmbakterier"],
          ["<b>Encelliga med kärna</b>", "en enda cell med cellkärna", "olika sätt", "amöba, encelliga alger"]])
 + roww("<h3 style='margin-top:0'>Svampar är varken djur eller växter</h3><p>Svampar ser ofta ut som växter, men de gör ingen fotosyntes. Det du plockar när du plockar kantareller är bara svampens fruktkropp. Själva svampen är ett nät av tunna trådar, <strong class='green'>mycel</strong>, som växer i marken och bryter ner död materia. Många svampar lever också tillsammans med träd och hjälper trädens rötter att ta upp vatten och näring. Svampar och bakterier är viktiga <strong class='green'>nedbrytare</strong>.</p>"
        "<h3>Laven: en samlevnad</h3><p>En lav ser ut som en enda organism men är två: en svamp och en alg (eller bakterie) som gör fotosyntes. Svampen ger skydd och vatten, och algen ger socker. Båda har nytta av varandra, och det kallas <strong class='green'>symbios</strong>. Garnlaven i bild 3.6 är en lav.</p>",
        [box("visste", "Visste du?", "<p>Du är också en art: <i>Homo sapiens</i>. Det betyder ”den kloka människan”.</p>")])
 + "<h3>Namn på latin</h3>"
 + "<p>Samma växt kan heta olika saker på olika språk. Därför har varje art ett <strong class='green'>vetenskapligt namn</strong> med två latinska ord. Det första är släktet och det andra är arten. Första ordet skrivs med stor bokstav, och hela namnet skrivs med kursiv stil. Tallen heter <i>Pinus sylvestris</i> och granen <i>Picea abies</i>. Systemet infördes av den svenske naturforskaren Carl von Linné på 1700-talet. Arter som liknar varandra hör till samma släkte, och släkten som liknar varandra hör till samma familj.</p>"
 + kq("3.2.1"))

# ------------------------------------------------------------------ 3.2.2
add("3.2.2", "Bestämningsnycklar", f"Kapitel {NR} · Delområde 3.2 {DELOMR['3.2']} · Bestämningsnycklar",
 row("<p>Hur vet man vad en växt eller ett djur heter? Man kan använda en <strong class='green'>bestämningsnyckel</strong>. Den består av en serie val med två alternativ. Varje val leder vidare till nästa tills du har kommit fram till arten. Du jämför det du ser (<strong class='green'>kännetecken</strong>) med nyckelns påståenden.</p>"
     "<p>Bild 3.9 visar en nyckel för fem vanliga träd i Norrbotten. Börja överst: har trädet barr eller blad? Följ sedan pilen till nästa fråga.</p>",
     [begrepp([("Bestämningsnyckel", "En serie val med två alternativ som leder till artens namn."), ("Kännetecken", "En egenskap som man kan se och som skiljer arter åt.")])])
 + fig(FIG+"nyckel.png", "<b>Bild 3.9</b> En bestämningsnyckel för fem träd. Tall och gran har barr, de övriga har blad.", "96%")
 + roww("<h3 style='margin-top:0'>Så använder du en nyckel</h3>"
        + steps(["Titta noga på hela växten. Notera blad eller barr, kvist och bark.", "Läs det första valet och bestäm vilket alternativ som stämmer.", "Följ pilen till nästa val. Fortsätt tills du kommer fram till ett namn.",
                 "Kontrollera: stämmer artens beskrivning och bild i en bok eller app med det du ser?", "Om det inte stämmer: gå tillbaka och prova det andra alternativet."], True),
        [box("tank", "Tänk efter", "<p>Du hittar ett träd med barr som sitter två och två i knippe. Vilket träd är det enligt nyckeln?</p>")])
 + "<h3>Så gör du en egen nyckel</h3>"
 + "<p>Välj några arter som du vill kunna skilja åt. Hitta ett kännetecken som delar gruppen i två: till exempel ”har fjädrar” eller ”saknar fjädrar”. Dela sedan varje halva med nästa kännetecken, tills varje art har fått sin egen plats. Bra kännetecken är sådana som alla kan se och som inte beror på årstid eller storlek, som antal ben, bladets form eller om växten har blommor.</p>"
 + kq("3.2.2"))

# ------------------------------------------------------------------ 3.2.3
add("3.2.3", "Anpassningar", f"Kapitel {NR} · Delområde 3.2 {DELOMR['3.2']} · Anpassningar",
 row("<p>Varje art är anpassad till sin miljö. En <strong class='green'>anpassning</strong> är ett drag hos arten, till exempel i byggnaden, hur kroppen fungerar eller hur den beter sig, som gör att den klarar sig i sin livsmiljö. Titta på fjällräven i bild 3.5. Den har tjock päls som är vit på vintern, små öron som släpper ut lite värme och ligger ofta i en snölya. Rödräven har större öron och längre ben och klarar sig bättre i skogen.</p>"
     "<p>Andra exempel är tallens vaxade, smala barr som tål torka och kyla, och renens breda klövar som bär på snö. Anpassningar är inte något en individ bestämmer sig för. De har uppstått över många generationer.</p>",
     [begrepp([("Anpassning", "Ett drag som gör att en art klarar sin miljö."), ("Variation", "Skillnader mellan individer av samma art."), ("Naturligt urval", "De individer som passar bäst i miljön överlever oftare och får fler ungar.")])])
 + "<h3>Hur uppstår en anpassning? Naturligt urval</h3>"
 + roww("<p>Individerna av en art är aldrig exakt likadana. Det finns <strong class='green'>variation</strong>, och en del av den går i arv. Om en variant klarar miljön bättre överlever de individerna oftare och får fler ungar, och dragen går vidare. Efter många generationer är draget vanligare. Det kallas <strong class='green'>naturligt urval</strong>. Du läser mer om evolutionen i kapitel 9.</p>"
        "<p>Ett klassiskt exempel är pepparfjärilen i England. Den finns i en ljus och en mörk variant. På 1800-talet, när sot från fabriker gjorde trädstammarna mörka, blev de mörka fjärilarna vanligare, för de syntes sämre för fåglarna. När luften blev renare och barken ljusare minskade de mörka igen. Försök där man satt ut fjärilar har visat att fåglar tar de fjärilar som syns bäst.</p>",
        [box("tank", "Tänk efter", "<p>Bild 3.10 visar en skog med ljus bark. Vad skulle hända med fjärilarna i en skog med mörk, sotig bark?</p>")])
 + fig(FIG+"urval.png", "<b>Bild 3.10</b> Naturligt urval i tre steg, med ljusa och mörka fjärilar på en ljus trädstam. Bilden är förenklad.", "96%")
 + kq("3.2.3"))

# ------------------------------------------------------------------ Labb 3.2
add("Labb", "3.2 Artbestämning med nyckel", f"Kapitel {NR} · Delområde 3.2 {DELOMR['3.2']} · Labb 3.2 Artbestämning med nyckel",
 "<p>Du ska använda en bestämningsnyckel för att bestämma träd i närområdet och dokumentera med bild.</p>"
 + roww("<p><strong class='green'>Frågeställning:</strong> Vilka arter av träd finns på skolgården eller i närmaste park?</p><p><strong class='green'>Hypotes:</strong> Skriv vilka träd du tror att du hittar.</p>"
        "<p><strong class='green'>Material:</strong> nyckeln i bild 3.9, mobilkamera, papper och penna, gärna en trädbok eller artapp.</p><h3>Gör så här</h3>"
        + steps(["Välj ett träd. Ta en bild på hela trädet, barken och bladen eller barren. Plocka bara löv som redan ligger på marken.",
                 "Använd nyckeln i bild 3.9 och följ den steg för steg. Skriv upp vilka val du gör.",
                 "Skriv trädets svenska och vetenskapliga namn. Kontrollera i en bok eller app.",
                 "Gör likadant med minst fyra olika träd. Skriv resultatet i tabellen.",
                 "Om du hittar ett träd som inte finns i nyckeln: skriv vilka kännetecken det har och vilket steg som inte stämmer."]),
        [box("begrepp", "Begrepp", "<b class='t'>Bestämma</b><p>Att ta reda på vilken art något är.</p><b class='t'>Dokumentera</b><p>Att skriva och fotografera det du gör.</p>"),
         box("tank", "Bra att veta", "<p>Samma art kan se olika ut. Titta på flera blad och kontrollera med flera kännetecken.</p>")])
 + table(["Träd nr", "Kännetecken", "Valen i nyckeln", "Svenskt namn", "Vetenskapligt namn"], [["1", "", "", "", ""], ["2", "", "", "", ""], ["3", "", "", "", ""], ["4", "", "", "", ""]], "tbl num")
 + "<h3>Frågor</h3>"
 + steps(["Vilket kännetecken var lättast att använda, och vilket var svårast?", "Fanns det träd som du inte kunde bestämma med nyckeln? Varför?", "Hur kan du kontrollera att du fått rätt art?", "Vad var svårt i undersökningen, och hur skulle du göra annorlunda nästa gång?"], True)
 + '<p class="note">Säkerhet: Smaka aldrig på växter, bär eller svampar. Plocka inte skyddade växter. Tvätta händerna efteråt.</p>')

SAMMAN = ["<strong>Biologisk mångfald</strong> är variationen av liv på tre nivåer: gener, arter och ekosystem.",
          "En <strong>art</strong> är individer som kan få fortplantningsdugliga ungar. En <strong>population</strong> är alla individer av en art i ett område.",
          "Ett ekosystem med många arter och stor genetisk variation är mer motståndskraftigt mot störningar.",
          "Människan är beroende av <strong>ekosystemtjänster</strong>: försörjande, reglerande, stödjande och kulturella.",
          "De största hoten är ändrad markanvändning, överuttag, klimatförändringar, föroreningar och invasiva arter.",
          "I Sverige följs arternas läge i <strong>rödlistan</strong>. I Rödlistan 2025 var 5 217 arter rödlistade och 2 373 hotade.",
          "Mångfalden skyddas genom skyddade områden, lagar, internationella avtal och genom vad vi gör som individer.",
          "Organismer delas in i <strong>riken</strong>: djur, växter, svampar, bakterier och encelliga med cellkärna. Varje art har ett vetenskapligt namn med två ord.",
          "Med en <strong>bestämningsnyckel</strong> kommer man fram till en arts namn genom att välja mellan två alternativ i taget.",
          "En <strong>anpassning</strong> är ett drag som gör att en art klarar sin miljö. Anpassningar uppstår genom <strong>naturligt urval</strong> över generationer."]

BEGR = [("Anpassning", "Ett drag som gör att en art klarar sin miljö."), ("Art", "Individer som kan få fortplantningsdugliga ungar med varandra."), ("Bestämningsnyckel", "Serie val med två alternativ som leder till artens namn."),
        ("Biologisk mångfald", "Variationen av liv: genetisk mångfald, artmångfald och ekosystemmångfald."), ("Ekosystem", "Alla organismer i ett område och den miljö de lever i."),
        ("Ekosystemtjänst", "Något naturen gör som människan har nytta av."), ("Gen", "Del av arvsmassan (DNA) som styr en egenskap."), ("Invasiv art", "Främmande art som människan fört in och som sprider sig och skadar inhemska arter."),
        ("Konsument", "Organism som äter andra organismer."), ("Lav", "Samlevnad mellan en svamp och en alg eller bakterie som gör fotosyntes."), ("Livsmiljö", "Platsen där en art kan leva och föröka sig."),
        ("Naturligt urval", "De individer som passar bäst i miljön överlever oftare och får fler ungar."), ("Nedbrytare", "Organism som bryter ner dött material till näring."), ("Näringsväv", "Flera näringskedjor som hänger ihop."),
        ("Pollinering", "Pollen förs mellan blommor så att de kan bilda frön."), ("Population", "Alla individer av en art inom ett område."), ("Producent", "Organism som gör sin egen näring genom fotosyntes."),
        ("Rike", "En av de största grupperna som organismer delas in i."), ("Rödlista", "Förteckning över arter och deras risk att dö ut."), ("Signalart", "Art som visar att en miljö har höga naturvärden."),
        ("Symbios", "Samlevnad där båda parter har nytta av varandra."), ("Variation", "Skillnader mellan individer av samma art."), ("Vetenskapligt namn", "Artens latinska namn med två ord: släkte och art."),
        ("Överuttag", "När människan tar mer ur naturen än vad som hinner växa till.")]

TEST = [
 ("A", "Vilket alternativ beskriver genetisk mångfald?", ["A Antalet arter i en skog.", "B Variationen i gener mellan individer av samma art.", "C Antalet olika ekosystem i ett land.", "D Antalet individer i en population."], 1, 0),
 ("A", "Vilket är ett exempel på en reglerande ekosystemtjänst?", ["A Virke från skogen.", "B Bär och svamp att plocka.", "C Humlor som pollinerar blåbärsris.", "D En vandring i fjällen."], 2, 0),
 ("A", "I en barrskog blir det plötsligt mycket färre skogssorkar. Vad händer troligen först?", ["A Blåbärsriset minskar.", "B Pärlugglorna får mindre mat.", "C Renarna blir fler.", "D Lavarna dör."], 1, 0),
 ("A", "Vilket rike tillhör en organism som inte gör fotosyntes, har cellkärna och tar upp näring från död materia?", ["A Växter", "B Svampar", "C Bakterier", "D Djur"], 1, 0),
 ("B", "Uppge två ekosystemtjänster som en våtmark ger.", None, 1, 3),
 ("B", "Blomsterlupinen är en invasiv art. Beskriv vad det innebär.", None, 1, 3),
 ("C", "TABELL", None, 2, 5),
 ("C", "Sven påstår: ”Naturligt urval betyder att varje individ anpassar sig när miljön ändras.” Förklara varför han har fel.", None, 2, 4),
 ("D", "Kommunen vill bygga ett nytt bostadsområde i en gammal skog där det växer garnlav. Vilka konsekvenser kan bygget få för den biologiska mångfalden? Ta ställning till om skogen ska bebyggas och motivera med minst två argument.", None, 3, 6),
 ("D", "Wilma påstår: ”Rödlistan visar att det går sämre för naturen eftersom antalet rödlistade arter har ökat sedan 2005.” Använd bild 3.4 och rutan Granska kritiskt. Har Wilma rätt? Förklara.", None, 3, 6),
 ("E", "Elias tror att det finns fler arter av lavar i gammal skog än i ung, planterad skog. Planera en undersökning som kan pröva hans idé. Beskriv vad du ska räkna eller mäta, hur du gör jämförelsen rättvis och hur du dokumenterar resultatet.", None, 2, 6),
 ("E", "Abborre, gädda, fiskgjuse och djurplankton lever i samma sjö. Ordna dem i en näringskedja och lägg till en producent först i kedjan. Förklara sedan vad som kan hända med gäddorna om nästan alla abborrar fångas.", None, 3, 6),
]
TEST_TABELL = (["Äng", "Ruta 1", "Ruta 2", "Ruta 3"], [["Betad äng", "21", "18", "24"], ["Igenvuxen äng", "9", "12", "6"]])
TEST_D_TEXT = "En klass räknade växtarter i provrutor på 1 m² vid två ängar. Den ena betas av kor. Den andra har inte betats på tio år och har börjat växa igen. Resultaten är påhittade."
TEST_D_SUB = ["a) Räkna ut medelvärdet av antalet arter för varje äng.", "b) Ge en möjlig förklaring till skillnaden."]
DEL_NAMN = {"A": "Välj ett alternativ", "B": "Svara kort", "C": "Tolka resultat och förklara", "D": "Resonera och ta ställning", "E": "Planera och resonera"}
FACIT = [
 "B", "C", "B", "B",
 "T.ex. de renar vatten, minskar översvämningar, binder kol och är livsmiljö för många arter.",
 "En invasiv art är en främmande art som människan fört in och som sprider sig och skadar eller tränger undan inhemska arter.",
 "a) Betad äng: (21 + 18 + 24) / 3 = 21. Igenvuxen äng: (9 + 12 + 6) / 3 = 9. b) T.ex. betet håller ängen öppen så att fler arter får ljus, medan en igenvuxen äng domineras av få höga växter som skuggar och tränger undan andra.",
 "Naturligt urval verkar på populationer över många generationer. Individerna är olika redan från början. De med de mest passande dragen överlever och får fler ungar, och dragen går i arv. En enskild individ ändrar inte sina gener för att miljön ändras.",
 "Öppet svar. Ett välutvecklat svar nämner att gammal skog har arter som är beroende av gamla träd och död ved, att garnlav är en signalart, att livsmiljöer tar hundratals år att återskapa, och väger detta mot behovet av bostäder och jobb. Minst två argument med motivering, gärna med en motsatt synpunkt.",
 "Nej, inte nödvändigtvis. Antalet bedömda arter ökade från cirka 19 000 till drygt 23 000, så fler nya arter kan ha blivit rödlistade bara för att forskarna hade bedömt dem. Man måste jämföra andelen eller samma arter över tid. Rödlistan visar ändå att många arter är hotade.",
 "Räkna och jämför lavarter i flera lika stora provrutor eller på lika många träd i gammal och ung skog. Håll storlek, tid på året, trädslag och sökmetod lika (rättvist försök). Skriv in antalet i en tabell, räkna medelvärde och dokumentera med foton och anteckningar. Flera upprepningar gör slutsatsen säkrare.",
 "Producent (t.ex. alger) → djurplankton → abborre → gädda → fiskgjuse. Om nästan alla abborrar fångas får gäddorna mindre mat och kan minska. Djurplankton kan öka eftersom färre abborrar äter dem. Gäddorna kan välja andra byten, så effekten beror på hur många alternativ som finns.",
]
LGR = ("Området täcker det centrala innehållet om biologisk mångfald (genetisk variation, arter och ekosystem), ekosystemtjänster och hot mot mångfalden, hur organismer grupperas och bestäms, samt anpassningar och naturligt urval i årskurs 7–9. "
       "Delområde 3.1 behandlar mångfaldens tre nivåer, ekosystemtjänster och hoten mot mångfalden. Delområde 3.2 behandlar riken, bestämningsnycklar och anpassningar. "
       "Labbarna tränar att planera och genomföra en inventering och att använda en nyckel. Uppgifterna följer betygskriteriernas progression: från att namnge och beskriva till att förklara samband och resonera i flera led, och är inspirerade av frisläppta nationella prov i biologi.")
FAKTA = ("Uppgifter i kapitlet kommer från öppnade källor och läroböcker; se lärarversionens källförteckning. Rödlistans siffror (23 103 bedömda, 5 217 rödlistade, 2 373 hotade) är kontrollerade mot SLU Artdatabanken. IPBES 2019 (cirka en miljon hotade arter och rangordningen av de fem drivkrafterna) är kontrollerat mot FN:s sammanfattning. "
         "Överenskommelsen att skydda minst 30 procent av land, sötvatten och hav till 2030 (Kunming–Montreal, december 2022) är kontrollerad. Siffrorna om pollinatörsberoende (cirka tre fjärdedelar av grödtyperna, cirka 35 procent av produktionsvolymen, men bara cirka 5–8 procents produktionsförlust utan pollinatörer) är kontrollerade mot Our World in Data. "
         "Fjällrävens fridlysning 1928, cirka 35–50 vuxna djur runt år 2000, lämlar som största födokälla och rödräven som konkurrent är kontrollerade mot SVT. Rättelse från äldre version: att skogsbruket påverkar ”över 1 700” rödlistade arter kunde inte beläggas. Naturvårdsverket anger bara att igenväxning och avverkning är de viktigaste negativa faktorerna och att jordbruks- och skogslandskapen hyser över 75 procent av de rödlistade arterna; inga siffror per faktor. "
         "Delvis kontrollerat: Irlands potatismögel (”omkring en miljon dog”), pepparfjärilens historia (förenklad; den senaste fältstudien visar att fåglar tar mörka fjärilar oftare på ljus bark), att garnlav är en signalart och viktig vinterföda för ren. Ej källkontrollerat: allmänna läroboksfakta om rikena och om Linné. "
         "Källor: Skolverket, Lgr22 kursplan i biologi. · Frisläppta nationella prov i biologi åk 9. · Illustrationer: egenritade för detta kapitel, utom bild 3.1, 3.2, 3.4–3.7 som är bearbetade från tidigare version.")
HANDLEDNING_HTML = """<h3>Handledning per moment (grundtext)</h3>
<p><b>Start.</b> Mål: eleven kan förklara att biologisk mångfald är mer än antalet arter. Låt eleverna först skriva sin lista över arter (Fundera) och jämföra. Siffran ”drygt två miljoner beskrivna arter” är osäker: poängen är att ingen vet hur många som finns.</p>
<p><b>Gener, arter och ekosystem.</b> C-mål: beskriva de tre nivåerna med egna exempel och förklara varför variation ger motståndskraft. Vanligt fel: att mångfald bara betyder antal arter. Vanligt fel: att alla individer av en art är lika. Näringsvävens energiriktning (pilarna) tas upp mer i kapitel 4.</p>
<p><b>Ekosystemtjänster.</b> C-mål: ge exempel på alla fyra typerna och förklara varför mångfald gör tjänsterna säkrare. Vanligt fel: att ekosystemtjänster bara är sådant man kan sälja. Låt eleverna klassa egna exempel (vandring, bär, bin, jord).</p>
<p><b>Hoten mot mångfalden.</b> C-mål: nämna hoten med exempel, tolka rödlistans diagram kritiskt och argumentera i en samhällsfråga. Rutan Granska kritiskt: fler bedömda arter ger fler rödlistade. Citaten i skogsfrågan är konstruerade; låt eleverna bedöma vem som har vilket intresse. Naturvårdsverket anger inga siffror per påverkansfaktor, så använd formuleringen ”viktigaste negativa faktorerna”.</p>
<p><b>Labb 3.1 Artinventering i en provruta.</b> Material: fyra pinnar, snöre, tumstock, mobil. Förväntat: fler arter på ängen än på den klippta gräsmattan, men det beror på plats och årstid. Vanliga fel: rutorna läggs på olika sätt; arter räknas dubbelt. Låt eleverna fotografera och numrera arter. Planera på sommarhalvåret.</p>
<p><b>Rikena.</b> C-mål: ange kännetecken för de fem rikena och förklara skillnaden mellan svamp och växt. Vanligt fel: att svampar är växter. Vanligt fel: att alla bakterier är sjukdomsframkallande. Laven är ett bra exempel på symbios.</p>
<p><b>Bestämningsnycklar.</b> C-mål: använda en färdig nyckel och förklara hur den är uppbyggd. Vanligt fel: att välja efter ”känsla” i stället för kännetecken. Låt eleverna bygga en egen nyckel för tre till fyra föremål i klassrummet.</p>
<p><b>Anpassningar.</b> C-mål: ge exempel på anpassningar och beskriva naturligt urval med variation, urval och ärftlighet. Vanligt fel: att individer anpassar sig medvetet eller att arter ”behöver” förändras. Pepparfjärilen är förenklad i häftet; fältförsök visar att fåglar tar de fjärilar som syns bäst.</p>
<p><b>Labb 3.2 Artbestämning med nyckel.</b> Material: nyckeln i bild 3.9, mobil, träd i närheten. Förväntat: eleverna hittar vanliga arter som tall, gran, björk, asp och rönn. Planera efter vilka träd som finns vid skolan. Vissa träd (t.ex. sälg eller al) finns inte i nyckeln: det är en del av övningen.</p>
"""

BONUS = dict(
 titel="Fallfällor: vilka djur lever på marken?",
 ingress="Eleverna gräver ner enkla fällor i två olika miljöer och jämför vilka smådjur som går i dem. Ett enkelt sätt att mäta artrikedom.",
 syfte="Eleverna undersöker artrikedom på två platser och jämför med fallfällor, planerar ett rättvist försök och dokumenterar och tolkar resultatet. Labben tränar systematiska undersökningar och kopplar till mångfald på artnivå.",
 tid="Grupper om tre till fyra. Förberedelse 20 minuter, fällorna står ute 1–2 dygn, utvärdering 40 minuter.",
 material=["Plastmuggar (ca 3 dl), minst sex per grupp", "Små trädgårdsspadar", "Takpapp eller bit plast som regnskydd, stenar att stötta upp med", "Burkar och petriskålar, pincett, penslar, lupp", "Artbestämningsbok eller app", "Anteckningsblad"],
 genomf=["Välj två platser, till exempel skogsbryn och klippt gräsmatta. Bestäm hur många fällor (minst tre per plats) och hur långt ifrån varandra de ska stå.", "Gräv ner mugg så att kanten är jämn med marken. Sätt ett regnskydd en bit ovanför.", "Låt fällorna stå 1–2 dygn. Notera datum och tid.", "Töm fällorna i en burk. Sortera djuren i grupper (t.ex. spindlar, skalbaggar, myror, mångfotingar) med pincett och lupp.", "Skriv resultatet i tabell: antal individer och antal grupper per fälla och plats. Beräkna medelvärde.", "Släpp ut djuren där de hittades. Ta bort alla fällor."],
 resultat="Skogsbryn och ängsmark har oftast fler grupper än en klippt gräsmatta, men resultatet varierar med väder och tid på året. Eleverna ska se att fler upprepningar ger säkrare slutsats, och att fällorna bara visar de djur som rör sig på marken.",
 sakerhet=["Ta bort alla fällor när försöket är slut så att inga djur fastnar.", "Hantera djuren försiktigt; släpp ut dem på samma plats.", "Tvätta händerna efteråt.", "Gräv bara där markägaren tillåter det."],
 problem=["För få fällor ger för osäkra resultat.", "Regn fyller fällorna: sätt regnskydd.", "Djur som kommer ut ur fällan: använd muggar med lite djup.", "Eleverna räknar olika: bestäm grupperna i förväg."],
 bedom=[("Grundläggande", "Redovisar vilka djur de fann och var."), ("Utvecklat", "Jämför platserna med medelvärden och förklarar skillnader med livsmiljön."), ("Välutvecklat", "Värderar metoden, diskuterar felkällor och föreslår förbättringar.")],
 forslag=["Finns det fler djurgrupper i skogen än på gräsmattan?", "Påverkar fuktighet vilka djur som fångas?", "Skiljer sig fångsten mellan dag och natt?"],
)
