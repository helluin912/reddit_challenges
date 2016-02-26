#!/usr/bin/python

import random
import string
SPECIAL = "~!@#$%^&*()-+=?<>/.,\\|"

#nums = "".join([random.choice(string.digits) for i in xrange(4)])
#chars = "".join([random.choice(string.letters) for i in xrange(4)])

#print nums + chars
def gen_pw(num_chars):
	new_pw = ""
	for i in xrange(int(pw_length)):
		if i % 3 == 0:
			#new_pw += "".join([random.choice(string.digits) for i in xrange(1)])
			new_pw += random.choice(string.digits)
		elif i % 3 == 1:
			new_pw += random.choice(string.letters)
		else:
			new_pw += random.choice(SPECIAL)
	
	return new_pw
	
def gen_pw2(num_chars):
	char_class = [string.digits, string.letters, SPECIAL]
	return "".join([random.choice(char_class[i % len(char_class)]) for i in range(int(num_chars))])

num_of_pw = raw_input("Please enter the number passwords to generate: ")
if (num_of_pw.isdigit()):

	pw_length = raw_input("Please enter the length for your password: ")
	if (pw_length.isdigit()):
		for i in xrange(int(num_of_pw)):
			password = gen_pw2(pw_length)
			print password
	else:
		print "Your password length value was not a valid integer"
else:
	print "Not a valid number of passwords to generate"