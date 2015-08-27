import re

def Emoticons(text):
	eyes, noses, mouths = r":;8BX=x-0%", r"-~\'\^_O", r")(/\\\|DPp[>O*&-o@"
	pattern = "[%s][%s]?[%s]" % tuple(map(re.escape, [eyes, noses, mouths]))

	return len(re.findall(pattern, text))

def laughEmoticons(text):
	eyes, noses, mouths = r":8%=*", r"-O^'", r")DPp3],"
	pattern = "[%s][%s]?[%s]" % tuple(map(re.escape, [eyes, noses, mouths]))
	laugh_pattern =  r"\b(a*ha+h[ha]*|o?l+o+l+[ol]*)\b"

	lp = re.findall(laugh_pattern, text)
	for i in lp:
		text = re.sub(lp,'happy',text)
	p = re.findall(pattern, text)
	for i in p:
		text = re.sub(p,'happy',text)
	return text

def sadEmoticons(text):
	eyes, noses, mouths = r":>;", r"-O:'", r"([{cC@|"
	pattern = "[%s][%s]?[%s]" % tuple(map(re.escape, [eyes, noses, mouths]))

	p = re.findall(pattern, text)
	for i in p:
		text = re.sub(p,'sad',text)
	return text

def replaceEmoticons(text):
	text = laughEmoticons(text)
	text = sadEmoticons(text)
	return text