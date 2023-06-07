# Dopamine receptor Hits Discovery 


This project aims at optimizing ML as a tool to screen chemical libraries for the dopamine D1 and D2 receptors. I employed ligand binding quantification and selection algorithms - diffdock (https://github.com/gcorso/DiffDock) and equibind (https://github.com/HannesStark/EquiBind). Equibind’s output was fined-tuned with a xgboost model — xgb cv models .Rmd

light_data contains the actives, decoy, and clustering datasets 


index.html : a cluster map of the decoys and actives which the xgboost model was trained on. 

requirements.txt contains a few dependencies needed to web scrapping off the DUD-e server

Code can be run with CPU on a cluster. However, for speed and time optimization, it is best to use request a GPU instance (T4 should be fine) to accelerate workflow. Scripts are written in Python, R, and bash. 

