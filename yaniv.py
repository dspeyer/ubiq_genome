#!/usr/bin/python

from scipy.stats import binom

yaniv={}
for line in file('../Yaniv_Erlich_Genome.txt'):
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

for line in file('snplist'):
    [ch, pos, snp, val, prob, qual, f] = line.split('\t')
    prob=float(prob)
    qual=float(qual)
    if prob==0:
        continue
    if snp not in yaniv:
        no23me += 1
        continue
    if yaniv[snp] == val*2 :
        hits += 1
        p_obs_given_yaniv = 1
    elif yaniv[snp]==val:
        sexhits += 1
        p_obs_given_yaniv = 1
    elif val in yaniv[snp]:
        heterohits += 1
        p_obs_given_yaniv = .5
        if prob>.5:
            heterocommon += 1
        else:
            heterorare += 1
    else:
        misses += 1
        p_obs_given_yaniv = 0.15 # 10**(-qual/10)
    if len(yaniv[snp])==1 or yaniv[snp][0]==yaniv[snp][1]:
        to_update=[0,2]
    else:
        to_update=[1,2]
    for i in to_update:
        p_obs = (p[i] * p_obs_given_yaniv) + ((1-p[i]) * prob)
        p[i] *= p_obs_given_yaniv / p_obs


print 'homozyg hits=%d, heterozyg hits=%d, sex chromosome hits=%d, misses=%d, not in 23&me=%d' % (hits, heterohits, sexhits, misses, no23me)
print 'hetero common=%d, hetero rare=%d,  p=%.4f' % (heterocommon, heterorare, binom.cdf(min(heterocommon, heterorare), heterocommon+heterorare, 0.5))
print 'Skipping hetero:   p(Yaniv)=%.2f%%' % (100*(p[0]))
print 'Using only hetero: p(Yaniv)=%.2f%%' % (100*(p[1]))
print 'Using everything:  p(Yaniv)=%.2f%%' % (100*(p[2]))
