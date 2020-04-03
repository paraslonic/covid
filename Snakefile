
rule all:
	input: "random/gisaid_nr_random.fasta"


rule select_random:
	input: "fasta/gisaid_nr.fasta_clean.fasta"
	output: "random/gisaid_nr_random.fasta"
	shell: 
		"""
		python helpers/select_random.py {input} {output} 5
		mkdir -p fna
		python helpers/split_contigs.py {output} fna
		"""

rule make_nr:
	input: "fasta/gisaid_cov2020_sequences.fasta"
	output: "fasta/gisaid_nr.fasta"
	threads: 10
	shell: "cd-hit -i {input} -o {output} -c 1 -T 10"

rule clean:
	input: "fasta/gisaid_nr.fasta"
	output: "fasta/gisaid_nr.fasta_clean.fasta"
	shell: "python helpers/sequence_cleaner.py {input} 29000 0.00001"



