set output 'summary-k.png'
set terminal png
set title 'Total Energy'
set xlabel 'Nk'
set ylabel 'Energy'
set grid
plot 'summary.txt' with linespoints pointtype 5
