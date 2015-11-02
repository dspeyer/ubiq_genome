#!/usr/bin/python
from glob import glob
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from bisect import bisect
from collections import defaultdict
import sys
import h5py
import time
import cStringIO
import xml.parsers.expat
import signal

for fn in glob(sys.argv[1]+'/*.fasta.xml'):
    try:
        res=NCBIXML.read(file(fn))
    except ValueError:
        print 'ValueError for %s' % fn
        continue
    outf=file(fn.replace('.fasta.xml','.match'),'w')
    outf.write('Raw Data: %d\n' % res.query_length)
    matches=defaultdict(lambda:0)
    for alignment in res.alignments:
        spe=' '.join(alignment.hit_def.replace('Primary structure of ','').split(' ')[0:2])
        for hsp in alignment.hsps:
            l=hsp.query_end-hsp.query_start
            if l>matches[spe]:
                matches[spe]=l
    keys=matches.keys()
    keys.sort(key=lambda(x):matches[x], reverse=True)
    for k in keys:
        outf.write('%s\t%d\n' % (k, matches[k]))
    outf.close()
