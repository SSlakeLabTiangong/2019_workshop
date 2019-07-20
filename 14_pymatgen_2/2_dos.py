from pymatgen.io.vasp import Vasprun, Element
from pymatgen.electronic_structure.plotter import DosPlotter

v = Vasprun('AgTe_dos/vasprun.xml')
cdos = v.complete_dos


element_dos = cdos.get_element_dos()
element_orbital = cdos.get_element_spd_dos(el=Element("Te"))

#print(cdos.pdos)

#px = cdos.get_site_orbital_dos(site=v.final_structure.sites[0],orbital=0)
#py = cdos.get_site_orbital_dos(site=v.final_structure.sites[0],orbital=2)
#pz = cdos.get_site_orbital_dos(site=v.final_structure.sites[0],orbital=1)


plotter = DosPlotter(zero_at_efermi=True)
plotter.add_dos_dict(element_dos)
#plotter.add_dos_dict(px)
#plotter.add_dos_dict(py)
#plotter.add_dos_dict(pz)

plotter.show(xlim=[-4, 4], ylim=[0, 10])