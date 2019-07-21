set term png size 1000,800 lw 1 enhanced font
datafile = "siesta.MDE"
set output "MD-E-T-P.png"
set multiplot layout 2, 2
set size 0.5,0.5
#set title ''
unset title
unset key
#set xrange [-3:3]

set origin 0, 0
set xlabel 'Time (fs)'
set ylabel 'Temperature (K)'
plot datafile u 1:2 with lines lw 1 

set origin 0.5, 0.5
set xlabel 'Time (fs)'
set ylabel 'Total Energy (eV)'
plot datafile u 1:4 with lines lw 1

set origin 0, 0.5
set xlabel 'Time (fs)'
set ylabel 'Pressure (kBar)'
plot datafile u 1:6 with lines lw 1

datafile2 = "bondlength.dat"
set origin 0.5, 0.0
set xrange [0:100]
set yrange [0.8:1.1]
set xlabel 'Time (fs)'
set ylabel 'Bond length'
plot datafile2 u 1:2 with lines lt 2 lw 2,\
     datafile2 u 1:3 with lines lt 5 lw 2

