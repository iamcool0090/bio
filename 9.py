# 9
from Bio import Phylo, AlignIO
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor
import matplotlib.pyplot as plt

alignment = AlignIO.read("aligned_sequences.aln", "clustal")
calculator = DistanceCalculator("identity")
distance_matrix = calculator.get_distance(alignment)
constructor = DistanceTreeConstructor()
tree = constructor.upgma(distance_matrix)
Phylo.write(tree, "phylogenetic_tree.nwk", "newick")

fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot(1, 1, 1)
Phylo.draw(tree, axes=ax)
plt.show()


CLUSTAL W(1.83) multiple sequence alignment


seq1               ATGCGTACGTAGCTAGCTAG
seq2               ATGCGTACGTTGCTAGCTAG
seq3               ATGCGTACGTAGCTTGCAGG
