#!/usr/bin/env python3
import sys

if len(sys.argv) != 3:
    print(f'Usage: {sys.argv[0]} name age')
    sys.exit()

Name = sys.argv[1]
Age = sys.argv[2]

print ('Hi ' + Name +', you are ' +str(Age)+ ' years old.')




