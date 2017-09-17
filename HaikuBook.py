import re
import sys
from random import sample
import random
import syllables_en
from sentences import split_into_sentences

#Function to count syllables
def CountSyllables(word, isName=True):
	return syllables_en.count(word)

# Start main program
def main():
	attempts = 4000 # attempts at finding sentence with given word

	print("Haiku generator\n")
	print("Input word or type 'r': ")
	user_input = input()

	if user_input == 'r':
		word = random.choice(open('20k.txt').readlines())[:-1]
		word_is_random = True
	else:
		word = input
		word_is_random = False

	#print("Word selected: ", word, "\n")

	#sentences = []
	fives = []
	sevens = []

	#for i in range(20):
	#   with open('10b.txt'.format(i)) as f:
	#       sentences += re.findall(r".*?[\.\!\?]+", f.read())

	#print("Extracting sentences from text file")

	with open('20b.txt', encoding='utf-8') as f:
		sentences = split_into_sentences(f.read())

	for sentence in sentences:
		s = ''.join(sentence) #turn sentence into string
		if CountSyllables(sentence) == 5:
			fives.append(sentence)
		if CountSyllables(sentence) == 7:
			sevens.append(sentence)

	#print("Number of sentences with five syllables: ", len(fives))
	#print("Number of sentences with seven syllables: ", len(sevens))

	wins = 0
	success1 = False
	success2 = False
	success3 = False

	while wins != 3:

		#Sentence 1

		count = 0

		while success1 == False:

			while count < (attempts + 1):

				s1 = sample(fives, 1)
				s2 = ''.join(s1)
				s2 = s2.split()

				#print("Attempt ", count)

				if word in s2:
					success1 = True
					wins += 1
					sen1 = s1
					break
				else:
					count += 1
					#print("Attempt ", count, "failed")

				if count == attempts:
					if word_is_random == True:
						#print("Giving up on ", word, ", trying new word: ")
						word = random.choice(open('20k.txt').readlines())[:-1]
						#print(word, "\n")
						count = 0


					else:
						print("Giving up on", word)
						sys.exit()


		#Sentence 2

		count = 0

		while success2 == False:

			while count < (attempts + 1):

				s1 = sample(sevens, 1)
				s2 = ''.join(s1)
				s2 = s2.split()

				#print("Attempt ", count)

				if word in s2:
					success2 = True
					wins += 1
					sen2 = s1
					break
				else:
					count += 1
					#print("Attempt ", count, "failed")

				if count == attempts:
					if word_is_random == True:
						#print("Giving up on ", word, ", trying new word: ")
						word = random.choice(open('20k.txt').readlines())[:-1]
						#print(word, "\n")
						count = 0


					else:
						print("Giving up on", word)
						sys.exit()

		#Sentence 3

		count = 0

		while success3 == False:

			while count < (attempts + 1):

				s1 = sample(fives, 1)
				s2 = ''.join(s1)
				s2 = s2.split()


				if word in s2:
					success3 = True
					wins += 1
					sen3 = s1
					break
				else:
					count += 1

				if count == attempts:
					if word_is_random == True:
						#print("Giving up on ", word, ", trying new word: ")
						word = random.choice(open('20k.txt').readlines())[:-1]
						#print(word, "\n")
						count = 0

					else:
						print("Giving up on", word)
						sys.exit()

	#Print results
	print("\nHaiku completed using seed word", word, "\n")
	print(sen1)
	print(sen2)
	print(sen3)

if __name__ == "__main__":
	main()
