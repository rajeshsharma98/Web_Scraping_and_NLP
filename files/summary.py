from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem.snowball import SnowballStemmer
import nltk

"""
Steps to build a Summarizer
1.Remove stop words  for the analysis.
2.Create frequency table of words - how many times each word appears in the text.
3.Assign score to each sentence depending on the words it contains and the frequency table created above.
4. Build summary by adding every sentence above a certain score threshold.
"""

class use:
	def fun(text):
		stemmer = SnowballStemmer("english")
		stopWords = set(stopwords.words("english"))
		words = word_tokenize(text)

		#Dictionary for word frequency table
		frequencyTable = dict()
		for word in words:
			word = word.lower()
			if word in stopWords:
				continue
			word = stemmer.stem(word)
			if word in frequencyTable:
				frequencyTable[word] += 1
			else:
				frequencyTable[word] = 1

		sentences = sent_tokenize(text)
		sentenceValue = dict()						 # to keep score of each sentence

		#algorithm used to score the sentences: adding the frequency of every non-stop word in a sentence.
		for sentence in sentences:
			for word, frequency in frequencyTable.items():
				if word in sentence.lower():
					if sentence in sentenceValue:
						sentenceValue[sentence] += frequency
					else:
						sentenceValue[sentence] = frequency

		sumValues = 0
		for sentence in sentenceValue:
			sumValues += sentenceValue[sentence]

		# Average value of a sentence from original text
		average = int(sumValues / len(sentenceValue))

		brief = ' '   #initialize
		for sentence in sentences:
			if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
				brief += " " + sentence
		# print(len(brief))
		return(brief)

# u=use()
# u.fun(para)
