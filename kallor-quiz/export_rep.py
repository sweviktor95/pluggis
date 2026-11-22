# -*- coding: utf-8 -*-
"""Bygger innehall/repetition.js: frågebank per kapitel (flervalsfrågor från Blooket-filerna) och
Tänk tillbaka-frågor per moment (ur kapitlens KQ med facit). Kör: python3 kallor-quiz/export_rep.py"""
import csv, glob, json, os, re, ast
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
bank = {}
for f in sorted(glob.glob(R + '/planering/*/*-blooket.csv')):
    m = re.search(r'/(biologi|kemi)-(\d)-blooket\.csv$', f)
    if not m: continue
    amne, nr = m.group(1), int(m.group(2))
    rows = [r for r in csv.reader(open(f, encoding='utf-8-sig')) if len(r) > 7 and r[7].strip().isdigit()]
    fr = []
    for r in rows:
        alts = [a for a in r[2:6] if a.strip()]
        ratt = int(r[7]) - 1
        if not r[1].strip() or ratt >= len(alts): continue
        fr.append([r[1].strip(), alts, ratt])
    nod = {('biologi', 1): 'biologi-vetenskap', ('biologi', 4): 'biologi-ekologi'}.get((amne, nr), f'{amne}-omrade-{nr}')
    bank[nod] = {'pre': f'{amne}-m-{nr}-', 'fr': fr}
# Tänk tillbaka: KQ ur kapitelfilerna (fråga, facit) per moment
kq_files = {f'kemi-{n}': R + f'/kallor-kemi/omrade{n}/ch0{n}k.py' for n in range(1, 5)}
kq_files['biologi-3'] = R + '/kallor-biologi/omrade3/ch03n.py'
tt = {}
for key, path in kq_files.items():
    src = open(path, encoding='utf-8').read()
    m = re.search(r'^KQ = (\{.*?^\})\s*$', src, re.S | re.M)
    if not m: print('saknar KQ', path); continue
    kq = ast.literal_eval(m.group(1))
    amne, nr = key.split('-')
    for k, qa in kq.items():
        if k == 'Start': continue
        tt[f'{amne}-m-{nr}-' + k.replace('.', '-')[2:]] = [list(x) for x in qa]
js = ('// Genereras av kallor-quiz/export_rep.py - ändra inte för hand.\n'
      '// repBank: per kapitelnod {pre: momentprefix, fr: flervalsfrågor [fråga, [svar...], index på rätt svar]. tankTillbaka: [fråga, facit] per moment.\n'
      'var repBank = ' + json.dumps(bank, ensure_ascii=False) + ';\n'
      'var tankTillbaka = ' + json.dumps(tt, ensure_ascii=False) + ';\n')
open(R + '/innehall/repetition.js', 'w', encoding='utf-8').write(js)
print({k: len(v['fr']) for k, v in bank.items()}, len(tt))
