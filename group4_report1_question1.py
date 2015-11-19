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

twodfailcount=rr("2D", path, "fail", "2D", "failed")
twodpasscount=rr("2D", path, "pass", "2D", "passed")
