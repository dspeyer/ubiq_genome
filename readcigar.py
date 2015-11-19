#!/usr/bin/python

import sys
import re

fqfn=sys.argv[1]
samfn=sys.argv[2]

try:
    fq=file(fqfn)
    sam=file(samfn)
except IOError as e:
    print e
    sys.exit()

fq.readline()
qseq=fq.readline()
fq.close()

for line in sam:
    if line[:3]=='@SQ':
        continue
    words=line.split('\t')
    cigar=words[5]
    rseq=words[9]
    break

sam.close()

cigarpieces = re.split('([0-9]*[A-Z])', cigar)
qi=0
ri=0
tot={'S':0, 'M':0, 'I':0, 'D':0}

for piece in cigarpieces:
    if not piece:
        continue
    n=int(piece[:-1])
    op=piece[-1]
    tot[op]+=n
    print '[qi=%d ri=%d]' % (qi,ri)
    if op=='S':
        print 'skipping %d' % n
        qi += n
        ri += n
    elif op=='M':
        print '%d should match:' % n
        print '  '+qseq[qi:(qi+n)]
        print '  '+rseq[ri:(ri+n)]
        qi+=n
        ri+=n
    elif op=='I':
        print '%d inserted:' % n
        print '  '+qseq[qi:(qi+n)]
        qi+=n
    elif op=='D':
        print '%d deleted:' % n
        print '  '+rseq[ri:(ri+n)]
        ri+=n
    else:
        print 'unknown op: %s' % op

print 'accounted %d of %d of query an %d of %d of ref' % (qi,len(qseq),ri,len(rseq))
for i in tot:
    print 'total %s: %d'%(i,tot[i])
