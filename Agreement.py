import re

words = ["agree","agreed","yea","yeah","yes","yo","yup","way to go","amen","that's it","you bet"\
	"course","me too","no problem","no problemo","touche","my point exactly","okay","ok","k","roger",\
	"roger that","of course","right on","right you are","there you go","too right","yeh","you're on"\
	,"you're telling me","sure","sure thing","jolly","jolly good",\
	"hold","concur","concord","match","fit","correspond","check","jibe","gibe","tally",\
	"harmonize","harmonise","consort","accord","concord","fit in"]

def Agreement():
	count = 0
	for i in words:
		if i in text:
			count += 1
			text = re.sub(i,'agree',text)
	return count, text