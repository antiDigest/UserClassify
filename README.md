# UserClassify

User Classify

##Characteristics to be extracted:

* Profile Features

	* Name -done -- Removed, does not help in classifying occupation

	* regional origin -> location -done -- Industries seem to concentrate in some areas

* User Network Structure

	* Following frequency -done --removed

	* Followers frequency -done --million fans if celeb or political person

* Tweeting Behaviour

	* No. of messages/tweets per day ?? -x --maybe important depends on experiments

	* No. of links, images etc -done --Based on experiments and how HITS algorithm works

	* Status Count -done --Check if you can get date of joining

* Linguistic Content

	* bad words --politician might not use bad words.

	* smileys/emoticons -done --removed, type maybe
 
	* repeated alphabets --removed

		* laugh -done 

		* shout -done

		* exasperation ??

		* agreement -done

		* honorifics like dude, man, bro etc ??

		* Excitement ??

		* Puzzlement ??

		* possessives like my this, my that, my bf, my prof etc (possessive bigrams) -CountVectoriser

	* Hash Tagged words -done --on the side

	* Sentiment Words -done --Useful

* Social Network

	* Who you tweet -done --on the side

	* tweets in response to tweets -done --number

	* retweets -done --number


##Basis Of Classification:

* Occupation

##Algorithms that can be employed:

* Multiclass SVM ??

* KNN

* Gradient Boost Decision Trees

###Comments

* we find that a support vector machine (SVM) trained on hashtag metadata outperforms an SVM trained on the full text of users’ tweets, yielding predictions of political affiliations with 91% accuracy. 

* In order to collect list information, we started crawling from the followers of Ashton Kutcher, one of the most popular people on Twitter who has more than 4 million followers. And then we crawled users’ profiles and lists information from his follower list. Because many users make their account and never use again, we defined a user who has at least one friend as an active user. Finally, we have crawled over 3.3 million users’ profiles to check if they are in lists, and it is roughly 10% of the total users in Twitter, as reported by techcrunch6 . After analyzing out data we found over nine hundred thousand lists, and about 12% of the users belong to at least one list.

#TODO:

* The dataset has been fetched and we need to get the tweets of the user. Twitter gives us 100 tweets per user so we are going to use 100 per person. So, *task 1* is to get the tweets using the user ids. But this also has to include the set of features that we will be extracting about the user, otherwise it would just be a waste of time.

* Second most important thing is starting to write the paper (We can atleast finish the dataset part if not the results and experiment). *Task 2* will be to write the RELATED WORKS and the PROPOSED ARCHITECTURE(dataset part). So, whosoever is doing this task, needs to find the RELATED WORKS (not just related to occupation, but sometimes other related to twitter are also useful) and then classify each of our extracted features as to why we are using it, and if there is no reason to use it, can we remove it(some of the removal is also determind through experiment).

* *Final task* will be to identify similar occupations in the dataset we are using. The dataset has a set of about 90 classes of occupations which I don't think would all be very much different and could be done into some upper less number of classes. So we'll divide them into classes like Business, Service, Government, Political etc.
