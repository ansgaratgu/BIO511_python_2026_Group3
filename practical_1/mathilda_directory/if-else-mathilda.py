#practecing if else


#fist simple if else
stringu = "variablestuesday"

print(len(stringu))

if len(stringu) == None:
    print("empty")
else: 
    print("not empty")


#multi-way if else
intern = 7

if intern > 0:
    print("posetive")
elif intern == 0:
    print("0")
else:
    print("negative")


#type gate / nested
life_list = ["sleep", "eat", "shit"]

if type(life_list) is list or tuple or range: 
    if len(life_list) == 0:
        print("empty")
    elif len(life_list) == 1:
        print("one item")
    elif len(life_list) > 1:
        print("multitude of items")
else:
    print("not sutible type")


#look up a sample
#defiening dictionary
read_counts = {"sample_A": 1520000, "sample_B": 830000, "sample_C": None}

print("sample_A" in read_counts) # prints True

# variables
sample = "sample_A"
passed_qc = True #boolean

#if elses:
if sample in read_counts:
    if read_counts[sample] == None:
        print("sequencing failed")   
    elif read_counts[sample] < 1000000:
        print("to few reads")
    elif read_counts[sample] >= 1000000 and passed_qc == True:
        print("ready for analysis")
else:
    print("unknown sample")



