#!/usr/bin/python
#https://www.reddit.com/r/dailyprogrammer/comments/3yiy2d/20151228_challenge_247_easy_secret_santa/
import random

def pick_rnd_person(fam_id, family, people):
	while(True):
		rnd_partner = random.choice(list(people))
		if rnd_partner not in family[fam_id]:
			people.discard(rnd_partner)
			return rnd_partner
#------------------------------------------------------------------------
family = []
people = set()
#families247.txt simple_family.txt
with open("families247.txt") as fh:
	for line in fh:
		family.append(line.rstrip('\n').split(" "))

for fam in family:
	for n in fam:
		people.add(n)

family = sorted(family, key=len, reverse=True)	
total_families = len(family)
#print family[0][0] - first person in family #0
#print len(family[0]) - number of members of family 0

for fam_id in range(len(family)): #0 through number of families - 1
	if len(people) == 0:
		break
	family_size = len(family[fam_id])
	for individual in range(family_size):
		#print family[fam_id][individual]
		#if "Julie" in family[fam_id]:
		#	print "Julie is in this family"
		if family[fam_id][individual] in people:
			people.remove(family[fam_id][individual])
			rnd_partner = pick_rnd_person(fam_id, family, people)
			print "%s -> %s" %(family[fam_id][individual], rnd_partner)
		