final.tex: assemble.sh header.tex part2.py part11.py
	./assemble.sh

final.dvi: final.tex
	latex final.tex

final.pdf: final.dvi
	dvipdf final.dvi
