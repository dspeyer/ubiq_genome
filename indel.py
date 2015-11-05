#!/usr/bin/python

import sys
from collections import defaultdict

inssize=defaultdict(lambda:0)
delsize=defaultdict(lambda:0)
insnuc=defaultdict(lambda:0)
delnuc=defaultdict(lambda:0)

tot=0

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
        tot += len(query)
        state='neither'
        indelsince=-1
        for i in xrange(len(query)):
            if query[i]=='-' and sbjct[i]=='-':
                print 'Error matching - %s %s %d' % (fn, name, i)
            if state=='neither':
                if query[i]=='-':
                    state='del'
                    delnuc[sbjct[i]] += 1
                    indelsince=i
                if sbjct[i]=='-':
                    state='ins'
                    insnuc[query[i]] += 1
                    indelsince=i
            elif state=='ins':
                if sbjct[i]=='-':
                    insnuc[query[i]] += 1
                else:
                    state='neither'
                    inssize[i-indelsince] += 1
            elif state=='del':
                if query[i]=='-':
                    delnuc[sbjct[i]] += 1
                else:
                    state='neither'
                    delsize[i-indelsince] += 1

print 'size\tins\tdels'
for i in sorted(list(set(inssize.keys()+delsize.keys()))):
#    print '%d\t%.2g%%\t%.2g%%' % (i, 100*inssize[i]/float(tot), 100*delsize[i]/float(tot))
    print '%d\t%d\t%d' % (i, inssize[i], delsize[i])

print 'nuc\t#ins\t#dels'
for i in sorted(list(set(insnuc.keys()+delnuc.keys()))):
    print '%s\t%d\t%d' % (i, insnuc[i], delnuc[i])
