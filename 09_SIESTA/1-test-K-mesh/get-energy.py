#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 11:12:40 2019

@author: ken
"""
import os
#import matplotlib.pyplot as plt

#fig, ax = plt.subplots(1,1,sharex=False,sharey=False,figsize=(7,6))
ek = []
x = range(2,9,1)
for i in x:
    tmp = str(i)
    os.chdir(tmp)
    command = 'grep "Etot" result | tail -1 | awk \'{printf "%12.6f \\n", $4}\''
    tmp = os.popen(command).readlines()[0]
    ektmp = float(tmp)
    ek.append(ektmp)
    os.chdir('../')

#ax.plot(x,ek,'--o',color='r',markerfacecolor='w',markersize=10,lw=3,label=r'')

f = open('ek.dat','w')
for i in range(len(x)):
   line = '  %13.9f     %13.9f'% \
   (x[i],ek[i]) #here is some shift
   f.write(line+'\n')
   #print line

f.close()

#ax.set_xlabel('K mesh',fontsize=24)
#ax.set_ylabel('Total Energy',fontsize=24)
#SaveName = __file__.split('/')[-1].split('.')[0]
#filename = SaveName + '.jpg'
#plt.tight_layout()
#plt.savefig(filename,dpi=600)
