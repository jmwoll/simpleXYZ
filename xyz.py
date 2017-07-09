

def load_xyz(xyzfile=None, xyzstring=None):
    mol = []
    inp_str = None
    if xyzstring is None:
        with open(xyzfile, 'r') as fin:
            inp_str = fin.read()
    else:
        inp_str = xyzstring
    inp_str = inp_str.strip().replace('\t', ' ')
    while '  ' in inp_str:
        inp_str = inp_str.replace('  ', ' ')

    for i, lne in enumerate(inp_str.split('\n')):
        atm = lne.strip().split(' ')
        try:
            atm = (atm[0], float(atm[1]), float(atm[2]), float(atm[3]))
            mol.append(atm)
        except:
            if i not in [0,1]: log('skipping line:\n' + lne)
    return mol

def save_xyz(mol, xyzfile=None):
    xyz_str = "{}\n\n".format(len(mol))
    for atm in mol:
        xyz_str += "{} {} {} {}\n".format(*atm)
    if xyzfile is not None:
        with open(xyzfile, 'w') as fout:
            fout.write(xyz_str)
    return xyz_str
