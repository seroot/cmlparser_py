def get_atoms(atomList, i):
   singleAtom = str(atomList[i].attrib)
   singleAtomSplit = singleAtom.split()
   return singleAtomSplit

def object_list(atoms):
   x_val = atoms[1].replace(",","").replace("'","")
   y_val = atoms[3].replace(",","").replace("'","")
   elem = atoms[5].replace(",","").replace("'","")
   atom_id = atoms[7].replace(",","").replace("'","")
   z_val = atoms[9].replace("}","").replace("'","")
   aList = [atom_id,elem,x_val,y_val,z_val]
   return aList

def bond_list(bonds):
   bond_type = bonds[4].replace("}","").replace("'","")
   bond_master = bonds[1].replace(",","").replace("'","")
   bond_slave = bonds[2].replace(",","").replace("'","")
   bList = [bond_type,bond_master,bond_slave]
   return bList

def get_bonds(bondList, i):
   singleBond = str(bondList[i].attrib)
   singleBondSplit = singleBond.split()
   return singleBondSplit

#def gen_alist:
