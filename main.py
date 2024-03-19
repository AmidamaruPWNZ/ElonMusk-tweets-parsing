import requests
import pandas as pd

twitter_data = []

payload = {
    'api_key': '83743cec7f796a37b4f6233ec3e1ed1c',
    'query': 'elonmusk',
    'num': '12',
}

response = requests.get(
    'https://api.scraperapi.com/structured/twitter/search', params=payload
)

data = response.json()

print(data.keys())
print(data)

all_tweets = data['organic_results']
for tweet in all_tweets:
    twitter_data.append(tweet)

df = pd.DataFrame(twitter_data)
df.to_csv('ElonTweets.csv', index=False)
print('Done')