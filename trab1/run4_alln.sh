#!/bin/sh

cd datasets
for i in n*.bz2; do
    echo -n "$i"
    for j in 0 1 2 3 4 5 6 7 8 9; do
       echo -n " $j"
       [ -f ../results/${i}.output_4_${j} ] && continue
       python2.7 ../run4.py ${i} > ${i}.output_4_${j}
       mv ${i}.output_4_${j} ../results/
    done
    echo " done"
done
