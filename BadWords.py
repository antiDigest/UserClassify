with open('badwords.txt','r') as f:
    badwords = f.read().split('\n')

def BadWords(text):
    count = 0
    text = text.split()
    for i in text:
        if i in badwords:
            print i
            count += 1

    return count