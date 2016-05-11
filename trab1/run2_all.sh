#!/bin/sh

for i in datasets/N*.bz2 datasets/n*.bz2; do
    echo -n "$i"
    for j in 0 1 2 3 4 5 6 7 8 9; do
       echo -n " $j"
       python2.7 run2.py ${i} > ${i}.output_2_${j}
       mv ${i}.output_2_${j} results/
    done
    echo " done"
done
