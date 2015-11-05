from operator import itemgetter
import matplotlib.pyplot as plt
import warnings


warnings.simplefilter("ignore")

def lilmaker(sdic):
    sol=0
    bab=0
    ovis=0
    bos=0
    wuch=0
    gong=0
    caps=0
    hom=0
    onc=0
    bis=0
    for key, value in sorted(sdic.items(), key=itemgetter(1), reverse=True):
        if key=="Solanum":
	    sol=value
        if key=="Ovis":
	    ovis=value
	if key=="Bos":
	    bos=value
	if key=="Babesia":
	    bab=value
        if key=="Wuchereria":
	    wuch=value
	if key=="Gonglylonema":
	    gong=value
	if key=="Capsicum":
	    caps=value
        if key=="Homo":
	    hom=value
	if key=="Onchocerca":
	    onc=value
	if key=="Bison":
	    bis=value

    labels = 'Solanum', 'Capsicum', 'Ovis', 'Bos', 'Homo', 'Bison', 'Babesia', 'Wuchereria', 'Gonglylonema', 'Onchocerca'
    sizes = [sol, caps, ovis, bos, hom, bis, bab, wuch, gong, onc]
    colors = ['yellowgreen', 'yellowgreen', 'lightcoral', 'lightcoral', 'lightcoral', 'lightcoral', 'lightskyblue', 'lightskyblue', 'lightskyblue', 'lightskyblue']
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    plt.savefig('genuspie.png')
    plt.clf()

def bigmaker(bdic):
    veg=0
    meat=0
    par=0
    for key, value in sorted(bdic.items(), key=itemgetter(1), reverse=True):
        if key=="Vegetables":
	    veg=value
        if key=="Meat":
	    meat=value
	if key=="Parasites":
	    par=value

    labels = 'Vegetables', 'Meat', 'Parasites'
    sizes = [veg, meat, par]
    colors = ['yellowgreen', 'lightcoral', 'lightskyblue']
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    plt.savefig('bigpie.png')
