#!/usr/bin/python
import sys
import os
from collections import defaultdict
import matplotlib.pyplot as plt
from operator import itemgetter
import warnings


warnings.simplefilter("ignore")

def rr(readtype, path, failorpass, histname):
	onedict={}
	twodict={}
	for filename in os.listdir(path+"downloads/"+failorpass+"/"):
	    fn=path+"downloads/"+failorpass+"/"+filename
	    os.system("python dump5.py "+fn+" >thishere.txt")
	    f=open("thishere.txt").readlines()
	    prev=False
	    printed=False
	    td=0
            tp=0
	    cp=0
	    twod=0
	    temp=0
            comp=0
	    key=""
            for line in f:
	        line=line.strip()
		if prev:
		    if "Done." in line:
			line=line.split(',')
			key= str(line[0][:-3])
		    	prev=False
		    	printed=True
                if line=="[/Analyses/Hairpin_Split_000/Log]":
                    prev=True
		if twod==2:
		    td=len(line) 
		    twod=0
		if twod==1:
		    twod=2
		if line=="[/Analyses/Basecall_2D_000/BaseCalled_2D/Fastq]":
		    twod=1
		if temp==2:
                    tp=len(line)
		    temp=0
		if temp==1:
		    temp=2
		if line=="[/Analyses/Basecall_1D_000/BaseCalled_template/Fastq]":
		    temp=1
		if comp==2:
  	            cp=len(line)
		    comp=0
		if comp==1:
		   comp=2
		if line=="[/Analyses/Basecall_1D_000/BaseCalled_complement/Fastq]":
		    comp=1
	    od=tp+cp
            if od!=0:
		if key in onedict:
		    onedict[key]+=od
		else:
		    onedict[key]=od
	    if td!=0:
	        if key in twodict:
		    twodict[key]+=td
		else:
		    twodict[key]=td 
        onek=[]
        onev=[]
	hold=0
	subval=0
	prev19=False
        prev20=False
        for key in sorted(onedict):
            try:
                    val=int(onedict[key])
                    key=key.split()
                    key=int(key[1].replace(":",""))
            except IndexError:
                    print 'Skipping key "%s"'%key
                    continue
	    if key-1900>=0 and prev19 is False:
		subval=subval+40
	        prev19 = True
	    if key-2000>=0 and prev20 is False:
		subval=subval+40
	        prev20 = True
            if subval==0:
		subval=key-1
            key=key-subval
	    onek.append(key)
	    hold+=val
	    onev.append(hold)
        twok=[]
	twov=[]
	prev19=False
	prev20=False
	hold=0
	subval=0
	for key in sorted(twodict):
            try:
                    val=int(twodict[key])
                    key=key.split()
                    key=int(key[1].replace(":",""))
            except IndexError:
                    print 'Skipping key "%s"'%key
                    continue
	    if key-1900>=0 and prev19 is False:
		subval=subval+40
	        prev19 = True
	    if key-2000>=0 and prev20 is False:
		subval=subval+40
	        prev20 = True
            if subval==0:
		subval=key-1
            key=key-subval
	    twok.append(key)
	    hold+=val
	    twov.append(hold)

	plt.clf()
	plt.plot(onek,onev)
	plt.xlabel('Time (min)')
	plt.ylabel('Nucleotides')
	plt.title('%s %s' % ("1D", failorpass))
	plt.savefig(''+histname+'1D.png',format='png')

	plt.clf()
	plt.plot(twok,twov)
	plt.xlabel('Time (min)')
	plt.ylabel('Nucleotides')
	plt.title('%s %s' % ("2D", failorpass))
	plt.savefig(''+histname+'2D.png',format='png')
	

path=sys.argv[1]

rr("2D", path, "fail", "failcum")
print '1D and 2D failure plots generated'
rr("2D", path, "pass", "passcum")
print '1D and 2D pass plots generated'

