#!/usr/bin/python
# Nombre de Fichero : readBin.py
import struct

f = file('prueba.bin','r')
i=1
f.seek(0,2) #vamos al final del archivo
fin = f.tell()
f.seek(0,0) #vamos al principio del archivo

while (f.tell() < fin):
    s = f.read(12)
    dato = str(struct.unpack("i b i", s)) # desempaquetamos
    print i ," ->",dato
    i+=1;
