#!/usr/bin/python
################################################################################################
# calc. mismatches between fa/fq query/ref pairs on poshitlist
#
# COMS E6998 - Group 4 - "Team Awesome"
# Robert Piccone - rap2186
# 2015-12-3
################################################################################################

import os
import numpy as np
import sys
import glob

path='/Users/robertpiccone/GithubRepos/ubiq_genome/h2fq/rob-bwa-out/'
filelist = open(path + 'poshitlist', 'r')
matches=0
mismatches=0
for line in filelist:
	fa_file=open(path + line.strip() + ".ref.fa","r")
	fq_file=open(path + line.strip() + ".query.fq","r")
	linenum=0
	for fa_line in fa_file:
		linenum+=1
		if linenum==2:
			fa_seq=fa_line.strip().upper()
	linenum=0
	for fq_line in fq_file:
		linenum+=1
		if linenum==2:
			fq_seq=fq_line.strip().upper()
	for i in range(len(fq_seq)):
		if fq_seq[i]==fa_seq[i]:
			matches+=1
		else:
			mismatches+=1
print "Matches: %s" % matches
print "Mismatches: %s" % mismatches
print "Pct mismatched:"
print float(mismatches)/float(matches+mismatches)
