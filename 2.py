# 2
from Bio import SeqIO


def read_fasta(file_path):
    for record in SeqIO.parse(file_path, "fasta"):
        print(f"Description:{record.description}")
        print(f"Sequence:{record.seq}")


fasta_file = r"C:\Users\adith\.vscode\bioProject\example.fasta"
read_fasta(fasta_file)

>seq1 Sample description
ATGCATGCATGC
>seq2 Another description
GCTAGCTAGCTA
