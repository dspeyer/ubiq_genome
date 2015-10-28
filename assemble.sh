#!/bin/sh

cat header.tex > final.tex
for i in `seq 11`; do
    if [ -e "ans${i}.tex" ]; then
	echo "\\section*{Problem $i}" >> final.tex
	cat ans${i}.tex >> final.tex
    fi
done
echo "\\end{document}" >> final.tex
