import csv
import argparse
import pandas as pd

parser = argparse.ArgumentParser() # no idea of what this does but I need it
parser.add_argument('-f', '--file', required = True, help = 'Input file') # -f or --file is argument and should be followed by input file name
args = parser.parse_args() # again, no clue but I need it

def arguments_and_pandas(pandas_input):

    with open(f'{pandas_input}', 'r') as file: # opens input file (from argument) in read mode
        reader = csv.reader(file, delimiter = ',') # csv reader, not sure why I need it
        for row in reader:
            print(row) # prints contents of the csv file to terminal
    df = pd.read_csv(f'{pandas_input}') # sets df (variable) as a csv file to be read by pandas
    print(df.to_string()) # prints pandas dataframe (df)

argument_call = arguments_and_pandas(args.file)