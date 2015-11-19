#!/usr/bin/python
import sys
import os

def rr(datatype, path, strand, fold):
	filename=""
	leng=0
	os.system("poretools winner --type "+datatype+" "+path+"downloads/"+fold+"/ >tempwinner.txt")
	data = open('tempwinner.txt').readlines()
	for line in data:
		if "fast5" in line:
			filename=line.split(strand,1)[1]
		else:
			leng=len(line)
	os.remove('tempwinner.txt')
	return filename, leng

path=sys.argv[1]

filename=""
leng=0
filename, leng = rr("2D", path, "strand_twodirections ","pass")
filename=os.path.basename(os.path.normpath(filename))
print "\nLONGEST PASSED 2D READ"
print "From file: "+filename.strip()
print "Number of nucleotides: "+str(leng)

filename=""
leng=0
filename, leng = rr("2D", path, "strand_twodirections ","fail")
filename=os.path.basename(os.path.normpath(filename))
print "\nLONGEST FAILED 2D READ"
print "From file: "+filename.strip()
print "Number of nucleotides: "+str(leng)
