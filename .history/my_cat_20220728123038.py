
#! /usr/bin/env python3
import sys

for i in range(len(sys.argv)):
    if i == 0:
        print("Function name: ", sys.argv[0])
    else:
        print(f"{i:1d}. argument: {sys.argv[i]}")
            
 