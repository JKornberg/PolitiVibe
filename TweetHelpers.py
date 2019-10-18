import pickle
import os
import re
import string
import pandas as pd
from textblob import TextBlob


def pickle_data(filename, data):
	outfile = open(filename, "wb")
	pickle.dump(data,outfile)
	outfile.close

def unpickle_data(filename):
    infile = open(filename, 'rb')
    data = pickle.load(infile)
    infile.close()
    return data

candidates = ["Joe Biden","Bernie Sanders","Elizabeth Warren","Beto O'Rourke","Pete Buttigieg"]
handles = ['JoeBiden','BernieSanders', 'SenWarren', 'BetoORourke', 'PeteButtigieg']
topics = ["healthcare", "environment", "military", "economy"]

def set_candidates(filename):
    arr = []
    for c, h in zip(candidates,handles):
        arr.append(CandidateNode(c, topics, h))
    pickle_data(filename, arr)





def create_directories():
    for candidate in candidates:
        for topic in topics:
            if not os.path.exists(candidate+"/"+topic):
                os.makedirs(candidate+"/"+topic)



def get_tweet_objects(candidate, topic):
	path = candidate + "/" + topic +"/raw"
	if os.path.exists(path):
		(_,_,filenames) = next(os.walk(path))
		data = []
		for file in filenames:
			data += unpickle_data(path+"/"+file)
			return data

def clean_text(text):
    #remove words with numbers in them
    text = text.lower()
    text = re.sub(r'@\w+','', text)
    text = re.sub(r'[%s]' % re.escape(string.punctuation),' ',text)
    text = re.sub(r'[^a-zA-Z0-9\s]','',text)
    text = re.sub(r'\w*\d\w*','',text)
    text = re.sub(r'\s+',' ', text)
    return text

def combine_data(data):
    s = ""
    for d in data:
        s+=d
    return s

def get_text_from_tweets(tweets):
    arr = []
    for t in tweets:
        arr.append(get_text_from_tweet(t))
    return arr

def get_text_from_tweet(t):
	tweet_text = ""
	if not t:
		return " "
	if 'extended_tweet' in t:
		tweet_text = t['extended_tweet']['full_text']
	else:
		tweet_text = t.text
	return tweet_text

def getSentiment(tweets):
	total_polarity = 0
	total_subjectivity = 0
	count = 0
	if tweets is None:
		return {
			'polarity' : 0,
			'subjectivity' : 0,
			'count' : 0,
			'favor': 0,
			'unfavor': 0,
			'fact' : 0,
			'opinion' : 0
			}
	favor = 0
	unfavor = 0
	fact = 0
	opinion = 0
	for t in tweets:
		tweet_text = get_text_from_tweet(t)
		sentiment = TextBlob(tweet_text).sentiment
		if sentiment.polarity >= 0:
			favor += 1
		else:
			unfavor += 1
		if sentiment.subjectivity >= .5:
			fact += 1
		else:
			opinion += 1
		total_polarity += sentiment.polarity
		total_subjectivity += sentiment.subjectivity
		count += 1
	#return SentimentNode(total_polarity/count, total_subjectivity/count)
	return  {
				'polarity' : total_polarity/count,
				'subjectivity' : total_subjectivity/count,
				'count' : count,
				'favor' : favor,
				'unfavor' : unfavor,
				'fact' : fact,
				'opinion' : opinion
			}

class CandidateNode():
    def __init__(self, name, topics, handle):
        self.name = name
        self.topics = topics
        self.handle = handle

cleaner = lambda x: clean_text(x)


def createData():
	data = [{} for _ in range(len(candidates))]
	candict = {}
	for i,c in enumerate(candidates):
		data[i] = {'info' : {'name' : c, 'handle' : handles[i]}, 'topics' : {}, 'favor' : [], 'subjectivity' : []}
		count = 0
		tp = 0
		ts = 0
		favor = 0
		unfavor = 0
		fact = 0
		opinion = 0
		for t in topics:
			tweets =  get_tweet_objects(c,t)
			sen = getSentiment(tweets)
			favor += sen['favor']
			unfavor += sen['unfavor']
			fact += sen['fact']
			opinion += sen['opinion']
			data[i]['topics'][t] = {'polarity' : sen['polarity'], 'subjectivity' : sen['subjectivity']}
			tp += sen['polarity'] * sen['count']
			ts += sen['subjectivity'] * sen['count']
			count += sen['count']
		print(favor)
		data[i]['favor'] = [favor, unfavor]
		data[i]['subjectivity'] = [fact, opinion]
		data[i]['topics']['all'] = {'polarity' : tp/count, 'subjectivity' : ts/count}
	return data



#term = "beyonce"
#list = unpickle_data("sample tweets.txt")
#dict = {term: list}
#print(dict["beyonce"][0])
