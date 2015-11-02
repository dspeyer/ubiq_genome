#!/usr/bin/python
from glob import glob
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from bisect import bisect
from collections import defaultdict
import sys
import h5py
import time
import cStringIO
import xml.parsers.expat
import signal

class TimeoutError(Exception):
    pass

class timeout:
    def __init__(self, seconds=1, error_message='Timeout'):
        self.seconds = seconds
        self.error_message = error_message
    def handle_timeout(self, signum, frame):
        raise TimeoutError(self.error_message)
    def __enter__(self):
        signal.signal(signal.SIGALRM, self.handle_timeout)
        signal.alarm(self.seconds)
    def __exit__(self, type, value, traceback):
        signal.alarm(0)

print xml.parsers.expat.ExpatError

#allfns = glob(sys.argv[1]+'/downloads/pass/*.fast5')

allfns = [
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch107_file2_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch143_file2_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch143_file4_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch152_file0_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch175_file1_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch175_file27_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch175_file3_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch192_file10_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch192_file17_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch192_file4_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch205_file27_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch223_file3_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch226_file1_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch243_file5_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch256_file6_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch260_file11_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch262_file12_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch262_file16_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch276_file4_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch296_file9_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch301_file10_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch301_file32_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch301_file34_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch301_file50_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch301_file52_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch301_file83_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch303_file34_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch303_file63_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch303_file66_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch308_file8_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch308_file9_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch309_file0_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch309_file19_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch309_file24_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch309_file58_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch309_file59_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch312_file12_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch312_file28_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch312_file45_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch312_file60_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch312_file65_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch312_file6_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch318_file5_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch319_file40_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch319_file65_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch320_file3_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch339_file25_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch354_file34_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch354_file6_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch361_file1_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch363_file1_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch36_file25_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch36_file2_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch36_file36_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch36_file3_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch370_file0_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch383_file10_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch383_file2_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch383_file30_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch395_file16_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch395_file28_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch398_file3_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch399_file24_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch399_file5_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch400_file16_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch400_file2_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch400_file9_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch401_file0_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch401_file11_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch406_file11_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch406_file39_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch408_file1_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch409_file1_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch411_file12_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch413_file0_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch418_file10_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch420_file2_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch420_file8_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch422_file25_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch450_file7_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch456_file3_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch458_file3_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch458_file9_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch459_file20_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch459_file23_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch459_file34_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch459_file43_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch459_file50_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch459_file57_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch459_file72_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch459_file81_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch459_file91_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch460_file13_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch460_file4_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch462_file1_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch464_file6_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch466_file7_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch469_file0_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch475_file13_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch475_file21_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch475_file2_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch475_file31_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch475_file7_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch485_file15_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch485_file9_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch486_file5_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch489_file0_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch492_file4_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch505_file2_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch508_file16_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch508_file19_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch508_file2_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch508_file3_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch511_file21_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch511_file26_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch511_file27_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch511_file31_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch511_file36_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch51_file10_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch51_file12_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch54_file19_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch6_file2_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch73_file14_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch73_file20_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch73_file21_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch73_file40_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch73_file45_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch86_file15_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch86_file31_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch86_file36_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch96_file1_strand.fast5",
"/home/dspeyer/hackathon1-rw/alldata/downloads/pass/MINION02_4teamawesome_2446_1_ch96_file5_strand.fast5"
]

batch = 1

for b in range(0, len(allfns), batch):
    print 'starting %d...' % b

    fns = allfns[b:b+batch]
    
    seqs=[]
    lens=[]
    starts=[0]

    print '  reading...'
    for fn in fns:
        f=h5py.File(fn,'r')
        seqs.append(f['Analyses']['Basecall_2D_000']['BaseCalled_2D']['Fastq'].value.split('\n')[1])
        lens.append(len(seqs[-1]))
        starts.append(starts[-1]+lens[-1])

    print '  querying...'
    try:
        with timeout(seconds=240):
            handle=NCBIWWW.qblast('blastn', 'nt',''.join(seqs),
                                  megablast=True,
                                  expect=1e-50,
                                  alignments=10,
                                  descriptions=10,
                                  hitlist_size=10)
    except TimeoutError:
        print '  timed out'
        continue
    print '  parsing...'
    try:
        res=NCBIXML.read(handle)
    except xml.parsers.expat.ExpatError:
        handle.seek(0)
        str=handle.read()
        str+='</Iteration_hits></Iteration></BlastOutput_iterations></BlastOutput>'
        handle2=cStringIO.StringIO(str)
        try:
            res=NCBIXML.read(handle2)
        except xml.parsers.expat.ExpatError:
            print 'XML Failure effecting files: '+', '.join(fns)
            continue

    print '  untangling...'
    matches = []
    for i in seqs:
        matches.append(defaultdict(lambda:0))

    for alignment in res.alignments:
        spe=' '.join(alignment.hit_def.replace('Primary structure of ','').split(' ')[0:2])
        for hsp in alignment.hsps:
            qs=hsp.query_start
            qe=hsp.query_end
            l=qe-qs
            s_in = bisect(starts,qs)-1
            e_in = bisect(starts,qs)-1
            if s_in!=e_in:
                continue
            if l > matches[s_in][spe]:
                matches[s_in][spe] = l

    print '  writing...'
    for i in range(len(seqs)):
        ofn = 'matches/'+fns[i].split('/')[-1].split('.')[0]+'.species'
        f=file(ofn, 'w')
        f.write('Raw Data\t%d\n' % lens[i])
        keys=matches[i].keys()
        keys.sort(key=lambda(x):matches[i][x], reverse=True)
        for k in keys:
            f.write('%s\t%d\n' % (k, matches[i][k]))
        f.close()

    print '  waiting...'
    time.sleep(3)
