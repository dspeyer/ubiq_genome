#!/usr/bin/python
import sys
import os

path=sys.argv[1]

print "Creating 1D and 2D failure histogram"
os.system("poretools hist --saveas q6hf.png "+path+"downloads/fail/")
print "Creating 1D and 2D pass histogram"
os.system("poretools hist --saveas q6hp.png "+path+"downloads/pass/")
