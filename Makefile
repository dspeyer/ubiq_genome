DIR=~/hackathon1-rw/alldata/

ans1_auto.tex: q1.py
	./q1.py ${DIR} | sed 's/.$$/&\\\\/g' |sed 's/_/\\_/g' > ans1_auto.tex

ans2_auto.tex: q2.py
	./q2.py ${DIR}/downloads/ > ans2_auto.tex

cumnucfail.png: q3.py
	./q3.py ${DIR}

q6hf.png: q6.py
	./q6.py ${DIR}

ans7_auto.tex: q7.py
	./q7.py ${DIR} | sed 's/.$$/&\\\\/g' |sed 's/_/\\_/g' > ans7_auto.tex

q8.png: q8.py
	./q8.py ${DIR}

q9.png: q9.py
	./q9.py ${DIR}

ans10_auto.tex: q10.py
	./q10.py ${DIR} | sed 's/$$/\\\\/g' | sed 's/%/\\%/g' > ans10_auto.tex

ans11_auto.tex: q11.py
	./q11.py ${DIR}/downloads/ > ans11_auto.tex

final.tex: assemble.sh header.tex ans1_auto.tex ans2_auto.tex ans3_manual.tex ans6_manual.tex ans7_auto.tex ans8_manual.tex ans9_manual.tex ans10_auto.tex ans11_auto.tex
	./assemble.sh

final.pdf: final.tex cumnucfail.png q6hf.png q8.png q9.png
	pdflatex final.tex
