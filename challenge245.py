#!/usr/bin/python
import re
#challenge 245 easy Date Dilemma
#https://www.reddit.com/r/dailyprogrammer/comments/3wshp7/20151214_challenge_245_easy_date_dilemma/

date = "2/13/15"
date2 = "1-31-10"
date3 = "5 1 2015"
date4 = "2012 3 17"
date5 = "2001-01-01"
date6 = "2008/01/07"

separated = re.split(r'[ /\-]', date3)
#print separated
	
def transform_year (yr):
	if len(yr) == 2:
		return "20" + yr
	else:
		return yr

def transform_other (x):
	if len(x) == 1:
		return '0' + x
	else:
		return x

if len(separated[0]) == 4:
	year = separated[0]
	month = transform_other(separated[1])
	day = transform_other(separated[2])
	print "%s-%s-%s" %(year, month, day)
else:
	month = transform_other(separated[0])
	day = transform_other(separated[1])
	year = transform_year(separated[2])
	print "%s-%s-%s" %(year, month, day)