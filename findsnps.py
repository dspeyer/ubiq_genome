#!/usr/bin/python

from collections import namedtuple
from collections import defaultdict
from bintrees import RBTree

#Read = namedtuple('Read', ['chr', 'start', 'end', 'id', 'qual', 'sense', 'file', 'value'])
#SNP = namedtuple('SNP', ['bin', 'chrom', 'chromStart', 'chromEnd', 'name', 'score', 'strand', 'refNCBI', 'refUCSC', 'observed', 'molType', 'type', 'valid', 'avHet', 'avHetSE', 'func', 'locType', 'weight', 'exceptions', 'submitterCount', 'submitters', 'alleleFreqCount', 'alleles', 'alleleNs', 'alleleFreqs', 'bitfields'])

class Read:
    fields = ['chr', 'start', 'end', 'id', 'qual', 'sense', 'file', 'value']
    def __init__(self, *args):
        for i in zip(self.fields,args):
            if i[0] in ['start', 'end', 'qual']:
                setattr(self, i[0], int(i[1]))
            else:
                setattr(self, i[0], i[1])

class SNP:
    fields = ['bin', 'chrom', 'chromStart', 'chromEnd', 'name', 'score', 'strand', 'refNCBI', 'refUCSC', 'observed', 'molType', 'type', 'valid', 'avHet', 'avHetSE', 'func', 'locType', 'weight', 'exceptions', 'submitterCount', 'submitters', 'alleleFreqCount', 'alleles', 'alleleNs', 'alleleFreqs', 'bitfields']
    def __init__(self, *args):
        for i in zip(self.fields,args):
            if i[0] in ['chromStart', 'chromEnd', 'score', 'alleleFreqCount']:
                setattr(self, i[0], int(i[1]))
            else:
                setattr(self, i[0], i[1])


data = defaultdict(lambda:RBTree())

for line in file('h2fq/rob-bwa-out/poshitlist'):
    line=line.rstrip()
    bed=file('h2fq/rob-bwa-out/%s.bed.1' % line).readline()
    value=file('h2fq/rob-bwa-out/%s.query.fa' % line).readline()
    words = bed.split('\t')
    words += [line, value]
    r = Read(*words)
    data[r.chr][r.start]=r

for line in file('../snp138Common.txt'):
    snp = SNP(*line.split('\t'))
    if snp.strand != '+':
        continue
    try:
        key = data[snp.chrom].floor_key(snp.chromStart)
        read = data[snp.chrom][key]
    except KeyError:
        continue
    if read.end > snp.chromEnd:
        nuc = read.value[snp.chromStart-read.start]
        nucs = snp.alleles.split(',')
        if nuc in nucs:
            freqs = snp.alleleFreqs.split(',')
            freq = freqs[nucs.index(nuc)]
        else:
            freq = '0'
        print '\t'.join(map(str,[snp.chrom, snp.chromStart, snp.name, nuc, freq, read.file]))
    
