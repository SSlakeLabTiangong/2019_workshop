from pymatgen.io.vasp.inputs import Kpoints
from pymatgen.core import Structure
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
from pymatgen.symmetry.bandstructure import HighSymmKpath

structure = Structure.from_file("Si_mp-149_primitive.cif")
spg_analy =SpacegroupAnalyzer(structure)
primitive_standard_structure=spg_analy.get_primitive_standard_structure(international_monoclinic=False)
primitive_standard_structure.to(fmt="poscar", filename="primitive_standard_structure_POSCAR")
kpath = HighSymmKpath(primitive_standard_structure)
kpts = Kpoints.automatic_linemode(divisions=40,ibz=kpath)
kpts.write_file("KPOINTS")
print(kpts)