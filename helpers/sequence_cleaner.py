import sys
import re
from Bio import SeqIO

clean_records = []
ids = dict()

def sequence_cleaner(fasta_file, min_length=0, por_n=100):
	for seq_record in SeqIO.parse(fasta_file, "fasta"):
		sequence = str(seq_record.seq).upper()
		if float(sequence.count("N")*100)/float(len(sequence))<por_n and len(sequence) > min_length: 
			seq_record.id = re.sub('\s', '_', seq_record.description)
			seq_record.id = re.sub('[^A-Za-z0-9]+', '_', seq_record.id)
			seq_record.id = seq_record.id[0:18]
			seq_record.name=""; seq_record.description=""
			if seq_record.id in ids: 
				ids[seq_record.id] += 1
				seq_record.id += str(ids[seq_record.id])
			else: ids[seq_record.id] = 1
			clean_records.append(seq_record)
	with open(fasta_file+"_clean.fasta", 'w') as f:
    		SeqIO.write(clean_records, f, 'fasta')

userParameters = sys.argv[1:]
print(userParameters)
if len(userParameters) == 1:
	sequence_cleaner(userParameters[0])
elif len(userParameters) == 2:
	sequence_cleaner(userParameters[0], float(userParameters[1]))
elif len(userParameters) == 3:
	sequence_cleaner(userParameters[0], float(userParameters[1]), float(userParameters[2]))
else:
	print("There is a problem!")
