# Haiku bot - Chris Pocock
# Reads some file of random text and detects sentences with 5 and 7 syllables
# and turns them into Haiku poems

import sys
import re
import textstat
from textstat.textstat import textstat

import random
from twython import Twython
from twython import TwythonStreamer
import json

#Function to count syllables
def CountSyllables(word, isName=True):
    vowels = "aeiouy"
    #single syllables in words like bread and lead, but split in names like Breanne and Adreann
    specials = ["ia","ea"] if isName else ["ia"]
    specials_except_end = ["ie","ya","es","ed"]  #seperate syllables unless ending the word
    currentWord = word.lower()
    numVowels = 0
    lastWasVowel = False
    last_letter = ""

    for letter in currentWord:
        if letter in vowels:
            #don't count diphthongs unless special cases
            combo = last_letter+letter
            if lastWasVowel and combo not in specials and combo not in specials_except_end:
                lastWasVowel = True
            else:
                numVowels += 1
                lastWasVowel = True
        else:
            lastWasVowel = False

        last_letter = letter

    #remove es & ed which are usually silent
    if len(currentWord) > 2 and currentWord[-2:] in specials_except_end:
        numVowels -= 1

    #remove silent single e, but not ee since it counted it before and we should be correct
    elif len(currentWord) > 2 and currentWord[-1:] == "e" and currentWord[-2:] != "ee":
        numVowels -= 1

    return numVowels
#End function    
    
#success = False
#count = 0

#Define our constant variables, this is all the data we wrote down in the first part of the tutorial.
CONSUMER_KEY = 	
CONSUMER_SECRET = 
ACCESS_KEY = 
ACCESS_SECRET = 

#Create a copy of the Twython object with all our keys and secrets to allow easy commands.
api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) 



#optionally generate random word
#word = random.choice(open('20k.txt').readlines())[:-1]
word = 'Trump'

print 'Random word: ', word

twitter=Twython(
    CONSUMER_KEY,
    CONSUMER_SECRET,
    ACCESS_KEY,
    ACCESS_SECRET
    )

# Find first line - 5 syllables
success = False

while success == False:

	results = twitter.search(q = word, count = 100)


	tweets = results['statuses']
	for tweet in tweets:
		tw = tweet['text']
		tw_clean = re.sub(r"http\S+", "", tw)
		if CountSyllables(tw_clean) == 5:
			print(tw_clean)
			success = True
		#break
		
		else:
			count += 1
			if count > 100
				break
		
# Find second line - 7 syllables
success = False

while success == False:

	results = twitter.search(q = word, count = 100)


	tweets = results['statuses']
	for tweet in tweets:
		tw = tweet['text']
		tw_clean = re.sub(r"http\S+", "", tw)
		if CountSyllables(tw_clean) == 7:
			print(tw_clean)
			success = True


# Find third line - 5 syllables
success = False

while success == False:

	results = twitter.search(q = word, count = 100)


	tweets = results['statuses']
	for tweet in tweets:
		tw = tweet['text']
		tw_clean = re.sub(r"http\S+", "", tw)
		if CountSyllables(tw_clean) == 5:
			print(tw_clean)
			success = True

#Using our newly created object, utilize the update_status to send in the text passed in through CMD
#api.update_status(status=s1)
