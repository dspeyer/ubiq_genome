#!/usr/bin/python
from glob import glob
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from bisect import bisect
from collections import defaultdict
import sys
import h5py
import xml
import time

allfns = glob(sys.argv[1]+'/downloads/pass/*.fast5')
batch = 15

for b in range(0, len(allfns), batch):
    print 'starting %d...' % b

    fns = allfns[b:b+batch]
    
    seqs=[]
    lens=[]
    starts=[0]

    print '  reading...'
    for fn in fns:
        f=h5py.File(fn,'r')
        seqs.append(f['Analyses']['Basecall_2D_000']['BaseCalled_2D']['Fastq'].value.split('\n')[1])
        lens.append(len(seqs[-1]))
        starts.append(starts[-1]+lens[-1])

    print '  querying...'
    handle=NCBIWWW.qblast('blastn', 'nt', ''.join(seqs),
                          megablast=True,
                          expect=1e-4)
    print '  parsing...'
    try:
        res=NCBIXML.read(handle)
    except xml.parsers.expat.ExpatError:
        print 'XML Failure effecting files: '+', '.join(fns)
        continue

    print '  untangling...'
    matches = []
    for i in seqs:
        matches.append(defaultdict(lambda:0))

    for alignment in res.alignments:
        spe=' '.join(alignment.hit_def.replace('Primary structure of ','').split(' ')[0:2])
        for hsp in alignment.hsps:
            qs=hsp.query_start
            qe=hsp.query_end
            l=qe-qs
            s_in = bisect(starts,qs)-1
            e_in = bisect(starts,qs)-1
            if s_in!=e_in:
                continue
            if l > matches[s_in][spe]:
                matches[s_in][spe] = l

    print '  writing...'
    for i in range(len(seqs)):
        ofn = 'matches/'+fns[i].split('/')[-1].split('.')[0]+'.species'
        f=file(ofn, 'w')
        f.write('Raw Data\t%d\n' % lens[i])
        keys=matches[i].keys()
        keys.sort(key=lambda(x):matches[i][x], reverse=True)
        for k in keys:
            f.write('%s\t%d\n' % (k, matches[i][k]))
        f.close()

    print '  waiting...'
    time.sleep(3)
