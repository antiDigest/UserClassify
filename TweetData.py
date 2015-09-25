import tweepy
import time
import thread
import sys, csv
import pandas as pd
reload(sys)
sys.setdefaultencoding('utf-8')

consumer_key = 'MbiHzivAIk3vLkWj19zVcw1WI'
consumer_secret = 'ctZF0ZwAQrhWnn90qiMyBvdRPpO4YgCEX8n6QkGNqN4q1XDrok'

access_token = '3253361905-3uXheHOx2Si4DE0Rio46NM9iNKjcwXPLpRZTeIV'
access_token_secret = 'RIoJvqwIimHuVlL7IBmfuloPSBPla2khnpXHV4rZE0j03'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def TweetData():
    i=0
    followers = api.followers_ids('@MariahCarey')
    userdata = []
    print len(followers)
    for follow in followers:
        statuses = api.statuses_lookup([follow])
        # print statuses
        for status in statuses:
            # print [status.text, status.id, status.author.statuses_count, status.author.followers_count,\
            #                 status.author.friends_count, status.author.location, status.author.favourites_count,\
            #                 status.author.name, status.author.created_at, status.author.time_zone,\
            #                 status._json['retweeted'],status._json['in_reply_to_screen_name'], \
            #                 status._json['in_reply_to_status_id']]
            userdata += [[status.text, status.id, status.author.statuses_count, status.author.followers_count,\
                                        status.author.friends_count, status.author.location, status.author.favourites_count,\
                                        status.author.name, status.author.created_at, status.author.time_zone,\
                                        status._json['retweeted'],status._json['in_reply_to_screen_name'], \
                                        status._json['in_reply_to_status_id']]]
            print userdata

TweetData()