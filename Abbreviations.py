

def AbbrevFind(abbrev, text):
    abbrev=abbrev.lower()
    text=text.lower()
    words=text.split()
    if not abbrev:
        return True
    if abbrev and not text:
        return False
    if abbrev[0]!=text[0]:
        return False
    else:
        return (AbbrevFind(abbrev[1:],' '.join(words[1:])) or
                any(AbbrevFind(abbrev[1:],text[i+1:])
                    for i in range(len(words[0]))))

def Abbreviations():
    for abbrev,text in tests:
        result=AbbrevFind(abbrev,text)
        print(abbrev,text,result)
        # assert result==answer