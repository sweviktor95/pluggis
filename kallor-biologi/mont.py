import sys,glob,subprocess
from PIL import Image
pdf,out=sys.argv[1],sys.argv[2];cols=int(sys.argv[3]) if len(sys.argv)>3 else 5;dpi=sys.argv[4] if len(sys.argv)>4 else '45'
subprocess.run(['rm','-rf','/tmp/bio/mt']);subprocess.run(['mkdir','/tmp/bio/mt'])
subprocess.run(['pdftoppm','-r',dpi,'-png',pdf,'/tmp/bio/mt/m'])
f=sorted(glob.glob('/tmp/bio/mt/m-*.png'));ims=[Image.open(x) for x in f];w,h=ims[0].size
rows=(len(ims)+cols-1)//cols;m=Image.new('RGB',(w*cols,h*rows),'white')
for i,im in enumerate(ims):m.paste(im,((i%cols)*w,(i//cols)*h))
m.save(out);print(len(ims),m.size)
