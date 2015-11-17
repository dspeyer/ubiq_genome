#!/usr/bin/python

import h5py
import sys

def parse(root, obj):
    if type(obj) == h5py._hl.dataset.Dataset:
        print '[%s]\n%s\n\n' % (root, obj.value)
    else:
        for k in obj.keys():
            try:
                ch=obj[k]
                parse(root+'/'+k, ch)
            except:
                print '<<Error at key %s/%s>>' % (root,k)

for i in sys.argv[1:]:
    print '=== '+ i + ' ==='
    f = h5py.File(i,'r')
    parse('',f)
