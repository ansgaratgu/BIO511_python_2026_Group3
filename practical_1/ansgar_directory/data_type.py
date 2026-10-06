# playing around with data types
integer = 3

floating_point = 3.14

string = "General Kenobi"

boolean = True

nonetype = None

list_1 = ["egg", "bacon", "potato"]

dictionary = {"name" : "Obi-Wan", "occupation" : "jedi knight"}

tuple = ("cow", "sheep", "frog")

set_1 = {"things", "stuff", "more_stuff"}

range_1 = range(10)

# boolean is true or false
print(boolean)
print(type(boolean))

# the range goes from 0 to 10
print(range_1)
print(list(range_1))


if "bacon" in list_1:
    print("Great Breakfast")
elif "egg" in list_1:
    print("Decent Breakfast")
else:
    print("Bad Breakfast")

print(type(range_1))