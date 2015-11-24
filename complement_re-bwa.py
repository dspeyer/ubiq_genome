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
				#fqname=filename.replace("/Users/robertpiccone/GithubRepos/ubiq_genome/h2fq/rob-bwa-out/","/Users/robertpiccone/GithubRepos/ubiq_genome/h2fq/h2fq-comp-rev/rev_").replace(".sam",".fastq")
				fqname=filename.replace("/Users/robertpiccone/GithubRepos/ubiq_genome/h2fq/rob-bwa-out/","/Users/robertpiccone/GithubRepos/ubiq_genome/h2fq/").replace(".sam",".fastq")
				try:
					orig_fq=open(fqname,"r")
				except:
					print fqname + " not found"
					revname=filename.replace("/Users/robertpiccone/GithubRepos/ubiq_genome/h2fq/rob-bwa-out/","/Users/robertpiccone/GithubRepos/ubiq_genome/h2fq/h2fq-comp-rev/sam_rev_").replace(".sam",".fastq")
					revfq=open(revname,"w")
					revfq.write("@" + fqname + "\n")	
					revfq.write(line.split("\t")[9] + "\n")
					revfq.write("+" + "\n")
					revfq.write(line.split("\t")[10][::-1] + "\n")	
					revfq.close
					continue
				revname=filename.replace("/Users/robertpiccone/GithubRepos/ubiq_genome/h2fq/rob-bwa-out/","/Users/robertpiccone/GithubRepos/ubiq_genome/h2fq/h2fq-comp-rev/rev_").replace(".sam",".fastq")
				revfq=open(revname,"w")
				wlinenum=0
				for wline in orig_fq:
					wlinenum+=1
					if wlinenum==1:
						revfq.write(wline + "\n")
					if wlinenum==2:
						strComp=wline[::-1]
						strComp=strComp.replace("A","1").replace("T","2").replace("G","3").replace("C","4")
						strComp=strComp.replace("1","T").replace("2","A").replace("3","C").replace("4","G")
						revfq.write(strComp + "\n")
					if wlinenum==3:
						revfq.write(wline + "\n")
					if wlinenum==4:
						revfq.write(wline[::-1] + "\n")
				revfq.close
				orig_fq.close
				
