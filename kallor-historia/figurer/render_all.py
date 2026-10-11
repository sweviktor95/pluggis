# -*- coding: utf-8 -*-
"""Renderar alla figurer till PNG för sajten: python3 render_all.py <prefix> <modul.py>... -> REPO/bilder/<prefix>-<nyckel>.png"""
import sys, importlib.util
from playwright.sync_api import sync_playwright
prefix=sys.argv[1]; mods=sys.argv[2:]
OUT='/mnt/user-data/outputs/pluggis/bilder'
with sync_playwright() as pw:
    b=pw.chromium.launch(executable_path='/opt/pw-browsers/chromium'); pg=b.new_page(viewport={'width':900,'height':700},device_scale_factor=2)
    for p in mods:
        spec=importlib.util.spec_from_file_location("figmod",p); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        for k,svg in m.FIGS.items():
            pg.set_content(f'<html><body style="margin:0;background:transparent"><div style="width:720px">{svg}</div></body></html>')
            pg.query_selector('svg').screenshot(path=f'{OUT}/{prefix}-{k}.png',omit_background=True); print(prefix,k)
    b.close()
