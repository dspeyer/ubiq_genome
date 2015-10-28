################################################################################################
# Extract Quality Scores from FastQ files,
# calculate mean, std dev, t-test comparisons
#
# COMS E6998 - Group 4 - "Team Awesome"
# Robert Piccone - rap2186
# 2015-10-28
#
# FastQ files created with following poretools command lines run within pass/fail subdirectories:
# poretools fastq --type 2D *.fast5 > pass2D_fastq.txt
# poretools fastq --type 2D *.fast5 > fail2D_fastq.txt
################################################################################################

from scipy import stats as sp
import numpy as np

def get_quality_sores(path,filename):
	file = open(path + filename, 'r')
	line_num=0
	score_list=[]
	for line in file:
		line_num+=1
		if (line_num%4==0):
			for i in range(len(line)):
				if (line[i].strip()!=""):
					#print line[i]
					#score_array=np.append(score_array, ord(line[i])-33)
					score_list.append(ord(line[i])-33)
	#print score_list
	score_array=np.array(score_list,dtype='int16')
	return score_array
				
path='/Users/robertpiccone/Documents/Courses/COMS E6998/alldata/downloads/fail/'
fail2D_scores=get_quality_sores(path,'fail2D_fastq.txt')
path='/Users/robertpiccone/Documents/Courses/COMS E6998/alldata/downloads/pass/'
pass2D_scores=get_quality_sores(path,'pass2D_fastq.txt')

print "Passed 2D Reads"
print "Mean:%s  Std. Dev.:%s" %(np.mean(pass2D_scores),np.std(pass2D_scores))
print
print "Failed 2D Reads"
print "Mean:%s  Std. Dev.:%s" %(np.mean(fail2D_scores),np.std(fail2D_scores))
print
print "T-test comparison:" 
print sp.stats.ttest_ind(pass2D_scores,fail2D_scores)
