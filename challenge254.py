#!/usr/bin/python
#https://www.reddit.com/r/dailyprogrammer/comments/45w6ad
import unittest
import string

#cipher_keys = list(map(chr, range(ord('a'), ord('z')+1)))
#alpha = list(map(chr, range(97, 123)))
cipher = {}
for alpha in (string.lowercase, string.uppercase):
	for i in range(0,26):
		cipher[alpha[i]] = alpha[25-i]

def translate(str):
	ret_str = ""
	for ch in str:
		if ch in cipher:
			ret_str += cipher[ch]
		else:
			ret_str += ch
	return ret_str

class TestTranslate(unittest.TestCase):
	def test_erin(self):
		self.assertEqual(translate('Erin'), 'Virm')
		
	def test_reddit(self):
		self.assertEqual(translate('/r/dailyprogrammer'), '/i/wzrobkiltiznnvi')
		
	def test_wizard(self):
		self.assertEqual(translate('wizard'), 'draziw')
		
	def test_garbled(self):
		self.assertEqual(translate('Gsrh rh zm Vcznkov lu gsv ZgyZhs Xrksvi'), 'This is an Example of the AtbAsh Cipher')
		
	def test_oops(self):
		self.assertEqual(translate('oops'), 'llkh')
#input = raw_input()
#print translate(input)

if __name__ == '__main__':
	unittest.main()