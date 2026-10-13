from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

copy_gc = []

# open the file
with open("dna.fasta") as file:

    #  look through the sequences in the fasta file one at a time
    for record in (SeqIO.parse(file, "fasta")):
        gc_count = 0

        # look through the bases in the sequence and check for G and C
        for base in record.seq:
            if base == "G" or base == "C":
                gc_count += 1

        # get the GC%
        if gc_count > 0:
            gc_percent = (gc_count * 100) / len(record)
        else:
            gc_percent = 0

        # round to 1 decimal place and print
        gc_percent = round(gc_percent, 1)
        print(f"GC% for {record.id} is {gc_percent}")

        # create a new file with descriptions for sequences containing GC%
        copy_record = SeqRecord((record.seq), id = f"{record.id}", description = f"GC={gc_percent}")
        copy_gc.append(copy_record)

    # create the new file
    SeqIO.write(copy_gc, "dna_with_gc.fasta", "fasta")


# translate each DNA sequence and print the first 10 amino acids
with open("dna.fasta") as file:
    for record in (SeqIO.parse(file, "fasta")):
        aa_seq = record.seq.transcribe().translate()
        print(aa_seq[:10])