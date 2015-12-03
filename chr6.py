#!/usr/bin/python

from scipy.stats import binom
from collections import defaultdict
from updateonsnp import update

ourvals={}
ourps={}

ngenomes=2405

ps=[.2/ngenomes]*ngenomes

hetcom=[0]*ngenomes
hetrare=[0]*ngenomes
hommatch=[0]*ngenomes
hommis=[0]*ngenomes

notes=[]
for i in range(ngenomes):
    notes.append(defaultdict(lambda:0))

for line in file('snplist'):
    words=line.split('\t')
    if words[0]=='chr6' and words[4]!='0':
        ourvals[words[2]] = words[3]
        ourps[words[2]] = float(words[4])

for line in file('/windows/ALL.chr6.ours.vcf'):
    words=line.rstrip().split('\t')
    snp = words[2]
    if snp not in ourvals:
        continue
    meaning=words[3:5]
    if len(meaning[1])>1:
        meaning=[meaning[0]]+meaning[1].split(',')
    for i in range(ngenomes):
        ref=words[i+9]
        try:
            ref=meaning[int(ref[0])]+meaning[int(ref[2])]
        except IndexError as e:
            print ref
            print meaning
            throw(e)
        ps[i]=update(ourvals[snp], ref, ps[i], ourps[snp], notes[i])

results = zip(ps, range(ngenomes))
results.sort(key=lambda(x):x[0],reverse=True)
for i in results:
    p=i[1]
    hetcom=notes[p]['hetcom']
    hetrare=notes[p]['hetrare']
    print 'Patient %d has p=%f homhit=%d hommiss=%d het common=%d rare=%d p=%f' % (p,i[0],notes[p]['homohit'],notes[p]['homomiss'], hetcom, hetrare, binom.cdf(min(hetcom, hetrare), hetcom+hetrare, 0.5))
    if i[0]<.1:
        break
