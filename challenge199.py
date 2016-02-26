#!/usr/bin/python
#https://www.reddit.com/r/dailyprogrammer/comments/2tr6yn/
DIGITS = """
    _  _     _  _  _  _  _
  | _| _||_||_ |_   ||_||_|
  ||_  _|  | _||_|  ||_| _| 
"""

FONT = range(10)
FONT[0] = """
._.
| |
|_|
""".splitlines()
FONT[1] = """
...
.|.
.|.
""".splitlines()
FONT[2] = """
._.
._|
|_.
""".splitlines()

FONT[3] = """
._.
._|
._|
""".splitlines()
FONT[4] = """
...
|_|
..|
""".splitlines()
FONT[5] = """
._.
|_.
._|
""".splitlines()
FONT[6] = """
._.
|_.
|_|
""".splitlines()
FONT[7] = """
._.
..|
..|
""".splitlines()
FONT[8] = """
._.
|_|
|_|
""".splitlines()
FONT[9] = """
._.
|_|
._|
""".splitlines()
number_to_print = "1234567890"
output = ""
for row in range(4):
	for digit in number_to_print:
		int_digit = int(digit)
		output += FONT[int_digit][row]
	output += "\n"

output = output.replace('.', ' ')
print output
import sys
sys.exit(0)


Matrix = [["0" for x in range(5)] for x in range(5)]

for x in range(5):
	for y in range(5):
		Matrix[x][y] = "%s, %s" % (x, y)
		#Matrix[x][y] = "%s" % x
		
#print Matrix
top_row = "^".join(Matrix[x][0] for x in range(5))
print top_row