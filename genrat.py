from operator import itemgetter

def grat(sdic,ndic):
    totalvalue=0.0
    for key, value in sorted(sdic.items(), key=itemgetter(1), reverse=True):
	totalvalue+=value

    for key, value in sorted(sdic.items(), key=itemgetter(1), reverse=True):
	ratioval=float(value)/totalvalue
	sdic[key]=ratioval

    return sdic,totalvalue
