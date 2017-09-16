import re
import sys
from random import sample
import random


# Function to count syllables
def CountSyllables(word, isName=True):
	vowels = "aeiouy"
	# single syllables in words like bread and lead, but split in names like Breanne and Adreann
	specials = ["ia", "ea"] if isName else ["ia"]
	specials_except_end = ["ie", "ya", "es", "ed"]  # seperate syllables unless ending the word
	currentWord = word.lower()
	numVowels = 0
	lastWasVowel = False
	last_letter = ""

	for letter in currentWord:
		if letter in vowels:
			# don't count diphthongs unless special cases
			combo = last_letter + letter
			if lastWasVowel and combo not in specials and combo not in specials_except_end:
				lastWasVowel = True
			else:
				numVowels += 1
				lastWasVowel = True
		else:
			lastWasVowel = False
		last_letter = letter

	# remove es & ed which are usually silent
	if len(currentWord) > 2 and currentWord[-2:] in specials_except_end:
		numVowels -= 1
	# remove silent single e, but not ee since it counted it before and we should be correct
	elif len(currentWord) > 2 and currentWord[-1:] == "e" and currentWord[-2:] != "ee":
		numVowels -= 1

	return numVowels
# End function
# -------------------------

# Start main program
print("Haiku generator\n")
print("Input word or type 'random': ")
input = input()

if input == 'random':
	word = random.choice(open('20k.txt').readlines())[:-1]
	word_is_random = True
else:
	word = input
	word_is_random = False

print("Word selected: ", word, "\n")

sentences = []
# for i in range(20):
#   with open('10b.txt'.format(i)) as f:
#       sentences += re.findall(r".*?[\.\!\?]+", f.read())

f = open('20b.txt')
sentences += re.findall(r".*?[\.\!\?]+", f.read())

# Sentence 1
success = False
count = 0

while success == False:
	while count < 101:
		s1 = sample(sentences, 1)
		temp1 = ''.join(s1)
		temp2 = temp1.split()

		if CountSyllables(temp1) == 5:
			if word in temp2:
				success = True
				print(s1)
				break
			else:
				count += 1

		if count == 100:
			if word_is_random == True:
				print("Giving up on ", word, ", trying new word: ")
				word = random.choice(open('20k.txt').readlines())[:-1]
				print(word, "\n")
				counter = 0
			else:
				print("Giving up on", word)
				sys.exit()

# Sentence 2
success = False
count = 0

while success == False:
	while count < 101:
		s1 = sample(sentences, 1)
		temp1 = ''.join(s1)
		temp2 = temp1.split()

		if CountSyllables(temp1) == 7:
			if word in temp2:
				success = True
				print(s1)
				break
			else:
				count += 1

		if count == 100:
			if word_is_random == True:
				print("Giving up on ", word, ", trying new word: ")
				word = random.choice(open('20k.txt').readlines())[:-1]
				print(word, "\n")
				counter = 0
			else:
				print("Giving up on", word)
				sys.exit()

# Sentence 3
success = False
count = 0

while success == False:
	while count < 101:
		s1 = sample(sentences, 1)
		temp1 = ''.join(s1)
		temp2 = temp1.split()

		if CountSyllables(temp1) == 5:
			if word in temp2:
				success = True
				print(s1)
				break
			else:
				count += 1

		if count == 100:
			if word_is_random == True:
				print("Giving up on ", word, ", trying new word: ")
				word = random.choice(open('20k.txt').readlines())[:-1]
				print(word, "\n")
				counter = 0
			else:
				print("Giving up on", word)
				sys.exit()
