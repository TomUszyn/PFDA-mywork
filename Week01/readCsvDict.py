# Program to read CSV file as a directory.
# Author: Tomasz Uszynski

import csv

FILENAME = 'data.csv'
DATADIR = 'data/'

with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.DictReader(fp, delimiter="," , quoting=csv.QUOTE_NONNUMERIC)
    total = 0
    count = 0
    for line in reader:
        total += line['age']
        
        count +=1
    print (f"average is {total/(count)}") # why is there no -1 this time? 
                                          # Because we are not counting the header row.