from pymatgen.io.vasp import Vasprun, Element
from pymatgen.electronic_structure.plotter import DosPlotter

v = Vasprun('AgTe_dos/vasprun.xml')
cdos = v.complete_dos
element_dos = cdos.get_element_dos()
element_orbital = cdos.get_element_spd_dos(el=Element("Ag"))

plotter = DosPlotter()
plotter.add_dos_dict(element_orbital)
plotter.show(xlim=[-4, 4], ylim=[0, 10])