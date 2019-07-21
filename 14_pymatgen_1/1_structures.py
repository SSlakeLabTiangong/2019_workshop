
# This initializes the REST adaptor. Put your own API key in.
from pymatgen import MPRester
from pymatgen.analysis.phase_diagram import PhaseDiagram, PDPlotter
from pymatgen.io.vasp import Poscar

a = MPRester("")

# Entries are the basic unit for thermodynamic and other analyses in pymatgen.
# This gets all entries belonging to the mp-48 material.
entry = a.get_entry_by_material_id("mp-48", inc_structure=True,property_data=["material_id","energy", "energy_per_atom", "volume"])

#print(entry)

structure=entry.structure

#print(structure)

p= Poscar(structure)

print(p)

