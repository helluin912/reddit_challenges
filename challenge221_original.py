#!/usr/bin/python
#https://www.reddit.com/r/dailyprogrammer/comments/3bi5na/20150629_challenge_221_easy_word_snake/

#>>> 'hello world'[::-1]
#'dlrow olleh'

import sys

def print_spaces (num_spaces):
	temp_str = ""
	for i in range(num_spaces):
		temp_str += " "
	return temp_str
	
#in_str = "SHENANIGANS SALTY YOUNGSTER ROUND DOUBLET TERABYTE ESSENCE ESSENTIAL LOVER"
#in_str = "IT'S SHOWTIME EMILY"
in_str = "CAN NINCOMPOOP PANTS SCRIMSHAW WASTELAND DIRK KOMBAT TEMP PLUNGE ESTER REGRET TOMBOY"
words = in_str.split(' ')

across = True
across_length = 0
n = 0
#iterate over each word in words
while n < len(words):
	if across:
		if len(words[n]) >= across_length:
			#print the word left to right
			if across_length > 0:
				#fixes off by 1 character (too far right by 1 character)
				across_length = across_length - 1

			output_str = print_spaces(across_length)
			output_str += words[n]
			across_length += len(words[n])
			print output_str
			n += 1
		else:
			#print backwards
			back_str = print_spaces(across_length - len(words[n]))
			back_str += words[n][::-1]
			across_length = across_length - len(words[n]) + 1
			print back_str
			n += 1
	else:
		#print vertical
		for c in range (1,len(words[n])):
			if n < len(words) and c < len(words[n]) - 1:
				temp = print_spaces(across_length - 1)
				temp += words[n][c]
			#if there's another word in the sentence and we're on the last character of the word being printed vertically,
			#skip this last letter & have it be dealt with when being printed across
				print temp
		n += 1
	across = not across

#if the snake ends in a vertical, the last letter of the last word needs to be printed	
if across == True:
	temp = print_spaces(across_length - 1)
	temp += words[n-1][-1]
	print temp
