DIR=~/hackathon1-rw/alldata/

${DIR}/downloads/fail/has2d: splitfails.py
	./splitfails.py ${DIR}/downloads/fail/

ans1_auto.tex: group4_report1_question1.py
	./group4_report1_question1.py ${DIR} | sed 's/.$$/&\\\\/g' |sed 's/_/\\_/g' > ans1_auto.tex

ans2_auto.tex: group4_report1_question2.py
	./group4_report1_question2.py ${DIR}/downloads/ > ans2_auto.tex

cumnucfail.png: group4_report1_question3.py ${DIR}/downloads/fail/has2d
	./group4_report1_question3.py ${DIR}

ans4_auto.tex: group4_report1_question4.py
	./group4_report1_question4.py ${DIR} > ans4_auto.tex

ans5_auto.tex: group4_report1_question5.py
	./group4_report1_question5.py ${DIR} > ans5_auto.tex

histallfail.png: group4_report1_question6.py
	./group4_report1_question6.py ${DIR}

ans7_auto.tex: group4_report1_question7.py
	./group4_report1_question7.py ${DIR} | sed 's/.$$/&\\\\/g' |sed 's/_/\\_/g' > ans7_auto.tex

q8.png: group4_report1_question8.py
	./group4_report1_question8.py ${DIR}

q9.png: group4_report1_question9.py ${DIR}/downloads/fail/has2d
	./group4_report1_question9.py ${DIR}

ans10_auto.tex: group4_report1_question10.py ${DIR}/downloads/fail/has2d
	./group4_report1_question10.py ${DIR} | sed 's/$$/\\\\/g' | sed 's/%/\\%/g' > ans10_auto.tex

ans11_auto.tex: group4_report1_question11.py
	./group4_report1_question11.py ${DIR}/downloads/ > ans11_auto.tex

final.tex: assemble.sh header.tex ans1_auto.tex ans2_auto.tex ans2_manual.tex ans3_manual.tex ans4_auto.tex ans4_manual.tex ans5_auto.tex ans6_manual.tex ans7_auto.tex ans8_manual.tex ans9_manual.tex ans10_auto.tex ans11_auto.tex
	./assemble.sh

final.pdf: final.tex cumnucfail.png histallfail.png q8.png q9.png
	pdflatex final.tex
