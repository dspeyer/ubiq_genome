#!/bin/sh

cat header.tex > final.tex
for i in `seq 11`; do
    echo "\\section*{Problem $i}" >> final.tex
    if [ -x "part${i}.py" ]; then
	./part${i}.py ~/hackathon1/downloads >> final.tex
    elif [ -x "part${i}.sh" ]; then
	./part${i}.sh ~/hackathon1/downloads >> final.tex
    fi
done
echo "\\end{document}" >> final.tex
