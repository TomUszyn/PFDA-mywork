# Program to read in the data and output each line as a list 
# modified to deal with the header line separately.
# Author: Tomasz Uszynski

import csv

FILENAME = 'data.csv'
DATADIR = 'data/'

with open(DATADIR + FILENAME, 'rt') as fp:
    reader = csv.reader(fp, delimiter=',')
    linecount = 0
    for line in reader:
        if not linecount: # first row is header row
            print (f"{line}\n---------------------")
        else: # all subsequent rows
            print (line)
        linecount += 1