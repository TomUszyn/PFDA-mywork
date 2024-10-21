# A sample code to find some text in an Access file.
# Author: Tomasz Uszynski

import re

# Findind the date and time in the access log.
# regex = "\[.*\]"    
# Finding Web addresses in the access log.
regex = "http[s]?://\\S+\\b"


filename = "smallerAccess.log"

with open(filename) as inputFile:
    for line in inputFile:
        foundTextList = re.findall(regex, line)
        if len(foundTextList) != 0:
            # print(foundTextList)
            foundText = foundTextList[0]
            # print(foundText)
            print(foundText)