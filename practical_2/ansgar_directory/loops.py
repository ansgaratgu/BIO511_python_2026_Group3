# simple loops
my_list = ["there", "are", "seven", "words", "in", "this", "list"]
item_index = 0 # the variable to show how many words have been printed in the for loop

for item in my_list:
    print(item)
    item_index += 1 # adding 1 to the current value of {item_index}
    if item_index >= 5:
        break # stops the for loop as soon as it is hit

# while loops
my_sequence = 'GATTACAGAACTGATAC'

## with while loop
a_count_w = 0
position_w = 0
while a_count_w < 3:
    if my_sequence[position_w] == "A":
        a_count_w += 1
        print(f"an A was found at {position_w}")
        a_count_w += 1
    position_w += 1
position_w += 1 # add one more since the while loop stops before the final position number is added
print(f"position of third A is {position_w}")

## with for loop
a_count = 0
position = 0
for base in my_sequence:
    if base == "A":
        a_count += 1
    if a_count < 3:
        position += 1
    if a_count == 3:
        print(f"position of third A is {position}")
        break

# nested loops
sequences = ['ATCTGAGTCCACACATG', 'GCGTCGTGCGATGTTCACGTTGAT', 'CAGTAGTACTCAGT', 'GGTATGCTAGACGAGATCTAATA']
start_codons = ['ATG']
stop_codons = ['TAA', 'TAG', 'TGA']

## observe: the monstrous block of if statements! (worlds most ugly solution to the exercise)
for sequence in sequences:
    for start_codon in start_codons:
        if sequence.find(start_codon) >= 0:
            print(f"start codon {start_codon} was found at position {sequence.find(start_codon)} in sequence {sequence}")
        else:
            print(f"no start codon {start_codon} was found in sequence {sequence}")
    for stop_codon in stop_codons:
        if sequence.find(stop_codon) >= 0:
            print(f"stop codon {stop_codon} was found at position {sequence.find(stop_codon)} in sequence {sequence}")
        if sequence.find(stop_codon) > sequence.find(start_codon) and sequence.find(start_codon) >= 0 and sequence.find(stop_codon) >= 0:
            print(f"start codon {start_codon} is before stop codon {stop_codon}")
        elif sequence.find(stop_codon) < sequence.find(start_codon) and sequence.find(start_codon) >= 0 and sequence.find(stop_codon) >= 0:
            print(f"start codon and stop codon {stop_codon} in wrong order")
        elif sequence.find(stop_codon) < 0:
            print(f"no stop codon {stop_codon} was found in sequence {sequence}")

# loop through a directory
data = {
    'pat_001': ['bacZZt98', 'bac889Ytd'], 
    'pat_002': ['bac0GFrr'], 
    'pat_003': ['bac889Ytd', 'bacFq55Hj', 'bacZZt98']
}

# Loop through the dict printing each key and each value as a list.
for key_patient, value_bact_list in data.items():  
  print(f"patient is {key_patient}")
  print(f"bact value is {value_bact_list}")

# add a line to see if the value (list) has the bacterial strain 'bac889Ytd'. 
# If it does it should return 'True'. If not, it should say 'False'.

for key_patient, value_bact_list in data.items():  
  print(key_patient)
  print(value_bact_list)
  print('bac889Ytd' in value_bact_list)

## reverse the dictionary

### collect unique bacteria
unique_bacteria = []

for my_patient, my_bact in data.items():
    for bacteria in my_bact:
        if bacteria not in unique_bacteria:
            unique_bacteria.append(bacteria)
print(f"strains found across patients: {unique_bacteria}")

### create the reverse dictionary
bacteria_to_patients = {}

for bacteria in unique_bacteria:
    if bacteria not in bacteria_to_patients:
        bacteria_to_patients[bacteria] = [] # [] creates an empty list with [bacteria] as key
print(f"Dictionary with unique bacterium as keys: {bacteria_to_patients}")

### add the patients to the reverse dictionary
for my_patient, my_bact in data.items():
    for bacteria_key, patient_list in bacteria_to_patients.items():
        if bacteria_key in my_bact: # is the bacteria from my dict in a list in the data dict
            patient_list.append(my_patient) # appends the patient with the bacteria to that bacteria's item list in my dict
print(f"Reversed dictionary: {bacteria_to_patients}")