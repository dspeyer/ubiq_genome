#!/bin/sh

cat header.tex > final.tex
for i in `seq 11`; do
    echo "\\section*{Problem $i}" >> final.tex
    if [ -e "ans${i}_manual.tex" ]; then
	cat ans${i}_manual.tex >> final.tex
    fi
    if [ -e "ans${i}_auto.tex" ]; then
	cat ans${i}_auto.tex >> final.tex
    fi
done
echo "\\end{document}" >> final.tex
