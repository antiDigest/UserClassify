from twython import Twython
import os
import ConfigParser
import json
import pandas as pd
from pandas.io.json import json_normalize

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))

config = ConfigParser.ConfigParser()
config.read(os.path.join(CURRENT_DIR, 'config.ini'))

twitter = Twython(
    config.get("Twitter","Consumer_Key"),
    config.get("Twitter","Consumer_Secret"),
    config.get("Twitter","Access_Token_Key"),
    config.get("Twitter","Access_Token_Secret")
)

ids = []

with open('jobs-users') as ju:
    for u in ju:
    	ids += [u.split(' ')[0]]

print ids

user_timeline = []
count = 0
output = []

for i in ids:
    try:
        user_timeline = twitter.get_user_timeline(user_id=i.split()[0], count=100)
        data = json.dumps(user_timeline)
        output += [pd.read_json(data)]
    except twython.exceptions.TwythonError:
        count += 1
        print count

