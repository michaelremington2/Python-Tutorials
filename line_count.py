#!/usr/bin/python
import sys

# sys.argv is the list of command line arguments
# sys.agrv[0] is the name of the program itself
# sys.argv[1] will be the command line argument


# for every line passed into the script
count = 0
for line in sys.stdin:
	count += 1

print(count)