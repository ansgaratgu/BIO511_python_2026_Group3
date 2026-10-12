# biopython
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from copy import deepcopy

# 1. & 2. 
# read all records
with open("dna.fasta") as file:
    for record in SeqIO.parse(file, "fasta"):
        print(record.id, len(record.seq)) 
        # record.id automatically return the name of the sequence
        # and record.seq returns the sequence itself automatically
        # 3.
        print(record.seq[:10])

# reverse complements
rc_records = [] # empty list to collect every record

with open("dna.fasta") as file2:
     for record in SeqIO.parse(file2, "fasta"):
        rc_seq = record.seq.reverse_complement() 
        rc_record = SeqRecord(rc_seq, id= f"{record.id}_rc", description= f"reverse complement of {record.id}_rc") # create new 
        # f string evaluates what's inside {} and puts the result into text
        rc_records.append(rc_record)

SeqIO.write(rc_records, "dna_rc.fasta", "fasta")
# format is: SeqIo.write(records, filename/handle, format)

# gc annotation


gc_records = []

with open("dna.fasta") as file3:
     for record in SeqIO.parse(file3, "fasta"):
         gc_count = 0 # reset for every record
         for base in record.seq:
            if base == "G" or base == "C":
                gc_count += 1
         gc_percentage = gc_count/len(record.seq) * 100
         rounded = round(gc_percentage, 1)
         record_copy = deepcopy(record)
         record_copy.description = f"{record.description} GC={rounded}%"
         gc_records.append(record_copy)

SeqIO.write(gc_records, "dna_with_gc.fasta", "fasta")

# translation
# 1. 
with open("dna.fasta") as file4:
     for record in SeqIO.parse(file4, "fasta"):
        translated = record.seq.translate()
        print(translated[:10]) # * in output means stop codon. you can stop at the first * by doing translate(to_stop=True)

# 2. 
with open("dna_rc.fasta") as file5:
    for record in SeqIO.parse(file5, "fasta"):
        print(record.id, "|", record.description)

# DYRLQIT
# RDIAISRYRD
# FKPGFK
# AAARRGAPRR
# IYIYIYI
# TLQRCNVATL
# HD*LMLAS*S
# seq1_rc | seq1_rc reverse complement of seq1_rc
# seq2_rc | seq2_rc reverse complement of seq2_rc
# seq3_rc | seq3_rc reverse complement of seq3_rc
# seq4_rc | seq4_rc reverse complement of seq4_rc
# seq5_rc | seq5_rc reverse complement of seq5_rc
# seq6_rc | seq6_rc reverse complement of seq6_rc
# seq7_rc | seq7_rc reverse complement of seq7_rc
# seq8_rc | seq8_rc reverse complement of seq8_rc