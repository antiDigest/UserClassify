import tweepy
import time
import thread
import sys, csv
import pandas as pd
from SentimentClassifier import getSenti
from BadWords import BadWords
from TweetBehav import TweetBehav
reload(sys)
sys.setdefaultencoding('utf-8')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

ids = []
jobs = []

with open('jobs-users') as f:
    tp = f.read().split('\n')
    for i in tp:
        ids += [i.split()[0]]
        jobs += [i.split()[1]]

def present(x):
    if x is not None:
        return 1
    else:
        return 0

def TweetData():
    userdata = []
    for i in range(0,len(ids)):
        # print ids[i]
        statuses = api.statuses_lookup(ids[i])
        # print statuses
        for status in statuses:
            userdata += [[status.text, status.id, status.author.statuses_count, status.author.followers_count,\
                                        status.author.location, status.author.created_at, \
                                        status.author.time_zone, status._json['retweeted'],\
                                        present(status._json['in_reply_to_screen_name']), \
                                        getSenti(status.text), BadWords(status.text), TweetBehav(status.text), \
                                        jobs[i]]]
            print userdata
            break
        break

if __name__ == '__main__':
    TweetData()