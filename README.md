# UserClassify

User Classify

##Characteristics to be extracted:

* Profile Features

	* Name -done

	* Gender ??

	* regional origin -> location -done

	* age ??

* User Network Structure

	* Following frequency -done

	* Followers frequency -done

* Tweeting Behaviour

	* No. of messages/tweets per day ??

	* No. of links, images etc -done

	* Status Count -done

* Linguistic Content

	* Types of words used : No. of abbreviations, lmao, wtf type of words etc ??

	* smileys/emoticons -done

	* repeated alphabets

		* laugh -done

		* shout -done

		* exasperation ??

		* agreement -done

		* honorifics like dude, man, bro etc ??

		* Excitement ??

		* Puzzlement ??

		* possessives like my this, my that, my bf, my prof etc (possessive bigrams) -

	* Hash Tagged words -done

	* Sentiment Words -done

* Social Network

	* Who you tweet -done

	* tweets in response to tweets -done

	* retweets -done


##Basis Of Classification:

* Occupation

* Religious Beliefs 


##Algorithms that can be employed:

* Multiclass SVM

* KNN

* Gradient Boost Decision Trees



###Comments

* we find that a support vector machine (SVM) trained on hashtag metadata outperforms an SVM trained on the full text of users’ tweets, yielding predictions of political affiliations with 91% accuracy. 

* Factorisation machines

* Political affiliation

* In order to collect list information, we started crawling from the followers of Ashton Kutcher, one of the most popular people on Twitter who has more than 4 million followers. And then we crawled users’ profiles and lists information from his follower list. Because many users make their account and never use again, we defined a user who has at least one friend as an active user. Finally, we have crawled over 3.3 million users’ profiles to check if they are in lists, and it is roughly 10% of the total users in Twitter, as reported by techcrunch6 . After analyzing out data we found over nine hundred thousand lists, and about 12% of the users belong to at least one list.

