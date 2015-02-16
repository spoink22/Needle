import sys
filename = sys.argv[1]
try:
	fin = open (filename,'r')
except:
	print "File not found!"
	exit()
#split up document into words, split by whitespace
originalwords = fin.read().split()
#go through each word, and make them follow the same convention
newWords = []
for i in originalwords:
    #The next line makes each word lower case, stripped of its periods and commas. I could continue in the same manner to remove any other symbol, but since only periods and commas were mentioned, I'll just strip those for now.
    #however, with the current settings for things to take out, '(the' will be different from 'the', and the same for any other symbol.
    newWord = i.lower().replace('.','').replace(',','')
    newWords.append(newWord)
#At this point, we have a new list that has all of the original words conformed to the same convention
#Luckily, Python already has a way to easily get the count of a word in the list. We can easily compare a word's count to the count of every other word in the list like this:
count = 0
winner = []
#Go through each word in the list
for i in newWords:
    #If the current word has a higher count that what was previously the record
    if newWords.count(i) > count:
        count = newWords.count(i)
        winner = [i]
    #It wasn't mentioned that I had to do it, but in case of a tie I wanted to return all of the "winners". If there's a tie it will 
    elif newWords.count(i) == count:
        if i not in winner:
            winner.append(i)
#If there's no tie, do this:
if len(winner) == 1:
    print "The most used word in this document is the word: " + winner[0]
    print "which shows up " + str(count) + " times."
#It occurred to me at this point that there should be a case for empty files.
elif len(winner) == 0:
    print "The supplied file is empty, you cheater!"
#If there is a tie, do this:
else:
    print "It was a tie between the following words:"
    for w in winner:
        print "\t"+w
    print "which show up " + str(count) + " times."
