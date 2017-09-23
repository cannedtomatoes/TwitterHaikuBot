# -*- coding: utf-8 -*-
import re
import sys
from random import sample
import random
import syllables_en
from sentences import split_into_sentences
from twython import Twython
from twython import TwythonStreamer


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

cword = random.choice(open('20k.txt').readlines())[:-1]
	
#sentences = []
fives = []
sevens = []

print("Extracting sentences and sorting sentences.")

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
	
		
	cword = random.choice(open('20k.txt').readlines())[:-1]
	
	


#Convert and clean sentences
sen1 = ''.join(sen1)
sen2 = ''.join(sen2)
sen3 = ''.join(sen3)


#sen1.strip()
#sen1.lstrip("'")
#sen1.lstrip().translate({ord(c): None for c in '"[]*_-'})
#sen2.strip()
#sen2.lstrip("'")
#sen2.lstrip().translate({ord(c): None for c in '"[]*_-'})
#sen3.strip()
#sen3.lstrip("'")
#sen3.lstrip().translate({ord(c): None for c in '"[]*_-'})

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

sen1.capitalize()
sen2.capitalize()
sen3.capitalize()

final = sen1 + '\n' + sen2 + '\n' + sen3
final.capitalize()

print("Posting:\n", final, "\n")

#Define our constant variables, this is all the data we wrote down in the first part of the tutorial.
CONSUMER_KEY = 	'wjcxNTp8xeyprkpDLg6sxi2k4'
CONSUMER_SECRET = 'QFup2rdBBfvNqhDInul7KLcAOAR83QCTjN1HokuqFI3ZrQrGJu'
ACCESS_KEY = '907828033503076354-4FGZZAi9rWwVnjIYPGUJcKmbObpVqba'
ACCESS_SECRET = 'sYsxpiteUc12kyQnYbWNl91xvGk71m3jFdQVeWySfF2Uv'

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) 
api.update_status(status = final)


