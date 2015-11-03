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

files = [
    "MINION02_4teamawesome_2446_1_ch111_file11_strand",
    "MINION02_4teamawesome_2446_1_ch111_file13_strand",
    "MINION02_4teamawesome_2446_1_ch111_file14_strand",
    "MINION02_4teamawesome_2446_1_ch111_file5_strand",
    "MINION02_4teamawesome_2446_1_ch111_file7_strand",
    "MINION02_4teamawesome_2446_1_ch118_file13_strand",
    "MINION02_4teamawesome_2446_1_ch118_file27_strand",
    "MINION02_4teamawesome_2446_1_ch11_file1_strand",
    "MINION02_4teamawesome_2446_1_ch126_file3_strand",
    "MINION02_4teamawesome_2446_1_ch133_file44_strand",
    "MINION02_4teamawesome_2446_1_ch133_file46_strand",
    "MINION02_4teamawesome_2446_1_ch133_file6_strand",
    "MINION02_4teamawesome_2446_1_ch145_file13_strand",
    "MINION02_4teamawesome_2446_1_ch149_file14_strand",
    "MINION02_4teamawesome_2446_1_ch149_file18_strand",
    "MINION02_4teamawesome_2446_1_ch149_file31_strand",
    "MINION02_4teamawesome_2446_1_ch151_file7_strand",
    "MINION02_4teamawesome_2446_1_ch166_file5_strand",
    "MINION02_4teamawesome_2446_1_ch172_file0_strand",
    "MINION02_4teamawesome_2446_1_ch173_file0_strand",
    "MINION02_4teamawesome_2446_1_ch175_file17_strand",
    "MINION02_4teamawesome_2446_1_ch175_file29_strand",
    "MINION02_4teamawesome_2446_1_ch175_file46_strand",
    "MINION02_4teamawesome_2446_1_ch175_file50_strand",
    "MINION02_4teamawesome_2446_1_ch175_file70_strand",
    "MINION02_4teamawesome_2446_1_ch175_file82_strand",
    "MINION02_4teamawesome_2446_1_ch18_file0_strand",
    "MINION02_4teamawesome_2446_1_ch192_file24_strand",
    "MINION02_4teamawesome_2446_1_ch192_file29_strand",
    "MINION02_4teamawesome_2446_1_ch199_file1_strand",
    "MINION02_4teamawesome_2446_1_ch202_file6_strand",
    "MINION02_4teamawesome_2446_1_ch205_file13_strand",
    "MINION02_4teamawesome_2446_1_ch205_file73_strand",
    "MINION02_4teamawesome_2446_1_ch206_file5_strand",
    "MINION02_4teamawesome_2446_1_ch208_file5_strand",
    "MINION02_4teamawesome_2446_1_ch208_file65_strand",
    "MINION02_4teamawesome_2446_1_ch212_file32_strand",
    "MINION02_4teamawesome_2446_1_ch212_file46_strand",
    "MINION02_4teamawesome_2446_1_ch212_file48_strand",
    "MINION02_4teamawesome_2446_1_ch212_file53_strand",
    "MINION02_4teamawesome_2446_1_ch212_file59_strand",
    "MINION02_4teamawesome_2446_1_ch212_file64_strand",
    "MINION02_4teamawesome_2446_1_ch222_file10_strand",
    "MINION02_4teamawesome_2446_1_ch222_file11_strand",
    "MINION02_4teamawesome_2446_1_ch222_file12_strand",
    "MINION02_4teamawesome_2446_1_ch222_file14_strand",
    "MINION02_4teamawesome_2446_1_ch222_file5_strand",
    "MINION02_4teamawesome_2446_1_ch222_file9_strand",
    "MINION02_4teamawesome_2446_1_ch227_file2_strand",
    "MINION02_4teamawesome_2446_1_ch228_file2_strand",
    "MINION02_4teamawesome_2446_1_ch228_file9_strand",
    "MINION02_4teamawesome_2446_1_ch230_file1_strand",
    "MINION02_4teamawesome_2446_1_ch230_file2_strand",
    "MINION02_4teamawesome_2446_1_ch238_file0_strand",
    "MINION02_4teamawesome_2446_1_ch241_file15_strand",
    "MINION02_4teamawesome_2446_1_ch241_file5_strand",
    "MINION02_4teamawesome_2446_1_ch260_file16_strand",
    "MINION02_4teamawesome_2446_1_ch260_file9_strand",
    "MINION02_4teamawesome_2446_1_ch262_file13_strand",
    "MINION02_4teamawesome_2446_1_ch265_file4_strand",
    "MINION02_4teamawesome_2446_1_ch26_file8_strand",
    "MINION02_4teamawesome_2446_1_ch296_file3_strand",
    "MINION02_4teamawesome_2446_1_ch296_file4_strand",
    "MINION02_4teamawesome_2446_1_ch301_file14_strand",
    "MINION02_4teamawesome_2446_1_ch301_file16_strand",
    "MINION02_4teamawesome_2446_1_ch301_file19_strand",
    "MINION02_4teamawesome_2446_1_ch303_file16_strand",
    "MINION02_4teamawesome_2446_1_ch303_file21_strand",
    "MINION02_4teamawesome_2446_1_ch303_file25_strand",
    "MINION02_4teamawesome_2446_1_ch303_file27_strand",
    "MINION02_4teamawesome_2446_1_ch303_file43_strand",
    "MINION02_4teamawesome_2446_1_ch303_file54_strand",
    "MINION02_4teamawesome_2446_1_ch303_file66_strand",
    "MINION02_4teamawesome_2446_1_ch308_file19_strand",
    "MINION02_4teamawesome_2446_1_ch308_file20_strand",
    "MINION02_4teamawesome_2446_1_ch308_file22_strand",
    "MINION02_4teamawesome_2446_1_ch309_file47_strand",
    "MINION02_4teamawesome_2446_1_ch312_file2_strand",
    "MINION02_4teamawesome_2446_1_ch312_file33_strand",
    "MINION02_4teamawesome_2446_1_ch312_file44_strand",
    "MINION02_4teamawesome_2446_1_ch312_file45_strand",
    "MINION02_4teamawesome_2446_1_ch312_file48_strand",
    "MINION02_4teamawesome_2446_1_ch312_file56_strand",
    "MINION02_4teamawesome_2446_1_ch312_file65_strand",
    "MINION02_4teamawesome_2446_1_ch318_file2_strand",
    "MINION02_4teamawesome_2446_1_ch319_file14_strand",
    "MINION02_4teamawesome_2446_1_ch319_file19_strand",
    "MINION02_4teamawesome_2446_1_ch319_file20_strand",
    "MINION02_4teamawesome_2446_1_ch319_file35_strand",
    "MINION02_4teamawesome_2446_1_ch319_file57_strand",
    "MINION02_4teamawesome_2446_1_ch319_file63_strand",
    "MINION02_4teamawesome_2446_1_ch320_file11_strand",
    "MINION02_4teamawesome_2446_1_ch320_file16_strand",
    "MINION02_4teamawesome_2446_1_ch320_file23_strand",
    "MINION02_4teamawesome_2446_1_ch32_file2_strand",
    "MINION02_4teamawesome_2446_1_ch354_file20_strand",
    "MINION02_4teamawesome_2446_1_ch36_file0_strand",
    "MINION02_4teamawesome_2446_1_ch36_file15_strand",
    "MINION02_4teamawesome_2446_1_ch36_file16_strand",
    "MINION02_4teamawesome_2446_1_ch36_file22_strand",
    "MINION02_4teamawesome_2446_1_ch36_file27_strand",
    "MINION02_4teamawesome_2446_1_ch370_file1_strand",
    "MINION02_4teamawesome_2446_1_ch377_file2_strand",
    "MINION02_4teamawesome_2446_1_ch378_file1_strand",
    "MINION02_4teamawesome_2446_1_ch383_file7_strand",
    "MINION02_4teamawesome_2446_1_ch384_file0_strand",
    "MINION02_4teamawesome_2446_1_ch394_file15_strand",
    "MINION02_4teamawesome_2446_1_ch394_file26_strand",
    "MINION02_4teamawesome_2446_1_ch394_file57_strand",
    "MINION02_4teamawesome_2446_1_ch394_file6_strand",
    "MINION02_4teamawesome_2446_1_ch394_file70_strand",
    "MINION02_4teamawesome_2446_1_ch394_file78_strand",
    "MINION02_4teamawesome_2446_1_ch395_file16_strand",
    "MINION02_4teamawesome_2446_1_ch395_file17_strand",
    "MINION02_4teamawesome_2446_1_ch398_file5_strand",
    "MINION02_4teamawesome_2446_1_ch399_file10_strand",
    "MINION02_4teamawesome_2446_1_ch399_file4_strand",
    "MINION02_4teamawesome_2446_1_ch3_file1_strand",
    "MINION02_4teamawesome_2446_1_ch400_file2_strand",
    "MINION02_4teamawesome_2446_1_ch400_file6_strand",
    "MINION02_4teamawesome_2446_1_ch401_file19_strand",
    "MINION02_4teamawesome_2446_1_ch401_file9_strand",
    "MINION02_4teamawesome_2446_1_ch408_file11_strand",
    "MINION02_4teamawesome_2446_1_ch411_file19_strand",
    "MINION02_4teamawesome_2446_1_ch411_file23_strand",
    "MINION02_4teamawesome_2446_1_ch411_file2_strand",
    "MINION02_4teamawesome_2446_1_ch411_file9_strand",
    "MINION02_4teamawesome_2446_1_ch416_file7_strand",
    "MINION02_4teamawesome_2446_1_ch418_file20_strand",
    "MINION02_4teamawesome_2446_1_ch422_file31_strand",
    "MINION02_4teamawesome_2446_1_ch422_file53_strand",
    "MINION02_4teamawesome_2446_1_ch422_file56_strand",
    "MINION02_4teamawesome_2446_1_ch430_file0_strand",
    "MINION02_4teamawesome_2446_1_ch430_file15_strand",
    "MINION02_4teamawesome_2446_1_ch430_file16_strand",
    "MINION02_4teamawesome_2446_1_ch430_file24_strand",
    "MINION02_4teamawesome_2446_1_ch430_file2_strand",
    "MINION02_4teamawesome_2446_1_ch432_file1_strand",
    "MINION02_4teamawesome_2446_1_ch447_file4_strand",
    "MINION02_4teamawesome_2446_1_ch450_file1_strand",
    "MINION02_4teamawesome_2446_1_ch458_file9_strand",
    "MINION02_4teamawesome_2446_1_ch459_file11_strand",
    "MINION02_4teamawesome_2446_1_ch459_file36_strand",
    "MINION02_4teamawesome_2446_1_ch459_file62_strand",
    "MINION02_4teamawesome_2446_1_ch466_file0_strand",
    "MINION02_4teamawesome_2446_1_ch466_file10_strand",
    "MINION02_4teamawesome_2446_1_ch467_file2_strand",
    "MINION02_4teamawesome_2446_1_ch470_file3_strand",
    "MINION02_4teamawesome_2446_1_ch475_file11_strand",
    "MINION02_4teamawesome_2446_1_ch475_file31_strand",
    "MINION02_4teamawesome_2446_1_ch489_file0_strand",
    "MINION02_4teamawesome_2446_1_ch508_file12_strand",
    "MINION02_4teamawesome_2446_1_ch508_file18_strand",
    "MINION02_4teamawesome_2446_1_ch508_file33_strand",
    "MINION02_4teamawesome_2446_1_ch508_file3_strand",
    "MINION02_4teamawesome_2446_1_ch50_file2_strand",
    "MINION02_4teamawesome_2446_1_ch511_file20_strand",
    "MINION02_4teamawesome_2446_1_ch54_file14_strand",
    "MINION02_4teamawesome_2446_1_ch73_file31_strand",
    "MINION02_4teamawesome_2446_1_ch73_file42_strand",
    "MINION02_4teamawesome_2446_1_ch86_file13_strand",
    "MINION02_4teamawesome_2446_1_ch86_file21_strand",
    "MINION02_4teamawesome_2446_1_ch86_file26_strand",
    "MINION02_4teamawesome_2446_1_ch86_file29_strand",
    "MINION02_4teamawesome_2446_1_ch86_file3_strand",
    "MINION02_4teamawesome_2446_1_ch96_file1_strand"
]


files = [
#    "MINION02_4teamawesome_2446_1_ch111_file14_strand",
#    "MINION02_4teamawesome_2446_1_ch111_file7_strand",
#    "MINION02_4teamawesome_2446_1_ch126_file3_strand",
#    "MINION02_4teamawesome_2446_1_ch149_file31_strand",
#    "MINION02_4teamawesome_2446_1_ch175_file29_strand",
#    "MINION02_4teamawesome_2446_1_ch175_file50_strand",
#    "MINION02_4teamawesome_2446_1_ch175_file82_strand",
    "MINION02_4teamawesome_2446_1_ch192_file24_strand",
#    "MINION02_4teamawesome_2446_1_ch202_file6_strand",
#    "MINION02_4teamawesome_2446_1_ch205_file73_strand",
#    "MINION02_4teamawesome_2446_1_ch208_file65_strand",
#    "MINION02_4teamawesome_2446_1_ch212_file46_strand",
#    "MINION02_4teamawesome_2446_1_ch222_file11_strand",
    "MINION02_4teamawesome_2446_1_ch222_file14_strand",
#    "MINION02_4teamawesome_2446_1_ch222_file5_strand",
    "MINION02_4teamawesome_2446_1_ch222_file9_strand",
    "MINION02_4teamawesome_2446_1_ch241_file5_strand",
    "MINION02_4teamawesome_2446_1_ch265_file4_strand",
    "MINION02_4teamawesome_2446_1_ch296_file3_strand",
#    "MINION02_4teamawesome_2446_1_ch301_file16_strand",
    "MINION02_4teamawesome_2446_1_ch303_file43_strand",
#    "MINION02_4teamawesome_2446_1_ch303_file54_strand",
#    "MINION02_4teamawesome_2446_1_ch308_file20_strand",
    "MINION02_4teamawesome_2446_1_ch312_file33_strand",
    "MINION02_4teamawesome_2446_1_ch319_file35_strand",
    "MINION02_4teamawesome_2446_1_ch319_file57_strand",
    "MINION02_4teamawesome_2446_1_ch319_file63_strand",
    "MINION02_4teamawesome_2446_1_ch320_file16_strand",
    "MINION02_4teamawesome_2446_1_ch36_file22_strand",
    "MINION02_4teamawesome_2446_1_ch370_file1_strand",
    "MINION02_4teamawesome_2446_1_ch378_file1_strand",
    "MINION02_4teamawesome_2446_1_ch384_file0_strand",
    "MINION02_4teamawesome_2446_1_ch394_file15_strand",
    "MINION02_4teamawesome_2446_1_ch394_file6_strand",
#    "MINION02_4teamawesome_2446_1_ch394_file78_strand",
#    "MINION02_4teamawesome_2446_1_ch400_file2_strand",
    "MINION02_4teamawesome_2446_1_ch400_file6_strand",
    "MINION02_4teamawesome_2446_1_ch401_file19_strand",
    "MINION02_4teamawesome_2446_1_ch401_file9_strand",
    "MINION02_4teamawesome_2446_1_ch418_file20_strand",
    "MINION02_4teamawesome_2446_1_ch422_file31_strand",
    "MINION02_4teamawesome_2446_1_ch422_file56_strand",
    "MINION02_4teamawesome_2446_1_ch430_file15_strand",
    "MINION02_4teamawesome_2446_1_ch430_file16_strand",
    "MINION02_4teamawesome_2446_1_ch430_file24_strand",
    "MINION02_4teamawesome_2446_1_ch430_file2_strand",
    "MINION02_4teamawesome_2446_1_ch459_file36_strand",
    "MINION02_4teamawesome_2446_1_ch459_file62_strand",
    "MINION02_4teamawesome_2446_1_ch475_file11_strand",
    "MINION02_4teamawesome_2446_1_ch508_file12_strand",
    "MINION02_4teamawesome_2446_1_ch508_file33_strand",
    "MINION02_4teamawesome_2446_1_ch508_file3_strand",
    "MINION02_4teamawesome_2446_1_ch73_file31_strand",
    "MINION02_4teamawesome_2446_1_ch86_file13_strand",
    "MINION02_4teamawesome_2446_1_ch96_file1_strand"
]

for fr in files:
    print fr
    f = h5py.File('/home/dspeyer/hackathon1-rw/alldata/downloads/pass/'+fr+'.fast5')
    seq=f['Analyses']['Basecall_2D_000']['BaseCalled_2D']['Fastq'].value.split('\n')[1]
    print '  querying...'

    try:
        with timeout(seconds=1200):
            handle=NCBIWWW.qblast('blastn', 'nt', seq,
                                  megablast=True,
                                  expect=1e-10,
                                  alignments=10,
                                  descriptions=10,
                                  hitlist_size=10,
                                  entrez_query='Tomato[organism]')
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
    print "  writing..."
    o=file('tomatoaligns/'+fr+'.align','w')
    for alignment in res.alignments:
        o.write(alignment.hit_def+'\n')
        o.write('Bases %d to %d (of %d) match bases %d to %d\n' % (alignment.hsps[0].query_start, alignment.hsps[0].query_end, len(seq), alignment.hsps[0].sbjct_start, alignment.hsps[0].sbjct_end))
        o.write(alignment.hsps[0].query)
        o.write('\n')
        o.write(alignment.hsps[0].match)
        o.write('\n')
        o.write(alignment.hsps[0].sbjct)
        o.write('\n')
    o.close()
