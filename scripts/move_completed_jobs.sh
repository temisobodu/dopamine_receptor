mkdir ../../../decoy # change to decoy_ligands if neccesary
mkdir ../decoy_result_backup
for i in *;
do 
mv ../../../decoy_ligands/$i decoy # change to decoy_ligands if neccesary
mv $i ../decoy_result_backup
done

