import struct
import math
import os
def eof(file):
    current_pos = file.tell()
    file.seek(0, os.SEEK_END)
    end_pos = file.tell()
    file.seek(current_pos)
    return current_pos == end_pos
  
def openw(names:str):
    return open(names,"bw")

def openr(names:str):
    return open(names,"br")

def opena(names:str):
    return open(names,"ba")


def closew(f1):
    f1.close()


def writesS(f1,s:str):
    f1.write(s.encode())


def writesf(f1,f):
    f1.write(struct.pack('<f',f))

def writesi(f1,i:int):
    f1.write(struct.pack('<i',i))

def readsS(f1,i:int):
    r=f1.read(i)
    a=r.decode()
    return a

def readsbb(f1):
    r=f1.read(1)
    
    return r

def readsf(f1):
    r=f1.read(4)
    ff=struct.unpack('<f',r)
    return ff[0]

def readsi(f1):
    r=f1.read(4)
    ii=struct.unpack('<i',r)
    return ii[0]

def writesb(f1,c):
    f1.write(bytearray(c))
    
def writesf(f1,f):
    f1.write(struct.pack('<f',f)) 

def writesh(f1,i:int):
    f1.write(struct.pack('>H',i))

def writeshh(f1,i:int):
    f1.write(struct.pack('<h',i))


def readsh(f1):
    a=f1.read(2)
    return struct.unpack('>H',a)[0]

def readshh(f1):
    a=f1.read(2)
    return struct.unpack('<h',a)[0]

   
def savesS(f1,s:str):
    writesb(f1,[1])
    writesh(f1,len(s)+1)
    ss=s+"\x00"
    writesS(f1,ss)

def savesm(f1,ar):
    for a in ar:
        savesS(f1,a)


def savesSBs(f1,ar):
    writesb(f1,[1])
    writesh(f1,len(ar)+1)
    ar.append(0)
    writesb(f1,ar)


