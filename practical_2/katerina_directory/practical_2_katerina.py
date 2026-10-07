# 1. 
my_list = ["ferrari", "mclaren", "mercedes", "audi", "lotus", "red bull", "toyota"]

#for item in my_list: 
 #   print(item)

# 2.
# enumerate gets both index and the value while iterating 
# enumerated_my_list = enumerate(my_list)

for index, item in enumerate(my_list, start=1):
    print(index)

# 3.
for item in my_list:
    print(item)
    if item == 'lotus':
        break

# WHILE LOOPS
sequence = 'GATTACAGAACTGATAC'
a_count = 0
position = 0

# 1. 
while a_count < 3:
    if sequence[position] == 'A':
        a_count += 1
    position += 1

a_position = position - 1
print("While loop:", a_position)

# 2.
enumated_sequence = enumerate(sequence)

# pos is a LETTER in the sequence
for pos in sequence:
    if sequence[position] == 'A':
        a_count += 1
        position += 1
    if a_count == 3:
        #a_pos = position
        break
a_pos = position - 1
print("For loop:", a_pos)


# NESTED LOOPS
sequences = ['ATCTGAGTCCACACATG', 'GCGTCGTGCGATGTTCACGTTGAT', 'CAGTAGTACTCAGT', 'GGTATGCTAGACGAGATCTAATA']
start_codon = 'ATG'
stop_codons = ['TAA', 'GTA', 'TAG']

# 2. 
for sequence in sequences:
    if start_codon in sequence:
        for stop in stop_codons:
            if stop in sequence:
                print(f"{start_codon} and {stop} are in {sequence}")

# 3. print only those with ATG before the stop codon
# loop through and keep track of the position and use str.find() the position of the ATG
for sequence in sequences:
    start = sequence.find('ATG')
    after_start = sequence[start:]
    for stop in stop_codons:
        if stop in after_start:
            print(f"{start_codon} and {stop} are in {sequence}")


# DICTIONARY
data = {
    'pat_001': ['bacZZt98', 'bac889Ytd'], 
    'pat_002': ['bac0GFrr'], 
    'pat_003': ['bac889Ytd', 'bacFq55Hj', 'bacZZt98']
}

# Loop through the dict printing each key and each value as a list.
for key_patient, value_bact_list in data.items():  
  print(key_patient)
  print(value_bact_list)

# add a line to see if the value (list) has the bacterial strain 'bac889Ytd'. 
# If it does it should return 'True'. If not, it should say 'False'.

# for key_patient, value_bact_list in data.items():  
#   print(key_patient)
#   print(value_bact_list)
#   print('bac889Ytd' in value_bact_list) # in returns a boolean: it checks whether bac88 is an element in the list. if it is it returns true, if not false

# 1. 
unique_bacteria = [] # this is an empty list 

# loop through data and then through each patient's list of bacteria
for key_patient, value_bact_list in data.items():
    for bacteria in value_bact_list:
        if bacteria not in unique_bacteria:
            unique_bacteria.append(bacteria)

print(unique_bacteria)

# 2.
bacteria_to_patients = {} # this is an empty dictionary

# don't do the loop over the dictionary, it wont work bc it's empty
# to add key to dictionary: dictionary[new_key] = value
for bacterium in unique_bacteria:
    if bacterium not in bacteria_to_patients:
        bacteria_to_patients[bacterium] = []

print(bacteria_to_patients)

# 3. 
for patient, bacteria in data.items(): # each patient and their bacteria
    for bacterium in bacteria: # goes through only that patient's bacteria
        bacteria_to_patients[bacterium].append(patient)

print(bacteria_to_patients)
