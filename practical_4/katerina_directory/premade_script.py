from Bio.Seq import Seq

def codons(sequence_file): # input is a fasta file
    """A function that reads a fasta file and returns a list of codons for each sequence in the file"""
    
    # First we read the fasta file and store each sequence in a dictionary, with its header as the key
    sequences = {}
    
    # Open the file
    with open(sequence_file) as fasta_file:
        # Read the file line by line
        for row in fasta_file:
            row = row.strip()
            # If the line starts with '>', it is a header and we start a new, empty sequence
            if row.startswith('>'):
                header = row[1:]
                sequences[header] = ""
            # If the line does not start with '>', it is part of the current sequence and we add it to that sequence
            else:
                sequences[header] += row
# we're seperating the sequences
    
    # Now we split each sequence into codons
    sequence_codons = {}
    
    for header, sequence in sequences.items():
        codon_list = []
        # Loop over the sequence in steps of 3
        for i in range(0, len(sequence), 3):
            # Append the codon to the list if it is a full codon (3 nucleotides)
            if i + 3 <= len(sequence):
                codon_list.append(sequence[i:i + 3])
        # Save the list of codons under the header of the sequence
        sequence_codons[header] = codon_list
    
    # Return the dictionary of codons
    return sequence_codons



def exercise_function(codon_list): # input is codon list from codons
    """translates each codon into an amino acid and saves it in a new variable"""
    aa_string = ""
    for codon in codon_list: # for each codon in codon_list
        amino_acid = Seq(codon).translate() # seq from bio.seq module. we're translating the codon into an amino acid 
        aa_string += str(amino_acid) # str creates a new string object. in aa_string we're adding all of the amino acids
    return aa_string # we have a variable that has all of the amino acids

