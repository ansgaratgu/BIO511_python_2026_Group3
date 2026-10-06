# string
a = "This is a test"

if a == 0:
    print('String is empty')
else:
    print('String is not empty')

print(len(a))

# integer 
b = 16

if b > 0:
    print('Integer is positive')
elif b == 0:
    print('Integer is equal to zero')
else:
    print('Integer is negative')

# this also works instead of else: 
# elif b < 0:
#    print('Integer is negative')

d = range(7) # range
h = ["loop", "lutz", "axel"] # list
i = ("loop", "lutz", "axel") # tuple

# can't do len(axel) because python can't read the string within the list
# so we have to call the variable (h) and then the position of 'axel' within it
# loop = 0, lutz = 1, axel = 2
if 'axel' in d or h or i:
    if len(h[2]) == 0: 
        print('Empty')
    if len(h[2]) == 1:
        print('Single item')
    if len(h[2]) > 1:
        print('Multiple items')
else:
    print('Wrong item for this task')

# this is a dictionary
read_counts = {"sample_A": 1520000, "sample_B": 830000, "sample_C": None}

sample_A = 1520000
sample_B = 830000
sample_C = None

# 1.
sample = sample_A

# we need to specify that we're looking at the VALUE of the sample, not just the stirng (ie 'sample_B')
if sample in read_counts.values():
    if sample == None:
        print('Sequencing failed')
    elif sample > 1000000:
        print('Enough reads')
    else:
        print('Too few reads')
else:
    print('Unknown sample')


# 2.
# to check for an unknown sample (ex. Sample_D) we need to write 
# sample = "sample_D" instead of sample = sample_D
# because in the first case it's checking directly in the dictionary which is what we want
# but in the second case it's checking the section:
# sample_A = 1520000, sample_B = 830000, sample_C = None
# to see if it exists there, which it obviously doesnt so it returns an error

# 3.
passed_qc = True   

if sample in read_counts.values():
    if sample == None:
        print('Sequencing failed')
    elif sample > 1000000 and passed_qc == True:
        print('Ready for analysis')
    else:
        print('Not ready for analysis')
else:
    print('Unknown sample')

# if passed_qc = False then for sample_A it returns "not ready for analysis", if that's not changed then it returns "not enough reads"

# extra GC
sequence = "ATGCGTACTTAGCAAT"

# 1. 
if sequence[0] == "G" or sequence[0] == "C":
    print('This sequence starts with G or C')
else:
    print("This sequence doesn't start with G or C")

# 2. 
gc_count = 0

for base in sequence:
    if base == "G" or base == "C":
        gc_count += 1

print(gc_count)

# 3. 
GC_percentage = gc_count/len(sequence)
print(GC_percentage)

# 4. 
sequence_2 = "TTAGGCATGCCGATATCGGCTTA"

gc_count_2 = 0

for base in sequence_2:
    if base == "G" or base == "C":
        gc_count_2 += 1

GC_percentage_2 = gc_count_2/len(sequence_2)
print(GC_percentage_2)
