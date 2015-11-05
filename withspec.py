import os
import shutil
import sys
from glob import glob

def pullspec(path):
    path='fullist/'
    try:
        os.mkdir('hasspec/')
    except:
        shutil.rmtree('hasspec/')
        os.mkdir('hasspec/')

    for directory, subdirectories, files in os.walk(path):
	    for fn in files:
		k=open(path+fn)
	   	ct=0
		for line in k:
                    ct+=1
		if ct>1:
		    try:
		 	    shutil.copy2(directory+'/'+fn, 'hasspec/'+fn)
		    except:
			    pass
