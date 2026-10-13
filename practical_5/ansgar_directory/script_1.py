import sys
import os
import csv

def file_manipulation(file_manipulation_input):

    if not os.path.isfile(file_manipulation_input):
        with open(f"{file_manipulation_input}", "w") as file:
            file.write(',,,,\n,,,,\n,,,,\n,,,,\n,,,,\n')

    elif sys.argv[1] == "-r":
         with open(f"{file_manipulation_input}", "w") as file:
                    file.write(',,,,\n,,,,\n,,,,\n,,,,\n,,,,\n')

    elif sys.argv[1] == "-a":
        with open(f"{file_manipulation_input}", "a") as file:
            writer = csv.writer(file)
            writer.writerow([f"{sys.argv[2]}",f"{sys.argv[3]}",f"{sys.argv[4]}",f"{sys.argv[5]}",f"{sys.argv[6]}"])

    return "Function 1 processed"

file_manipulation_output = file_manipulation("file1.csv")
print(file_manipulation_output)