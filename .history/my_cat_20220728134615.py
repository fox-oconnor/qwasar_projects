
#! /usr/bin/env python3
import sys
output = ""
for i in range(len(sys.argv)):
    if i >= 1:
        with open(sys.argv[i], 'r') as file:
            file = file.read()
            output += file
print(strip(output))    



 