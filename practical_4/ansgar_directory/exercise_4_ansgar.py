# I will need to do pip install biopython

# 1: Makes a dictionary called sequences where headers are keys and sequences are values
# Then creates a second dictionary called sequence_codons where headers are keys and the values are lists of codons in each sequence
# Returns this second dictionary

# 2: a fasta file named sequence_file ?


# 1: Input is the values in the sequence_codons dictionary (codon_list)

# 2: Looks at the codons in codon_list and translates it to amino acids with a .translate function ?
# And adds the amino acids in order to a string called aa_string

import Bio
from Bio.Seq import Seq

# create a sequence object
my_seq = Seq("CATGTAGACTAG")

# print out some details about it
print("seq %s is %i bases long" % (my_seq, len(my_seq)))
print("reverse complement is %s" % my_seq.reverse_complement())
print("protein translation is %s" % my_seq.translate())
