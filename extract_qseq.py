#!/usr/bin/python

import sys
import re

fn=sys.argv[1]
sam=file(fn)
for line in sam:
    if line[:1]=='@':
        continue
    words=line.split('\t')
    cigar=words[5]
    seq=words[9]
    break

cigarpieces = re.split('([0-9]*[A-Z])', cigar)
i=0

ins={'A':0, 'C':0, 'G':0, 'T':0}

seqf=file(fn.replace('.sam','.query.fa'), 'w')
insf=file(fn.replace('.sam','.insertions'), 'w')

for piece in cigarpieces:
    if not piece:
        continue
    n=int(piece[:-1])
    op=piece[-1]
    if op=='S':
        i += n
    elif op=='I':
        for c in seq[i:(i+n)]:
            ins[c]+=1
        i += n
    elif op=='M':
        seqf.write(seq[i:(i+n)])
        i+=n
    elif op=='D':
        seqf.write('-'*n)
    else:
        print '<<unknown op: %s>>' % op

for c in 'ACTG':
    insf.write('%s %d\t'%(c,ins[c]))
insf.write('\n')

seqf.close()
insf.close()
