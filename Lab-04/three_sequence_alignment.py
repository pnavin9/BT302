from Bio import SeqIO
from Bio.Align.Applications import ClustalOmegaCommandline

# Get user input for protein sequences
num_sequences = 0
sequences = []

while num_sequences < 3:
    sequence = input(f"Enter protein sequence {num_sequences + 1}: ")
    sequences.append(sequence)
    num_sequences += 1

# Write sequences to a temporary file in FASTA format
temp_fasta = "temp_sequences.fasta"
with open(temp_fasta, "w") as fasta_file:
    for i, sequence in enumerate(sequences):
        fasta_file.write(f">Seq{i + 1}\n{sequence}\n")

# Perform progressive multiple sequence alignment using Clustal Omega
output_alignment = "aligned_sequences.fasta"
clustalomega_cline = ClustalOmegaCommandline(infile=temp_fasta, outfile=output_alignment)
clustalomega_cline()

# Read and print the aligned sequences
aligned_sequences = SeqIO.parse(output_alignment, "fasta")
print("Aligned sequences:")
for record in aligned_sequences:
    print(f">{record.id}\t{record.seq}")

# Clean up temporary files
import os
os.remove(temp_fasta)
