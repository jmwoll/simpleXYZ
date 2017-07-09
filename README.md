
This project provides a very simplistic python library for reading
and writing .xyz molecule files, as defined in the code snippet below.
```
from simpleXYZ import xyz
mol = xyz.load_xyz(xyzfile="test.xyz")
print(mol)
# Output: [('C', 0.0, 0.0, 0.0), ('H', 1.0, 1.0, 1.0), ('H', 2.0, 2.0, 2.0), ('H', 3.0, 3.0, 3.0)]
mol = xyz.load_xyz(xyzstring="""4\nSimple xyz test file\nC 0 0 0\nH 1 1 1\nH 2 2 2\nH 3 3 3\n""")
print(mol)
# Output: [('C', 0.0, 0.0, 0.0), ('H', 1.0, 1.0, 1.0), ('H', 2.0, 2.0, 2.0), ('H', 3.0, 3.0, 3.0)]
xyzstring = xyz.save_xyz(mol, xyzfile="test.xyz")
print(xyzstring)
# Output:
4

C 0.0 0.0 0.0
H 1.0 1.0 1.0
H 2.0 2.0 2.0
H 3.0 3.0 3.0
```
