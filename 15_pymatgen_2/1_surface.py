# This initializes the REST adaptor. Put your own API key in.
from pymatgen import MPRester
from pymatgen.core.surface import generate_all_slabs
from pymatgen.io.vasp import Poscar

a = MPRester("")

# Entries are the basic unit for thermodynamic and other analyses in pymatgen.
# This gets all entries belonging to the Fe material.
entry = a.get_entry_by_material_id("mp-13", inc_structure=True,
                                   property_data=["material_id", "energy", "energy_per_atom", "volume"])

slabs = generate_all_slabs(entry.structure, 1, 4, 10)

print(len(slabs))

print(slabs[0])

pos = Poscar(slabs[0])

pos.write_file(filename="POSCAR_fe_111")