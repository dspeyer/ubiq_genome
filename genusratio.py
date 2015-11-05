from operator import itemgetter

def grat(sdic,ndic):
    totalvalue=0.0
    for key, value in sorted(sdic.items(), key=itemgetter(1), reverse=True):
	genlen=open('genomelen.txt')
	for line in genlen:
	    line=line.split()
	    if line[0].strip()==key:
		wholegen=float(line[1])*.1
		divval=value/wholegen
		multval=divval
		newval=0
		for num in range(1,(ndic[key])+1):
		    newval+=multval
  	        sdic[key]=newval
		totalvalue+=newval

    for key, value in sorted(sdic.items(), key=itemgetter(1), reverse=True):
	ratioval=float(value)/totalvalue
	sdic[key]=ratioval

    return sdic,totalvalue
