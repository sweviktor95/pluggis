const pptxgen = require("pptxgenjs");
const sharp = require("sharp");
const SK = "/root/.claude/skills/synced/6ae81e9c-8cca-465f-9842-aa2795e9fcf8_27c14566-9107-4d09-9b16-8940ba7b45cb/pptx";
const { applyTheme } = require(SK + "/scripts/apply_theme.js");
const FIG = process.env.FIG || "/tmp/bio/fig01n/";
const THEME = {
  name: "Biologi grön", headFontFace: "Calibri", bodyFontFace: "Calibri",
  colors: { dk1: "1F2A24", lt1: "FFFFFF", dk2: "245040", lt2: "EAF3EC", accent1: "2F6B4F", accent2: "E0782F", accent3: "4F8A63", accent4: "2B6A8A", accent5: "A8651A", accent6: "B3402F", hlink: "2B6A8A", folHlink: "6B625B" }
};
const W = 13.33, H = 7.5, MX = 0.6;

async function size(f) { const m = await sharp(FIG + f).metadata(); return [m.width, m.height]; }
async function fit(f, bw, bh) { const [w, h] = await size(f); const r = Math.min(bw / w, bh / h); return [w * r, h * r]; }

async function build(cfg) {
  const pres = new pptxgen();
  pres.layout = "LAYOUT_WIDE";
  pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
  pres.title = cfg.title; pres.author = "Pluggis"; pres.subject = "Biologi åk 7–9";
  const C = pres.SchemeColor;
  const foot = cfg.foot;
  pres.defineSlideMaster({ title: "TITEL", background: { color: C.accent1 }, objects: [] });
  pres.defineSlideMaster({ title: "AVSNITT", background: { color: C.text2 }, objects: [
    { placeholder: { options: { name: "title", type: "title", x: 0.8, y: 2.3, w: 11.7, h: 1.6, fontSize: 44, bold: true, color: C.background1, align: "left", valign: "middle", margin: 0 }, text: "" } },
    { placeholder: { options: { name: "body", type: "body", x: 0.8, y: 4.0, w: 11.7, h: 0.9, fontSize: 22, color: C.background2, align: "left", valign: "top", margin: 0 }, text: "" } }] });
  pres.defineSlideMaster({ title: "INNEHALL", background: { color: C.background1 }, slideNumber: { x: W - 1.0, y: H - 0.5, w: 0.5, h: 0.3, fontSize: 11, color: C.text2 },
    objects: [
      { placeholder: { options: { name: "title", type: "title", x: MX, y: 0.35, w: W - 2 * MX, h: 1.0, fontSize: 36, bold: true, color: C.text2, align: "left", valign: "middle", margin: 0 }, text: "" } },
      { text: { text: foot, options: { x: MX, y: H - 0.5, w: 9, h: 0.3, fontSize: 11, color: C.text2, margin: 0, isTextBox: true } } }] });

  const sections = {};
  function sec(name) { if (!sections[name]) { pres.addSection({ title: name }); sections[name] = 1; } return name; }
  function newSlide(master, section, notes) { const s = pres.addSlide({ masterName: master, sectionTitle: section }); if (notes) s.addNotes(notes); return s; }

  // title slide
  { sec("Start"); const s = newSlide("TITEL", "Start", cfg.titleNotes);
    s.addText(cfg.kicker, { x: 0.8, y: 1.6, w: 11.7, h: 0.5, fontSize: 20, bold: true, color: C.background2, margin: 0, isTextBox: true, charSpacing: 4 });
    s.addText(cfg.title, { x: 0.8, y: 2.2, w: 11.7, h: 1.8, fontSize: 54, bold: true, color: C.background1, margin: 0, valign: "top", isTextBox: true });
    s.addText(cfg.sub, { x: 0.8, y: 4.3, w: 11.7, h: 1.2, fontSize: 24, color: C.background1, margin: 0, valign: "top", isTextBox: true });
    s.addText(cfg.lessons, { x: 0.8, y: 6.2, w: 11.7, h: 0.6, fontSize: 16, color: C.background2, margin: 0, isTextBox: true });
  }

  const helpers = {
    section(name, sub, notes) { sec(name); const s = newSlide("AVSNITT", name, notes); s.addText(name, { placeholder: "title" }); s.addText(sub, { placeholder: "body" }); },
    async imgText(sect, title, bullets, img, o = {}) {
      const s = newSlide("INNEHALL", sect, o.notes); s.addText(title, { placeholder: "title" });
      const left = o.imgLeft; const iw = o.iw || 5.6, ih = 4.9; const [w, h] = await fit(img, iw, ih);
      const tx = left ? MX + iw + 0.5 : MX, tw = W - 2 * MX - iw - 0.5; const ix = left ? MX + (iw - w) / 2 : MX + tw + 0.5 + (iw - w) / 2;
      s.addText(bullets.map((b, i) => ({ text: b, options: { bullet: true, breakLine: i < bullets.length - 1, paraSpaceAfter: 10 } })), { x: tx, y: 1.7, w: tw, h: 4.9, fontSize: o.fs || 24, color: C.text1, valign: "top", margin: 0, isTextBox: true });
      s.addImage({ path: FIG + img, x: ix, y: 1.7 + (ih - h) / 2, w, h, altText: o.alt || title });
      if (o.cap) s.addText(o.cap, { x: ix - 0.2, y: 1.7 + (ih + h) / 2 + 0.05, w: w + 0.4, h: 0.5, fontSize: 12, color: C.text2, italic: true, margin: 0, isTextBox: true, align: "center" });
      return s; },
    cards(sect, title, items, o = {}) {
      const s = newSlide("INNEHALL", sect, o.notes); s.addText(title, { placeholder: "title" });
      const n = items.length, gap = 0.3, cw = (W - 2 * MX - gap * (n - 1)) / n, cy = 1.7, ch = o.h || 4.2;
      const cols = [C.accent1, C.accent2, C.accent4, C.accent5];
      items.forEach(([h, t], i) => { const x = MX + i * (cw + gap);
        s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: cy, w: cw, h: ch, rectRadius: 0.12, fill: { color: C.background2 }, line: { color: C.background2, width: 0 }, objectName: "Kort " + (i + 1) });
        s.addShape(pres.shapes.OVAL, { x: x + 0.25, y: cy + 0.25, w: 0.55, h: 0.55, fill: { color: cols[i % 4] }, line: { color: cols[i % 4], width: 0 }, objectName: "Siffra " + (i + 1) });
        s.addText(String(i + 1), { x: x + 0.25, y: cy + 0.25, w: 0.55, h: 0.55, fontSize: 18, bold: true, color: C.background1, align: "center", valign: "middle", margin: 0, isTextBox: true });
        s.addText(h, { x: x + 0.25, y: cy + 0.95, w: cw - 0.5, h: 0.6, fontSize: 22, bold: true, color: C.text2, margin: 0, valign: "top", isTextBox: true });
        s.addText(t, { x: x + 0.25, y: cy + 1.6, w: cw - 0.5, h: ch - 1.8, fontSize: 18, color: C.text1, margin: 0, valign: "top", isTextBox: true }); });
      if (o.note) s.addText(o.note, { x: MX, y: 6.15, w: W - 2 * MX, h: 0.7, fontSize: 16, bold: true, color: C.accent2, margin: 0, isTextBox: true });
      return s; },
    table(sect, title, head, rows, o = {}) {
      const s = newSlide("INNEHALL", sect, o.notes); s.addText(title, { placeholder: "title" });
      const hdr = head.map(t => ({ text: t, options: { bold: true, color: C.background1, fill: { color: C.accent1 }, fontSize: o.fs || 20 } }));
      const body = rows.map(r => r.map((t, j) => ({ text: t, options: { fontSize: o.fs || 20, bold: j === 0, color: C.text1, fill: { color: C.background1 } } })));
      s.addTable([hdr, ...body], { x: MX, y: 1.7, w: W - 2 * MX, colW: o.colW, border: { type: "solid", color: "C9D8CD", pt: 1 }, margin: [0.08, 0.12, 0.08, 0.12], valign: "middle", autoPage: false, rowH: o.rowH || 0.8 });
      if (o.note) s.addText(o.note, { x: MX, y: o.noteY || 6.1, w: W - 2 * MX, h: 0.8, fontSize: 18, bold: true, color: C.accent2, margin: 0, isTextBox: true });
      return s; },
    steps(sect, title, items, o = {}) {
      const s = newSlide("INNEHALL", sect, o.notes); s.addText(title, { placeholder: "title" });
      const rh = Math.min(0.95, 4.9 / items.length);
      items.forEach((t, i) => { const y = 1.65 + i * rh;
        s.addShape(pres.shapes.OVAL, { x: MX, y: y + 0.08, w: 0.55, h: 0.55, fill: { color: C.accent2 }, line: { color: C.accent2, width: 0 }, objectName: "Steg " + (i + 1) });
        s.addText(String(i + 1), { x: MX, y: y + 0.08, w: 0.55, h: 0.55, fontSize: 18, bold: true, color: C.background1, align: "center", valign: "middle", margin: 0, isTextBox: true });
        s.addText(t, { x: MX + 0.85, y, w: (o.tw || W - 2 * MX - 0.85), h: 0.7, fontSize: 24, color: C.text1, valign: "middle", margin: 0, isTextBox: true }); });
      return s; },
    kolla(sect, title, qs, o = {}) {
      const s = newSlide("INNEHALL", sect, o.notes || "Låt eleverna svara i par eller på whiteboard. Facit finns i lärarversionen av kapitlet."); s.addText(title, { placeholder: "title" });
      s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: MX, y: 1.7, w: W - 2 * MX, h: 4.7, rectRadius: 0.15, fill: { color: C.background2 }, line: { color: C.accent3, width: 2 }, objectName: "Kolla dig själv" });
      s.addText("KOLLA DIG SJÄLV", { x: MX + 0.4, y: 1.9, w: 6, h: 0.4, fontSize: 14, bold: true, color: C.accent1, charSpacing: 3, margin: 0, isTextBox: true });
      s.addText(qs.map((q, i) => ({ text: q, options: { bullet: { type: "number" }, breakLine: i < qs.length - 1, paraSpaceAfter: 12 } })), { x: MX + 0.4, y: 2.4, w: W - 2 * MX - 0.8, h: 3.8, fontSize: 26, color: C.text1, valign: "top", margin: 0, isTextBox: true });
      return s; },
    async chartSlide(sect, title, bullets, chart, o = {}) {
      const s = newSlide("INNEHALL", sect, o.notes); s.addText(title, { placeholder: "title" });
      s.addText(bullets.map((b, i) => ({ text: b, options: { bullet: true, breakLine: i < bullets.length - 1, paraSpaceAfter: 10 } })), { x: MX, y: 1.7, w: 5.6, h: 4.9, fontSize: 22, color: C.text1, valign: "top", margin: 0, isTextBox: true });
      s.addChart(chart.type(pres), chart.data, Object.assign({ x: 6.6, y: 1.6, w: 6.1, h: 5.0, showTitle: true, showValue: chart.line ? false : true, showLegend: !!chart.legend, legendPos: "b", legendFontSize: 14, legendColor: "1F2A24",
        catAxisLabelColor: "1F2A24", valAxisLabelColor: "1F2A24", catAxisLabelFontSize: 14, valAxisLabelFontSize: 14, dataLabelFontSize: 16, dataLabelColor: "1F2A24",
        valGridLine: { color: "D9E3DC", size: 0.75 }, catGridLine: { style: "none" }, titleFontSize: 18, titleColor: "245040", catAxisLabelFontFace: "+mn-lt", valAxisLabelFontFace: "+mn-lt", dataLabelFontFace: "+mn-lt", titleFontFace: "+mn-lt", legendFontFace: "+mn-lt" }, chart.opts));
      return s; },
    stat(sect, title, big, small, bullets, o = {}) {
      const s = newSlide("INNEHALL", sect, o.notes); s.addText(title, { placeholder: "title" });
      s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: MX, y: 1.7, w: 4.6, h: 4.5, rectRadius: 0.15, fill: { color: C.accent1 }, line: { color: C.accent1, width: 0 }, objectName: "Siffra" });
      s.addText(big, { x: MX, y: 2.2, w: 4.6, h: 1.8, fontSize: 80, bold: true, color: C.background1, align: "center", valign: "middle", margin: 0, isTextBox: true });
      s.addText(small, { x: MX + 0.3, y: 4.1, w: 4.0, h: 1.8, fontSize: 18, color: C.background1, align: "center", valign: "top", margin: 0, isTextBox: true });
      s.addText(bullets.map((b, i) => ({ text: b, options: { bullet: true, breakLine: i < bullets.length - 1, paraSpaceAfter: 10 } })), { x: 5.7, y: 1.7, w: W - 5.7 - MX, h: 4.7, fontSize: 22, color: C.text1, valign: "top", margin: 0, isTextBox: true });
      return s; },
    pres, C, sec
  };
  await cfg.slides(helpers);
  const out = cfg.out;
  await pres.writeFile({ fileName: out });
  await applyTheme(out, THEME);
  console.log("wrote", out);
}
module.exports = { build, THEME };
