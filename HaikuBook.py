# -*- coding: utf-8 -*-
import re
import sys
from random import sample
import random
import syllables_en
from sentences import split_into_sentences
import time
import argparse

#Function to count syllables
def CountSyllables(word, isName=True):
	return syllables_en.count(word)

def GenSentence(rword, slist, att):
	
	count = 0
	
	while count <= att:
	
		s1 = sample(slist, 1)
		s2 = ''.join(s1)
		#s3 = s2 # version of the sentence for use in deletion from sentences vector
		s2 = s2.split()

		#print("Attempt ", count)

		if rword in s2:
			return s1
			break
			
		if count == att:
			return 'fail'
			break
		
		count += 1
		
#Process arguments
parser = argparse.ArgumentParser()
parser.add_argument('-r', '--random', help='Create Haiku based on random word', action="store_true")
parser.add_argument('-s', '--specific', help='Create Haiku based on specific word', action="store")
args = parser.parse_args()
	

# Start main program

attempts = 4000 # attempts at finding sentence with given word

print("Haiku generator\n")
#print("Input word or type 'r': ")
#user_input = input()

start = time.time()

if args.random:
	cword = random.choice(open('20k.txt').readlines())[:-1]
	word_is_random = True
else:
	cword = args.specific
	word_is_random = False
	print("Specific word chosen:", args.specific)

#print("Word selected: ", word, "\n")

#sentences = []
fives = []
sevens = []

print("Extracting and sorting sentences.")

with open('40b.txt') as f:
	sentences = split_into_sentences(f.read())

for sentence in sentences:
	s = ''.join(sentence) #turn sentence into string
	if CountSyllables(sentence) == 5:
		fives.append(sentence)
	if CountSyllables(sentence) == 7:
		sevens.append(sentence)

#print("Number of sentences with five syllables: ", len(fives))
#print("Number of sentences with seven syllables: ", len(sevens))

trials = 1
count = 1
sen1 = 'fail'
sen2 = 'fail'
sen3 = 'fail'

# Generate 3 sentences

print("Generating Haiku.")

while sen1 == 'fail' or sen2 == 'fail' or sen3 == 'fail':

	
	#print("Attempting 5 syl with",cword)
	sen1 = GenSentence(cword, fives, attempts)
	#print(sen1)
	
	#print("Attempting 7 syl with",cword)
	sen2 = GenSentence(cword, sevens, attempts)	
	#print(sen2)
	
	#print("Attempting 5 syl with",cword)
	sen3 = GenSentence(cword, fives, attempts)
	#print(sen3)
	
	trials += 1
	
	if sen1 == sen2 or sen1 == sen3 or sen2 == sen3:
		sen1 = 'fail'
		sen2 = 'fail'
		sen3 = 'fail'
	
	prevword = cword
	
	if word_is_random:
		#print("Moving to next word")	
		cword = random.choice(open('20k.txt').readlines())[:-1]
	
	if word_is_random == False and trials == 1000: #let's make sure it gives up eventually
		print("Giving up on", cword)
		sys.exit()

print("Sanitising text.")

#Convert and clean sentences
sen1 = ''.join(sen1)
sen2 = ''.join(sen2)
sen3 = ''.join(sen3)

for i in range(len(sen1)):
    if sen1[i].isalpha():        #True if its a letter
    	pos = i                   	#first letter position
    	break

sen1 = sen1[pos:]

for i in range(len(sen2)):
    if sen2[i].isalpha():        #True if its a letter
    	pos = i                   	#first letter position
    	break

sen2 = sen2[pos:]

for i in range(len(sen3)):
    if sen3[i].isalpha():        #True if its a letter
    	pos = i                   	#first letter position
    	break

sen3 = sen3[pos:]

for ch in ['\"', '[', ']', '*', '_', '-']:
	if ch in sen1:
		 sen1 = sen1.replace(ch,"")
		 
for ch in ['\"', '[', ']', '*', '_', '-']:
	if ch in sen2:
		 sen2 = sen2.replace(ch,"")

for ch in ['\"', '[', ']', '*', '_', '-']:
	if ch in sen3:
		 sen3 = sen3.replace(ch,"")

sen1.strip()
sen2.strip()
sen3.strip()

sen1.capitalize()
sen2.capitalize()
sen3.capitalize()

final = sen1 + '\n' + sen2 + '\n' + sen3

end = time.time()

#Print results
print("\nHaiku completed using seed word:", prevword, "after", trials, "trials and", round(end-start), "seconds.\n")
print(final)
#print(sen1)
#print(sen2)
#print(sen3)
print("\n")

