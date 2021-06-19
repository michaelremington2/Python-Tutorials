#!/usr/bin/python
import sys, re

# sys.argv is the list of command line arguments
# sys.agrv[0] is the name of the program itself
# sys.argv[1] will be the command line argument

regex = sys.argv[1]

# print(sys.argv)
# print(regex)
# for every line passed into the script

for line in sys.stdin:
	if re.search(regex, line):
		sys.stdout.write(line)


# pipe command cat somefile.txt | python egrep.py "\W*(cat)\W*" | python line_count.py
