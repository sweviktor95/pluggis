# Korrekt sidfotslyft: flyttar bara text i block UTAN översättning (sidfot och sidnummer), inte brödtexten.
import sys,re,bisect
from pypdf import PdfReader,PdfWriter
from pypdf.generic import DecodedStreamObject,NameObject
TM=re.compile(rb'(1 0 0 -1 )(-?[\d.]+) (-?[\d.]+)( Tm)')
EV=re.compile(rb'^(q|Q|(-?[\d.]+) (-?[\d.]+) (-?[\d.]+) (-?[\d.]+) (-?[\d.]+) (-?[\d.]+) cm)$',re.M)
DELTA=28.0
def fix(path,out):
    r=PdfReader(path);w=PdfWriter(clone_from=r);n=0
    for pg in w.pages:
        h=float(pg.mediabox.height)
        d=pg.get_contents().get_data()
        if not d.lstrip().startswith(b'.23999999 0 0 -.23999999'): continue
        lim=(h-28)/0.75
        st=[];cur=0.0;poss=[];tys=[]
        for m in EV.finditer(d):
            t=m.group(1)
            if t==b'q': st.append(cur)
            elif t==b'Q': cur=st.pop() if st else 0.0
            else:
                ty=float(m.group(7))
                if abs(float(m.group(2))-3.125)<0.01 and abs(ty)>1: cur=ty
            poss.append(m.start());tys.append(cur)
        def sub(m):
            nonlocal n
            i=bisect.bisect_right(poss,m.start())-1
            ty=tys[i] if i>=0 else 0.0
            y=float(m.group(3))
            if abs(ty)<=1 and y>lim:
                n+=1;return m.group(1)+m.group(2)+b' '+(b'%.5f'%(y-DELTA))+m.group(4)
            return m.group(0)
        nd=TM.sub(sub,d)
        s=DecodedStreamObject();s.set_data(nd)
        pg[NameObject('/Contents')]=w._add_object(s);pg.compress_content_streams()
    w.write(out);return n
if __name__=='__main__': print(fix(sys.argv[1],sys.argv[2]))
