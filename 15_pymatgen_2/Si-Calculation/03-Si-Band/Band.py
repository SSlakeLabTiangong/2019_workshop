# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 16:23:21 2018

@author: hxjia
"""
import pymatgen
from pymatgen.io.vasp.outputs import Vasprun
from pymatgen.electronic_structure.plotter import BSPlotter

vaspout = Vasprun("vasprun.xml")
bandstr = vaspout.get_band_structure(line_mode=True)
#Force the band structure to be considered as a run along symmetry lines

print(bandstr.get_band_gap())

plt = BSPlotter(bandstr).get_plot(ylim=[-4,4])
plt.yticks(range(-4,5))
plt.savefig("band.pdf")
