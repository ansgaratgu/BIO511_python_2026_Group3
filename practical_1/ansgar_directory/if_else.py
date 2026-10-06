# double check what type a variable is with 
# type(variablename), to determine which variable to use

my_string = "ohnopleasehelpmesomeone"

print(len(my_string))

if len(my_string) == 0:
    print("Empty")
else:
    print("Not empty")

# multi-way
integer = -9

if integer > 0:
    print("Positive")
elif integer == 0:
    print("Integer is zero")
else:
    print("Negative")

# type gate
my_range = range(30)

if type(my_range) is tuple or list or range:
    if len(my_range) == 0:
        print("Empty")
    elif len(my_range) == 1:
        print("Single item")
    elif len(my_range) > 1:
        print("Multiple items")
else:
    print("Wrong type for this task")

# look up a sample
read_counts = {"sample_A": 1520000, "sample_B": 830000, "sample_C": None}

print("sample_A" in read_counts) # prints True

# this is how to print the value of an item in the dictionary
print(read_counts["sample_A"])

# assign the value of sample_A to the sample variable
sample = read_counts["sample_A"]

sample = "sample_A"

# double-check it worked
print(sample)

if sample not in read_counts:
    print("Unknown sample")
elif sample == None:
    print("Sequencing failed")
elif int(sample) >= 1000000: ????????
    print("Enough reads")
else:
    print("Too few reads")

