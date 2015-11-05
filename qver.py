#!/usr/bin/python

import sys
from collections import defaultdict

corr=defaultdict(lambda:0)
miss=defaultdict(lambda:0)

for fn in sys.argv[1:]:
    f=file(fn)
    while f:
        try:
            name=f.next()
            pos=f.next()
            query=f.next()
            match=f.next()
            sbjct=f.next()
        except StopIteration:
            break
        [_, start, _, end, _, outof] = pos.split(' ')[:6]
        if (int(end)-int(start)) / float(outof[:-1]) < .95:
            continue
        if len(query)!=len(sbjct):
            print 'Length mismatch %s %s (%d vs %d)' % (fn, name, len(query), len(sbjct))
            continue
        quality=file(fn.replace('.align','.q')).read()
        qi=int(start)
        for i in range(len(query)):
            if query[i]=='-':
                continue
            if match[i]=='|':
                corr[quality[qi]]+=1
            else:
                miss[quality[qi]]+=1
            qi+=1

for i in range(30):
    c=chr(i+33)
    print '%d, %d, %d' % (i, corr[c], miss[c])
