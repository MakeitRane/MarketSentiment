import requests
import nltk
import pandas as pd
from web_scraper import scrape_tweets
from packages_test import Preprocessing
from statistics import mean

def main():
    coin_name = input("Want the market sentiment for a particular cryptocurrency? Type its ticker here: ")
    tweet_count = int(input("How many tweets do you want to analyze? Make sure your number is at least 10: "))
    pos_scores = [] #positive scores
    neg_scores = [] #negative scores
    neu_scores = [] #neutral scores

    tweets = scrape_tweets(coin_name, tweet_count)

    for tweet in tweets["Tweet Text"]:
        score = Preprocessing.sent_analysis(tweet)
        if score == 0:
            neu_scores.append(score)
        elif score > 0:
            pos_scores.append(score)
        else:
            neg_scores.append(score)

    num_pos_scores = len(pos_scores)
    num_neg_scores = len(neg_scores)
    num_neu_scores = len(neu_scores)

    avg_pos_scores = mean(pos_scores) if num_pos_scores > 0 else 0
    avg_neg_scores = mean(neg_scores) if num_neg_scores > 0 else 0
    avg_neu_scores = mean(neu_scores) if num_neu_scores > 0 else 0

    final_score = max(avg_pos_scores, avg_neg_scores, avg_neu_scores) * 10

    print("Final Sentiment Score: ", final_score)


        
main()
    
