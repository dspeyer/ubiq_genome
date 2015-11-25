#!/usr/bin/python

from glob import glob
import re


continent_of = {
    'CEU': 'Europe', # European (any)
    'CHB': 'Asia',   # Han Chinese
    'HCB': 'Asia',   # Han Chinese
    'JPT': 'Asia',   # Japanese
    'YRI': 'Africa', # Yoruba (West African)
    'ASW': 'Africa', # African (any)
    'CHD': 'Asia',   # Chinese (any)
    'GIH': 'India',  # Gujarati (India)
    'LWK': 'Africa', # Luhya (Bantu; East African)
    'MEX': 'Mexico', # Mexicans -- how do you categorize that?
    'MKK': 'Africa', # Maasai
    'TSI': 'Europe'  # Tuscany (Italy)
}

pop = {
    'CEU': 180,
    'CHB': 90,
    'HCB': 90,
    'JPT': 91,
    'YRI': 180,
    'ASW': 90,
    'CHD': 100,
    'GIH': 100,
    'LWK': 100,
    'MEX': 90,
    'MKK': 180,
    'TSI': 100
}


p = {
    'Europe': .2,
    'Asia': .2,
    'Africa': .2,
    'Mexico': .2,
    'India': .2
}

for fn in glob('snpedia/*.info'):
    val = file(fn).readline()[7]
    counts = {
        'Europe': [0,0],
        'Asia': [0,0],
        'Africa': [0,0],
        'Mexico': [0,0],
        'India': [0,0]
    }
    opts = ['?','?']
    for line in file(fn.replace('info','mw')):
        m = re.match('\\| geno2=\\(([ACTG]);([ACTG])\\)', line)
        if m:
            opts = m.groups()
            if val not in opts:
                print 'WARNING: val %s is neither %s nor %s for snp %s' % (val, opts[0], opts[1], fn)
        m = re.match('\\| ([A-Z]{3}) \\| ([0-9.]*) \\| ([0-9.]*) \\| ([0-9.]*)', line)
        if m:
            homo=[0,0]
            (group, homo[0], hetero, homo[1]) = m.groups()
            if group not in continent_of:
                print 'WARNING: unrecognized %s in %s' % (group, fn)
                continue
            for i in [0,1]:
                counts[continent_of[group]][i] += (2*float(homo[i])+float(hetero)) * pop[group]
    p_obs_given_cont = {}
    p_obs = 0
    if opts[0]=='?':
        continue
    print fn
    print 'counts: %s' % counts

    try:
        for continent in counts:
            p_obs_given_cont[continent] = counts[continent][opts.index(val)] / sum(counts[continent])
            p_obs += p_obs_given_cont[continent] * p[continent]
    except ZeroDivisionError:
        print 'abort\n'
        continue
    for continent in counts:
        p[continent] *= p_obs_given_cont[continent] / p_obs
    print 'p(obs|cont) = %s' % p_obs_given_cont
    print 'p(cont) = %s' % p
    print

for i in p:
    print '%s: %.1f%%' % (i,100*p[i])
                
