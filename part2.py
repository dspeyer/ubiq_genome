#!/usr/bin/python

import sys
from glob import glob
from collections import defaultdict

dir=sys.argv[1]

cnt=defaultdict(lambda:0)

for i in glob(dir+'/pass/*.fast5')+glob(dir+'/fail/*.fast5'):
    fn=i.split('/')[-1]
    pieces=fn.split('_')
    ch=pieces[4][2:]
    cnt[ch]+=1


sum=0
nch=0
max=-1
argmax=-1
for i in cnt:
    nch+=1
    sum+=cnt[i]
    if cnt[i]>max:
        max=cnt[i]
        argmax=i

print "%d channels had at least one read. " % nch
print "The average channel had %.1f reads. " % (float(sum)/nch)
print "Channel %s had %d reads, which was the most." % (argmax, max)
