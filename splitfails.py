#!/usr/bin/python

import sys
from glob import glob
import h5py
import os

faildir=sys.argv[1]

fns=glob(faildir+'/*.fast5')

try:
    os.mkdir(faildir+'/has2d')
except:
    pass
try:
    os.mkdir(faildir+'/no2d')
except:
    pass


for fp in fns:
    fn=fp.split('/')[-1]
    f=h5py.File(fp,'r')
    if 'BaseCalled_2D' in f['Analyses']['Basecall_2D_000'].keys():
        os.symlink(fp, faildir+'/has2d/'+fn)
    else:
        os.symlink(fp, faildir+'/no2d/'+fn)
