for i in decoy/*;do obabel $i/lig_equibind_corrected.sdf -O $i/lig_equibind_corrected.pdb;echo $i; done


cd ../
mkdir decoy_complex

for i in *;do cat ../../../../data/decoy_ligands/AACBYFOMUGHPDB-MRXNPFEDSA-N/AACBYFOMUGHPDB-MRXNPFEDSA-N_protein.pdb $i/lig_equibind_corrected.pdb > ../decoy_complex/complex_$i.pdb;done
