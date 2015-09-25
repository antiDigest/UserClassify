# Avazu CTR prediction
# SGD Logistic regression + hashing trick.

import pandas as pd
import numpy as np
from datetime import datetime, date, time
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction import FeatureHasher
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import log_loss
import scipy as sp

cols = ['tweet']

# add two columns for hour and weekday
def dayhour(timestr):
    d = datetime.strptime(str(x), "%y%m%d%H")
    return [float(d.weekday()), float(d.hour)]

def textClean(s):
    remove = ['\\t','\\n','  ']
    # s = s.replace(i, Noneunct)

    for i in remove:
        s = re.sub(i,'',s)
    s = s.lower()
    s = s.split()
    return s

def textCleaner(value):
    for i in parenthesis:
        value = value.replace(i, '')
    # print value
    for word in value.split(' '):
        if '#' in word:
            if word[0] == '#':
                value = re.sub(word,"",value)
        if '@' in word:
            value = re.sub(word,"",value)
            # print word
        if 'http://' in word or 'http' in word or '.com' in word:
            value = re.sub(word,"",value)
            # print word
    for i in string.punctuation:
        value = value.replace(i, '')
    return value

fh = FeatureHasher(n_features = 2**20, input_type="string", non_negative=True)

# Train classifier
clf = MultinomialNB()
train = pd.read_csv("newtrain.csv", chunksize = 50000, iterator = True)
all_classes = np.array([0, 1])
for chunk in train:
    y_train = chunk["polarity"]
    chunk = chunk[cols]
    chunk['tweet'] = textCleaner(chunk['tweet'])
    chunk['tweet'] = textClean(chunk['tweet'])
    Xcat = fh.transform(np.asarray(chunk.astype(str)))
    clf.partial_fit(Xcat, y_train, classes=all_classes)
    
# Create a submission file
usecols = cols + ["id"]
X_test = pd.read_csv("newtest.csv", usecols=usecols)

X_enc_test = fh.transform(np.asarray(X_test.astype(str)))

y_act = pd.read_csv("newtest.csv", usecols=['click'])
y_pred = clf.predict_proba(X_enc_test)[:, 1]

with open('logloss.txt','a') as f:
    f.write('\n'+str(log_loss(y_act, y_pred))+'\tMultinomialNB')

with open("sentiment.csv", "w") as f:
    f.write("id,tweet,sentiment\n")
    for idx, xid in enumerate(X_test.id):
        f.write(str(xid) + "," + str(idx) + ',' + "{0:.10f}".format(y_pred[idx]) + "\n")
f.close()