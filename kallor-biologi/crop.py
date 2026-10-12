from PIL import Image
K=220/50
def crop(src,page,box,name,outdir):
    im=Image.open(f'{src}-{page:02d}.png');x0,y0,x1,y1=[int(v*K) for v in box]
    im.crop((x0,y0,x1,y1)).save(f'{outdir}/{name}.png')
def sheet(outdir,names,path,W=1400):
    ims=[Image.open(f'{outdir}/{n}.png') for n in names]
    ims=[i.resize((W,int(i.size[1]*W/i.size[0]))) if i.size[0]>W else i for i in ims]
    h=sum(i.size[1]+6 for i in ims);m=Image.new('RGB',(max(i.size[0] for i in ims),h),'#888');y=0
    for i in ims:m.paste(i,(0,y));y+=i.size[1]+6
    m.save(path)
