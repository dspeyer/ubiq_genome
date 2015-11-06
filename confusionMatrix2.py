#!/usr/bin/python

from __future__ import division
import sys
from collections import defaultdict
from tabulate import tabulate

inssize=defaultdict(lambda:0)
delsize=defaultdict(lambda:0)
insnuc=defaultdict(lambda:0)
delnuc=defaultdict(lambda:0)

tot=0

trueA = 0
AtoC = 0
AtoT = 0
AtoG = 0
Ainsert= 0
Adel = 0  
trueC = 0
CtoA = 0
CtoT = 0
CtoG = 0
Cinsert = 0
Cdel = 0
trueT = 0
TtoA = 0
TtoC = 0
TtoG = 0
Tinsert = 0
Tdel = 0  
trueG = 0
GtoA = 0
GtoC = 0
GtoT = 0
Ginsert = 0
Gdel = 0  
noClass = 0

for fn in sys.argv[1:]:
    f=file(fn)
    while f:
        try:
            name=f.next()
            pos=f.next()
            query=f.next()
            match=f.next()
            sbjct=f.next()
        except StopIteration:
            break
        [_, start, _, end, _, outof] = pos.split(' ')[:6]
        if (int(end)-int(start)) / float(outof[:-1]) < .95:
            continue
        if len(query)!=len(sbjct):
            print 'Length mismatch %s %s (%d vs %d)' % (fn, name, len(query), len(sbjct))
            continue
        tot += len(query)
        state='neither'
        indelsince=-1
	for i in xrange(0, len(query)):
		if sbjct[i] == 'A' and query[i] == 'A':
			trueA +=1
		elif sbjct[i] == 'A' and query[i] == 'C':
			AtoC +=1
		elif sbjct[i] == 'A' and query[i] == 'T':
			AtoT +=1
		elif sbjct[i] == 'A' and query[i] == 'G':
			AtoG +=1
		elif sbjct[i] == 'A' and query[i] == '-':
			Adel +=1
		elif sbjct[i] == '-' and query[i] == 'A':
			Ainsert +=1
		elif sbjct[i] == 'C' and query[i] == 'C':
			trueC +=1
		elif sbjct[i] == 'C' and query[i] == 'A':
			CtoA +=1
		elif sbjct[i] == 'C' and query[i] == 'T':
			CtoT +=1
		elif sbjct[i] == 'C' and query[i] == 'G':
			CtoG +=1
		elif sbjct[i] == 'C' and query[i] == '-':
			Cdel +=1
		elif sbjct[i] == '-' and query[i] == 'C':
			Cinsert +=1
		elif sbjct[i] == 'T' and query[i] == 'T':
			trueT +=1
		elif sbjct[i] == 'T' and query[i] == 'A':
			TtoA +=1
		elif sbjct[i] == 'T' and query[i] == 'C':
			TtoC +=1
		elif sbjct[i] == 'T' and query[i] == 'G':
			TtoG +=1
		elif sbjct[i] == 'T' and query[i] == '-':
			Tdel +=1
		elif sbjct[i] == '-' and query[i] == 'T':
			Tinsert +=1
		elif sbjct[i] == 'G' and query[i] == 'G':
			trueG +=1
		elif sbjct[i] == 'G' and query[i] == 'A':
			GtoA +=1
		elif sbjct[i] == 'G' and query[i] == 'C':
			GtoC +=1
		elif sbjct[i] == 'G' and query[i] == 'T':
			GtoT +=1
		elif sbjct[i] == 'G' and query[i] == '-':
			Gdel +=1
		elif sbjct[i] == '-' and query[i] == 'G':
			Ginsert +=1
		else:
			noClass +=1


# total = trueA + AtoC + AtoT + AtoG + Ainsert + Adel + trueC + CtoA + CtoT + CtoG + Cinsert + Cdel + trueT + TtoA + TtoC + TtoG + Tinsert + Tdel + trueG + GtoA + GtoT + GtoC + Ginsert + Gdel
# print total

# Making table

print tabulate([['A', trueA, AtoC, AtoG, AtoT, Adel], ['', (trueA/(trueA + AtoC + AtoG + AtoT + Adel)), (AtoC/(trueA + AtoC + AtoG + AtoT + Adel)), (AtoG/(trueA + AtoC + AtoG + AtoT + Adel)), (AtoT/(trueA + AtoC + AtoG + AtoT + Adel)), (Adel/(trueA + AtoC + AtoG + AtoT + Adel))], ['C', CtoA, trueC, CtoG, CtoT, Cdel], ['', (CtoA/(CtoA + trueC + CtoG + CtoT + Cdel)), (trueC/(CtoA + trueC + CtoG + CtoT + Cdel)), (CtoG/(CtoA + trueC + CtoG + CtoT + Cdel)), (CtoT/(CtoA + trueC + CtoG + CtoT + Cdel)), (Cdel/(CtoA + trueC + CtoG + CtoT + Cdel))], ['G', GtoA, GtoC, trueG, GtoT, Gdel], ['', (GtoA/(GtoA + GtoC + trueG + GtoT + Gdel)), (GtoC/(GtoA + GtoC + trueG + GtoT + Gdel)), (trueG/(GtoA + GtoC + trueG + GtoT + Gdel)), (GtoT/(GtoA + GtoC + trueG + GtoT + Gdel)), (Gdel/(GtoA + GtoC + trueG + GtoT + Gdel))], ['T', TtoA, TtoC, TtoG, trueT, Tdel], ['', (TtoA/(TtoA + TtoC + TtoG + trueT + Tdel)), (TtoC/(TtoA + TtoC + TtoG + trueT + Tdel)), (TtoG/(TtoA + TtoC + TtoG + trueT + Tdel)), (trueT/(TtoA + TtoC + TtoG + trueT + Tdel)), (Tdel/(TtoA + TtoC + TtoG + trueT + Tdel))], ['Insertion', Ainsert, Cinsert, Ginsert, Tinsert, '-'], ['', (Ainsert/(Ainsert + Cinsert + Ginsert + Tinsert)), (Cinsert/(Ainsert + Cinsert + Ginsert + Tinsert)), (Ginsert/(Ainsert + Cinsert + Ginsert + Tinsert)), (Tinsert/(Ainsert + Cinsert + Ginsert + Tinsert)), '-']], headers=['Reference', 'A', 'C', 'G', 'T', 'Deletion'])
