
#! /usr/bin/env python3
import sys

for i in range(len(sys.argv)):
    with open(i) as file:
        contents = file.read()
    print(file)    

 