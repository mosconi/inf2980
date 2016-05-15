#!/bin/sh

cd datasets
for i in N-usa79.bz2 N-tiw56r72.bz2 N-tiw56r67.bz2 N-tiw56r66.bz2 N-tiw56r58.bz2 N-tiw56r54.bz2 N-tiw56n72.bz2 N-tiw56n67.bz2 N-tiw56n66.bz2 N-tiw56n62.bz2 N-tiw56n58.bz2 N-tiw56n54.bz2 N-t75u11xx.bz2 N-t75n11xx.bz2 N-t75k11xx.bz2 N-t75i11xx.bz2 N-t75e11xx.bz2 N-t75d11xx.bz2 N-t74d11xx.bz2 N-t70x11xx.bz2 N-t70w11xx.bz2 N-t70u11xx.bz2 N-t70n11xx.bz2 N-t70l11xx.bz2 N-t70k11xx.bz2 N-t70i11xx.bz2 N-t70f11xx.bz2 N-t70d11xxb.bz2 N-t70d11xx.bz2 N-t70b11xx.bz2 N-t69r11xx.bz2 N-t65w11xx.bz2 N-t65n11xx.bz2 N-t65l11xx.bz2 N-t65i11xx.bz2 N-t65f11xx.bz2 N-t65d11xx.bz2 N-t65b11xx.bz2 N-t59n11xx.bz2 N-t59i11xx.bz2 N-t59f11xx.bz2 N-t59d11xx.bz2 N-t59b11xx.bz2 N-stabu75.bz2 N-stabu74.bz2 N-stabu70.bz2 N-be75tot.bz2 N-be75oi.bz2 N-be75np.bz2 N-be75eec.bz2 ; do
    echo -n "$i"
    for j in 0 1 2 3 4 5 6 7 8 9; do
       echo -n " $j"
       [ -f ../results/${i}.output_2_${j} ] && continue
       python2.7 ../run2.py ${i} > ${i}.output_2_${j}
       mv ${i}.output_2_${j} ../results/
    done
    echo " done"
done

