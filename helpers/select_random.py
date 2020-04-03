import sys
import re
import random
from Bio import SeqIO

records = []

def sequence_random(fasta_file, fasta_out, nseq=100):
	for seq_record in SeqIO.parse(fasta_file, "fasta"):
		records.append(seq_record)
	random_records = random.choices(records, k=nseq)	
	with open(fasta_out, 'w') as f:
    		SeqIO.write(random_records, f, 'fasta')

userParameters = sys.argv[1:]
print(userParameters)
if len(userParameters) == 2:
	sequence_random(userParameters[0], userParameters[1])
elif len(userParameters) == 3:
	sequence_random(userParameters[0], userParameters[1], int(userParameters[2]))
else:
	print("There is a problem!")
