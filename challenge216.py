#!/usr/bin/python
import random
#Challenge 216 Easy
#Deals out the cards and prints out the players' hands
cards = list(range(0,52))
deck = {}
for n in cards:
	deck[n] = 0

# n divide by 13 = suit. 0 -> hearts, 1 -> diamonds, 2 -> spades, 3 -> clubs
# n mod 13 = value. 0 = ace, 1 = 2 ... 12 = king
suit = {
	0 : "Hearts",
	1 : "Diamonds",
	2 : "Spades",
	3 : "Clubs",
}

values = {
	0 : "Ace of",
	1 : "2 of",
	2 : "3 of",
	3 : "4 of",
	4 : "5 of",
	5 : "6 of",
	6 : "7 of",
	7 : "8 of",
	8 : "9 of",
	9 : "10 of",
	10 : "Jack of",
	11 : "Queen of",
	12: "King of",
}
def burn_card (cards, deck):
	generate = True
	while (generate):
		n = random.choice(cards)
		if (deck[n] == 0):
			deck[n] = 1
			generate = True
			return

def flip_card (cards, deck, num):
	i = 0
	card_list = []
	while (i < num):
		n = random.choice(cards)
		if (deck[n] == 0):
			deck[n] = 1
			card_list.append(n)
			i += 1
	return card_list

def which_card(urhand):
	hand = ""
	count = 0
	while (count < len(urhand)):
		div = urhand[count] / 13
		mod = urhand[count] % 13
		count += 1
		hand += " %s %s," % (values[mod], suit[div])	
	return hand[:-1]

players = int(raw_input("How many players (2-8)? "))
your_hand = flip_card(cards, deck, 2)
print "Your hand:%s" % which_card(your_hand)
for i in range (1, players):
	temp_hand = flip_card(cards, deck, 2)
	print "CPU %s:%s" % (str(i), which_card(temp_hand))
	
burn_card(cards, deck)
flop = flip_card(cards, deck, 3)
burn_card(cards, deck) 
turn = flip_card(cards, deck, 1)
burn_card(cards, deck)
river = flip_card(cards, deck, 1)

print
print "Flop:%s" % which_card(flop)
print "Turn:%s" % which_card(turn)
print "River:%s" % which_card(river)
#rnd = random.choice(cards)

#unused = 0
#for i in range (len(cards)):
#	if deck[i] == 0:
#		unused += 1
#print unused

# (players * 2) + (3 burns) + (3 flop) + (1 turn) + (1 river)
# 16 + 3 + 3 + 1 + 1 = 24 used. 52 -24 = 28
#deal to players, burn, flop, burn, turn, burn, river