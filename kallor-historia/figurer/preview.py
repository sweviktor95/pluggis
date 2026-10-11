# -*- coding: utf-8 -*-
"""python3 /tmp/figs/preview.py <modul-sökväg.py> [nyckel...]  -> /tmp/figs/prev/<nyckel>.png (för att titta på med Read)"""
import sys, os, importlib.util
from playwright.sync_api import sync_playwright
p=sys.argv[1]; spec=importlib.util.spec_from_file_location("figmod",p); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
keys=sys.argv[2:] or list(m.FIGS)
os.makedirs('/tmp/figs/prev',exist_ok=True)
with sync_playwright() as pw:
    b=pw.chromium.launch(executable_path='/opt/pw-browsers/chromium'); pg=b.new_page(viewport={'width':900,'height':700},device_scale_factor=1.5)
    for k in keys:
        pg.set_content(f'<html><body style="margin:0;background:#fff"><div style="width:800px">{m.FIGS[k]}</div></body></html>')
        el=pg.query_selector('svg'); el.screenshot(path=f'/tmp/figs/prev/{k}.png'); print('prev',k)
    b.close()
