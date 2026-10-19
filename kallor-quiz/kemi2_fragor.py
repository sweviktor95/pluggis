# -*- coding: utf-8 -*-
import csv, random
random.seed(2)
# (fråga, rätt, [fel1, fel2, fel3])
Q = [
 ("Vad menas med materia?", "Allt som har massa och tar plats", ["Bara fasta föremål", "Allt som går att se", "Bara det som väger mer än 1 kg"]),
 ("Hur ligger partiklarna i ett fast ämne?", "Tätt i ett mönster och de vibrerar", ["Långt ifrån varandra", "De glider fritt förbi varandra", "De står helt stilla"]),
 ("Hur rör sig partiklarna i en gas?", "Snabbt åt alla håll med stora avstånd", ["De ligger tätt i ett mönster", "De glider förbi varandra tätt", "De rör sig inte alls"]),
 ("Vad bevisar att partiklar rör sig?", "Diffusion, till exempel att doft sprids", ["Att vatten är blött", "Att is är hård", "Att metall leder värme"]),
 ("Hur räknar man ut densitet?", "Massa delat med volym", ["Volym delat med massa", "Massa gånger volym", "Massa plus volym"]),
 ("Ett föremål har massan 24 g och volymen 8 cm³. Vilken densitet har det?", "3 g/cm³", ["16 g/cm³", "32 g/cm³", "0,33 g/cm³"]),
 ("Varför flyter is på vatten?", "Is har lägre densitet än flytande vatten", ["Is är kallare", "Is har högre densitet", "Is har ingen massa"]),
 ("Hur mäter man volymen hos en sten med oregelbunden form?", "Med vattenförskjutning i en mätcylinder", ["Med en våg", "Med en termometer", "Med ett filter"]),
 ("Vad kallas övergången från fast form till vätska?", "Smältning", ["Kondensation", "Förångning", "Stelning"]),
 ("Vad kallas övergången från gas till vätska?", "Kondensation", ["Smältning", "Stelning", "Fällning"]),
 ("Varför ligger temperaturen still medan is smälter?", "Värmen går åt att bryta loss partiklarna", ["Isen tar inte emot värme", "Termometern slutar fungera", "Vattnet är redan 100 °C"]),
 ("Vad är ett rent ämne?", "Ett ämne med bara en sorts partiklar", ["Ett ämne utan färg", "Ett ämne som är flytande", "En blandning av två ämnen"]),
 ("Vilket är en homogen blandning?", "Saltvatten", ["Sand i vatten", "Sallad", "Granit"]),
 ("Vad kallas det som löser ett ämne i en lösning?", "Lösningsmedel", ["Fällning", "Filtrat", "Destillat"]),
 ("Vilken metod skiljer sand från vatten?", "Filtrering", ["Kromatografi", "Fällning", "Diffusion"]),
 ("Hur får du tillbaka saltet ur saltvatten?", "Indunsta vattnet", ["Filtrera blandningen", "Frys blandningen", "Rör om länge"]),
 ("Varför går löst salt inte att filtrera bort?", "Saltpartiklarna är så små att de går genom filtret", ["Salt är för tungt", "Filtret löser salt", "Salt är en gas"]),
 ("På vad bygger destillation?", "Att ämnen har olika kokpunkter", ["Att ämnen har olika färg", "Att ämnen har olika massa", "Att ämnen har olika form"]),
 ("Vad används kromatografi till?", "Att skilja ämnen som vandrar olika långt", ["Att mäta densitet", "Att filtrera sand", "Att kyla vätskor"]),
 ("Vad är en fällning?", "Ett fast ämne som bildas när lösningar blandas", ["En gas som bildas vid kokning", "Ett filter av papper", "En sorts lösningsmedel"]),
 ("Ett lag skulle få 5,0 g salt men fick 4,2 g. Vad blir utbytet?", "84 %", ["16 %", "119 %", "4,2 %"]),
 ("Varför räcker det inte att mäta en egenskap för att identifiera ett ämne?", "Flera ämnen kan ha liknande värde på en egenskap", ["Egenskaper går inte att mäta", "Alla ämnen har samma egenskaper", "Det räcker alltid med smältpunkt"]),
]
rows=[["Question #","Question Text","Answer 1","Answer 2","Answer 3 (Optional)","Answer 4 (Optional)","Time Limit (sec) (Max: 300 seconds)","Correct Answer(s) (Only include Answer #)"]]
for n,(q,r,w) in enumerate(Q,1):
    a=[r]+w; random.shuffle(a)
    t=30 if ("Ett " in q or "Ett lag" in q) else 20
    rows.append([n,q]+a+[t,a.index(r)+1])
with open('/tmp/kem/out/kemi-2-blooket.csv','w',encoding='utf-8',newline='') as f: csv.writer(f).writerows(rows)
print(len(rows)-1)
