#!/usr/bin/python
################################################################################################
# ID complement alignments, create reversed fastq file for each
#
# COMS E6998 - Group 4 - "Team Awesome"
# Robert Piccone - rap2186
# 2015-11-20
################################################################################################

import os
import numpy as np
import sys
import glob

sampath="/Users/robertpiccone/GithubRepos/ubiq_genome/h2fq/rob-bwa-out/"

strFlag=""

samfiles=glob.glob(sampath + "*.sam")

for filename in samfiles:
	file = open(filename, 'r')
	linenum=0
	for line in file:
		linenum+=1
		if linenum==95:
			if (line.split("\t")[1]=='16'):
				fqname=filename.replace("/Users/robertpiccone/GithubRepos/ubiq_genome/h2fq/rob-bwa-out/","/Users/robertpiccone/GithubRepos/ubiq_genome/h2fq/h2fq-comp-rev/rev_").replace(".sam",".fastq")
				revfq=open(fqname,"w")
				revfq.write("@" + fqname + "\n")
				revfq.write(line.split("\t")[9][::-1] + "\n")
				revfq.write("+" + "\n")
				revfq.write(line.split("\t")[10][::-1] + "\n")
				revfq.close
				
