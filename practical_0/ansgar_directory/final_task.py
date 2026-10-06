# make the script print the basename of a file
import os
import sys

file_path = sys.argv[1]

base_name = os.path.basename(file_path)

print(base_name)