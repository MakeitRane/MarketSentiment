import pandas as pd
import nltk

text = """This is a test sentence. I love testing things because they're so wonderful. It's really insane how the standards for testing have grown over the years."""

#word tokenization
from nltk.tokenize import word_tokenize
#words = word_tokenize(text)

#sentence tokenization
#from nltk.tokenize import sent_tokenize
#print(sent_tokenize(text))

#takes a parameter as tokenized words
#gives number of samples and outcomes
from nltk.probability import FreqDist 
#fd = FreqDist(words)
#print(fd.most_common(3))



#stop words --> words which NLTK will ignore
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english')) #default list of stop words in a set to remove repetition
#print(stop_words) 

#CHANGE - removed text.lower
words_tokenized = word_tokenize(text)

without_stop_words = []
for word in words_tokenized:

    if word not in stop_words:
        without_stop_words.append(word)


#print the set of stop words which were excluded from the sample test sentence
#print(set(words_tokenized) - set(without_stop_words))

#all words which are not stop words
#print(without_stop_words)



# SENTIMENT ANALYSIS, STEMMING, LEMMATIZATION
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.sentiment import SentimentIntensityAnalyzer, SentimentAnalyzer
demo_words = [""]

#lemmatization considers the context and converts the word to its meaning base form aka the lemma
#stemming removes the last few characters from a word
lemmatizer = WordNetLemmatizer() 
stemmer = PorterStemmer()

#for word in demo_words:
    #left stem, right lemmatize
    #print(word, stemmer.stem(word), lemmatizer.lemmatize(word, "v"))

#sentiment analysis
sent_int_anal = SentimentIntensityAnalyzer()

#prints scores for sentiment analysis
print(sent_int_anal.polarity_scores("$BTC touched $30000 for the first time since April. We are so back. TO THE MOON."))
#Why I believe $BTC will reach between $100K - $200K and $ETH $16K - $34K in the next bull run.
#print(sent_int_anal.score_valence)
#print(sent_int_anal.print_valence())








