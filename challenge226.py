#!/usr/bin/python
#Easy #226

def gcd(a, b):
	#Euclidean algorithm explanation
	#http://www.programiz.com/python-programming/examples/hcf
	while (b):
		a, b = b, a % b
		
	return a

	
#input = ['2', '1/6', '3/10']
#input = ['3', '1/3', '1/4', '1/12']
input = ['10', '1/7', '35/192', '61/124', '90/31', '5/168', '31/51', '69/179', '32/5', '15/188', '10/17']
#input = ['5', '2/9', '4/35', '7/34', '1/2', '16/33']
#5 inputs : 89962/58905
#10 inputs : 351910816163/29794134720

if not input:
	print "You have an empty list of inputs!"
else:
	fractions = []
	for i in range (1, int(input[0]) + 1, 1):
		fractions.append(input[i].split("/"))
		
	denominator = 1
	for i in range(0, len(fractions), 1):
		denominator *= int(fractions[i][-1])

	numerator = 0
	for i in range(0, len(fractions), 1):
		temp = denominator / int(fractions[i][-1])
		numerator += (temp * int(fractions[i][0]))

	#print numerator
	#print denominator

	gcd = gcd(denominator, numerator)
	#print gcd
	print "%s/%s" % (str(numerator/gcd), str(denominator/gcd))