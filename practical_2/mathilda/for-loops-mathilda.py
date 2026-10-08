#practical 2 - for loops
#mathilda järkestig 07-10-26

#simple loop:

#the todo list for today in order of importance
to_do = ["last thing of practical 0", "extra exercise of practical 1", "finnish practical 2 if not able to during lesson", "cook nice orange/korena chicken dinner", "start adding python to syntax dictionary", "make bread", "start working on individual practice priject: my code language encodera and interpriter", "start working on course project"]
loop_num = 0 #varible (a sort of total) to keep track or the loop numbers

#for each task in to to list
#for task in to_do:
    #loop_num += 1 #add 1 to loop number at the start or each loop
    #if loop_num < 6: #only print task if loop number is lower then 6
        #print(f"{loop_num}. {task}") #f string to print both varibles with a dot and space in between 
    #else:
        #break #stop the lop when loop number reaches 6


#while loop:

#sequence = 'GATTACAGAACTGATAC'
#a_count = 0
#position = 0
#count_a = 3

#the while version:
#while a_count < count_a:
    #if sequence[position] == "A":
        #a_count += 1
    #position += 1
#print(f" the {a_count}rd A have been found at position {position - 1}")

#the for loop version:
#for base in sequence:
    #if a_count < count_a:
        #if sequence[position] == "A":
            #a_count += 1
        #position += 1
    #else:
        #break
#print(f" the {a_count}rd A have been found at position {position - 1}") 


#nested loops:

sequences = ['ATCTGAGTCCACACATG', 'GCGTCGTGCGATGTTCACGTTGAT', 'CAGTAGTACTCAGT', 'GGTATGCTAGACGAGATCTAATA']
stop_codons = ['TAA', 'TAG', 'TGA']
start_codon = 'ATG'
position_in_sequence = 0
start_position = 0
stop_position = 0

# #without overcomplicating it:

# for sequence in sequences:
#   for codon in stop_codons:
#     if codon and start_codon in sequence:
#       if sequence.find(start_codon) < sequence.find(codon):
#         print(f"in {sequence} {start_codon} is at postion {sequence.find(start_codon)} and {codon} is at position {sequence.find(codon)}")


#the in frame biologicaly correct version (unfinished and not working):

for sequence in sequences:
    for frame1 in sequence:
        start_of_codon = 0
        end_of_codon = 2
        for codons in frame1:
            for codon in frame1:
                print(start_of_codon)
                if start_codon in sequence[start_of_codon:end_of_codon]:
                    start_position = start_of_codon
                    print(f"{start_codon} at position {start_of_codon} in {sequence}")
                    for codon in stop_codons:
                        if codon in sequence[start_of_codon:end_of_codon]:
                            stop_position = start_of_codon
                            print(f"{codon} at position {start_of_codon} in {sequence}")
            start_of_codon += 3
            end_of_codon += 3
        
        
    if start_position < stop_position:
       print(f"in {sequence} start codon occurs before stop codon")

  

#loop though a dictionary:

# data = {
#     'pat_001': ['bacZZt98', 'bac889Ytd'], 
#     'pat_002': ['bac0GFrr'], 
#     'pat_003': ['bac889Ytd', 'bacFq55Hj', 'bacZZt98']
# } #dictionary where each item is a list 

# unique_bacteria = []

# for key_patient, value_bact_list in data.items():  
#     for bacteria in value_bact_list: #since value_bact_list is a list loop over every entry in the list
#         if bacteria not in unique_bacteria:
#             unique_bacteria.append(bacteria) #if a bacterea is not in the unique list add it
# #print(unique_bacteria)

# bacteria_to_patients = {}

# for bacteria in unique_bacteria:
#     if bacteria not in bacteria_to_patients:
#         bacteria_to_patients[bacteria] = [] #for each batteria in unique bacteria add it as a key to dict and add a ampty list as it's idtem
# #print(bacteria_to_patients)

# for key_patient, value_bact_list in data.items():  
#     for bacteria in value_bact_list: # for each bacteria of each patient
#         if bacteria in bacteria_to_patients:
#             bacteria_to_patients[bacteria].append(key_patient) #if bacteria is a key append the list bacteria_to_patients[bacteria] with the patient
# print(bacteria_to_patients)


