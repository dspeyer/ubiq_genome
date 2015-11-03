###########################################################################
# Confusion matrix
# path = tomatoaligns directory (/Users/annebozack/Documents/genomics/upload/ubiq_genome/tomatoaligns/)
###########################################################################

import sys
import os

path = sys.argv[1]

files = os.listdir(''+path+'')

ref = ''
read = ''
for i in range(0, len(files)):
	f = open(''+path+''+files[i]+'')
	lines = f.readlines()
	ref = ref + lines[4]
	read = read + lines[2]

ref = list(ref)
read = list(read)

# Determining matches/mismatches/indels

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

for i in range(0, len(ref)):
	if ref[i] == 'A' and read[i] == 'A':
		trueA +=1
	elif ref[i] == 'A' and read[i] == 'C':
		AtoC +=1
	elif ref[i] == 'A' and read[i] == 'T':
		AtoT +=1
	elif ref[i] == 'A' and read[i] == 'G':
		AtoG +=1
	elif ref[i] == 'A' and read[i] == '-':
		Adel +=1
	elif ref[i] == '-' and read[i] == 'A':
		Ainsert +=1
	elif ref[i] == 'C' and read[i] == 'C':
		trueC +=1
	elif ref[i] == 'C' and read[i] == 'A':
		CtoA +=1
	elif ref[i] == 'C' and read[i] == 'T':
		CtoT +=1
	elif ref[i] == 'C' and read[i] == 'G':
		CtoG +=1
	elif ref[i] == 'C' and read[i] == '-':
		Cdel +=1
	elif ref[i] == '-' and read[i] == 'C':
		Cinsert +=1
	elif ref[i] == 'T' and read[i] == 'T':
		trueT +=1
	elif ref[i] == 'T' and read[i] == 'A':
		TtoA +=1
	elif ref[i] == 'T' and read[i] == 'C':
		TtoC +=1
	elif ref[i] == 'T' and read[i] == 'G':
		TtoG +=1
	elif ref[i] == 'T' and read[i] == '-':
		Tdel +=1
	elif ref[i] == '-' and read[i] == 'T':
		Tinsert +=1
	elif ref[i] == 'G' and read[i] == 'G':
		trueG +=1
	elif ref[i] == 'G' and read[i] == 'A':
		GtoA +=1
	elif ref[i] == 'G' and read[i] == 'C':
		GtoC +=1
	elif ref[i] == 'G' and read[i] == 'T':
		GtoT +=1
	elif ref[i] == 'G' and read[i] == '-':
		Gdel +=1
	elif ref[i] == '-' and read[i] == 'G':
		Ginsert +=1
	else:
		noClass +=1

# print trueA
# print AtoC
# print AtoT
# print AtoG
# print trueC
# print CtoA
# print CtoT
# print CtoG
# print trueT
# print TtoA
# print TtoC
# print TtoG
# print trueG
# print GtoA
# print GtoC
# print GtoT
# print insert
# print delete
# print noClass

total = trueA + AtoC + AtoT + AtoG + Ainsert + Adel + trueC + CtoA + CtoT + CtoG + Cinsert + Cdel + trueT + TtoA + TtoC + TtoG + Tinsert + Tdel + trueG + GtoA + GtoT + GtoC + Ginsert + Gdel
print total

# Making table

from tabulate import tabulate
print tabulate([['A', trueA, AtoC, AtoG, AtoT, Adel], ['C', CtoA, trueC, CtoG, CtoT, Cdel], ['G', GtoA, GtoC, trueG, GtoT, Gdel], ['T', TtoA, TtoC, TtoG, trueT, Tdel], ['Insertion', Ainsert, Cinsert, Ginsert, Tinsert, '-']], headers=['Reference', 'A', 'C', 'G', 'T', 'Deletion'])






