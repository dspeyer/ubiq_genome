import sys
import os

path=sys.argv[1]

print "Plotting cumulative nucleotides sequenced as a function of time for 'failed' reads"
os.system("poretools yield_plot --plot-type basepairs --saveas cumnucfail.png --savedf faildf.txt '"+path+"downloads/fail/'")

print "Plotting cumulative nucleotides sequenced as a function of time for 'passed' reads"
os.system("poretools yield_plot --plot-type basepairs --saveas cumnucpass.png --savedf passdf.txt '"+path+"downloads/pass/'")
