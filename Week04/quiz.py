# This is code for the quiz
# Author: Tomasz Uszynski

import re

regex = "^$"
filename = "quiz.txt"

with open(filename) as quizFile:
    for line in quizFile:
        searchResult = re.search(regex, line)
        if (searchResult):
            matchingLine = line
            # I set the end to blank because each line will already have a \n
            print (matchingLine, end="")
            
# a. hello              line 1
# b. Hello              lines 2,3 and 5
# c. ^Hello             lines 2,3
# d. ^Hell*o            lines 2,3,4,6
# e. ^Hell+o            lines 2,3,6
# f. ^Hell?o            lines 2,3,4
# g. ^hello [A-Z]       Nothing
# h. ^Hello [A-Z]       line 3
# i. =                  line 7
# j. #                  line 8
# k. [                  error: unterminated character set at position 0
# l. ^$                 empty line