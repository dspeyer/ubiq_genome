#!/usr/bin/python
################################################################################################
# group4_report2_question6.py [path to .sam files]
# Scan .sam files to get count of alignment successes
#
# COMS E6998 - Group 4 - "Team Awesome"
# Robert Piccone - rap2186
# 2015-11-19
################################################################################################

import os
import numpy as np
import sys

if len(sys.argv)==1:
	sampath="/Users/robertpiccone/GithubRepos/ubiq_genome/h2fq/rob-bwa-out/"
else:
	sampath=sys.argv[1]

strFlag=""

samfiles=os.listdir(sampath)

for filename in samfiles:
	file = open(sampath + filename, 'r')
	linenum=0
	for line in file:
		linenum+=1
		if linenum==95:
			strFlag+=line.split("\t")[1] +";"
flags=np.array(strFlag[:-1].split(";"))
flags=flags.astype(int)
read_counts=np.unique(flags, return_counts=True)

print "Total # of aligned reads: %i" % sum(read_counts[1][np.where(read_counts[0]!=4)])
print "Total # of unaligned reads: %i" % read_counts[1][np.where(read_counts[0]==4)]
print
print "Total # of reads: %i" % sum(read_counts[1])

'''
Output generated:
Total # of aligned reads: 851
Total # of unaligned reads: 231

Total # of reads: 1082

'''