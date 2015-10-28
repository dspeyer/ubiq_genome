#!/usr/bin/python
import sys
import os


path=sys.argv[1]

print "Plotting cumulative nucleotides sequenced as a function of time for 'failed' reads"
os.system("poretools yield_plot --plot-type basepairs --saveas cumnucfail.png '"+path+"downloads/fail/has2d' &>/dev/null")

print "Plotting cumulative nucleotides sequenced as a function of time for 'passed' reads"
os.system("poretools yield_plot --plot-type basepairs --saveas cumnucpass.png '"+path+"downloads/pass/has2d' &>/dev/null")
