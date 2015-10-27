#!/usr/bin/python

import sys
from glob import glob
import h5py
import numpy
import matplotlib.pyplot as plot

fns= glob(sys.argv[1]+'/pass/*.fast5')

data=numpy.zeros( (len(fns)*2, 4**5) )
durs=numpy.matrix(numpy.zeros( (len(fns)*2, 1) ))

nv={'A':0, 'C':1, 'G':2, 'T':3}
vn='ACGT'
places=[4**x for x in range(5)]

def l2n(seq):
    return numpy.dot([nv[l] for l in seq], places)

def n2l(n):
    o=''
    for i in range(5):
        o+=vn[n%4]
        n/=4
    return o

fnc=0
for fn in fns:
    f=h5py.File(fn,'r')
    for side in ['template','complement']:
        dur=f['Analyses']['Basecall_2D_000']['BaseCalled_'+side]['Events'].attrs['duration']
        seq=f['Analyses']['Basecall_2D_000']['BaseCalled_'+side]['Fastq'].value.split('\n')[1]
        for i in range(len(seq)-5):
            data[fnc][l2n(seq[i:i+5])]+=1
        durs[fnc][0] = dur
        fnc+=1

costs = numpy.linalg.pinv(data)*durs

pred = data * costs

plot.scatter(durs, pred, c=['red','blue']*len(fns))
plot.show()

# fnc=0
# for fn in fns:
#     print '%s, template, %.1f, %.1f' % (fn, durs[fnc][0], pred[fnc][0])
#     fnc+=1
#     print '%s, complement, %.1f, %.1f' % (fn, durs[fnc][0], pred[fnc][0])
#     fnc+=1
