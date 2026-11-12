import re,sys
f=float(sys.argv[2]); p=sys.argv[1]; s=open(p.replace('.py','.orig')).read()
def sc(m):
    v=float(m.group(2))
    if 7.5<=v<=12.6: v=round(v*f*10)/10
    return m.group(1)+('%g'%v)+'pt'
# font shorthand "font:[700 ]Xpt" and font-size:Xpt
i=s.index('DYS_TEXT = r')
a,b=s[:i],s[i:]
orig_b=open(p.replace('.py','.orig')).read()
j=orig_b.index('DYS_TEXT = r')
def scl(x):
    x=re.sub(r'(font:(?:italic |700 |bold )?)(\d+(?:\.\d+)?)pt',sc,x)
    return re.sub(r'(font-size:)(\d+(?:\.\d+)?)pt',sc,x)
out=scl(orig_b[:j])+orig_b[j:]
# POST: något tätare sida så att labbsidor inte flödar över
out=out.replace('margin:14mm 14.8mm 17mm 18mm','margin:12mm 14.8mm 15mm 18mm',1)
out=out.replace('font-size:12pt;line-height:1.46','font-size:12pt;line-height:1.4',1)
open(p,'w').write(out)
