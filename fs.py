import binarys
import os
print("\033c\033[47;30m\nget me a file script to open .fs")
a=input().strip()
b=a.replace(".fs","")
f1=open(a,"r")
c=f1.read()
f1.close()
cc=c.split("\n")

f1=binarys.openw(b+".bin",)
counter=1
for n in cc:
    nn=n.split("=")
    if len(nn)>1:
        nn[0]=nn[0].strip()
        nn[1]=nn[1].strip()
        nn[0]=nn[0].lower()
        if nn[0]=="string":
            nn[1]=nn[1].replace("\\n","\n")
            nn[1]=nn[1].replace("\\r","\r")
            nn[1]=nn[1].replace("\\t","\t")
            nn[1]=nn[1].replace("\\a","\a")
            nn[1]=nn[1].replace("\\b","\b")
            binarys.writesS(f1,nn[1])
        elif nn[0]=="int":
            ff=nn[1].split(",")
            for f in ff:
                f=f.strip()
                binarys.writesi(f1,int(f))
        elif nn[0]=="float":
            ff=nn[1].split(",")
            for f in ff:
                f=f.strip()
                binarys.writesf(f1,float(f))
        elif nn[0]=="short":
            ff=nn[1].split(",")
            for f in ff:
                f=f.strip()
                binarys.writeshh(f1,int(f))
        elif nn[0]=="array":
            ff=nn[1].split(",")
            fff=[]
            for f in ff:
                f=f.strip()
                fff.append(int(int(f)& 0xff))
            binarys.writesb(f1,fff)
        elif nn[0]=="file":
            ff=nn[1].split(",")
            fff=[]
            for f in ff:
                f=f.strip()
                f2=open(f,"br")
                xc=f2.read()
                f2.close()
                binarys.writesb(f1,xc)
        elif nn[0]=="size":
            nn[1]=nn[1].replace("\\n","\n")
            nn[1]=nn[1].replace("\\r","\r")
            nn[1]=nn[1].replace("\\t","\t")
            nn[1]=nn[1].replace("\\a","\a")
            nn[1]=nn[1].replace("\\b","\b")
            binarys.savesS(f1,nn[1])
        

binarys.closew(f1)