from twython import Twython
import twython
import os
import ConfigParser

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))

config = ConfigParser.ConfigParser()
config.read(os.path.join(CURRENT_DIR, 'config.ini'))

twitter = Twython(
    config.get("Twitter","Consumer_Key"),
    config.get("Twitter","Consumer_Secret"),
    config.get("Twitter","Access_Token_Key"),
    config.get("Twitter","Access_Token_Secret")
)

with open('jobs-users') as twitter_user_ids:
    ids = twitter_user_ids.readlines()

user_timeline = []
count = 0

for i in ids:
    try:
        user_timeline += [twitter.get_user_timeline(user_id=i.split()[0], count=100)]
    except twython.exceptions.TwythonError:
        with open('jobs-users','a') as f:
            f.write(user_timeline)
        user_timeline = []
        count += 1

print 'Count :',count