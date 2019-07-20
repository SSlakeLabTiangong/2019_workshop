
# This initializes the REST adaptor. Put your own API key in.
from pymatgen import MPRester, Element
from pymatgen.analysis.phase_diagram import PhaseDiagram, PDPlotter
from pymatgen.io.vasp import Poscar

a = MPRester("")

# Entries are the basic unit for thermodynamic and other analyses in pymatgen.
# This gets all entries belonging to the MnO2 material.
entry = a.get_entry_by_material_id("mp-18759", inc_structure=True,property_data=["material_id","energy", "energy_per_atom", "volume"])

#print(entry)

structure=entry.structure

#print(structure)

lattice = structure.lattice
#print(lattice)
print(lattice.volume)

sites = structure.sites

for site in sites:
    print(site)



structure.add_oxidation_state_by_guess()
print(structure)

structure.remove_oxidation_states()
print(structure)


structure.replace_species({Element("Mn"): Element("Ti")})
print(structure)
