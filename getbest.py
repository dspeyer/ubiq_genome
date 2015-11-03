import os
import sys
from operator import itemgetter

path = sys.argv[1]

def num_there(s):
    return any(i.isdigit() for i in s)

def best(path):
    try:
    	os.mkdir(path+'/hasspec')
    except:
        pass

    for directory, subdirectories, files in os.walk(path):
        for file in files:
	    num_lines=0
	    f = open(path+file)
     	    for line in f:
		num_lines+=1
	    if num_lines>1:
		try:
		    os.symlink('../'+file, path+'/hasspec/'+file)
		except:
		    pass


    genera=[]
    for directory, subdirectories, files in os.walk(path+'/hasspec'):
        for file in files:
	    f = open(path+file)
	    spec=""
	    itr=1
	    for line in f:
		if itr==1:
		    itr+=1
		else:
		    spec=line.split()
		    if not num_there(spec[1]) and spec[0]!="PREDICTED" and spec[0]!="PREDICTED:":
		        spec=""
			genera.append(line)
			break
		    else:
			spec=""
		    itr+=1
    return genera
