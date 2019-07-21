#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 11:12:40 2019

@author: ken
"""
import os
#import matplotlib.pyplot as plt

#fig, ax = plt.subplots(1,1,sharex=False,sharey=False,figsize=(7,6))
def readFeimilevel(filename = 'siesta.EIG', sep = False):
  """
  return the Feimi Level read from systemLabel.EIG
  """
  eigFile = open(filename)
  line = eigFile.readline()
  EFermi = float(line.split()[0])
  return EFermi

fermilevel = readFeimilevel()
#declare the file you use
def readPDOS(filename):
    lines = open(filename).readlines()
    C5P=[]
    E=[]
    for line in lines:
        line = [j for j in line.split()]
        try:
            float(line[0])           
        except ValueError:
            continue
        else:
            E.append(float(line[0]))   
            C5P.append(float(line[1]))
    return E,C5P

dos = []
E = []
data = readPDOS('siesta.DOS')
E = data[0]
dos = data[1]

E = [(i-(fermilevel)) for i in E]

f = open('dos.dat','w')
for i in range(len(E)):
   line = '  %13.9f     %13.9f'% \
   (E[i],dos[i]) #here is some shift
   f.write(line+'\n')
   #print line

f.close()

#ax.set_xlabel('K mesh',fontsize=24)
#ax.set_ylabel('Total Energy',fontsize=24)
#SaveName = __file__.split('/')[-1].split('.')[0]
#filename = SaveName + '.jpg'
#plt.tight_layout()
#plt.savefig(filename,dpi=600)
