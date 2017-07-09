
from simpleXYZ import xyz
mol = xyz.load_xyz(xyzfile="test.xyz")
print(mol)
mol = xyz.load_xyz(xyzstring="""4\nSimple xyz test file\nC 0 0 0\nH 1 1 1\nH 2 2 2\nH 3 3 3\n""")
print(mol)
xyzstring = xyz.save_xyz(mol, xyzfile="test.xyz")
print(xyzstring)
