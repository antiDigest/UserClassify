# UserClassify

Classify twitter Users on the basis of their occupation using tweets and metadata related to tweets.

##Characteristics to be extracted:

* Profile Features

	* location -- Industries seem to concentrate in some areas Y

* User Network Structure

	* Followers frequency --million fans if celeb or political person Y

* Tweeting Behaviour

	* No. of messages/tweets per day ?? --maybe important depends on experiments

	* No. of links, images etc --Based on experiments and how HITS algorithm works

	* Status Count --Check if you can get date of joining

* Linguistic Content

 	* bad words --politician might not use bad words. Y

	* Hash Tagged words --on the side 

	* Sentiment Words --Useful Y

* Social Network

	* Who you tweet --on the side

	* tweets in response to tweets --number Y

	* retweets --number Y


##Basis Of Classification:

* Occupation


##Algorithms that can be employed:

* Multiclass SVM ??

* KNN

* Gradient Boost Decision Trees


###Comments

* we find that a support vector machine (SVM) trained on hashtag metadata outperforms an SVM trained on the full text of users’ tweets, yielding predictions of political affiliations with 91% accuracy. 


##TODO:

*	We are getting the tweets and have about 40k records of tweets. Only thing we need to do now is to extract meaningful data from these tweets.

*	HITS does not give a value on the link (It works on graphs and we do not have the web graph). Also, I don't know how number of links will work for us. Rest everything is done, I think we can start extracting data from the tweets and visualise how things work out for us.

*	We only need to select classifiers to work now, I hope that will not take much time.

*	We need to meet Tanvir Sir after doing this.
