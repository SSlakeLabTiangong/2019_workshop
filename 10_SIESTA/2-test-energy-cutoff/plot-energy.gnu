set term png size 1000,800 lw 4 enhanced font
datafile = "ek.dat"
set output "ek.png"
#set size 0.6,0.6
#set title ''
unset title
unset key
set xlabel 'Energy Cutoff'
set ylabel 'Total Energy'

plot datafile with linespoints linecolor 2 lw 1 pointtype 3 pointsize 3 
