# Program to read CSV file modified to calculate the average age (float). 
# Author: Tomasz Uszynski

import csv

FILENAME = 'data.csv'
DATADIR = 'data/'

with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter="," , quoting=csv.QUOTE_NONNUMERIC)
    linecount = 0
    total = 0
    for line in reader:
        if not linecount: # first row is header row
            pass
        else: # all subsequent rows
            total += line[1]    # why 1 ?  
                                # Because the age is in the second column.
            
        linecount += 1
    print (f"average is {total/(linecount-1)}") # why -1 ? 
                                                # Because we are not counting the header row.