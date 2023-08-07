import requests
import nltk
import pandas as pd
from web_scraper import WebScraper
#from nltk_test import sent_analysis
from nltk_test import final_score
from nltk_test import Preprocessing


def main():
    coin_name = input("Want the market sentiment for a particular cryptocurrency? Type its ticker here: ")
    pos_tweets = [] #positive tweets
    neg_tweets = [] #negative tweets
    neu_tweets = [] #neutral tweets

    #put coin name/ticker into twitter api search
    webscraper = WebScraper()
    tweets = webscraper.scrape_data(coin_name)

    #while loop to process each tweet
    #curr_tweet_num = 0

    #gets compound score and organizes it accordingly
    preprocessing = Preprocessing(tweets)
    for tweet in tweets:#
        score = preprocessing.sent_analysis(tweet)
        if score == 0:
            neu_tweets.append(tweet)
        elif score > 0:
            pos_tweets.append([tweet, score])
        else:
            neg_tweets.append([tweet, score])

    #number of positive, negative, and neutral tweets. can be used for further analysis or extra metrics
    num_pos_tweets = len(pos_tweets)
    num_neg_tweets = len(neg_tweets)
    num_neu_tweets = len(neu_tweets)

    

    #give final score between 0-10
    pos_score = final_score(pos_tweets, num_pos_tweets)
    neg_score = final_score(neg_tweets, num_neg_tweets)
    neu_score = final_score(neu_tweets, num_neu_tweets)

    final_score = 10*(pos_score+neg_score+neu_score)/3
    return final_score
    #idea: get average positive, negative, and neutral, whichever is highest multiply by 10 and that's the sentiment?



    
