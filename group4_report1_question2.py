#!/usr/bin/python

import sys
from glob import glob
from collections import defaultdict
import matplotlib.pyplot as plot
import warnings

warnings.simplefilter("ignore")

dir=sys.argv[1]

cnt=defaultdict(lambda:0)

for i in glob(dir+'/pass/*.fast5')+glob(dir+'/fail/*.fast5'):
    fn=i.split('/')[-1]
    pieces=fn.split('_')
    ch=pieces[-3][2:]
    cnt[ch]+=1


total=0
nch=0
max=-1
argmax=-1
for i in cnt:
    nch+=1
    total+=cnt[i]
    if cnt[i]>max:
        max=cnt[i]
        argmax=i

print "%d channels had at least one read, and %d had at least five.  " % (nch, sum([x>=5 for x in cnt.values()]))
print "This compares with 412 ``active'' channels during initialization, and 618 immediately after loading fuel\n"
print "The average channel had %.1f reads. " % (float(total)/nch)
print "Channel %s had %d reads, which was the most." % (argmax, max)

plot.clf()
plot.hist(cnt.values(), bins=20)
plot.xlabel('Reads per Channel')
plot.ylabel('Channels with that many Reads')
plot.savefig('part2hist.eps',format='eps')

print "\nJust for fun, here's a histogram of reads per channel\\\\"
