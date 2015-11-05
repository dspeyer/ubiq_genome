import os
import shutil
import sys
from glob import glob

def alter(genus):
	if genus=="Bovine" or genus=="B.taurus" or genus=="bovine" or genus=="Cow":
		genus="Bos"
	if genus=="S.lycopersicum" or genus=="Tomato" or genus=="Lycopersicon" or genus=="Duckeodendron" or genus=="L.esculentum":
		genus="Solanum"
	if genus=="Human":
		genus="Homo"
	if genus=="Pig":
		genus="Sus"
	if genus=="Tobacco" or genus=="N.sylvestris":
		genus="Nicotiana"
	if genus=="Goat":
		genus="Capra"
	if genus=="H.annuus":
		genus="Helianthus"
	return genus

def finder(path):
    path='hasspec/'
    genuslist=['Solanum', 'Ovis', 'Bos', 'Babesia', 'Wuchereria', 'Gongylonema', 'Capsicum', 'Homo', 'Onchocerca', 'Bison', 'Capra', 'Bubalus', 'Petunia',  'Sus', 'Nicotiana', 'Mus', 'Canis', 'Hevea', 'Pan', 'Eimeria', 'Mitreola', 'Oreocarya', 'Beta', 'Pongo', 'Muntiacus', 'Cucumis', 'Odocoileus', 'Callithrix', 'Euphydryas', 'Pseudorca', 'Aepyceros', 'Pantholops', 'Physalis', 'Lemna', 'Vitis', 'Impatiens', 'Pedicularis', 'Orobanche', 'Ellisia', 'Convolvulus', 'Nolana', 'Diapensia', 'Iochroma', 'Dunalia', 'Atropa', 'Helianthus', 'Salvia', 'Boea', 'Malus']

    sdict={}
    ndict={}
    for directory, subdirectories, files in os.walk(path):
	    for fn in files:
		k=open(path+fn)
		lineitr=0
		for line in k:
		    if lineitr!=1:
			lineitr+=1
		    elif lineitr==1:
			lineitr+=1
   			line=line.split()
			genus=line[0].strip()
			genus=alter(genus)
			if genus in genuslist:
			    if genus in sdict:
			        sdict[genus]+=(float(line[2])*.1)
			        ndict[genus]+=1
			    else:
			        sdict[genus]=(float(line[2])*.1)
				ndict[genus]=1
		    else:
			lineitr+=1
    return sdict, ndict
