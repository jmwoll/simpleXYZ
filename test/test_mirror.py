
from simpleXYZ import xyz
mol = xyz.load_xyz(xyzfile="test.xyz")
print(mol)
mol = [(atom_symbol,-atom_x,atom_y,atom_z) for (atom_symbol,atom_x, atom_y, atom_z) in mol]
print(mol)
xyzstring = xyz.save_xyz(mol,xyzfile="test_mirrored.xyz")
print(xyzstring)
