import shutil
import os
from getbests import finder
from genusratio import grat
from bigratio import brat
from operator import itemgetter
import matplotlib.pyplot as plt
import warnings


warnings.simplefilter("ignore")


par=[]
veg=[]
meat=[]
for i in range(1,1749):
    path=str(i)+'min/'
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

    specdict,ndict=finder('hasspec/')
    specdict, total=grat(specdict,ndict)
    overalldict=brat(specdict)

    if "Vegetables" not in overalldict:
	veg.append(0.0)
    else:
	veg.append(overalldict["Vegetables"])
    if "Meat" not in overalldict:
	meat.append(0.0)
    else:
	meat.append(overalldict["Meat"])
    if "Parasites" not in overalldict:
	par.append(0.0)
    else:
	par.append(overalldict["Parasites"])
    print i

xax=[]
for num in range(1,1749):
    xax.append(num)

fig, ax = plt.subplots()
ax.plot(xax, meat, 'r--', label='Meat')
ax.plot(xax, par, 'b--', label='Parasites')
ax.plot(xax, veg, 'g--', label='Vegetables')
plt.title('Ratio of ingredients found over time')

# Found this on some tutorial site -- pretty cool
legend = ax.legend(loc='upper center', shadow=True)
frame = legend.get_frame()
frame.set_facecolor('0.90')
for label in legend.get_texts():
    label.set_fontsize('large')
for label in legend.get_lines():
    label.set_linewidth(1.5)

plt.savefig('ratioovertime.png')

