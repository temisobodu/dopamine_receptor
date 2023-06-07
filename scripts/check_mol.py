from rdkit import Chem
from pathlib import Path
import sys
ligand_dir = sys.argv[1]
list_of_ligands = Path(ligand_dir).glob('*/*.sdf')
for ligand in list_of_ligands:
    try:

        mols = [i for i in Chem.SDMolSupplier(str(ligand))]
        if mols == [None]:
            print(ligand)
    except OSError:
        print(ligand)
    
