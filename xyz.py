# Copyright (C) 2017  Jan Wollschläger <jmw.tau@gmail.com>
# This file is part of simpleXYZ.
#
# Tau is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

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
