#!/usr/bin/python
import sys
import os

path=sys.argv[1]

tempfilename=""
templen=0
compfilename=""
complen=0
twodfilename=""
twodlen=0
os.system("poretools winner --type fwd "+path+"downloads/pass/ >tempwinner.txt")
data = open('tempwinner.txt').readlines()
for line in data:
	if "fast5" in line:
		tempfilename=line.split("strand_template ",1)[1]
	else:
		templen=len(line)
os.remove('tempwinner.txt')

os.system("poretools winner --type rev "+path+"downloads/pass/ >tempwinner.txt")
data = open('tempwinner.txt').readlines()
for line in data:
	if "fast5" in line:
		compfilename=line.split("strand_complement ",1)[1]
	else:
		complen=len(line)
os.remove('tempwinner.txt')

os.system("poretools winner --type 2D "+path+"downloads/pass/ >tempwinner.txt")
data = open('tempwinner.txt').readlines()
for line in data:
	if "fast5" in line:
		twodfilename=line.split("strand_twodirections ",1)[1]
	else:
		twodlen=len(line)
os.remove('tempwinner.txt')

print "\nLONGEST TEMPLATE READ"
print "From file: "+tempfilename.strip()
print "Number of nucleotides: "+str(templen)

print "\nLONGEST COMPLEMENT READ"
print "From file: "+compfilename.strip()
print "Number of nucleotides: "+str(complen)

print "\nLONGEST 2D READ"
print "From file: "+twodfilename.strip()
print "Number of nucleotides: "+str(twodlen)
