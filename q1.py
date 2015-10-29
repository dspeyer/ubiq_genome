#!/usr/bin/python
import sys
import os

def rr(runtype, path, passfail, typ, fp):
	os.system("poretools fastq --type "+runtype+" "+path+"downloads/"+passfail+"/ >tempholderfastqfile.txt")
	data = open('tempholderfastqfile.txt').read()
	allcount = data.count('.fast5')
	print "Number of "+typ+" reads classified as "+fp+": "+str(allcount)
	os.remove('tempholderfastqfile.txt')
	return allcount

path=sys.argv[1]

allfailcount=rr("all", path, "fail", "1D and 2D", "failed")
allpasscount=rr("all", path, "pass", "1D and 2D", "passed")
twodfailcount=rr("2D", path, "fail", "2D", "failed")
twodpasscount=rr("2D", path, "pass", "2D", "passed")

fractwodpass=float(twodpasscount)/float(allpasscount)
fractwodfail=float(twodfailcount)/float(allfailcount)

print "Fraction of 2D reads in failed folder: "+str(fractwodfail)
print "Fraction of 2D reads in passed folder: "+str(fractwodpass)
