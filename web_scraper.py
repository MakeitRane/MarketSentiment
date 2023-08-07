import requests
import pandas as pd

class WebScraper:
    def retrieve_data(self, data): 
            all_tweets = data['tweet_id']
            for tweet in all_tweets:
                data.append({'ID': tweet['tweet_id'],'User': tweet["user"],'Tweet': tweet["text"],'URL': tweet["link"]})
            df = pd.DataFrame(data)
            df.to_json('scraped_tweets.json', orient='index')
            return df
    def scrape_data (self, user_input):
        twitter_data = []
        #print("hi")
        payload = {'api_key':'77dd07486d8909f02d4145c881e49f75', 'query': user_input, 'num': '1', 'time_period':'1D'}
        response = requests.get('https://api.scraperapi.com/structured/twitter/search', params=payload)
        #print(response.content)
        #output = self.retrieve_data(response)
        #data = output.json()
        #print(data)
        return "hii"

     
    