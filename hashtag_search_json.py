# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 03:01:57 2016

@author: Sam
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 01:52:08 2016

@author: Sam
"""

import tweepy
import csv
import time

consumer_key = "hWig6yKVznpC71X7xWGWFeFKG"
consumer_secret = "mkk5QHN3grkujgieRB0JICqz2BAicwpEcKvql7ZnEuBi5Zj23V"
access_key = "4807911254-6bCdHMn1DXA7ISS26RCjHJkhNU1Qb2xykY6kJxE"
access_secret = "zSciGwVMS5g3OYqotCqFRVzlVGBUQbNWJtQhCxcLMvF2N"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except RateLimitError:
            print("oh that blasted error")
            time.sleep(15 * 60)
            
        except StopIteration:
            break

search_text = "#Justice4Liang"
search_number = 10
new_tweets = api.search(search_text, rpp=search_number)
print("Its a miracle")
max_tweets = 10

searched_tweets = [status._json for status in tweepy.Cursor(api.search, search_text).items(max_tweets)]

saveFile = open('apiraw_tweets3.json', 'a', encoding='utf-8')
json_data = searched_tweets
saveFile.write('\n]')
saveFile.write(str(json_data))

saveFile.write('\n]')
saveFile.write(',')

saveFile.close()
exit()        
