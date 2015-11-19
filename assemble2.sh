#!/bin/sh

cat header.tex | sed 's/Hackathon 1/Hackathon2/' | grep -v Anne > final2.tex
for i in 1 2 3 6 7; do
    if [ $i -eq 3 -o $i -eq 6 ]; then
	echo '\\newpage' >> final2.tex
    fi
    if [ $i -lt 4 ]; then
	echo "\\section*{Problem $i}" >> final2.tex
    else
	echo "\\section*{Problem `expr $i - 2`}" >> final2.tex
    fi
    if [ -e "ans${i}_manual.tex" ]; then
	cat ans${i}_manual.tex >> final2.tex
    fi
    if [ -e "ans${i}_auto.tex" ]; then
	cat ans${i}_auto.tex >> final2.tex
    fi
done
for i in 6 7 8; do
    echo "\\section*{Problem $i}" >> final2.tex
    if [ -e "ans2_${i}_manual.tex" ]; then
	cat ans2_${i}_manual.tex >> final2.tex
    fi
    if [ -e "ans2_${i}_auto.tex" ]; then
	cat ans2_${i}_auto.tex >> final2.tex
    fi
done

echo "\\end{document}" >> final2.tex
