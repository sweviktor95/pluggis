// Liten QR-kodsgenerator (byte-läge, felrättning L, version 1–40). Ingen extern kod.
// Användning: qrSvg("text") returnerar en SVG-sträng, eller null om texten är för lång.
(function () {
  var ECC = [-1, 7, 10, 15, 20, 26, 18, 20, 24, 30, 18, 20, 24, 26, 30, 22, 24, 28, 30, 28, 28, 28, 28, 30, 30, 26, 28, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30];
  var BLK = [-1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 4, 4, 4, 4, 4, 6, 6, 6, 6, 7, 8, 8, 9, 9, 10, 12, 12, 12, 13, 14, 15, 16, 17, 18, 19, 19, 20, 21, 22, 24, 25];
  function rawModules(v) {
    var r = (16 * v + 128) * v + 64;
    if (v >= 2) { var n = Math.floor(v / 7) + 2; r -= (25 * n - 10) * n - 55; if (v >= 7) { r -= 36; } }
    return r;
  }
  function dataCw(v) { return Math.floor(rawModules(v) / 8) - ECC[v] * BLK[v]; }
  function gfMul(x, y) { var z = 0; for (var i = 7; i >= 0; i--) { z = (z << 1) ^ ((z >>> 7) * 0x11D); z ^= ((y >>> i) & 1) * x; } return z; }
  function rsDiv(deg) {
    var r = []; for (var i = 0; i < deg - 1; i++) { r.push(0); } r.push(1);
    var root = 1;
    for (i = 0; i < deg; i++) {
      for (var j = 0; j < r.length; j++) { r[j] = gfMul(r[j], root); if (j + 1 < r.length) { r[j] ^= r[j + 1]; } }
      root = gfMul(root, 2);
    }
    return r;
  }
  function rsRem(data, div) {
    var r = div.map(function () { return 0; });
    data.forEach(function (b) { var f = b ^ r.shift(); r.push(0); div.forEach(function (c, i) { r[i] ^= gfMul(c, f); }); });
    return r;
  }
  function interleave(data, v) {
    var nb = BLK[v], el = ECC[v], raw = Math.floor(rawModules(v) / 8), ns = nb - raw % nb, sl = Math.floor(raw / nb);
    var blocks = [], div = rsDiv(el), k = 0;
    for (var i = 0; i < nb; i++) {
      var dat = data.slice(k, k + sl - el + (i < ns ? 0 : 1)); k += dat.length;
      var ecc = rsRem(dat, div);
      if (i < ns) { dat.push(0); }
      blocks.push(dat.concat(ecc));
    }
    var out = [];
    for (i = 0; i < blocks[0].length; i++) {
      for (var j = 0; j < nb; j++) { if (i !== sl - el || j >= ns) { out.push(blocks[j][i]); } }
    }
    return out;
  }
  function bit(x, i) { return ((x >>> i) & 1) !== 0; }
  function make(bytes) {
    var v, need;
    for (v = 1; v <= 40; v++) {
      need = 4 + (v <= 9 ? 8 : 16) + bytes.length * 8;
      if (need <= dataCw(v) * 8) { break; }
    }
    if (v > 40) { return null; }
    var bits = [];
    function put(val, n) { for (var i = n - 1; i >= 0; i--) { bits.push((val >>> i) & 1); } }
    put(4, 4); put(bytes.length, v <= 9 ? 8 : 16);
    bytes.forEach(function (b) { put(b, 8); });
    var cap = dataCw(v) * 8;
    put(0, Math.min(4, cap - bits.length));
    while (bits.length % 8) { bits.push(0); }
    for (var pad = 0xEC; bits.length < cap; pad ^= 0xEC ^ 0x11) { put(pad, 8); }
    var data = []; for (var i = 0; i < bits.length; i += 8) { var b = 0; for (var j = 0; j < 8; j++) { b = (b << 1) | bits[i + j]; } data.push(b); }
    var all = interleave(data, v);
    var size = v * 4 + 17, m = [], f = [];
    for (i = 0; i < size; i++) { m.push(new Array(size).fill(false)); f.push(new Array(size).fill(false)); }
    function setF(x, y, d) { m[y][x] = d; f[y][x] = true; }
    for (i = 0; i < size; i++) { setF(6, i, i % 2 === 0); setF(i, 6, i % 2 === 0); }
    function finder(cx, cy) {
      for (var dy = -4; dy <= 4; dy++) { for (var dx = -4; dx <= 4; dx++) {
        var d = Math.max(Math.abs(dx), Math.abs(dy)), x = cx + dx, y = cy + dy;
        if (x >= 0 && x < size && y >= 0 && y < size) { setF(x, y, d !== 2 && d !== 4); }
      } }
    }
    finder(3, 3); finder(size - 4, 3); finder(3, size - 4);
    var pos = [];
    if (v > 1) {
      var na = Math.floor(v / 7) + 2, step = v === 32 ? 26 : Math.ceil((v * 4 + 4) / (na * 2 - 2)) * 2;
      pos = [6]; for (var p = size - 7; pos.length < na; p -= step) { pos.splice(1, 0, p); }
    }
    for (i = 0; i < pos.length; i++) { for (j = 0; j < pos.length; j++) {
      if ((i === 0 && j === 0) || (i === 0 && j === pos.length - 1) || (i === pos.length - 1 && j === 0)) { continue; }
      for (var dy = -2; dy <= 2; dy++) { for (var dx = -2; dx <= 2; dx++) { setF(pos[i] + dx, pos[j] + dy, Math.max(Math.abs(dx), Math.abs(dy)) !== 1); } }
    } }
    function fmt(mask) {
      var d = (1 << 3) | mask, r = d;
      for (var i = 0; i < 10; i++) { r = (r << 1) ^ ((r >>> 9) * 0x537); }
      var bs = ((d << 10) | r) ^ 0x5412;
      for (i = 0; i <= 5; i++) { setF(8, i, bit(bs, i)); }
      setF(8, 7, bit(bs, 6)); setF(8, 8, bit(bs, 7)); setF(7, 8, bit(bs, 8));
      for (i = 9; i < 15; i++) { setF(14 - i, 8, bit(bs, i)); }
      for (i = 0; i < 8; i++) { setF(size - 1 - i, 8, bit(bs, i)); }
      for (i = 8; i < 15; i++) { setF(8, size - 15 + i, bit(bs, i)); }
      setF(8, size - 8, true);
    }
    fmt(0);
    if (v >= 7) {
      var r = v; for (i = 0; i < 12; i++) { r = (r << 1) ^ ((r >>> 11) * 0x1F25); }
      var vb = (v << 12) | r;
      for (i = 0; i < 18; i++) { var c = bit(vb, i), a = size - 11 + i % 3, b2 = Math.floor(i / 3); setF(a, b2, c); setF(b2, a, c); }
    }
    var k = 0;
    for (var right = size - 1; right >= 1; right -= 2) {
      if (right === 6) { right = 5; }
      for (var vert = 0; vert < size; vert++) { for (j = 0; j < 2; j++) {
        var x = right - j, up = ((right + 1) & 2) === 0, y = up ? size - 1 - vert : vert;
        if (!f[y][x] && k < all.length * 8) { m[y][x] = bit(all[k >>> 3], 7 - (k & 7)); k++; }
      } }
    }
    function mask(t) {
      for (var y = 0; y < size; y++) { for (var x = 0; x < size; x++) {
        var inv;
        switch (t) {
          case 0: inv = (x + y) % 2 === 0; break;
          case 1: inv = y % 2 === 0; break;
          case 2: inv = x % 3 === 0; break;
          case 3: inv = (x + y) % 3 === 0; break;
          case 4: inv = (Math.floor(x / 3) + Math.floor(y / 2)) % 2 === 0; break;
          case 5: inv = x * y % 2 + x * y % 3 === 0; break;
          case 6: inv = (x * y % 2 + x * y % 3) % 2 === 0; break;
          default: inv = ((x + y) % 2 + x * y % 3) % 2 === 0;
        }
        if (!f[y][x] && inv) { m[y][x] = !m[y][x]; }
      } }
    }
    function penalty() {
      var s = 0, y, x, run, dark = 0;
      for (y = 0; y < size; y++) {
        run = 1;
        for (x = 1; x < size; x++) { if (m[y][x] === m[y][x - 1]) { run++; if (run === 5) { s += 3; } else if (run > 5) { s++; } } else { run = 1; } }
        run = 1;
        for (x = 1; x < size; x++) { if (m[x][y] === m[x - 1][y]) { run++; if (run === 5) { s += 3; } else if (run > 5) { s++; } } else { run = 1; } }
      }
      for (y = 0; y < size; y++) { for (x = 0; x < size; x++) {
        if (m[y][x]) { dark++; }
        if (x > 0 && y > 0 && m[y][x] === m[y][x - 1] && m[y][x] === m[y - 1][x] && m[y][x] === m[y - 1][x - 1]) { s += 3; }
      } }
      s += Math.floor(Math.abs(dark * 20 - size * size * 10) / (size * size)) * 10;
      return s;
    }
    var best = 0, bp = Infinity;
    for (var t = 0; t < 8; t++) {
      mask(t); fmt(t); var pe = penalty(); if (pe < bp) { bp = pe; best = t; } mask(t);
    }
    mask(best); fmt(best);
    return m;
  }
  window.qrSvg = function (text, px) {
    var bytes = Array.prototype.slice.call(new TextEncoder().encode(text));
    var m = make(bytes); if (!m) { return null; }
    var n = m.length, q = 4, d = "";
    for (var y = 0; y < n; y++) { for (var x = 0; x < n; x++) { if (m[y][x]) { d += "M" + (x + q) + " " + (y + q) + "h1v1h-1z"; } } }
    var tot = n + 2 * q;
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ' + tot + ' ' + tot + '" width="' + (px || 320) + '" height="' + (px || 320) + '" shape-rendering="crispEdges" role="img" aria-label="QR-kod"><rect width="100%" height="100%" fill="#fff"/><path d="' + d + '" fill="#000"/></svg>';
  };
})();
