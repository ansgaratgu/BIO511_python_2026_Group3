# file manipulation
import csv
import sys # for argv 

# 1. this is a LIST
rows = [
    ["id", "name", "age", "city", "score"],
    [1, "Alice", 30, "Berlin", 88.5],
    [2, "Bob", 25, "Paris", 92.0],
    [3, "Carla", 41, "Madrid", 79.5],
    [4, "Dmitri", 35, "Warsaw", 85.0],
]

with open('file.csv', 'w') as f: # this creates a file.csv
    writer = csv.writer(f, delimiter=',')
    writer.writerows(rows)

# or with for loop:
# with open('file.csv', 'w', newline='', encoding='utf-8') as f:
#     writer = csv.writer(f)
#     for row in rows:
#         writer.writerow(row)

# 2. 
new_row = [arg.strip(',') for arg in sys.argv[1:]]

with open('file.csv', 'a') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(new_row)

with open('file.csv', 'r') as f:
    print(f.read())