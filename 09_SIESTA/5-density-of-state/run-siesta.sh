#!/bin/bash
#SBATCH -J siesta                   
#SBATCH -N 1                     
#SBATCH --ntasks-per-node=12
#SBATCH -p regular
#SBATCH -t 00:10:00
pwd | cat >> pwd.dat
#module load mpi/mpich/gcc/3.3
source /public/software/profile.d/compiler_gcc-4.8.4.sh
module load mpi/mvapich2/gnu/2.3b
module load apps/siesta/gnu/4.1-b4
EXEC=siesta
srun --mpi=pmi2 $EXEC < input.fdf > result

