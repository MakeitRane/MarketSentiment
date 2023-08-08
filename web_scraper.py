import tweepy 
import pandas as pd


API_KEY = ''
SECRET_API = ''
BEARER_TOK = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

def scrape_tweets(keyword, tweet_count):
    client = tweepy.Client(BEARER_TOK)

    keyword_two = ' -has:media -is:retweet'
    keyword_final = keyword + keyword_two 
    response = client.search_recent_tweets(query = keyword_final, max_results = tweet_count)

    if response.data:
        attribute_container = []
        for tweet in response.data:
            tweet_id = tweet.id
            text = tweet.text
            
            attribute_container.append([tweet_id, text])
    else:
        attribute_container = []

    columns = ["Tweet ID", "Tweet Text"]
    df_tweet = pd.DataFrame(attribute_container, columns=columns)

    return df_tweet

