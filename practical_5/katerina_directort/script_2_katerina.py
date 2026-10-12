# arguments and pandas
import argparse
import csv
import pandas as pd
import numpy as np

# 1. & 2.
parser = argparse.ArgumentParser(description="Read a csv file and print its rows.")
# the above is a parser object: it reads the command line. description is text that shows up if you run python script.py -h
parser.add_argument('--file', required=True, help='Path to the input csv file')
# this tells parser that the script expects one argument and names it file
args = parser.parse_args()
# this reads what was typed and stores it in args

# 3. 
with open (args.file) as f: # NOT ('args.file') bc it will search for a file literally called that
    reader = csv.reader(f)
    for row in reader:
        print(row)

# 4. convert data into pandas dataframe, print statistical summary
df = pd.read_csv(args.file)
print(df)

## statistical summary, doesn't work with my file bc it's not just numbers
# df.describe(args.file)