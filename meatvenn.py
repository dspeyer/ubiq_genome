#!/usr/bin/python

import sys
from collections import defaultdict

names = {
    "Bovine alpha": "Cow",
    "Bovine genomic": "Cow",
    "Bovine satellite": "Cow",
    "Bubalus bubalis": "Bison",
    "Capra hircus": "Goat",
    "Pig DNA": "Pin",
    "Pongo abelii": "Primate",
    "PREDICTED Bos": "Cow",
    "PREDICTED: Callithrix": "Marmoset",
    "PREDICTED: Camelus": "Camel",
    "PREDICTED: Ceratotherium": "Rhino",
    "PREDICTED: Cercocebus": "Primate",
    "PREDICTED: Chinchilla": "Chinchilla",
    "PREDICTED: Chlorocebus": "Primate",
    "PREDICTED: Homo": "Primate",
    "PREDICTED: Lipotes": "Cetacean",
    "PREDICTED: Mustela": "Weasal",
    "PREDICTED: Pan": "Primate",
    "PREDICTED: Physeter": "Cetacean",
    "PREDICTED: Pteropus": "Bat",
    "PREDICTED: Vicugna": "Alpaca",
    "Sus scrofa": "Boar",
    "Bovine 680": "Cow",
    "Human chromosome": "Primate",
    "Mus musculus": "Mouse",
    "PREDICTED: Balaenoptera": "Cetacean",
    "Human DNA": "Primate",
    "PREDICTED: Orcinus": "Cetacean",
    "Muntiacus muntjak": "Muntjak",
    "Muntiacus reevesi": "Muntjak",
    "Pan troglodytes": "Primate",
    "PREDICTED: Pantholops": "Antelope",
    "Homo sapiens": "Primate",
    "Ovis aries": "Sheep",
    "PREDICTED: Capra": "Goat",
    "PREDICTED: Bubalus": "Water Buffalo",
    "PREDICTED: Bison": "Bison",
    "B.taurus DNA": "Cow",
    "PREDICTED: Bos": "Cow",
    "Bos taurus": "Cow",
    "Ovis canadensis": "Bighorn"
}

for i in names.keys():
    if names[i] not in ['Cow', 'Sheep', 'Bighorn']:
        names[i]='Other'

cnt = defaultdict(lambda:0)
cnteach = defaultdict(lambda:0)

for fn in sys.argv[1:]:
    f=file(fn)
    spes={}
    for line in f:
        latin=line.split('\t')[0]
        if latin in names:
            spes[names[latin]] = 1
    f.close()
    for i in spes:
        cnteach[i]+=1
    spes=spes.keys()
    spes.sort()
    spes=', '.join(spes)
    cnt[spes]+=1

for i in cnt:
    print '%d\t%s' % (cnt[i], i)

print

for i in cnteach:
    print '%d\t%s' % (cnteach[i], i)
