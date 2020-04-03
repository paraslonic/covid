threads=$1
orthofinder  -t $threads -og -f faa -S blast
mkdir -p Results
mkdir -p Results/ortho

find faa -name 'Orthogroups.txt' -exec cp {} Results/ortho \; 
find faa -name 'Orthogroups_SingleCopyOrthologues.txt' -exec cp {} Results/ortho/SingleCopyOrthogroups.txt \; 
perl scripts/namedGroups2table.pl Results/ortho/Orthogroups.txt Results/ortho/

