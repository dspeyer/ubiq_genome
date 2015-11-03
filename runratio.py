import sys
import os
from getbest import best
from gettop3 import top3
from getall import _all
from operator import itemgetter

path=sys.argv[1]
type=sys.argv[2]
grouping=sys.argv[3]

genera=[]
if type=="best":
	genera=best(path)

elif type=="top3":
	genera=top3(path)

elif type=="all":
	genera=_all(path)

else:
	print "invalid search type"

gendict={}
foundbac=False
for species in genera:
	species=species.strip()
	spec=species.split()
	genus=""
	whole=""
	genus=spec[0]
	whole=spec[0]+" "+spec[1]
	b = open('bacGenera.txt')
	for line in b:
		if genus.strip()==line.strip():
			print "\nBacteria found: "+whole
			foundbac=True
	if grouping=="s":
	    if whole in gendict:
	        gendict[whole]+=(float(spec[2])*.01)
	    else:
		gendict[whole]=(float(spec[2])*.01)
	if grouping=="g":
	    if genus in gendict:
		gendict[genus]+=(float(spec[2])*.01)
	    else:
		gendict[genus]=(float(spec[2])*.01)
	
if not foundbac:
		print "\nNo bacteria found"
overall=0.0
for key, value in sorted(gendict.items(), key=itemgetter(1), reverse=True):
	overall+=value	


print"\nRatios"
for key, value in sorted(gendict.items(), key=itemgetter(1), reverse=True):
	print key, str(value/overall)
