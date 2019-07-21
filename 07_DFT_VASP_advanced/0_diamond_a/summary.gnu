set output 'summary-a.png'
set terminal png
set title 'Total Energy'
set xlabel 'a'
set ylabel 'Energy'
set grid
plot 'summary.txt' with linespoints pointtype 5
