import sys
from pullfromdir import pullfile
from withspec import pullspec
from getbests import finder
from genusratio import grat
from bigratio import brat
from pieplotter import lilmaker
from pieplotter import bigmaker
from operator import itemgetter

path=sys.argv[1]

pullfile(path)
print "Got files ran through NCBI"
pullspec(path)
print "Got files with at least one match"
specdict,ndict=finder(path)
print "Got dictionary of top species"
specdict, total=grat(specdict,ndict)
print "Got genus ratios"
overalldict=brat(specdict)
print "Got overall ratios"

print"\n\nRatios by genus"
for key, value in sorted(specdict.items(), key=itemgetter(1), reverse=True):
    print key,str(value)

print"\n\nRatios in overall form"
for key, value in sorted(overalldict.items(), key=itemgetter(1), reverse=True):
    print key,str(value)

lilmaker(specdict)
bigmaker(overalldict)
