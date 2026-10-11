#!/usr/bin/env python3
from premade_script import codons
import argparse # need to install this 
import os

# when we run the script, we need to write: python main.py -s path/to/sequences.fa. why?

def existing_file(file_path):
    """This function checks if the provided file path exists and is a file."""
    if not os.path.isfile(file_path):
        raise argparse.ArgumentTypeError(f"'{file_path}' is not a valid file")
    return file_path


def main():
    # First we capture the input arguments from the command line
    parser = argparse.ArgumentParser(description="Split the sequences in a FASTA file into codons.")
    parser.add_argument('-s', '--sequence', type=existing_file, required=True, help='Path to the input FASTA file')
    args = parser.parse_args()
    
    # We first call the function from the script, and use the input file path as an argument
    sequence_codons = codons(args.sequence)
    
    # Here you need to check the output of the function
    print(sequence_codons)
    # {'sequence_1_short': ['ATG', 'GCT', 'TTT', 'TAA'], 
    # 'sequence_2_varied': ['ATG', 'CCA', 'GAA', 'TGG', 'TGA'], 
    # 'sequence_3_gc_rich': ['ATG', 'GCG', 'GCG', 'TAA'], 
    # 'mystery_sequence': ['atg', 'tac', 'cat', 'gtg', 'gag', 'aga', 'tgc', 'aga', 'gcc', 'ttc', 'aca', 'atc', 'tcc', 'ttc', 'ctg', 'ctg', 'ttc', 'gag', 'gag', 'ctg', 'tcc', 'taa']}
    
    # Here you need to call the exercise_function from premade_script.py
    from premade_script import exercise_function

    # And check the output of that function
    print(sequence_codons(aa_string))

if __name__ == "__main__":
    main()

# EXTRA 

from collections import Counter

# 1. 
for codon in :
    codon_number = Counter(codon)
    print(codon_number)
    


# 2. 
for codon in :
    codon_number.most_common(1) # by defining most_common(1) we say we only want the codon that appears the most
    print(codon_number.most_common(1))

# 3.
for amino_acids in aa_string:
    aa_number = Counter(amino_acids)