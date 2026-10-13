from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

records = list(SeqIO.parse("dna.fasta", "fasta"))

rc_list = [] # empty list for adding reverse seqs
with open("dna.fasta") as file:
    for record in (SeqIO.parse(file, "fasta")):
        print(f"ID: {record.id}\nLength: {len(record)}\nFirst 10 bases: {record.seq[:10]}")
        rev = record.reverse_complement()
        print(f"Reverse comp: {rev.seq}") # .seq makes it only print the sequence and not the other bs

        # for every sequence, make a new seqrecord for reverse complement
        # set the IDs to the old ID + _rc for all reverse complements
        reverse_rec = SeqRecord((rev.seq), id = f"{record.id}_rc", description = "")
        rc_list.append(reverse_rec)

# write to a new file called dna_rc.fasta
SeqIO.write(rc_list, "dna_rc.fasta", "fasta") # why is it reversed backwards?