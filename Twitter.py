import tweepy
import json

import util.kaffter_constants as const

from producer.Producer import kafka_producer
from util.kaffter_constants import Constants

print(Constants.API_KEY)
####Twitter API keys
consumer_key = Constants.API_KEY
consumer_secret = Constants.API_KEY_SECRET
access_token = Constants.ACCESS_TOKEN
access_token_secret = Constants.ACCESS_TOKEN_SECRET

#Twitter Autentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

count = 0
#iter twitter cursor
for tweet in tweepy.Cursor(api.search,q="#ElectionResults2020",count=100,
                           lang="en",
                           since="2020-11-08").items():
    str_json = json.dumps(tweet._json)
    #call kafka producer to send tweet message 
    kafka_producer(str_json)

    count += 1
    print('#######################################################################')
    print(str_json)
    print('count: '+ str(count))
    print('#######################################################################')