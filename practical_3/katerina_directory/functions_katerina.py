# Provided inputs
nums = [3, -1, 7, 2, 9, 0, 4]
limit = 4
text = "Room 101: bring 2 apples & 1 banana."

# Global variables
count = 999
summary = "unset"
result = "unset"


# COUNT NUMBERS ABOVE A LIMIT 


def count_above(seq, lim):
    count = 0
    for number in seq:
        if number > lim:
            count += 1
    return count

# so: count_above(nums, limit):
#       count = 0
        # for number in nums:
            # if number > limit:
                # count += 1
# we're setting what seq and lim are later in the code with count_above(nums, limit)

print(count)

count_above(nums, limit)
print(count_above(nums, limit))

print(count)


# SUMMARIZE A TEXT


def summarize_text(s):
    summary = {"digits": 0, "letters": 0, "other": 0}
    other_chars = [] # creates empty list
    for character in s:
        if character.isdigit(): # .isdigit() returns true if character is a digit
            summary["digits"] += 1
        elif character.isalpha(): # .isalpha() returns true if character is a letter
            summary["letters"] += 1
        else:
            summary["other"] += 1
            other_chars.append(character) # puts what's defined as other in the other_chars list
    return summary, other_chars # keeps the other_chars list
# digits, letters and other are string literals NOT variables, they belong in the dictionary
# so "digits" += 1 returns SyntaxError: 'literal' is an illegal expression for augmented assignment
# we need to specify dictionary[key] (summary["digits"]) for it to work

print(summary) # global summary

summarize_text(text)

print(summarize_text(text))
print(len(text)) # check that the numbers add up to the length of the string
# {'digits': 5, 'letters': 21, 'other': 10}
# 36: numbers line up 
# other refers to the spaces, &, .
counts, other_chars = summarize_text(text)
print(other_chars)

print(summary) # global summary


# AGGREGATE WITH A MODE

def aggregate(seq, mode, threshold):
    result = mode
    if mode == "sum" or mode == "count":
        result = 0
    if mode == "max":
        result = None
    for n in seq:
        if n < 0:
            continue
        if n >= threshold:
            if mode == "sum":
                result += n
            elif mode == "count":
                result += 1
            else:
                mode = "max"
                if result == None or n > result:
                    result = n
    return result
            
# = means assigning a value. x = 3 means we're assigning the value 3 to x
# == equality check 
# so result == None checks whether result is None
# whereas result = None assigns the value None to result

print(result)

aggregate(nums, "sum", limit) # we're adding up all of the numbers that are at least or above the threshold
print(aggregate(nums, "sum", limit))
# 20

aggregate(nums, "count", limit) # we're counting how many numbers are at or above the threshod
print(aggregate(nums, "count", limit))
# 3

aggregate(nums, "max", limit)
print(aggregate(nums, "max", limit))
# 9

aggregate(nums, "max", 100)
print(aggregate(nums, "max", 100))
# None

# when threshold was set to limit, then the function only used the numbers in num: 3, -1, 2, 0, 4
# when threshold is set to 100, then it uses ALL of the numbers
# "max" means "no qualifying value found yet"
# we have if n < 0 and if n >= threshold
# there's no if for when n > 0 and < threshold
# so the function stops at line 78: if mode == max, result = None

# ERRORS

try:
    number = int('five')
    print(number)
except ValueError:
    print('That is not a valid number')

values = ['10', '5', 'hello', '8', 'three', '2']

# 1. 
for val in values:
    number = int(val)
    print(number)
# ValueError: invalid literal for int() with base 10: 'hello'

# 2. 
try:
    for val in values:
        number = int(val)
        print(number)
except ValueError:
    print("Skipping invalid value: hello")

# 3 & 4. 
for val in values:
    try:
        number = int(val)
        print(number)
    except ValueError:
        print("Skipping invalid value: {val}")