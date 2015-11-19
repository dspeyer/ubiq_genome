#!/usr/bin/python

from collections import defaultdict
import sys

cnt=defaultdict(lambda:defaultdict(lambda:0))

fl = file('h2fq/rob-bwa-out/poshitlist')
for fn in fl:
    fn=fn.rstrip()
    ref=file('h2fq/rob-bwa-out/'+fn+'.ref.fa').readlines()[1].rstrip().upper()
    query=file('h2fq/rob-bwa-out/'+fn+'.query.fa').read().rstrip()
    if len(ref)!=len(query):
        print 'error in %s %d!=%d'%(fn,len(ref),len(query))
    for i in range(len(ref)):
        cnt[ref[i]][query[i]] += 1
    ins=file('h2fq/rob-bwa-out/'+fn+'.insertions').read()
    for clause in ins.split('\t'):
        if clause=='\n':
            break
        try:
            (c,n)=clause.split(' ')
            cnt['-'][c]+=int(n)
        except ValueError:
            print 'Skipping "%s"' % clause
            

#print '\\documentclass{article}'
#print '\\begin{document}'
print '\\begin{tabular}{r||r|r|r|r|r}'

order='ACGT-'
print ' & '.join(' '+order)+'\\\\ \\hline'
for row in order:
    print '\\hline'
    sys.stdout.write(row+' & ')
    for col in order:
        sys.stdout.write('%d'%cnt[row][col])
        if col!='-':
            sys.stdout.write(' & ')
    sys.stdout.write('\\\\ \n')

print '\\end{tabular}'
#print '\\end{document}'
