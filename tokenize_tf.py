from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.lancaster import LancasterStemmer
from collections import Counter
import string
import operator
import math

stemmer = LancasterStemmer()
def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed
def termFrequency(term, document):
    normalizeDocument = document
    return normalizeDocument.count(term) / float(len(normalizeDocument))

stopset = set(stopwords.words('english'))
punc = list(string.punctuation)
punc.append("''")
punc.append("...")

output = open("output.txt","w")
with open('sample.txt', 'r') as text_file:
	for word in text_file:
		if 'index' in word:
			ind = 'C' + word[6: ]
			#print ind
			output.write(ind)
			output.write("[")
		if '#!' in word:
			tokens=word_tokenize(str(word))
			tokens = [w for w in tokens if not w in stopset if not w in punc]
			stems = stem_tokens(tokens, stemmer)
			#print stems
			stems.sort()
			#print stems
			"""counts = Counter(stems)
			counts = sorted(counts.items(),key=lambda item: item[0])
			print(counts)"""
			pre="ggg"
			c=0
			for t in stems:
                        	tf = termFrequency(t, stems)
				if t == pre:
					continue
				pre=t
				#c=c+1;				
				output.write(t)
				output.write(":")
				output.write(str(round(tf,4)))
				output.write(" ")
			output.write("]")
			#output.write(",")
			#output.write(str(c))
			output.write("\n")

				

