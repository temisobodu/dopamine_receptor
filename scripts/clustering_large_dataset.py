from rdkit import Chem
from rdkit import DataStructs
from rdkit.Chem import Draw
from rdkit.Chem.Draw import IPythonConsole
from rdkit.Chem import rdDepictor, rdMolDescriptors
import time
import argparse
import rdkit
from rdkit.Chem import rdMolDescriptors
from rdkit.SimDivFilters import rdSimDivPickers
import pandas as pd
rdDepictor.SetPreferCoordGen(True)
print(rdkit.__version__)


def get_clustered_molecules(lst_of_smiles):

    ms = [x for x in Chem.SmilesMolSupplier(lst_of_smiles) if x is not None]
    fps = [rdMolDescriptors.GetMorganFingerprintAsBitVect(m,2,2048) for m in ms]

    lp = rdSimDivPickers.LeaderPicker()
    thresh = 0.3 # <- minimum distance between cluster centroids
    picks = lp.LazyBitVectorPick(fps,len(fps),thresh)

    return pd.DataFrame([[Chem.MolToSmiles(ms[x]),Chem.inchi.MolToInchiKey(ms[x])]  for x in picks], columns=["smiles", "inchikey"])

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Compound clustering algorithm based on similarity")
    parser.add_argument("--smiles_file", help="smiles file")
    parser.add_argument("--output_tsv", help="smiles file")
    args = parser.parse_args()

    get_clustered_molecules(args.smiles_file).to_csv(args.output_tsv, index=False, sep="\t")
