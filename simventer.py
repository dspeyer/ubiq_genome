#!/usr/bin/python

from random import random
from updateonsnp import error_rate
from collections import defaultdict 

homo=set()
het=set()

fn='/home/awesome/Venterdata.txt'
person=fn.split('/')[-1].split('.')[0].replace('data','')
for line in file(fn):
    if line[0]=='#':
        continue
    [snp, ch, pos, val] = line.rstrip().split('\t')
    if val[0]==val[1]:
        homo.add(snp)
    else:
        het.add(snp)

homolist=[]
heterolist=[]

for line in file('snplist'):
    [ch, pos, snp, val, prob, qual, f] = line.split('\t')
    prob=float(prob)
    if prob==0:
        continue
    if snp in homo:
        homolist.append(prob)
    if snp in het:
        heterolist.append(prob)

cnt=defaultdict(lambda:0)

for run in range(100000):
    hitcnt=0
    for p in homolist:
        hit = random()<p
        if random()<error_rate:
            hit = not hit
        if hit:
            hitcnt+=1
    cnt[hitcnt] += 1

for k in range(len(homolist)):
    print '%d,%d'%(k,cnt[k])

cnt=defaultdict(lambda:0)

for run in range(100000):
    hitcnt=0
    for p in heterolist:
        isthis = random()<p
        if random()<error_rate:
            isthis = not isthis
        iscommon = (isthis == (p>.5))
        if iscommon:
            hitcnt+=1
    cnt[hitcnt] += 1

for k in range(len(heterolist)):
    print '%d,%d'%(k,cnt[k])

