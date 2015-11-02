import os
import sys

path = sys.argv[1]

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



for directory, subdirectories, files in os.walk(path+'/hasspec'):
    for file in files:
	f = open(path+file)
	spec=""
	itr=1
	for line in f:
		if itr==2:
			spec=line
			itr+=1
		else:
			itr+=1
	spec=spec.split()
	genus=""
	whole=""
	if spec[0] == "PREDICTED:":
		genus=spec[1]
		whole=spec[1]+" "+spec[2]
	else:
		genus=spec[0]
		whole=spec[0]+" "+spec[1]
	b = open('bacGenera.txt')
	for line in b:
		if genus.strip()==line.strip():
			print "Bacteria found: "+whole
	f.close()
		
