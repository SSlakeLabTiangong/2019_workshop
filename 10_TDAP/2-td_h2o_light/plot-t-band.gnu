set term png size 1000,800 lw 4 enhanced font
datafile = "t-band.dat"
set output "t-band.png"
#set size 0.6,0.6
#set title ''
unset title
unset key
set xrange [0:50]
set xlabel 'Time (fs)'
set ylabel 'Energy (ev)'

plot for [i=2:10] datafile using 1:i with lines lw 1 lt i
