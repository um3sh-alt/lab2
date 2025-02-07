#!/usr/bin/env python3

# Author: Umesh Pandey
# Author ID: upandey3
# Date Created: 2025/02/07

import sys
if len(sys.argv) == 1:
    timer = 3
elif len(sys.argv) != 1:
    timer = int(sys.argv[1])
while timer != 0:
    print (timer)
    timer = timer -1
print ('blast off!')
