# 1.Using the Seq class from Biopython, create a DNA sequence object and: i. Slicethesequence to extract a specific region (e.g., from index 3 to 10). ii. Concatenate this sequencewith another sequence. iii. Transcribe and translate the concatenated sequence intoRNAand protein sequences.

from Bio.Seq import Seq
dna_sequence = Seq("ATGCTAGCTAGCTAGCTG")
sliced_sequence = dna_sequence[3:11]
print("Sliced Sequence:", sliced_sequence)
another_sequence = Seq("GGCTAG")
concatenated_sequence = sliced_sequence + another_sequence
print("Concatenated Sequence:", concatenated_sequence)
rna_sequence = concatenated_sequence.transcribe()
print("RNA Sequence:", rna_sequence)
protein_sequence = rna_sequence.translate()
print("Protein Sequence:", protein_sequence)
