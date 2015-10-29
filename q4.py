#!/usr/bin/python
import sys
import os
import matplotlib.pyplot as plot
import warnings

warnings.simplefilter("ignore")


path=sys.argv[1]

os.system("poretools yield_plot --plot-type basepairs --saveas cumnucpassgenques.png --savedf passdf.txt '"+path+"downloads/pass/' &>/dev/null")

times=[]
cumu=[]
qh=-1
hh=-1
reads = file('passdf.txt')
for line in reads:
    words=line.split('\t')
    if len(words)!=4:
        continue
    times.append(float(words[2]))
    cumu.append(float(words[3]))
    if qh==-1 and times[-1]>0.25:
        qh=len(times)
    if hh==-1 and times[-1]>0.5:
        hh=len(times)

plot.clf()
plot.scatter(times[0:qh], cumu[0:qh])
plot.xlabel('Time (hours)')
plot.ylabel('Base Pairs (cumulative)')
plot.axis([0,.25,0,cumu[qh]])
plot.savefig('q4qh.eps',format='eps')

plot.clf()
plot.scatter(times[0:hh], cumu[0:hh])
plot.xlabel('Time (hours)')
plot.ylabel('Base Pairs (cumulative)')
plot.axis([0,.5,0,cumu[hh]])
plot.savefig('q4hh.eps',format='eps')

rate=cumu[qh]/times[qh]
total=3e9/rate

os.remove('cumnucpassgenques.png')

print "\nOver the first half hour, the rate was %.1f base pairs per second.  Therefore, to handle the 3 billion base pairs of the human genome would take %.1f hours." % (rate/3600, total)
