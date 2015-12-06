#!/usr/bin/python
################################################################################################
# Read/Report Quality Scores across sam filess
#
# COMS E6998 - Group 4 - "Team Awesome"
# Robert Piccone - rap2186
# 2015-12-3
################################################################################################

import os
import numpy as np
import sys
import glob
	
sampath="/Users/robertpiccone/GithubRepos/ubiq_genome/h2fq/rob-bwa-out/"

strFlag=""

samfiles=glob.glob(sampath + "*.sam")
score_list=[]
for filename in samfiles:
	file = open(filename, 'r')
	linenum=0
	for line in file:
		linenum+=1
		if linenum>=95:
			if (line.split("\t")[1]!='4'):
				phredline= line.split("\t")[10]
				for i in range(len(phredline)):
					score_list.append(ord(phredline[i])-33)
score_array=np.array(score_list,dtype='int16')
print "Mean Quality Score=%g\\\\  Std. Dev.=%g\\\\ n=%s\\\\" %(np.mean(score_array),np.std(score_array),np.size(score_array))
print "Median=%g" % (np.median(score_array))
				