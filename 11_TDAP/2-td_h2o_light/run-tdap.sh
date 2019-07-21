#!/bin/bash
#SBATCH -J tdap                   
#SBATCH -N 1                     
#SBATCH --ntasks-per-node=12
#SBATCH -p regular
#SBATCH -t 00:30:00
pwd | cat >> pwd.dat
#module load mpi/mpich/gcc/3.3
source /public/software/profile.d/compiler_gcc-4.8.4.sh
module load mpi/mvapich2/gnu/2.3b
module load apps/TDAP/2.1.0/mvapich
EXEC=tdap
srun --mpi=pmi2 $EXEC < input.fdf > result

