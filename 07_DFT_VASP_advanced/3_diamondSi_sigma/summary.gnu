set output 'summary-sigma.png'
set terminal png
set title 'Total Energy'
set xlabel 'sigma'
set ylabel 'Energy'
set grid
plot 'summary.txt' with linespoints pointtype 5
