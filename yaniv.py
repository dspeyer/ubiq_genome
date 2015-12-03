#!/usr/bin/python

from scipy.stats import binom
from collections import defaultdict
from updateonsnp import update

yaniv={}
#fn='../Yaniv_Erlich_Genome.txt'
fn='/home/awesome/Venterdata.txt'
for line in file(fn):
    if line[0]=='#':
        continue
    [snp, ch, pos, val] = line.rstrip().split('\t')
    yaniv[snp]=val

hits=0
heterohits=0
sexhits=0
misses=0
no23me=0

heterorare=0
heterocommon=0

p = [0.2, 0.2, 0.2]
notes= [defaultdict(lambda:0), defaultdict(lambda:0), defaultdict(lambda:0)]

errprob=0.1

for line in file('snplist'):
    [ch, pos, snp, val, prob, qual, f] = line.split('\t')
    prob=float(prob)
    qual=float(qual)
    if prob==0:
        continue
    if snp not in yaniv:
        no23me += 1
        continue
    if len(yaniv[snp])==1 or yaniv[snp][0]==yaniv[snp][1]:
        to_update=[0,2]
    else:
        to_update=[1,2]
    for i in to_update:
        p[i] = update(val, yaniv[snp], p[i], prob, notes[i], i==0, error_rate=.05)

print 'homozyg hits=%d, heterozyg hits=%d, sex chromosome hits=%d, homo misses=%d hetero misses=%d' % (notes[2]['homohit'], notes[2]['heterohit'], notes[2]['sexhits'], notes[2]['homomiss'], notes[2]['heteromiss'])
heterocommon=notes[2]['hetcom']
heterorare=notes[2]['hetrare']
print 'hetero common=%d, hetero rare=%d,  p=%.4f' % (heterocommon, heterorare, binom.cdf(min(heterocommon, heterorare), heterocommon+heterorare, 0.5))
print 'Skipping hetero:   p(Yaniv)=%.2f%%' % (100*(p[0]))
print 'Using only hetero: p(Yaniv)=%.2f%%' % (100*(p[1]))
print 'Using everything:  p(Yaniv)=%.2f%%' % (100*(p[2]))
