import os
import ConfigParser
import json, sys, time
import pandas as pd
from pandas.io.json import json_normalize
import twython
reload(sys)
sys.setdefaultencoding('utf-8')

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))

config = ConfigParser.ConfigParser()
config.read(os.path.join(CURRENT_DIR, 'config.ini'))

twitter = twython.Twython(
    config.get("Twitter","Consumer_Key"),
    config.get("Twitter","Consumer_Secret"),
    config.get("Twitter","Access_Token_Key"),
    config.get("Twitter","Access_Token_Secret")
)

ids = []

with open('jobs-users') as ju:
    for u in ju:
    	ids += [u.split(' ')[0]]

# print ids

user_timeline = []
count = 0
output = []


for i in ids:
    try:
        user_timeline = twitter.get_user_timeline(user_id=i.split()[0], count=100)
        data = json.dumps(user_timeline)
        data = pd.read_json(data)
        data.to_csv('Data/output.csv',header=True,index=True,mode='a')
    except twython.exceptions.TwythonError:
        time.sleep(60*15)
        twitter = twython.Twython(
            config.get("Twitter","Consumer_Key"),
            config.get("Twitter","Consumer_Secret"),
            config.get("Twitter","Access_Token_Key"),
            config.get("Twitter","Access_Token_Secret")
        )


