import requests
import nltk
import pandas as pd
from web_scraper import WebScraper
#from packages_test import sent_analysis

"""def main():
    coin_name = input("Want the market sentiment for a particular cryptocurrency? Type its ticker here: ")
    pos_tweets = [] #positive tweets
    neg_tweets = [] #negative tweets
    neu_tweets = [] #neutral tweets

    #put coin name/ticker into twitter api search
    tweets = twitter_data(coin_name)

    #while loop to process each tweet
    curr_tweet_num = 0

    #gets compound score and organizes it accordingly
    while curr_tweet_num <= len(tweets):
        curr_tweet = tweets[curr_tweet_num]
        tweet_phrase = curr_tweet["ID", ["tweet"]][curr_tweet_num]
        score = sent_analysis(tweet_phrase)
        if score == 0:
            neu_tweets.append(tweet_phrase)
        elif score > 0:
            pos_tweets.append([tweet_phrase, score])
        else:
            neg_tweets.append([tweet_phrase, score])

        curr_tweet_num += 1

    #number of positive, negative, and neutral tweets. can be used for further analysis or extra metrics
    num_pos_tweets = len(pos_tweets)
    num_neg_tweets = len(neg_tweets)
    num_neu_tweets = len(neu_tweets)

    #to do: give final score between 0-10
    #idea: get average positive, negative, and neutral, whichever is highest multiply by 10 and that's the sentiment?
"""

webscraper = WebScraper()
test = webscraper.scrape_data('$BTC')

        

    







