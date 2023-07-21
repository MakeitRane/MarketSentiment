import pandas as pd
import nltk
from statistics import mean
#nltk.download()

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

words_tokenized = word_tokenize(text.lower())

without_stop_words = []
for word in words_tokenized:

    if word not in stop_words:
        without_stop_words.append(word)


#print the set of stop words which were excluded from the sample test sentence
print(set(words_tokenized) - set(without_stop_words))

#all words which are not stop words
print(without_stop_words)



# SENTIMENT ANALYSIS, STEMMING, LEMMATIZATION
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.sentiment import SentimentIntensityAnalyzer, SentimentAnalyzer
demo_words = ["playing", "happiness", "going", "doing", "yes", "no", "I", "having", "had", "halved", "coding", "programming", "word", "rap", "genius", "go", "do"]

#lemmatization considers the context and converts the word to its meaning base form aka the lemma
#stemming removes the last few characters from a word
lemmatizer = WordNetLemmatizer() 
stemmer = PorterStemmer()

for word in demo_words:
    #left stem, right lemmatize
    print(word, stemmer.stem(word), lemmatizer.lemmatize(word, "v"))

#sentiment analysis
sent_int_anal = SentimentIntensityAnalyzer()

crypto_slang = {
    "Fomo": -0.2, 
    "FUD": -0.3,
    "fear uncertainty doubt": -0.3,
    "HODL": 0.2,
    "hold on for dear life": 0.2, 
    "shill": 0.4, 
    "rekt": 0.1, 
    "sats": 0.0, 
    "whale": 0.3, 
    "pump and dump": -0.1,
    "bagholder": 0.1, 
    "when lambo?": 0.3,  
    "flippening": 0.2, 
    "no coiner": 0.1,
    "vaporwave": 0.1,
    "BTD": 0.4,
    "BTFD": 0.45,
    "buy the dip": 0.4, 
    "buy the fucking dip": 0.45, 
    "cryptosis": 0.3,
    "KYC": 0.1,
    "know your customer": 0.1, 
    "addy": 0.0,
    "airdrop": 0.1, 
    "altcoin": 0.1, 
    "bear": -0.3,
    "bearwhale": -0.4, 
    "blocks": 0.2,
    "block reward": 0.2, 
    "bitcoin maximalist": 0.2,
    "bull": 0.3,
    "consensus": 0.1, 
    "cryptography": 0.0,
    "cryptojacking": -0.4,
    "decentralization": 0.1,  
    "defi": 0.1, 
    "dex": 0.2,
    "double-spend": 0.2,  
    "exchange": 0.0,
    "exit scam": -0.3,
    "fiat": 0.1,
    "gas": 0.0,
    "gwei": 0.0,
    "hash": 0.1, 
    "immutability": 0.1,
    "lambo": 0.4,
    "mining": 0.1,
    "mempool": 0.2,
    "moon": 0.1,
    "nocoiner": 0.2,
    "node": 0.0, 
    "p2p": 0.0, 
    "peer-to-peer": 0.0,
    "private key": 0.1,
    "public key": 0.2,
    "proof-of-stake": 0.1,
    "proof-of-work": 0.1,
    "public key": 0.0,
    "proof-of": 0.0,
    "satoshi": 0.0,
    "seed phrases": 0.0, 
    "shitcoin": -0.1,
    "smart contract": 0.0,
    "stablecoin": 0.1,
    "wallet": 0.0,
    "weak hands": -0.1,
    "ATH": 0.5,
    "all time high": 0.5,
    "DYOR": 0.0,
    "do your own research": 0.0,
    "EVM": 0.0, 
    "ethereum virtual machine": 0.0,
    "FOMO": -0.2,
    "fear of missing out": -0.2,
    "ICO": 0.1,
    "initial coin offering": 0.1,
    "WAGMI": 0.4,
    "we’re all gonna make it": 0.4,
    "NGMI": -0.4, 
    "not gonna make it": -0.4,
    "NFA": 0.0,
    "not financial advice": 0.0,
    "rugged": -0.2,
    "rugpull": -0.3, 
    "wen moon": 0.3, 
    "SAFU": 0.0,
    "paper hands": -0.2,
    "diamond hands": 0.2, 
    "dApp": 0.0, 
    "LFG": 0.3,
    "let’s fucking go": 0.3, 
    "degen": 0.0,
    "‘probably nothing’": 0.2
}

sent_int_anal.lexicon.update(crypto_slang)

#prints scores for sentiment analysis
def sent_analysis(tweet) -> float:
    scores = sent_int_anal.polarity_scores(tweet)["compound"]
    return scores

#Why I believe $BTC will reach between $100K - $200K and $ETH $16K - $34K in the next bull run.
#print(sent_int_anal.score_valence)
#print(sent_int_anal.print_valence())
