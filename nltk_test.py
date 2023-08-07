import pandas as pd
import nltk
from statistics import mean
#nltk.download()
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.sentiment import SentimentIntensityAnalyzer, SentimentAnalyzer


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




class Preprocessing:
    def sent_analysis(tweet) -> float:
        # Tokenize the words, so you can break up the entire tweet into a list of words
        words_tokenized = word_tokenize(tweet.lower())

        # Set the stop words to filter out of tweet
        stop_words = set(stopwords.words('english'))

        without_stop_words = []
        # Loop to create a list without stop words
        for word in words_tokenized:
            if word not in stop_words:
                without_stop_words.append(word)

        # create stemmer object from PorterStemmer class
        stemmer = PorterStemmer()

        stemmed_words =[]
        # stem words and then append to new list
        for word in without_stop_words:
            stemmed_words.append(stemmer.stem(word)) 

        # Rejoin stemmed words
        stemmed_text = ' '.join(stemmed_words)

        # Instantiate class for SentimentIntensityAnalyzer
        sent_int_anal = SentimentIntensityAnalyzer()

        # update the crypto slang to the vader list
        sent_int_anal.lexicon.update(crypto_slang)

        # find the polarity score of the words
        scores = sent_int_anal.polarity_scores(stemmed_text)["compound"]
        return scores


def final_score(score_list, count):
    score = 0
    for item in score_list:
        score = score + int(item)
    score/count
