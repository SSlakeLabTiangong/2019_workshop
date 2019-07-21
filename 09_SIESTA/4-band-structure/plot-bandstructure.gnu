set term png size 1000,800 lw 4 enhanced font
datafile = "bandstructure"
set output "band.png"
#set size 0.6,0.6
#set title ''
unset title
unset key
set yrange [-3:3]
set xlabel 'K point'
set ylabel 'Energy (eV)'

plot datafile with lines lw 1 
