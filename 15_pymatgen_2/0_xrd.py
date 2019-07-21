
# This initializes the REST adaptor. Put your own API key in.
from pymatgen import MPRester, Element
from pymatgen.analysis.diffraction.xrd import XRDCalculator

a = MPRester("")

# Entries are the basic unit for thermodynamic and other analyses in pymatgen.
# This gets all entries belonging to the MnO2 material.
entry = a.get_entry_by_material_id("mp-18759", inc_structure=True,property_data=["material_id","energy", "energy_per_atom", "volume"])

#print(entry)

xrdc = XRDCalculator()
xrdc.get_plot(entry.structure).show()
