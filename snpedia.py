#!/usr/bin/python

from wikitools import wiki, category, page

site = wiki.Wiki("http://bots.snpedia.com/api.php")

for line in file('snplist'):
    [chr, pos, snp, val, f, q, fi]=line.split('\t')
    if f=='0':
        continue
    try:
        pagehandle = page.Page(site,snp)
        snp_page = pagehandle.getWikiText()
        f = file('snpedia/%s.mw'%snp, 'w')
        f.write(snp_page)
        f.close()
        f = file('snpedia/%s.info'%snp, 'w')
        f.write('Read = %s\nLoc = %s:%s\nQuality = %s\nFile = %s\n' % (val, chr, pos, q, fi))
        f.close()
    except:
        pass
