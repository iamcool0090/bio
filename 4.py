# 4.Given a FASTA file, write a Python script that reads the file and converts it into GenBankformat, while preserving the sequence and annotations.
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord


def convert_fasta_to_genbank(fasta_file, genbank_file):
    records = []
    for record in SeqIO.parse(fasta_file, "fasta"):
        dna_sequence = record.seq
        description = record.description
        genbank_record = SeqRecord(
            dna_sequence,
            id=record.id,
            name="Example_Gene",
            description=description,
            annotations={
                "molecule_type": "DNA",
                "gene": "ExampleGene",
                "function": "Hypothetical protein"
            }
        )
        records.append(genbank_record)

    with open(genbank_file, "w") as output_file:
        SeqIO.write(records, output_file, "genbank")

    print(f"All FASTA sequences converted to GenBank format and saved as {
          genbank_file}")


fasta_file = r"C:\Users\sujay\OneDrive\Desktop\biopython\example.fasta"
genbank_file = "example_output.gb"
convert_fasta_to_genbank(fasta_file, genbank_file)
