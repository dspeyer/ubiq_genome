#!/usr/bin/python
import sys
import os

path=sys.argv[1]

# how to get only 2D reads??

# Nucleotide composition of passed reads
print "Computing nucleotide composition of passed reads..."
os.system("poretools nucdist '"+path+"downloads/fail/has2d' >tempcomposition.txt")
data = open('tempcomposition.txt').readlines()
print "Failed reads %Composition"
for line in data:
    base = line.split()
    percent = 100 * float(base[3])
    print "% "+str(base[0])+": "+str(percent)
os.remove('tempcomposition.txt')

# Nucleotide composition of failed reads
print "Computing nucleotide composition of failed reads..."
os.system("poretools nucdist '"+path+"downloads/pass/' >tempcomposition.txt")
data = open('tempcomposition.txt').readlines()
print "Passed reads %Composition"
for line in data:
    base = line.split()
    percent = 100 * float(base[3])
    print "% "+str(base[0])+": "+str(percent)
os.remove('tempcomposition.txt')
