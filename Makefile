DIR=~/hackathon1-rw/alldata/

ans1.tex: q1.py
	./q1.py ${DIR} > ans1.tex

ans2.tex: q2.py
	./q2.py ${DIR}/downloads/ > ans2.tex

ans6.tex: q6.py
	./q6.py ${DIR} > ans6.tex

ans7.tex: q7.py
	./q7.py ${DIR} > ans7.tex

ans10.tex: q10.py
	./q10.py ${DIR} > ans10.tex

ans11.tex: q11.py
	./q11.py ${DIR}/downloads/ > ans11.tex

final.tex: assemble.sh header.tex ans1.tex ans2.tex ans6.tex ans7.tex ans10.tex ans11.tex
	./assemble.sh

final.dvi: final.tex
	latex final.tex

final.pdf: final.dvi
	dvipdf final.dvi
