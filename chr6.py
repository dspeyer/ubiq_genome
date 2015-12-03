#!/usr/bin/python

from scipy.stats import binom

ourvals={}
ourps={}

ngenomes=2405

ps=[.2/ngenomes]*ngenomes

hetcom=[0]*ngenomes
hetrare=[0]*ngenomes
hommatch=[0]*ngenomes
hommis=[0]*ngenomes

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
    if ourvals[snp]==words[3]:
        ourval='0'
    elif ourvals[snp]==words[4]:
        ourval='1'
    else:
        continue
    for i in range(ngenomes):
        ref=words[i+9]
        if ref[0]==ref[2]: # homozygous case
#            continue
            if ourval==ref[0]: # match
                p_obs_given_match = 1
                hommatch[i] += 1
            else:
                p_obs_given_match = .05 # wild guess
                hommis[i] += 1
            p_obs_given_mismatch = ourps[snp]
        else: # heterozygous
            p_obs_given_match = 0.5
            p_obs_given_mismatch = ourps[snp]
            if ourps[snp]>.5:
                hetcom[i] += 1
            else:
                hetrare[i] += 1
        p_obs = ps[i]*p_obs_given_match + (1-ps[i])*p_obs_given_mismatch
        ps[i] *= p_obs_given_match / p_obs

results = zip(ps, range(ngenomes))
results.sort(key=lambda(x):x[0],reverse=True)
for i in results:
    print 'Patient %d has p=%f homhit=%d hommiss=%d het common=%d rare=%d p=%f' % (i[1],i[0],hommatch[i[1]],hommis[i[1]],hetcom[i[1]], hetrare[i[1]], binom.cdf(min(hetcom[i[1]], hetrare[i[1]]), hetcom[i[1]]+hetrare[i[1]], 0.5))
    if i[0]<.1:
        break
