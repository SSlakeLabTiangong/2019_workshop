set term png size 1000,800 lw 4 enhanced font
datafile = "dos.dat"
set output "dos.png"
#set size 0.6,0.6
#set title ''
unset title
unset key
set xrange [-3:3]
set xlabel 'Energy (eV)'
set ylabel 'Density Of States'

plot datafile  with lines lw 1 
