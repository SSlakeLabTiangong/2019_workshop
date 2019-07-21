#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 16:22:49 2019

@author: ken
"""

import numpy as np
import os

nostep = os.popen('grep "MD.FinalTimeStep" input.fdf').readline().split()[1]
nostep = int(nostep)
timestep = os.popen('grep "MD.LengthTimeStep" input.fdf').readline().split()[1]
timestep = float(timestep)

command = 'grep "TDAP : Energy  :" result'
lines = os.popen(command).readlines()

energy = []
for line in lines:
    tmp = line.split()[4:]
    tmp = [float(i) for i in tmp]
    energy.append(tmp)
    
energy = np.array(energy)
print energy
time = timestep*np.arange(0,nostep)
f = open('t-band.dat','w')
for i in range(energy.shape[0]):
    tmpline = []
    tmpline.append(str(time[i])+'  ')
    for j in range(energy.shape[1]):
        tmpline.append(str(energy[i][j])+'  ')
    tmpline.append('\n')
    f.writelines(tmpline)
   #print line
f.close()
