#!/usr/bin/python

import sys
from collections import defaultdict

inssize=defaultdict(lambda:0)
delsize=defaultdict(lambda:0)
insnuc=defaultdict(lambda:0)
delnuc=defaultdict(lambda:0)

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
        state='neither'
        indelsince=-1
        for i in xrange(len(query)):
            if query[i]=='-' and sbjct[i]=='-':
                print 'Error matching - %s %s %d' % (fn, name, i)
            if state=='neither':
                if query[i]=='-':
                    state='ins'
                    insnuc[sbjct[i]] += 1
                    indelsince=i
                if sbjct[i]=='-':
                    state='del'
                    delnuc[query[i]] += 1
                    indelsince=i
            elif state=='ins':
                if query[i]=='-':
                    insnuc[sbjct[i]] += 1
                else:
                    state='neither'
                    inssize[i-indelsince] += 1
            elif state=='del':
                if sbjct[i]=='-':
                    insnuc[query[i]] += 1
                else:
                    state='neither'
                    delsize[i-indelsince] += 1

print 'size\t#ins\t#dels'
for i in set(inssize.keys()+delsize.keys()):
    print '%d\t%d\t%d' % (i, inssize[i], delsize[i])

print 'nuc\t#ins\t#dels'
for i in set(insnuc.keys()+delnuc.keys()):
    print '%s\t%d\t%d' % (i, insnuc[i], delnuc[i])
