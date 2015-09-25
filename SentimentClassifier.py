import random, re
import string
import csv
import nltk
from nltk.corpus import stopwords, wordnet
from stemming.porter2 import stem
import pandas as pd
import math
import sys
import os
import codecs
from robe.settings import BASE_DIR
reload(sys)
sys.setdefaultencoding('utf-8')

# pos = os.path.join(BASE_DIR,'positive.txt')
# neg = os.path.join(BASE_DIR,'negative.txt')

# with open(pos,'r') as f:
#     positive = f.read().split('\n')

# with open(neg,'r') as f:
#     negative = f.read().split('\n')

parenthesis = [')','(', ']','[','{','}','*','&','\\','!','$','^',';','<','>','?','_','=','+','RT','.']
# print stopwords.words('english')
def getTaggedWords():

    return taggedtext

customstopwords = ['band', 'they', 'them','and','the']

def getWords(taggedtext): # seems correct
    # print wordlist

    tweets = []
    customstopwords = ['band', 'they', 'them']

    for (word, sentiment) in taggedtext:
        word_filter = [i.lower() for i in word.split()]
        tweets.append((word_filter, sentiment))

    wordlist = getWordFeatures(getAllWords(tweets))
    wordlist = [i for i in wordlist if not i in stopwords.words('english')]
    wordlist = [i for i in wordlist if not i in customstopwords]

    return wordlist

def textCleaner(value):
    # print value
    
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


def getAllWords(tweets):
    allwords = []
    for (words, sentiment) in tweets:
        allwords.extend(words)
    return allwords

#Order a list of tweets by their frequency.
def getWordFeatures(listoftweets):
    #Print out wordfreq if you want to have a look at the individual counts of words.
    wordfreq = nltk.FreqDist(listoftweets)
    words = wordfreq.keys()
    return words

taggedtext = getTaggedWords()
word_features = getWords(taggedtext)

def makeDocument(tweets): # seems correct
    documents = []
    for (words, sentiment) in tweets:
        words_filtered = [e.lower() for e in words]
        documents.append((words_filtered, sentiment))
    return documents

def textClean(s):
    remove = ['\\t','\\n','  ']
    # s = s.replace(i, Noneunct)

    for i in remove:
        s = re.sub(i,'',s)
    s = s.lower()
    s = s.split()
    return s

def classify(raw):
    # raw = str(raw_input('enter : '))
    document_words = set(textClean(raw))
    # print document_words
    features = {}
    value = 0
    num = 0
    for word in document_words:
        antonyms = []
        synonyms = []
        for i,j in enumerate(wordnet.synsets(word)):
            for x in j.lemmas():
                antonyms += [y.name() for y in x.antonyms() if not y.name() in antonyms]
            synonyms += [y.name() for y in j.lemmas() if not y.name() in synonyms]
        total = synonyms + antonyms
        # print word, ':', total
        for w in synonyms:
            num += 1
            if word in positive:
                value += 1
            elif word in negative:
                value -= 1
        for w in antonyms:
            num += 1
            if word in positive:
                value -= 1
            elif word in negative:
                value += 1

    # print '%0.5f' % (float(value)/float(num))
    if value==0:
        return 0
    else:
        return value

def getSenti(stmt):
    print 'Getting Sentiment ... '
    # print stmt
    count_neg =0
    count_pos =0
    count_neutral = 0
    for s in stmt:
        # print s
        # s = textClean(s)
        if s!=' ':
            out = classify(s)
            # print out
            if out < 0:
                count_neg += 1
            elif out > 0.0:
                count_pos += 1
            else:
                count_neutral += 1
            # print s, out
    # print count_neutral, count_neg, count_pos, len(stmt)
    return count_neutral, count_neg, count_pos, len(stmt)