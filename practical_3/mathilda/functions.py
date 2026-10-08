###practical 3 - functions###
###mathilda järkestig 08-10-26###


# Provided inputs
nums = [3, -1, 7, 2, 9, 0, 4]
limit = 4
text = "Room 101: bring 2 apples & 1 banana."

# Global variables
count = 999
summary = "unset"
result = "unset"

###count function:

def count_above(seq, lim):
    count = 0
    for num in seq:
        if num > lim:
            count += 1
            print(f"{num} > {lim} -> {count - 1} + 1 = {count}")
    return count

# funcount = count_above(nums, limit)
# print(f"function: {funcount}")

# print(count)


###summarise function:

def summarize_text(s):
    summary = {"digits" : 0, "letters" : 0, "other" : 0}
    for chr in s:
        if chr.isdigit() == True:
            summary["digits"] += 1
        elif chr.isalpha() == True:
            summary["letters"] += 1
        else:
            summary["other"] += 1
    return summary

# test = summarize_text(text)
# print(test)

# print(summary)


###aggrigate w mode:

def aggregate(seq, mode, threshold):
    #define result base on mode
    if mode == "sum":
        result = 0
    elif mode == "count":
        result = 0
    elif mode == "max":
        result = None
    #loop though seq
    for n in seq:
        if not n < 0:
            if n >= threshold:
                if mode == "sum":
                    result += n
                if mode == "count":
                    result += 1
                if mode == "max":
                    if result == None or n > result:
                        result = n
    return result

test = aggregate(nums, "sum", limit)
print(test)

print(result)


        




