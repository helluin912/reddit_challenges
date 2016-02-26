#!/usr/bin/python

words = []
with open("input228.txt") as fh:
	for line in fh:
		words.append(line.rstrip('\n'))

for text in words:
	letters = list(text)
	letters.sort()
	test_str = ''.join(letters)
	if test_str == text:
		print "%s IN ORDER" % text
	else:
		print "%s NOT IN ORDER" % text