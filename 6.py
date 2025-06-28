# 6
from Bio import Entrez
from Bio import SeqIO

Entrez.email = "your_email@example.com"
accession_number = "NM_001301717"

handle = Entrez.efetch(db="nucleotide", id=accession_number,
                       rettype="gb", retmode="text")
seq_record = SeqIO.read(handle, "genbank")

print(f"Accession Number: {seq_record.id}")
print(f"Description: {seq_record.description}")
print(f"Organism: {seq_record.annotations['organism']}")
print(f"Sequence: {seq_record.seq}")
print(f"Length of Sequence: {len(seq_record.seq)}")
print(f"Features: {seq_record.features}")
