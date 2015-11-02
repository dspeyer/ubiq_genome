import os
import sys
from operator import itemgetter

path = sys.argv[1]


def num_there(s):
    return any(i.isdigit() for i in s)


try:
    os.mkdir(path+'/hasspec')
except:
    pass

for directory, subdirectories, files in os.walk(path):
    for file in files:
	num_lines=0
	f = open(path+file)
     	for line in f:
		num_lines+=1
	if num_lines>1:
		try:
			os.symlink('../'+file, path+'/hasspec/'+file)
		except:
			pass


gendict={}
genera=[]
for directory, subdirectories, files in os.walk(path+'/hasspec'):
    for file in files:
	f = open(path+file)
	spec=""
	itr=1
	for line in f:
		if itr==1:
			itr+=1
		else:
			spec=line.split()
			if not num_there(spec[1]):
				spec=""
				genera.append(line)
			else:
				spec=""
			itr+=1

foundbac=False
for species in genera:
	species=species.strip()
	spec=species.split()
	genus=""
	whole=""
	if spec[0] == "PREDICTED:":
		genus=spec[1]
		whole=spec[1]
	else:
		genus=spec[0]
		whole=spec[0]+" "+spec[1]
	b = open('bacGenera.txt')
	for line in b:
		if genus.strip()==line.strip():
			print "Bacteria found: "+whole
			foundbac=True
	if whole in gendict:
		gendict[whole]+=1
	else:
		gendict[whole]=1
if not foundbac:
		print "No bacteria found"
print "\nSpecies    # Occurrences"
for key, value in sorted(gendict.items(), key=itemgetter(1), reverse=True):
	print(key, value)	
