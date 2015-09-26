import re

parenthesis = [')','(', ']','[','{','}','*','&','\\','!','$','^',';','<','>','?','_','=','+','RT','.']

def TweetBehav(text):

    hashtags = []
    to = []
    link = []

    for i in parenthesis:
        value = value.replace(i, '')

    for word in text.split(' '):
        if '#' in word:
            if word[0] == '#':
                hashtags += [word]
                text = re.sub(word,"",text)
        if '@' in word:
            to += [word]
            text = re.sub(word,"",text)
            # print word
        if 'http://' in word or 'http' in word or '.com' in word:
            link += [word]
            text = re.sub(word,"",text)
            # print word
    for i in string.punctuation:
        text = text.replace(i, '')
    countlink = len(link)
    countto = len(to)
    counthash = len(hashtags)

    return countlink