#!/usr/bin/python
import sys

meat=[
    'Antilocapra',
    'Apteryx',
    'Bison',
    'Bos',
    'bovine',
    'Bovine',
    'Brown',
    'B.taurus',
    'Bubalus',
    'Capra',
    'Cervus',
    'C.hircus',
    'Cow',
    'Giraffa',
    'Goat',
    'Homo',
    'M.muntjak',
    'Muntiacus',
    'Mus',
    'O.aries',
    'Odocoileus',
    'Ovis',
    'Pantholops',
    'Pig',
    'Sus',
    'Tragelaphus',
    'Camelus',
    'Equus'
]

parasites=[
    'Babesia',
    'Eimeria',
    'Gongylonema',
    'Onchocerca'#,
#    'Wuchereria'
]

for fn in sys.argv[1:]:
    mv=0
    pv=0
    for line in file(fn):
        [org, num] = line.split('\t')
        num=int(num.rstrip())
        if org=='Raw Data':
            tot=num
        [genus, species] = org.split(' ')
        if genus in meat or species in meat:
            if num>mv:
                mv=num
        if genus in parasites or  species in parasites:
            if num>pv:
                pv=num
    print '%s\t%d\t%d\t%d' % (fn,tot,mv,pv)
