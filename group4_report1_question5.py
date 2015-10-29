#!/usr/bin/python
################################################################################################
# group4_report1_question5.py
# Extract Quality Scores from FastQ files,
# calculate mean, std dev, t-test comparisons
#
# COMS E6998 - Group 4 - "Team Awesome"
# Robert Piccone - rap2186
# 2015-10-28
#
# FastQ files generated and used by code created with following poretools command lines run within pass/fail subdirectories:
# poretools fastq --type 2D *.fast5 > pass2D_fastq.txt
# poretools fastq --type 2D *.fast5 > fail2D_fastq.txt
# poretools times *.fast5 > passtimes.tsv
# (above FastQ files all uploaded to github repo)
################################################################################################

from scipy import stats as sp
import numpy as np
import os
import sys

def get_quality_scores(path,filename,pick_files=False):
	if (pick_files==False):
		include_score=True
	file = open(path + filename, 'r')
	line_num=0
	score_list=[]
	for line in file:
		line_num+=1
		if ((line_num+3)%4==0 and pick_files!=False):
			if (line.split(":",1)[1].strip() in pick_files):
				include_score=True
			else:
				include_score=False
		if (line_num%4==0 and include_score==True):
			for i in range(len(line)):
				if (line[i].strip()!=""):
					score_list.append(ord(line[i])-33)
	score_array=np.array(score_list,dtype='int16')
	return score_array

if len(sys.argv)==1:
	path='/Users/robertpiccone/Documents/Courses/COMS_E6998/GroupReadWrite/alldata/'
else:
	path=sys.argv[1]
os.chdir(path)
strCall='poretools fastq --type 2D ./downloads/fail/*.fast5 > fail2D_fastq.txt'
os.system(strCall)
fail2D_scores=get_quality_scores(path,'fail2D_fastq.txt')
strCall='poretools fastq --type 2D ./downloads/pass/*.fast5 > pass2D_fastq.txt'
os.system(strCall)
pass2D_scores=get_quality_scores(path,'pass2D_fastq.txt')

print "\\subsection*{Passed 2D Reads}"
print "Mean Quality Score=%g\\\\  Std. Dev.=%g\\\\ n=%s\\\\" %(np.mean(pass2D_scores),np.std(pass2D_scores),np.size(pass2D_scores))
print
print "\\subsection*{Failed 2D Reads}"
print "Mean Quality Score=%g\\\\  Std. Dev.=%g\\\\ n=%s\\\\" %(np.mean(fail2D_scores),np.std(fail2D_scores),np.size(fail2D_scores))
print
print "\\subsection*{T-test comparison}" 
print "T-Statistic=%g\\\\" % sp.stats.ttest_ind(pass2D_scores,fail2D_scores)[0]
print "P-Value=%g\n" % sp.stats.ttest_ind(pass2D_scores,fail2D_scores)[1]
print
#printing commentary/discussion of results in next 2 lines
print "The P-value was confirmed to be returned as 0 from Python/numpy."
print "We believe that the true value is above 0 but beneath the lowest threshold of Python's float value (2.2250738585072014e-308)."
print
strCall='poretools times ./downloads/pass/*.fast5 > passtimes.tsv'
os.system(strCall)
startendtimes=np.loadtxt(path + 'passtimes.tsv', delimiter="\t",usecols=(4,6),dtype='int32',skiprows=1)
starttime=np.amin(startendtimes[:,0])
endtime=np.amax(startendtimes[:,1])
firsthour_ind= np.where(startendtimes[:,1]<=(starttime+3600))
lasthour_ind= np.where(startendtimes[:,1]>=(endtime-3600))
fast5names=np.loadtxt(path + 'passtimes.tsv', delimiter="\t",usecols=(1,),dtype='str',skiprows=1)
firsthour_scores=get_quality_scores(path,'pass2D_fastq.txt',fast5names[firsthour_ind])
lasthour_scores=get_quality_scores(path,'pass2D_fastq.txt',fast5names[lasthour_ind])

print "\\subsection*{Passed 2D Reads - First Hour}"
print "Mean Quality Score=%g\\\\  Std. Dev.=%g\\\\ n=%s\\\\" %(np.mean(firsthour_scores),np.std(firsthour_scores),np.size(firsthour_scores))
print "Median=%g" % (np.median(firsthour_scores))
print
print "\\subsection*{Passed 2D Reads - Last Hour}"
print "Mean Quality Score=%g\\\\  Std. Dev.=%g\\\\ n=%s\\\\" %(np.mean(lasthour_scores),np.std(lasthour_scores),np.size(lasthour_scores))
print "Median=%g" % (np.median(lasthour_scores))
print
#printing commentary/discussion of results in next 2 lines
print "The quality of the reads does not appear to have degraded over the timespan of the sequencing"
print "(on the contrary, there is a slight increase)."

##################################################
#
# OUTPUT OF ABOVE CODE, with commentary/discusson:
#
# Passed 2D Reads
# Mean Quality Score:10.3775  Std. Dev.:1.83151 n:2764522
#
# Failed 2D Reads
# Mean Quality Score:9.48623  Std. Dev.:2.06174 n:1417759
#
# T-test comparison:
# T-Statistic:451.124
# P-Value:0
# 
# The P-value was confirmed to be returned as 0 from Python/numpy. 
# We believe in actuality that the true value was beneath the lowest threshold of Python's float value (2.2250738585072014e-308).
# 
# Passed 2D Reads - First Hour
# Mean Quality Score:10.3668  Std. Dev.:1.82208 n:1970130
# Median:10
# 
# Passed 2D Reads - Last Hour
# Mean Quality Score:11.5651  Std. Dev.:2.12032 n:968
# Median:11
# 
# The quality of the reads does not appear to have degraded over the timespan of the sequencing 
# (on the contrary, there is a slight increase).
# 
#####################################################
