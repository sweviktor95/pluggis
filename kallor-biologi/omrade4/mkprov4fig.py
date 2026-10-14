# Figur till prov 4: sorkpopulation (påhittade siffror). Kör: python3 mkprov4fig.py
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
for f in fm.findSystemFonts():
    if "Carlito" in f: fm.fontManager.addfont(f)
plt.rcParams["font.family"] = "Carlito"
yrs = list(range(2014, 2022)); v = [50, 110, 200, 340, 520, 560, 190, 150]
fig, ax = plt.subplots(figsize=(7.04, 3.75), dpi=100); fig.patch.set_facecolor("#f6f9f6"); ax.set_facecolor("#f6f9f6")
ax.plot(yrs, v, color="#2d6a4f", lw=3.2, marker="o", ms=8)
ax.set_title("Sorkar på ett fält (påhittade siffror)", color="#4a5d55", fontsize=14, pad=12)
ax.set_xlabel("År", color="#4a5d55", fontsize=12); ax.set_ylabel("Antal sorkar", color="#4a5d55", fontsize=12)
ax.set_xticks(yrs); ax.set_ylim(0, 720)
for s in ("top", "right"): ax.spines[s].set_visible(False)
ax.annotate("Mycket torr sommar", xy=(2019.5, 395), xytext=(2019.5, 650), ha="center", color="#c0392b", fontsize=13, arrowprops=dict(arrowstyle="->", color="#c0392b"))
fig.tight_layout(); fig.savefig("/tmp/bio/fig04n/p_sorkar.png", facecolor=fig.get_facecolor())
