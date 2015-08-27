import re

def Emoticons():
	eyes, noses, mouths = r":;8BX=x-0%", r"-~\'\^_O", r")(/\\\|DPp[>O*&-o@"
	pattern = "[%s][%s]?[%s]" % tuple(map(re.escape, [eyes, noses, mouths]))

	text = "bla bla bla :-/ more text 8^P and another smiley =-D even more text"
	print re.findall(pattern, text)

def laughEmoticons():
	eyes, noses, mouths = r":%", r"-O", r")DPp"
	pattern = "[%s][%s]?[%s]" % tuple(map(re.escape, [eyes, noses, mouths]))
	laugh_pattern =  r"\b(a*ha+h[ha]*|o?l+o+l+[ol]*)\b"

	text = "lololol :-) hahahah aaahahahaha llloooollll"
	print re.findall(laugh_pattern, text)
	print re.findall(pattern, text)