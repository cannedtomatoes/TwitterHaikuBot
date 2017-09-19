# -*- coding: utf-8 -*-
import re
import sys
from random import sample
import random
import syllables_en
from sentences import split_into_sentences

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
		
	
		
	

# Start main program

attempts = 4000 # attempts at finding sentence with given word

print("Haiku generator\n")
print("Input word or type 'r': ")
user_input = input()

if user_input == 'r':
	cword = random.choice(open('20k.txt').readlines())[:-1]
	word_is_random = True
else:
	cword = user_input
	word_is_random = False

#print("Word selected: ", word, "\n")

#sentences = []
fives = []
sevens = []

#print("Extracting sentences from text file")

with open('25b.txt') as f:
	sentences = split_into_sentences(f.read())

for sentence in sentences:
	s = ''.join(sentence) #turn sentence into string
	if CountSyllables(sentence) == 5:
		fives.append(sentence)
	if CountSyllables(sentence) == 7:
		sevens.append(sentence)

print("Number of sentences with five syllables: ", len(fives))
print("Number of sentences with seven syllables: ", len(sevens))

trials = 1
count = 1
sen1 = 'fail'
sen2 = 'fail'
sen3 = 'fail'

# Generate 3 sentences

while sen1 == 'fail' or sen2 == 'fail' or sen3 == 'fail':

	
	print("Attempting 5 syl with",cword)
	sen1 = GenSentence(cword, fives, attempts)
	print(sen1)
	
	print("Attempting 7 syl with",cword)
	sen2 = GenSentence(cword, sevens, attempts)	
	print(sen2)
	
	print("Attempting 5 syl with",cword)
	sen3 = GenSentence(cword, fives, attempts)
	print(sen3)
	
	trials += 1
	
	prevword = cword
	
	if word_is_random:
		print("Moving to next word")	
		cword = random.choice(open('20k.txt').readlines())[:-1]
	else:
		print("Giving up on", cword)
		sys.exit()



#Convert and clean sentences
sen1 = ''.join(sen1)
sen2 = ''.join(sen2)
sen3 = ''.join(sen3)

sen1.strip("[']")
sen2.strip("[']")
sen3.strip("[']")

#Print results
print("\nHaiku completed using seed word:", prevword, "after", trials, "trials\n")
print(sen1)
print(sen2)
print(sen3)

