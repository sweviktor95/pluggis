// Biologisk mångfald – sajtsidor byggda utifrån Kapitel 3 (häftet).
// Begrepp, definitioner och siffror ska följa häftet. Bilderna är utklippta ur häftet.

var innehall = window.innehall || {};

var RUTA = function(typ, rubrik, text) {
  return '<div class="ruta ruta-' + typ + '"><span class="ruta-rubrik">' + rubrik + '</span>' + text + '</div>';
};

innehall["biologi-mangfald-vad-ar"] = {
  intro: "Biologisk mångfald betyder variationen av liv på jorden. Ordet används ofta om hur många arter som finns, men det är bara en del av sanningen. Forskare delar in mångfalden i tre nivåer som hänger ihop.",
  sektioner: [
    {
      ikon: "🌍",
      titel: "Tre nivåer av mångfald",
      text: [
        "Biologisk mångfald finns på tre nivåer: <strong>inom arter</strong>, <strong>mellan arter</strong> och <strong>mellan ekosystem</strong>."
      ],
      bild: "bilder/mangfald-tre-nivaer.png",
      bildText: "Bild 3.1 Biologisk mångfald finns på tre nivåer: inom arter, mellan arter och mellan ekosystem."
    },
    {
      ikon: "🧬",
      titel: "1. Genetisk mångfald – variation inom en art",
      text: [
        "Alla tallar tillhör samma art, men ingen tall är exakt lik en annan. Deras <strong>gener</strong> skiljer sig lite åt. En tall kanske tål torka bättre, en annan klarar kyla eller en viss svampsjukdom.",
        "När miljön förändras är det de individer som har ”rätt” gener som överlever och får avkomma (ungar). Därför gör stor genetisk variation att en art kan anpassa sig."
      ],
      kontrollfraga: "Varför kan stor genetisk variation hjälpa en art att överleva när klimatet blir varmare?",
      kontrollsvar: "Individerna har olika gener och tål därför olika saker. När klimatet förändras är det de individer som har de gener som passar bäst som överlever och får avkomma, så arten kan anpassa sig."
    },
    {
      ikon: "🦊",
      titel: "2. Artmångfald – variation mellan arter",
      text: [
        "Artmångfald är antalet olika arter i ett område. En <strong>art</strong> är en grupp individer som kan para sig med varandra och få avkomma som också kan få ungar. (Det gäller organismer som fortplantar sig genom parning. Bakterier delar sig i stället.)",
        "En blåbärsskog med hundratals arter av insekter, svampar och mossor har högre artmångfald än en gräsmatta.",
        RUTA("fakta", "Fakta", "Forskare har hittills beskrivit ungefär två miljoner arter på jorden. Troligen finns det många miljoner till som ingen har upptäckt – mest insekter, svampar och mikroorganismer.")
      ],
      kontrollfraga: "Förklara med egna ord vad en art är.",
      kontrollsvar: "En art är en grupp individer som kan para sig med varandra, och som får ungar som också själva kan få ungar. Båda delarna ska med."
    },
    {
      ikon: "🏔️",
      titel: "3. Ekosystemmångfald – variation mellan livsmiljöer",
      text: [
        "Fjäll, myr, gammal skog, älv och skärgård är olika <strong>ekosystem</strong>. Varje ekosystem har sina egna arter och sitt eget samspel.",
        "Om ett landskap bara har en typ av miljö, till exempel planterad skog i samma ålder, försvinner arter som behöver något annat."
      ],
      kontrollfraga: "Varför räcker det inte att räkna antalet arter för att veta hur rik naturen är i ett område?",
      kontrollsvar: "Mångfald handlar inte bara om hur många arter som finns. Den finns också inom arterna (olika gener) och mellan olika livsmiljöer (ekosystem). Två områden kan ha lika många arter, men om det ena bara har en sorts miljö försvinner arter som behöver något annat."
    }
  ],
  begrepp: [
    { term: "Art", forklaring: "Individer som kan få fortplantningsdugliga ungar med varandra." },
    { term: "Population", forklaring: "Alla individer av en art inom ett visst område." },
    { term: "Gen", forklaring: "En del av arvsmassan (DNA) som styr en egenskap." },
    { term: "Ekosystem", forklaring: "Alla organismer i ett område och den miljö de lever i." },
    { term: "Biologisk mångfald", forklaring: "Variationen av liv: genetisk mångfald, artmångfald och ekosystemmångfald." }
  ],
  exitTicket: [
    {
      fraga: "Vilka är de tre nivåerna av biologisk mångfald? Ge ett exempel på varje.",
      svar: "Genetisk mångfald (tallar av samma art med olika gener), artmångfald (till exempel gran, räv och flugsvamp) och ekosystemmångfald (olika livsmiljöer som fjäll, skog, myr och älv)."
    }
  ]
};

innehall["biologi-mangfald-varfor-viktig"] = {
  intro: "I ett ekosystem är alla arter beroende av varandra, och vi människor är beroende av dem. Därför är biologisk mångfald viktig – både för naturen och för oss.",
  sektioner: [
    {
      ikon: "🕸️",
      titel: "Producenter, konsumenter och nedbrytare",
      text: [
        "Gröna växter är <strong>producenter</strong>: med hjälp av solljus bygger de upp socker genom fotosyntes. Djur är <strong>konsumenter</strong> som får sin energi genom att äta växter eller andra djur. <strong>Nedbrytare</strong>, till exempel svampar och bakterier, bryter ner döda växter och djur, så att näringen kan användas igen.",
        "En <strong>näringskedja</strong> visar vem som äter vem, till exempel <em>blåbär → skogssork → pärluggla</em>. Men i naturen äter de flesta djur flera olika saker. Därför ritar man ofta en <strong>näringsväv</strong> med många kedjor som är sammanflätade."
      ],
      bild: "bilder/mangfald-naringsvav.png",
      bildText: "Bild 3.2 En förenklad näringsväv i en norrländsk barrskog. Pilarna visar åt vilket håll energin går – från det som blir uppätet till den som äter.",
      kontrollfraga: "Vad är skillnaden mellan en producent och en konsument? Skriv också en näringskedja med tre led från Bild 3.2. Välj en annan kedja än exemplet i texten.",
      kontrollsvar: "En producent gör sin egen näring genom fotosyntes, medan en konsument äter andra organismer. Exempel på godtagbara kedjor: tall → skogshare → räv, eller blåbär → skogssork → hermelin (pilarna går från den som blir äten till den som äter)."
    },
    {
      ikon: "🧩",
      titel: "Många arter – fler reservdelar",
      text: [
        "Ett ekosystem med många arter är oftast mer <strong>motståndskraftigt</strong>, det vill säga det tål störningar bättre. Vissa år blir det ont om sork. Då kan räven äta mer hare eller fågelägg i stället. I ett artfattigt system finns det färre ”reservdelar”. Om en viktig art försvinner kan hela ekosystemet förändras.",
        "Man kan jämföra med ett nät: du kan klippa av några trådar utan att det går sönder, men klipper du av för många rasar det ihop.",
        RUTA("historia", "Ett exempel från historien", "På 1840-talet odlade man nästan bara en sorts potatis på Irland. Alla plantor var genetiskt mycket lika. När sjukdomen potatisbladmögel kom fanns inga plantor som tålde den. Skördarna slogs ut och omkring en miljon människor dog av svält."),
        RUTA("tank", "Tänk efter", "Titta på Bild 3.2. Vad händer med räven om skogssorkarna blir färre? Vilken annan föda kan räven välja?")
      ],
      kontrollfraga: "Förklara varför ett artrikt ekosystem klarar störningar bättre än ett artfattigt.",
      kontrollsvar: "Om en art försvinner eller får det svårt kan andra arter ta över, till exempel kan räven äta mer hare om det blir ont om sork. I ett artfattigt system finns det färre ”reservdelar”, så hela ekosystemet förändras lättare. (Irlandsexemplet går också bra: bara en potatissort gjorde att alla plantor slogs ut.)"
    },
    {
      ikon: "🎁",
      titel: "Naturens gratistjänster",
      text: [
        "Allt vi äter, luften vi andas och vattnet vi dricker beror på andra arter. Det naturen gör för oss kallas <strong>ekosystemtjänster</strong>. De är gratis, och därför märker vi dem ofta inte förrän de slutar fungera. Man brukar dela in dem i fyra grupper:",
        "<strong>Försörjande:</strong> saker vi kan ta från naturen, som mat, fisk, bär, virke, rent vatten och ämnen till läkemedel.<br><strong>Reglerande:</strong> naturen styr och renar – bin och humlor pollinerar, våtmarker renar vatten och skog binder koldioxid.<br><strong>Stödjande:</strong> grunden för allt annat – nedbrytare skapar bördig jord, och växter bildar syre genom fotosyntes.<br><strong>Kulturella:</strong> det naturen ger oss som människor – friluftsliv, jakt, fiske, vila, inspiration och kulturarv."
      ],
      kontrollfraga: "Ge ett exempel på varje typ av ekosystemtjänst.",
      kontrollsvar: "Försörjande: till exempel mat, fisk, bär eller virke. Reglerande: till exempel att bin pollinerar eller att våtmarker renar vatten. Stödjande: till exempel att nedbrytare skapar bördig jord. Kulturella: till exempel friluftsliv eller inspiration."
    },
    {
      ikon: "🐝",
      titel: "Pollinering – en tjänst värd mycket",
      text: [
        "När en humla flyger mellan blommor för att samla nektar, tar den med sig pollen. Att <strong>pollinera</strong> betyder att föra över pollen från en blomma till en annan. Då blir blommorna befruktade och kan bilda frön och bär. Utan pollinerare skulle det bli mycket mindre blåbär, lingon, äpplen och raps. Ungefär tre av fyra av världens grödor ger större eller bättre skörd om de pollineras av djur. Räknat i mängd mat är det ungefär en tredjedel av det vi odlar som beror på pollinerare, eftersom de stora spannmålsgrödorna inte gör det.",
        RUTA("visste", "Visste du?", "I vissa fruktodlingar i Kina har det funnits så få bin att människor har fått pollinera blommorna för hand med små penslar. Det tar lång tid och kostar mycket pengar.")
      ]
    },
    {
      ikon: "💧",
      titel: "Våtmarker och skog",
      text: [
        "En myr fungerar som en disksvamp: den suger upp vatten vid kraftiga regn och släpper ut det långsamt. Det minskar risken för översvämningar. Samtidigt fastnar näringsämnen och partiklar, så att vattnet som rinner vidare blir renare.",
        "Skogen tar upp koldioxid när träden växer och lagrar kol i stammar och i marken."
      ],
      kontrollfraga: "Hur kan en myr minska risken för översvämningar?",
      kontrollsvar: "En myr suger upp vatten vid kraftiga regn och släpper ut det långsamt, ungefär som en disksvamp. Då kommer inte allt vatten på en gång."
    },
    {
      ikon: "🛟",
      titel: "Mångfald ger säkrare tjänster",
      text: [
        "Om det finns många olika arter som pollinerar spelar det mindre roll om en av dem får ett dåligt år. Därför är biologisk mångfald en sorts försäkring för ekosystemtjänsterna: går något fel finns det andra arter som kan ta över."
      ],
      kontrollfraga: "Förklara varför många olika arter av pollinerare är bättre än en enda.",
      kontrollsvar: "Om en pollinerare får ett dåligt år kan de andra ta över, så pollineringen fungerar ändå. Med bara en art är tjänsten mycket mer sårbar."
    }
  ],
  begrepp: [
    { term: "Producent", forklaring: "Organism som gör sin egen näring genom fotosyntes." },
    { term: "Konsument", forklaring: "Organism som äter andra organismer." },
    { term: "Nedbrytare", forklaring: "Organism som bryter ner dött material till näring." },
    { term: "Näringskedja", forklaring: "Visar vem som äter vem i en följd." },
    { term: "Näringsväv", forklaring: "Flera näringskedjor som hänger ihop." },
    { term: "Ekosystemtjänst", forklaring: "Något naturen gör som människan har nytta av." },
    { term: "Pollinering", forklaring: "Pollen förs mellan blommor så att de kan bilda frön." }
  ],
  exitTicket: [
    {
      fraga: "Abborre, gädda, fiskgjuse och djurplankton lever i samma sjö. Ordna dem i en näringskedja och lägg till en producent först i kedjan. Förklara sedan vad som kan hända med gäddorna om nästan alla abborrar fångas.",
      svar: "Växtplankton (alger) → djurplankton → abborre → gädda → fiskgjuse. Gäddorna får mindre mat och kan minska. De kan också börja äta mer av andra fiskar, eller äta varandra."
    },
    {
      fraga: "I en barrskog blir det plötsligt mycket färre skogssorkar. Vad händer troligen först? Använd Bild 3.2.",
      svar: "Pärlugglorna (och hermelinerna) får mindre mat, eftersom de äter skogssork. Räven får också mindre mat men kan byta till skogshare och tjäder."
    }
  ]
};

innehall["biologi-mangfald-hot"] = {
  intro: "Arter har alltid dött ut och nya har utvecklats. Men i dag försvinner arter mycket snabbare än vad som är naturligt. Den internationella expertpanelen IPBES bedömde 2019 att upp till en miljon arter riskerar att dö ut. Nästan alla hot har samma grundorsak: människans aktiviteter.",
  sektioner: [
    {
      ikon: "⚠️",
      titel: "Fem stora hot",
      text: [
        "<strong>Ändrad markanvändning:</strong> skog avverkas, myrar dikas och ängar växer igen. Det här är det största hotet.<br><strong>Överuttag:</strong> vi fiskar, jagar eller skördar mer än vad som hinner växa till.<br><strong>Klimatförändringar:</strong> arter måste flytta norrut eller uppåt – fjällens arter har ingenstans att ta vägen.<br><strong>Föroreningar:</strong> miljögifter, plast och övergödning skadar liv i mark och vatten. Övergödning betyder att det kommer för mycket näring till sjöar och hav.<br><strong>Invasiva arter:</strong> främmande arter tränger undan de inhemska (de som hör hemma här), till exempel blomsterlupin."
      ]
    },
    {
      ikon: "📋",
      titel: "Rödlistan – Sveriges hälsokontroll",
      text: [
        "Vart femte år bedömer forskare vid SLU Artdatabanken (Sveriges lantbruksuniversitet) hur stor risken är att olika arter försvinner från Sverige. Resultatet kallas <strong>rödlistan</strong>. I den senaste rödlistan, som kom i mars 2026, bedömdes drygt 23 000 arter. Av dem var 5 217 rödlistade, och 2 373 räknades som hotade.",
        "Rödlistans kategorier: <strong>LC</strong> livskraftig, <strong>NT</strong> nära hotad, <strong>VU</strong> sårbar, <strong>EN</strong> starkt hotad, <strong>CR</strong> akut hotad, <strong>RE</strong> nationellt utdöd och <strong>DD</strong> kunskapsbrist. Arter i VU, EN och CR räknas som hotade. Alla utom LC kallas rödlistade. DD betyder att forskarna vet för lite om arten för att kunna bedöma den – men den kan vara hotad.",
        "Det som påverkar flest rödlistade arter på land är skogsbruket – över 1 700 arter – och att ängar och betesmarker växer igen. Bland arterna som nu är rödlistade finns djur som många känner till, till exempel lax, sill, ladusvala och älg. De är dock bara ”nära hotade” (NT), inte hotade. Rödlistad betyder alltså inte alltid hotad. Men det finns också goda nyheter: uttern och havsörnen har blivit så många igen att de inte längre är rödlistade."
      ],
      bild: "bilder/mangfald-rodlista-diagram.png",
      bildText: "Bild 3.3 Antal rödlistade arter i Sverige vid olika år (staplarna visar antalet arter i rödlistan). Källa: SLU Artdatabanken.",
      bildBredd: 520
    },
    {
      ikon: "🔎",
      titel: "Granska kritiskt",
      text: [
        "Antalet rödlistade arter har ökat. Men antalet arter som forskarna bedömer har också ökat över tid, till drygt 23 000 år 2025. Då är det bra att jämföra <em>andelen</em>: hur många av alla bedömda arter som är rödlistade."
      ],
      kontrollfraga: "Betyder ökningen i Bild 3.3 att alla nya rödlistade arter har fått det sämre? Vilken annan förklaring kan finnas?",
      kontrollsvar: "Inte nödvändigtvis. Antalet rödlistade arter har ökat, men samtidigt bedömdes fler arter 2025 än tidigare. En del av ökningen beror på mer kunskap, inte bara på att arterna har fått det sämre. Andelen rödlistade (ca 23 % år 2025, alltså 5 217 av drygt 23 000) är därför ett bättre mått att jämföra."
    },
    {
      ikon: "🦊",
      titel: "Mångfald i Norrbotten: fjällräven",
      text: [
        "Norrbotten har några av Sveriges största orörda områden: fjäll, myrar, gammal skog och några av landets sista outbyggda älvar. Här finns också tydliga exempel på både hot och räddningsinsatser.",
        "Fjällräven jagades hårt för sin vackra vinterpäls. Den blev fridlyst redan 1928, men stammen återhämtade sig inte. Runt år 2000 fanns bara några tiotal vuxna djur kvar i Sverige. Fjällräven lever mest av lämlar (små gnagare), och lämmelåren, när det finns många lämlar, har blivit ovanligare. Dessutom tar sig rödräven allt högre upp på fjället när klimatet blir mildare. Rödräven är större och konkurrerar om både mat och lyor (hålor där ungarna föds).",
        "Med stödutfodring (människor lägger ut extra mat) och jakt på rödräv nära lyorna har fjällräven ökat igen, men den är fortfarande hotad."
      ],
      bild: "bilder/mangfald-fjallrav-rodrav.png",
      bildText: "Bild 3.4 Fjällräven (till vänster) är mindre och har små öron. Rödräven har längre ben och stora öron.",
      bildBredd: 520,
      kontrollfraga: "Ge två orsaker till att fjällräven har haft svårt att öka.",
      kontrollsvar: "Till exempel att lämmelåren har blivit ovanligare (fjällräven lever mest av lämlar) och att rödräven tar sig högre upp på fjället när klimatet blir mildare och konkurrerar om mat och lyor. Jakt är inte en orsak nu, eftersom fjällräven är fridlyst sedan 1928."
    },
    {
      ikon: "🌲",
      titel: "Gammal skog och signalarter",
      text: [
        "I skog som aldrig har kalavverkats (där man aldrig har avverkat alla träd på en gång) finns gamla träd, död ved och hängande lavar. Många arter kan bara leva där. Ett exempel är garnlaven, som hänger i långa grågröna trådar från granar. Den kallas en <strong>signalart</strong>: hittar man den är skogen troligen gammal och artrik. Hänglavar är också viktig reservföda för renarna, särskilt när snön har låst betet."
      ],
      bild: "bilder/mangfald-garnlav.png",
      bildText: "Bild 3.5 Garnlav – en signalart.",
      bildBredd: 220,
      kontrollfraga: "Vad är en signalart? Ge ett exempel.",
      kontrollsvar: "En art som visar att en miljö har höga naturvärden, till exempel att den är artrik eller har många sällsynta arter. Exempel: garnlav, som visar att en skog troligen är gammal och artrik."
    },
    {
      ikon: "🏞️",
      titel: "Fria älvar och fjäll i förändring",
      text: [
        "Torne, Kalix och Pite älv är tre av Sveriges fyra nationalälvar, som skyddas från nya stora vattenkraftverk. Där kan laxen fortfarande vandra upp för att leka. Fjällen är däremot den landskapstyp i Sverige där andelen rödlistade arter har ökat mest. Orsaken är främst att klimatet blir varmare och att skog och buskar breder ut sig uppåt."
      ]
    },
    {
      ikon: "🗣️",
      titel: "Samhällsfrågan: Vad ska skogen användas till?",
      text: [
        "Skogen i Norrbotten ger jobb, virke och biobränsle. Den är också hem för tusentals arter och betesmark för renar. Olika grupper ser olika saker i samma skog. Det här är en fråga om <strong>hållbar utveckling</strong>: hur vi kan använda naturen utan att framtida generationer och naturen själv förlorar. Citaten nedan är <em>ståndpunkter</em>, inte fakta.",
        "<strong>Skogsbolaget:</strong> ”Skogsbruket ger jobb i hela länet och virke som kan ersätta plast och betong. Vi lämnar kvar gamla träd och skyddar värdefulla områden.”<br><strong>Miljöorganisation:</strong> ”Det finns för lite gammal skog kvar. Kalhyggen (där alla träd avverkas på en gång) förstör livsmiljöer som tar hundratals år att bygga upp.”<br><strong>Renskötaren:</strong> ”När gammal skog avverkas försvinner hänglaven. Då har renarna mindre att äta på vintern.”<br><strong>Kommunen:</strong> ”Vi behöver både arbetstillfällen och natur som lockar turister och gör det skönt att bo här.”",
        "Välj en ståndpunkt. Ge två argument med biologisk grund och bemöt ett argument från en annan grupp. Fundera också på vilka intressen varje avsändare har och vad du skulle vilja kontrollera."
      ],
      kontrollfraga: "Skriv ett kort svar: vilken ståndpunkt väljer du, och varför?",
      kontrollsvar: "Ett starkt svar tar ställning, ger minst två biologiska argument (till exempel att gammal skog är livsmiljö för många arter och signalarter, eller att skogen ger jobb och virke), och bemöter ett argument från en annan grupp. Ju fler led du resonerar i (”eftersom … därför … vilket leder till …”) och ju mer balanserat du väger olika intressen, desto starkare blir svaret."
    },
    {
      ikon: "🌱",
      titel: "Vad kan vi göra?",
      text: [
        "Det viktigaste för att skydda den biologiska mångfalden är att bevara och återskapa livsmiljöer. Det sker på flera nivåer samtidigt – från FN till din egen trädgård.",
        "<strong>Världen:</strong> år 2022 kom världens länder överens om att skydda och bevara 30 procent av jordens land, sötvatten och hav till år 2030.<br><strong>Sverige:</strong> nationalparker och naturreservat skyddar natur. I Norrbotten finns världsarvet Laponia med bland annat Sarek och Padjelanta. Lagar styr skogsbruk, jakt och fiske.<br><strong>Du själv:</strong> låt en bit gräsmatta bli äng. Välj hållbart fiskad mat (fisk från bestånd som inte fiskas för hårt). Du kan också engagera dig i frågor som ändrar mer än en enskild handling, till exempel hur skog och hav ska användas. Rapportera arter du ser i Artportalen (en webbplats där alla kan rapportera sina fynd). Släng aldrig trädgårdsväxter i naturen – de kan bli invasiva, som blomsterlupinen.",
        "Ibland behöver naturen hjälp att återhämta sig. Man kan till exempel dämma igen diken så att en myr blir blöt igen, låta kor beta igenvuxna ängar eller bränna skog under kontroll. Många arter i skogen är nämligen anpassade till skogsbränder."
      ]
    },
    {
      ikon: "🔬",
      titel: "Undersök själv: Hur många arter finns i en ruta?",
      text: [
        "<strong>Frågeställning:</strong> Finns det fler växtarter på en ängsmark än på en klippt gräsmatta?",
        "<strong>Hypotes:</strong> Skriv vad du tror och varför innan du börjar.",
        "<strong>Material:</strong> 4 pinnar, 4 m snöre, tumstock, mobilkamera eller artbok/app.",
        "<strong>Gör så här:</strong><br>1. Märk ut en ruta på 1 × 1 meter med pinnar och snöre på ängen.<br>2. Räkna hur många olika växtarter som finns i rutan. Du behöver inte veta vad de heter – ta en bild och ge dem nummer.<br>3. Gör likadant på gräsmattan.<br>4. Upprepa med minst tre rutor på varje plats. Varför är det viktigt?<br>5. Skriv in resultatet i en tabell och räkna ut medelvärdet för varje plats. Gör rutorna lika stora och undersök på samma dag, så att jämförelsen blir rättvis. Visa gärna resultatet i ett stapeldiagram.",
        "<table class=\"mini-tabell\"><tr><th>Plats</th><th>Ruta 1</th><th>Ruta 2</th><th>Ruta 3</th><th>Medelvärde</th></tr><tr><td>Äng</td><td></td><td></td><td></td><td></td></tr><tr><td>Gräsmatta</td><td></td><td></td><td></td><td></td></tr></table>",
        "<strong>Utvärdera:</strong> Stämde din hypotes? Vad kan ha påverkat resultatet, till exempel tid på året, var du lade rutan eller om du kunde skilja arterna åt? Hur skulle du kunna göra undersökningen mer tillförlitlig? Tänk också på att du bara mäter en del av mångfalden: antalet växtarter."
      ],
      kontrollfraga: "Varför ska man upprepa mätningen i minst tre rutor på varje plats?",
      kontrollsvar: "För att slumpen ska jämnas ut. En enda ruta kan råka ha ovanligt många eller få arter. Med flera rutor kan man räkna ut ett medelvärde som är mer tillförlitligt.",
      bild: "bilder/mangfald-provruta.png",
      bildText: "Bild 3.6 En provruta på 1 × 1 meter (1 kvadratmeter).",
      bildBredd: 420
    }
  ],
  begrepp: [
    { term: "Rödlista", forklaring: "Förteckning över arter som riskerar att dö ut, med en bedömning av hur stor risken är." },
    { term: "Invasiv art", forklaring: "En art som människan fört in och som sprider sig och skadar inhemska arter." },
    { term: "Livsmiljö", forklaring: "Den plats där en art kan leva och föröka sig." },
    { term: "Signalart", forklaring: "Art som visar att en miljö har höga naturvärden." },
    { term: "Överuttag", forklaring: "När människan tar mer ur naturen än vad som hinner växa till." }
  ],
  exitTicket: [
    {
      fraga: "Nämn tre hot mot den biologiska mångfalden och ge ett exempel på varje.",
      svar: "Tre av dessa, till exempel ändrad markanvändning (skog avverkas), överuttag (överfiske), klimatförändringar (fjällens arter har ingenstans att ta vägen), föroreningar (miljögifter, plast, övergödning) och invasiva arter (blomsterlupin)."
    }
  ]
};

window.innehall = innehall;
