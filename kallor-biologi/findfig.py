import pdfplumber,sys
def clusters(pdf,pad=3,minw=60,minh=35):
    res={}
    with pdfplumber.open(pdf) as P:
        for i,pg in enumerate(P.pages,1):
            bx=[(o['x0'],o['top'],o['x1'],o['bottom']) for o in pg.rects+pg.curves+pg.lines if (o['x1']-o['x0'])<pg.width*0.98]
            bx=[b for b in bx if b[3]-b[1]>0.1 or b[2]-b[0]>0.1]
            # merge
            changed=True
            cl=[list(b) for b in bx]
            while changed:
                changed=False;out=[]
                for b in cl:
                    for o in out:
                        if b[0]<o[2]+pad and b[2]>o[0]-pad and b[1]<o[3]+pad and b[3]>o[1]-pad:
                            o[0]=min(o[0],b[0]);o[1]=min(o[1],b[1]);o[2]=max(o[2],b[2]);o[3]=max(o[3],b[3]);changed=True;break
                    else: out.append(b)
                cl=out
            res[i]=[tuple(round(v,1) for v in c) for c in cl if c[2]-c[0]>=minw and c[3]-c[1]>=minh]
    return res
if __name__=='__main__':
    r=clusters(sys.argv[1])
    for p,c in r.items(): print(p,c)
