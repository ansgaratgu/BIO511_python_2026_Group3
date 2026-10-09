def add_two_numbers(num_one, num_two):
    number_to_return = num_one + num_two
    return number_to_return

my_added_numbers = add_two_numbers(1, 1)

print(my_added_numbers) # will print 2

#### setup
# Provided inputs
nums = [3, -1, 7, 2, 9, 0, 4]
limit = 4
text = "Room 101: bring 2 apples & 1 banana."

# Global variables
count = 999
summary = "unset"
result = "unset"

#### count numbers abode a limit
def count_above(seq, lim):
    count = 0
    for number in seq:
        if number > lim:
            count += 1
    return count

print(count) # will print globar variable = 999

returned_number = count_above(nums, limit)
print(returned_number) # will print the variable local to the function = 2 but NOT change global = 999

print(count) # indeed, global variable is still = 999

#### summarize a text
def summarize_text(s):
    summary = {"digits": 0,"letters": 0, "other": 0}
    for character in s:
        if character.isdigit():
            summary["digits"] += 1
        elif character.isalpha():
            summary["letters"] += 1
        else:
            summary["other"] += 1
    return summary

print(summary)

summary_call = summarize_text(text)
print(summary_call)

print(summary)

# "other" in this case is ANYTHING that is not a number or letter: " ", ".", "&"

print(len(text)) # yes they add up

#### aggregate with a mode
def aggregate(seq, mode, threshhold):
    if mode == "sum" or mode == "count":
        result = 0
    elif mode == "max":
        result = None
    for number in seq:
        if number < 0:
            continue
        elif number >= threshhold:
            if mode == "sum":
                result += number
            elif mode == "count":
                result += 1
            else:
                if result == None or number > result:
                    result = number
    return result

print(result)

agg_sum = aggregate(nums, "sum", limit)
print(agg_sum)

agg_count = aggregate(nums, "count", limit)
print(agg_count)

agg_max = aggregate(nums, "max", limit)
print(agg_max)

print(result)

agg_max_100 = aggregate(nums, "max", 100)
print(agg_max_100)
# this skips all numbers as both the if n < 0 and elif n >= threshold fail
# to fix this, add another else statement

#### errors and try/except
