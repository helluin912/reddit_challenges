#!/usr/bin/python
import string
all_letters = string.letters

def scramble (word):
	word = word.lower()
	punctuation = -1
	for n in range(len(word)):
		# if not word[n] in all_letters:
		if word[n] not in all_letters:
			punctuation = n
	
	ch  = ''.join(sorted(word))
	if punctuation != -1:
		ch = ch[1:]
		#has punctuation somewhere
	
	new_word = ''
	i = 0
	while (i < len(ch)):
		if i == punctuation:
			new_word += word[i]
			new_word += ch[i]
		else:
			new_word += ch[i]
			#print "%s : %s" %(str(i), new_word)
		i += 1
	
	if punctuation == (len(word) - 1):
		new_word += word[punctuation]
	return new_word
	
input_str = raw_input("Enter a string: ")
#input_str = "traveller"
words = input_str.split()
sorted_words = []

for i in words:
	i = scramble(i)
	sorted_words.append(i)

sorted_words[0]	= sorted_words[0][0:1].upper() + sorted_words[0][1:]
print ' '.join(sorted_words)