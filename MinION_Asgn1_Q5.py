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
#
# poretools times *.fast5 > passtimes.tsv
################################################################################################

from scipy import stats as sp
import numpy as np

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
				
path='/Users/robertpiccone/Documents/Courses/COMS E6998/alldata/downloads/fail/'
fail2D_scores=get_quality_scores(path,'fail2D_fastq.txt')
path='/Users/robertpiccone/Documents/Courses/COMS E6998/alldata/downloads/pass/'
pass2D_scores=get_quality_scores(path,'pass2D_fastq.txt')

print "Passed 2D Reads"
print "Mean Quality Score:%g  Std. Dev.:%g n:%s" %(np.mean(pass2D_scores),np.std(pass2D_scores),np.size(pass2D_scores))
print
print "Failed 2D Reads"
print "Mean Quality Score:%g  Std. Dev.:%g n:%s" %(np.mean(fail2D_scores),np.std(fail2D_scores),np.size(fail2D_scores))
print
print "T-test comparison:" 
print "T-Statistic:%g" % sp.stats.ttest_ind(pass2D_scores,fail2D_scores)[0]
print "P-Value:%g" % sp.stats.ttest_ind(pass2D_scores,fail2D_scores)[1]
print
startendtimes=np.loadtxt(path + 'passtimes.tsv', delimiter="\t",usecols=(4,6),dtype='int32',skiprows=1)
starttime=np.amin(startendtimes[:,0])
endtime=np.amax(startendtimes[:,1])
firsthour_ind= np.where(startendtimes[:,1]<=(starttime+3600))
lasthour_ind= np.where(startendtimes[:,1]>=(endtime-3600))
fast5names=np.loadtxt(path + 'passtimes.tsv', delimiter="\t",usecols=(1,),dtype='str',skiprows=1)
firsthour_scores=get_quality_scores(path,'pass2D_fastq.txt',fast5names[firsthour_ind])
lasthour_scores=get_quality_scores(path,'pass2D_fastq.txt',fast5names[lasthour_ind])

print "Passed 2D Reads - First Hour"
print "Mean Quality Score:%g  Std. Dev.:%g n:%s" %(np.mean(firsthour_scores),np.std(firsthour_scores),np.size(firsthour_scores))
print "Median:%g" % (np.median(firsthour_scores))
print
print "Passed 2D Reads - Last Hour"
print "Mean Quality Score:%g  Std. Dev.:%g n:%s" %(np.mean(lasthour_scores),np.std(lasthour_scores),np.size(lasthour_scores))
print "Median:%g" % (np.median(lasthour_scores))