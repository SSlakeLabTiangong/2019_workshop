
# This initializes the REST adaptor. Put your own API key in.
from pymatgen import MPRester
from pymatgen.analysis.phase_diagram import PhaseDiagram, PDPlotter
from pymatgen.io.vasp import Poscar

a = MPRester("")

# Entries are the basic unit for thermodynamic and other analyses in pymatgen.
# This gets all entries belonging to the Ca-C-O system.
entries = a.get_entries_in_chemsys(["Ca","C","O"], inc_structure=True,property_data=["material_id","energy", "energy_per_atom", "volume"])

print(len(entries))

for entry in entries:
    #print(entry)
    print(entry.composition.formula)


#structure=entry.structure

#p=Poscar(structure)

#print(p)

# With entries, you can do many sophisticated analyses,
# like creating phase diagrams.
pd = PhaseDiagram(entries)
plotter = PDPlotter(pd)
plotter.show()

