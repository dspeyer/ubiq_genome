#!/bin/sh

cd ~awesome
samtools faidx hg19.fa
cd ~/ubiq_genome/h2fq/rob-bwa-out
for i in *.sam;do samtools view -bS $i -o `echo $i | sed 's/sam/bam/'`;done
for i in *.bam; do bedtools bamtobed -i $i > `echo $i | sed 's/bam/bed/'`;done
for i in *.bed; do head -n 1 $i > $i.1;done
rm `wc -l *.bed.1 | grep '0 ' | awk '{print $2}'`
for i in *.bed.1; do bedtools getfasta -fi ~awesome/hg19.fa -bed $i
-fo `echo $i | sed 's/bed.1/ref.fa/'` -s; done
head -n 1 *.ref.fa | grep '(+)' -B 1 | grep = | awk '{print $2}' | sed
's/.ref.fa//' > poshitlist
for i in `ls *.bed.1 | sed 's/bed.1/sam/'`; do ../../extract_qseq.py  $i;done
