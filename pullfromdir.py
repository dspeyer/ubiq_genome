import os
import shutil
import sys
from glob import glob

def pullfile(path):

    try:
        os.mkdir('fullist/')
    except:
        shutil.rmtree('fullist/')
        os.mkdir('fullist/')

    for directory, subdirectories, files in os.walk(path):
	    for fn in files:
	        if not fn.endswith('.txt'):
			try:
    	 	            shutil.copy2(directory+'/'+fn, 'fullist/'+fn)
			except:
			    pass

