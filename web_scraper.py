"""import requests
import pandas as pd
twitter_data = []
payload = {'api_key':'77dd07486d8909f02d4145c881e49f75', 'query': 'bitcoin', 'num': '5'}
response = requests.get('https://api.scraperapi.com/structured/twitter/search', params= payload)
print(response.text)
data = response.json()
print(data)

#need to fix this to scrape twitter for a user keyword
def twitter_data(twitter_data): 
    all_tweets = data['tweet_id']
    for tweet in all_tweets:
        twitter_data.append({'ID': tweet['tweet_id'],'User': tweet["user"],'Tweet': tweet["text"],'URL': tweet["link"]})
    df = pd.DataFrame(twitter_data)
    df.to_json('scraped_tweets.json', orient='index')
    return df"""

import requests
import pandas as pd
twitter_data = []

def extract_twitter_data(): 
    twitter_data = []
    payload = {'api_key':'77dd07486d8909f02d4145c881e49f75', 'query': 'bitcoin', 'num': '5'}
    response = requests.get('https://api.scraperapi.com/structured/twitter/search', params= payload)
    data = response.json()
    for result in data['organic_results']:
        twitter_data.append({'Title': result['title'], 'Snippet': result['snippet'], 'URL': result['link']})
    df = pd.DataFrame(twitter_data)
    df.to_json('scraped_tweets.json', orient='index')
    snippets = [result["snippet"] for result in data["organic_results"]]
    return snippets




