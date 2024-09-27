# Program to read in the data and output each line as a list.
# Author: Tomasz Uszynski

import csv

FILENAME = 'data.csv'
DATADIR = 'data/'

with open(DATADIR + FILENAME, 'rt') as fp:
    reader = csv.reader(fp, delimiter=',')
    for line in reader:
        print(line)
        
# Output is presented as a list of lists. Each list represents a row in the csv file.