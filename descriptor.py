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

import math
# see https://en.wikipedia.org/wiki/Atomic_radii_of_the_elements_(data_page)
vdw_radii = {'H': 120, 'He': 140, 'Li': 182, 'Be': 153, 'B': 192, 'C': 170, 'N': 155, 'O': 152, 'F': 147, 'Ne': 154, 'Na': 227, 'Mg': 173,
'Al': 184, 'Si': 210, 'P': 180, 'S': 180, 'Cl': 175, 'Ar': 188, 'K': 275, 'Ca': 231, 'Sc': 211, 'Ti': 0, 'V': 0, 'Cr': 0, 'Mn': 0,
'Fe': 0, 'Co': 0, 'Ni': 163,
'Cu': 140, 'Zn': 139, 'Ga': 187, 'Ge': 211, 'As': 185, 'Se': 190, 'Br': 185, 'Kr': 202, 'Rb': 303, 'Sr': 249, 'Y': 0,
'Zr': 0, 'Nb': 0, 'Mo': 0, 'Tc': 0, 'Ru': 0,
'Rh': 0, 'Pd': 163, 'Ag': 172, 'Cd': 158, 'In': 193, 'Sn': 217, 'Sb': 206, 'Te': 206, 'I': 198, 'Xe': 216, 'Cs': 343, 'Ba': 268,
'La': 0, 'Ce': 0, 'Pr': 0,
'Nd': 0, 'Pm': 0, 'Sm': 0, 'Eu': 0, 'Gd': 0, 'Tb': 0, 'Dy': 0, 'Ho': 0, 'Er': 0, 'Tm': 0, 'Yb': 0, 'Lu': 0, 'Hf': 0,
'Ta': 0, 'W': 0, 'Re': 0, 'Os': 0,
'Ir': 0, 'Pt': 175, 'Au': 166, 'Hg': 155, 'Tl': 196, 'Pb': 202, 'Bi': 207, 'Po': 197, 'At': 202, 'Rn': 220, 'Fr': 348, 'Ra': 283,
'Ac': 0, 'Th': 0, 'Pa': 0, 'U': 186,
'Np': 0, 'Pu': 0, 'Am': 0, 'Cm': 0, 'Bk': 0, 'Cf': 0, 'Es': 0, 'Fm': 0, 'Md': 0, 'No': 0, 'Lr': 0, 'Rf': 0, 'Db': 0,
'Sg': 0, 'Bh': 0, 'Hs': 0, 'Mt': 0, 'Ds': 0,
'Rg': 0, 'Cn': 0, 'Nh': 0, 'Fl': 0, 'Mc': 0, 'Lv': 0, 'Ts': 0, 'Og': 0}


def to_center(mol):
    cx,cy,cz = center_of_geometry(mol)
    c_mol = [ ]
    for atm in mol:
        c_mol.append((atm[0],atm[1]-cx,atm[2]-cy,atm[3]-cz))
    return c_mol



def vdw_radius_element(element):
    return vdw_radii[element[0].upper()+element[1:].lower()] / 100.0 # in Angstrom



def vdw_volume_molecule(molecule):
    return 4 / 3.0 * math.pi * sum([vdw_radius_element(atom[0])**3 for atom in molecule])


def center_of_geometry(molecule):
    x,y,z = ( sum([atom[1] for atom in molecule]), sum([atom[2] for atom in molecule]),
        sum([atom[3] for atom in molecule]) )
    lm = float(len(molecule))
    return (x/lm,y/lm,z/lm)

def smallest_sphere_radius_around_molecule(molecule, increment=0.05):
    center = center_of_geometry(molecule)
    r = 0.0
    while any([atom[1]**2 + atom[2]**2 + atom[3]**2 > r**2 for atom in molecule]):
        r += increment
    return r

def anisotropy_vector(molecule):
    cx,cy,cz=center_of_geometry(molecule)
    atoms = [(atom[0],atom[1]-cx,atom[2]-cy,atom[3]-cz) for atom in molecule]
    ax,ay,az=( sum([atom[1] for atom in atoms]), sum([atom[2] for atom in atoms]),
        sum([atom[3] for atom in atoms]) )

    return ax, ay, az

def anisotropy_vector_length(molecule):
    av = anisotropy_vector(molecule)
    return math.sqrt(av[0]**2 + av[1]**2 + av[2]**2)
