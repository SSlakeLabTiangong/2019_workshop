from pymatgen.io.vasp.outputs import Vasprun
from pymatgen.electronic_structure.plotter import DosPlotter
from collections import OrderedDict

vaspout = Vasprun("vasprun.xml")

dos = vaspout.complete_dos

all_dos = OrderedDict()
all_dos["Total"] = dos

plt = DosPlotter()
plt.add_dos_dict(all_dos)
plt = plt.get_plot(xlim=[-10,10],ylim=[0,1.5])
plt.savefig('dos.pdf')

