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
            binarys.writesS(f1,nn[1])
        elif nn[0]=="int":
            binarys.writesi(f1,int(nn[1]))
        elif nn[0]=="float":
            binarys.writesf(f1,float(nn[1]))
        

binarys.closew(f1)