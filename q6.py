import sys
import os

path=sys.argv[1]

print "Creating 1D & 2D failure histogram"
os.system("poretools hist "+path+"downloads/fail/")
print "Creating 1D & 2D pass histogram"
os.system("poretools hist "+path+"downloads/pass/")
