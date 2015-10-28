#!/usr/bin/python
import sys
import os

path=sys.argv[1]

os.system("poretools fastq --type all "+path+"downloads/fail/ >tempholderfastqfile.txt")
data = open('tempholderfastqfile.txt').read()
allfailcount = data.count('.fast5')
print "Number of 1D and 2D reads classified as failed: "+str(allfailcount)
os.remove('tempholderfastqfile.txt')

os.system("poretools fastq --type all "+path+"downloads/pass/ >tempholderfastqfile.txt")
data = open('tempholderfastqfile.txt').read()
allpasscount = data.count('.fast5')
print "Number of 1D and 2D reads classified as passed: "+str(allpasscount)
os.remove('tempholderfastqfile.txt')

os.system("poretools fastq --type 2D "+path+"downloads/fail/ >tempholderfastqfile.txt")
data = open('tempholderfastqfile.txt').read()
twodfailcount = data.count('.fast5')
os.remove('tempholderfastqfile.txt')

os.system("poretools fastq --type 2D "+path+"downloads/pass/ >tempholderfastqfile.txt")
data = open('tempholderfastqfile.txt').read()
twodpasscount = data.count('.fast5')
os.remove('tempholderfastqfile.txt')

fractwodpass=float(twodpasscount)/float(allpasscount)
fractwodfail=float(twodfailcount)/float(allfailcount)

print "Fraction of 2D reads in passed folder: "+str(fractwodpass)
print "Fraction of 2D reads in failed folder: "+str(fractwodfail)
