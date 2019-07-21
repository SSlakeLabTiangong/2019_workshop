
from pymatgen.electronic_structure.plotter import BSPlotter, BSPlotterProjected
from pymatgen.io.vasp import Vasprun, BandStructure

v = Vasprun("AgTe_bs/vasprun.xml")
bands = v.get_band_structure(kpoints_filename="AgTe_bs/KPOINTS",line_mode=True)

print(bands.get_band_gap())


plt = BSPlotter(bands)
#plt.plot_brillouin()

plt.get_plot(zero_to_efermi=True,vbm_cbm_marker=True,ylim=(-3,3)).show()
#plt.get_plot(zero_to_efermi=True,vbm_cbm_marker=True,ylim=(-2.2,0.5)).savefig(fname="bs.eps",img_format="eps")



