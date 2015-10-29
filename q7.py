#!/usr/bin/python
import sys
import os

def rr(datatype, path, strand):
	filename=""
	leng=0
	os.system("poretools winner --type "+datatype+" "+path+"downloads/pass/ >tempwinner.txt")
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

filename, leng = rr("fwd", path, "strand_template ")
filename=os.path.basename(os.path.normpath(filename))
print "\nLONGEST TEMPLATE READ"
print "From file: "+filename.strip()
print "Number of nucleotides: "+str(leng)

filename, leng = rr("rev", path, "strand_complement ")
filename=os.path.basename(os.path.normpath(filename))
print "\nLONGEST COMPLEMENT READ"
print "From file: "+filename.strip()
print "Number of nucleotides: "+str(leng)

filename, leng = rr("2D", path, "strand_twodirections ")
filename=os.path.basename(os.path.normpath(filename))
print "\nLONGEST 2D READ"
print "From file: "+filename.strip()
print "Number of nucleotides: "+str(leng)

