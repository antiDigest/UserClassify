import re

parenthesis = [')','(', ']','[','{','}','*','&','\\','!','$','^',';','<','>','?','_','=','+','RT','.']

code_match = re.compile('<pre>(.*?)</pre>',re.MULTILINE|re.DOTALL)
link_match = re.compile('<a href="http://.*?".*?>(.*?)</a>',re.MULTILINE|re.DOTALL)

def links(text):
    
    link_count_in_code = 0
    
    # count links in code to later subtract them
    for match_str in code_match.findall(text):
        link_count_in_code += len(link_match.findall(match_str))
    
    return len(link_match.findall(text)) – link_count_in_code

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