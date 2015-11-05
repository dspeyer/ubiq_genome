import sys
import os
import csv
import warnings
from operator import itemgetter
import shutil


warnings.simplefilter("ignore")

#path is link to directory for downloads folder
path=sys.argv[1]
#matches in link to hasspec directory that should have been created when infopipeline.py was run
matches=sys.argv[2]


warn=raw_input("WARNING: Running this script will make ~1700 folders. Use at your own risk! \nPress enter to continue")
os.system('poretools times '+path+'downloads/pass/ >'+path+'downloads/pass/timesPass.txt')
with open(''+path+'downloads/pass/timesPass.txt') as times_readP: 
	reader = csv.reader(times_readP, delimiter='\t') 
	timesPass = list(reader)

holder={}
master_start=8000000000000000000000000
for line in timesPass:
	if line[0]!="channel":
	    begintime=line[4]
            if int(begintime)<master_start:
	        master_start=int(begintime)

biggest=0
for line in timesPass:
	if line[0]!="channel":
	    filename=line[1]
	    filename=os.path.basename(os.path.normpath(filename))
	    begintime=line[4]
	    duration=line[5]
	    timeend=int(begintime)+int(duration)
	    val=float(timeend-master_start)/60
	    if val>biggest:
		biggest=val
	    holder[filename]=val

mins=1
while mins<=biggest:
    try:
        os.mkdir(str(mins)+'min/')
    except:
        shutil.rmtree(str(mins)+'min/')
        os.mkdir(str(mins)+'min/')
    storekeys=[]
    for key, value in sorted(holder.items(), key=itemgetter(1), reverse=False):
	    if float(value)<=float(mins):
	        key = key[:-6]
	        storekeys.append(key)

    for thing in storekeys:
	    if os.path.isfile(matches+thing+'.species'):
	        shutil.copy2(matches+thing+'.species', str(mins)+'min/'+thing+'.species')
	    elif os.path.isfile(matches+thing+'.match22'):
	        shutil.copy2(matches+thing+'.match22', str(mins)+'min/'+thing+'.match22')
    mins+=1
