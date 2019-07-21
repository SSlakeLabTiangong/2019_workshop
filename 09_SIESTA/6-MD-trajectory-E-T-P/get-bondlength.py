#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 16:27:45 2018

@author: ken
"""
import numpy as np
import os

nostep = os.popen('grep "MD.FinalTimeStep" input.fdf').readline().split()[1]
nostep = int(nostep)
timestep = os.popen('grep "MD.LengthTimeStep" input.fdf').readline().split()[1]
timestep = float(timestep)
if os.path.exists('input.fdf'):  
   #get lattice vectors
   lines=os.popen('grep -A 4 "block LatticeVectors" input.fdf').readlines()
   vector1=[float(i) for i in lines[1].split()]
   vector2=[float(i) for i in lines[2].split()]
   vector3=[float(i) for i in lines[3].split()]
   vector=[vector1,vector2,vector3] 
   #calculate vectorlength
   #vectorl=[]
   #for j in 0,1,2:
   #    tmp=0
   #    for i in range(0,3):         
   #      tmp += pow(vector[j][i],2)
   #    tmp=pow(tmp,1.0/2)
   #    vectorl.append(tmp)
   #print vectorl
#get atoms' coordinate
if os.path.exists('siesta.MD_CAR'):
  coor1=[]
  coor2=[]
  coor3=[]  
  lines = open('siesta.MD_CAR').readlines()  
  for i in range(nostep):
     j = [8+i*10,9+i*10,10+i*10]    
     coorx = float(lines[j[0]-1].split()[0])
     coory = float(lines[j[0]-1].split()[1])
     coorz = float(lines[j[0]-1].split()[2])
     coor1.append([coorx, coory, coorz]) 

     coorx = float(lines[j[1]-1].split()[0])
     coory = float(lines[j[1]-1].split()[1])
     coorz = float(lines[j[1]-1].split()[2])
     coor2.append([coorx, coory, coorz])

     coorx = float(lines[j[2]-1].split()[0])
     coory = float(lines[j[2]-1].split()[1])
     coorz = float(lines[j[2]-1].split()[2])
     coor3.append([coorx, coory, coorz])
  #print len(coor1)
#coorodinate change
coor1new = coor1
coor2new = coor2  
coor3new = coor3
for i in np.arange(0,len(coor1)):
    for j in 0,1,2:    
        coor1new[i][j] = coor1[i][0]*vector[0][j]+coor1[i][1]*vector[1][j]+coor1[i][2]*vector[2][j] 
        coor2new[i][j] = coor2[i][0]*vector[0][j]+coor2[i][1]*vector[1][j]+coor2[i][2]*vector[2][j]
        coor3new[i][j] = coor3[i][0]*vector[0][j]+coor3[i][1]*vector[1][j]+coor3[i][2]*vector[2][j]
coor1 = coor1new
coor2 = coor2new
coor3 = coor3new
#calculate bonds
#H-O
bondsl=[[],[],[]]
for i in np.arange(0,len(coor1)):
    tmp = 0
    for j in 0,1,2:
        tmp += (coor1[i][j]-coor3[i][j])**2
    tmp=pow(tmp,1.0/2)
    bondsl[0].append(tmp)
#print bondsl[0]

for i in np.arange(0,len(coor1)):
    tmp = 0
    for j in 0,1,2:
        tmp += (coor2[i][j]-coor3[i][j])**2
    tmp=pow(tmp,1.0/2)
    bondsl[1].append(tmp)
#print len(bondsl[1])
for i in np.arange(0,len(coor1)):
    tmp = 0
    for j in 0,1,2:
        tmp += (coor1[i][j]-coor2[i][j])**2
    tmp=pow(tmp,1.0/2)
    bondsl[2].append(tmp)

time = timestep*np.arange(0,nostep)
f = open('bondlength.dat','w')
for i in range(len(time)):
   line = '  %d     %13.9f    %13.9f'% \
   (time[i],bondsl[0][i],bondsl[1][i]) #here is some shift
   f.write(line+'\n')
   #print line

f.close()

