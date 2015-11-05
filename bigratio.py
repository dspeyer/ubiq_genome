from operator import itemgetter

def brat(sdic):
    bdic={}
    for key, value in sorted(sdic.items(), key=itemgetter(1), reverse=True):
	genlen=open('gengrouping.txt')
	for line in genlen:
	    line=line.split(',')
	    for genus in line:
	    	if genus.strip()==key:
		    if line[0] in bdic:
			bdic[line[0]]+=value
		    else:
 			bdic[line[0]]=value

    for key, value in sorted(bdic.items(), key=itemgetter(1), reverse=True):
	ratioval=float(value)/1.0
	bdic[key]=ratioval
    return bdic
