import sys
import re
import random
from Bio import SeqIO

records = []

def split_fasta(fasta_file, fasta_dir):
	for seq_record in SeqIO.parse(fasta_file, "fasta"):
		with open(fasta_dir+"/"+seq_record.id+".fasta", 'w') as f:
    			SeqIO.write(seq_record, f, 'fasta')

userParameters = sys.argv[1:]
print(userParameters)
if len(userParameters) == 2:
	split_fasta(userParameters[0], userParameters[1])
else:
	print("There is a problem!")
