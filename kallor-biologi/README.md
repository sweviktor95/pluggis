# Källor: biologi kapitel 4 (Ekologi)
Bygger alla sex PDF:er (vanlig, lättläst, fördjupning, med/utan lärarversion) från HTML via Chromium.
Kopiera mappen till /tmp/bio, ha typsnitt i /tmp/fonts (Lora) och kör:
  python3 bbuild.py --k ; python3 bbuild_latt.py ; python3 bbuild_fordj.py
Resultat hamnar i out/. Figurer ligger i fig/.

Flera kapitel: välj kapitel med miljövariabeln CH (t.ex. CH=01 python3 bbuild.py --k).
Kapitel 1 ligger i ch01.py, ch01_latt.py, ch01_fordj.py med figurer i fig01/. Hjälpskript: findfig.py (hittar figurer i gamla PDF:er), crop.py, mont.py (kontaktark), mkcykel.py (ritar forskningscykeln).
