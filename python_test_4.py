import sys

def decoder (sentence):
    key = "abcdefghijklmnopqrstuvwxyz"
    sentence = sentence.lower()
    score = 0
    for l in sentence:
        if l in key:
            score = score + 1 + key.index(l)
    return str(score)

filename = sys.argv[1]
fin = open (filename,'r')
#It says I can assume that the file given will follow standard English practices. I found when I split by a period and two spaces it would cut off the final
#period of all but the last sentence of the document. As far as I know, there's no other reason to use two spaces together in English, so it should work to just split
#by double spaces, but if that doesn't work, it's an error of my knowledge of English, not coding.
sentences = fin.read().split('  ')
for i in sentences:
    print i + ", " + decoder(i)
