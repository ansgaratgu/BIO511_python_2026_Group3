from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

with open("dna.fasta") as file:
    for sequence in (SeqIO.parse(file, "fasta")):
        gc_count = 0
        for base in sequence.seq:
            if base == "G" or base == "C":
                gc_count += 1
                print(gc_count)
        
        gc_percent = len(sequence) / gc_count # wrong
        print(f"GC% for {sequence.id} is {gc_percent}")


