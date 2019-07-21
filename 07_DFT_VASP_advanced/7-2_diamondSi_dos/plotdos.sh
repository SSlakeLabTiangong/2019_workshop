awk 'BEGIN{i=1} /dos>/,\
                /\/dos>/ \
                 {a[i]=$2 ; b[i]=$3 ; i=i+1} \
     END{for (j=12;j<i-5;j++) print a[j],b[j]}' vasprun.xml > dos.dat

ef=`awk '/efermi/ {print $3}' vasprun.xml`

cat >plotfile<<!
set term png
set output "dos.png"
set title 'Density of states'
set xlabel 'dos'
set ylabel 'energy'
set xrange [-10:10]
set grid
plot "dos.dat" using (\$1-$ef):(\$2) with linespoints pointtype 5
!

gnuplot -persist plotfile

rm dos.dat plotfile
