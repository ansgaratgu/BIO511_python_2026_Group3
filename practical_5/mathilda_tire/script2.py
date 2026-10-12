#prictical 5
#mathilda järketig 12-10-26

#imports:
import argparse
import csv
import pandas as pd

#argumants:

parser = argparse.ArgumentParser ()
parser.add_argument('--inputcsv', help='this code needs a csv file as input')
args = parser.parse_args()

print(f"input file {args.inputcsv} will be used")


with open(args.inputcsv, newline='\n') as flick:
    reader = csv.reader(flick)
    for row in reader:
        print(row)