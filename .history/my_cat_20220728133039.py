
#! /usr/bin/env python3
import sys

for i in range(len(sys.argv)):
    if i >= 1:
        with open(i, 'r') as file:
            file = file.read()
        print(file)    



 