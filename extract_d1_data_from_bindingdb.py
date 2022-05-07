import pandas as pd
d1_uniprot_id = "P21728"

data = "./heavy_data/BindingDB_All_2022m4.tsv.zip"
df = pd.read_csv(data, compression="zip", sep="\t", usecols=["BindingDB Reactant_set_id", "Ligand SMILES","Ligand InChI", "Ligand InChI Key",
                    "BindingDB MonomerID","BindingDB Ligand Name", "Target Name Assigned by Curator or DataSource", 
                    "Target Source Organism According to Curator or DataSource", "Ki (nM)", "IC50 (nM)","Kd (nM)", "EC50 (nM)",
                    "Curation/DataSource", "UniProt (SwissProt) Primary ID of Target Chain", 
                    "UniProt (SwissProt) Secondary ID(s) of Target Chain", "Article DOI", "Patent Number", 
                    "Authors", "Institution"])
df = df[df["UniProt (SwissProt) Primary ID of Target Chain"] == d1_uniprot_id]
df.to_csv("heavy_data/d1_binding_db_data.tsv", index=False, sep="\t")
df["Ligand SMILES"].to_csv("heavy_data/d1_binding_db_smiles.tsv", index=False, sep="\t")
#print(df["UniProt (SwissProt) Primary ID of Target Chain"])
