# This code anonymizes the subdomains of IP addresses.
# Author: Tomasz Uszynski

import re

regex = "(\d{1,3}\.\d{1,3}\.)\d{1,3}\.\d{1,3}" # note the space at the end
replacementText="\\1XXX.XXX " # note the space at the end to match above
filename = "smallerAccess.log"
outputFileName = "anonymisedIPs.txt"

with open(filename) as inputFile:
    with open(outputFileName, 'w') as outputFile:
        for line in inputFile:
            # for debugging
            #foundText = re.search(regex, line).group()
            #print(foundText)
            newLine = re.sub(regex, replacementText, line)
            outputFile.write(newLine)