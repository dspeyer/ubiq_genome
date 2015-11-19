#!/usr/bin/python
import sys
import os
from collections import defaultdict
import matplotlib.pyplot as plot
import warnings


warnings.simplefilter("ignore")


def rr(readtype, path, failorpass, histname):
	os.system("poretools fastq --type "+readtype+" "+path+"downloads/"+failorpass+"/ >histfileanalyzer.txt")
	data = open('histfileanalyzer.txt').readlines()
	prev=False
	ct=0
	analyzer=defaultdict(lambda:0)
	for line in data:
		if prev:
			line=line.strip()
			prev = False
			analyzer[ct]=len(line)
			ct+=1
		else:
			if "fast5" in line:
				prev = True
	os.remove('histfileanalyzer.txt')

	plot.clf()
	plot.hist(analyzer.values(), bins=20)
	plot.xlabel('Read Length')
	plot.ylabel('Number of Reads')
        plot.title('%s %s' % (readtype, failorpass))
	plot.savefig(''+histname+'.png',format='png')


path=sys.argv[1]

rr("2D", path, "fail", "2Dfailures")
print '2D failure histogram generated'
rr("2D", path, "pass", "2Dpasses")
print '2D pass histogram generated'
