from searchtweets import ResultStream, gen_rule_payload, load_credentials, collect_results
import tweepy
import pickle
import TweetHelpers
import os
auth = tweepy.OAuthHandler("vjNghcPpck7YYMdRjAzZ8PDse", "OsxQhkUDRu99rFHZjYWLqs9KMe7c0ul046I2zjXlQKF6iUXfRD")
auth.set_access_token("2914673259-QFH02b2WE9DvQSLcLWAmDbk87Nc4B7nfmjepGys", "3x0JowxzOeFnD9dqBa5j5Y4SSpHvPdgUEmqDf3RulUJvO")
api = tweepy.API(auth)


premium_search_args = load_credentials(filename="twitter_keys.yaml",
                 yaml_key="search_tweets_api",
                 env_overwrite=False)






def get_premium_tweets(candidate, handle, topic):
    rule = gen_rule_payload(topic + " to:" + handle , results_per_call=100)
    tweets = collect_results(rule,
                         max_results=100,
                         result_stream_args=premium_search_args)
    data = TweetHelpers.get_tweet_objects(candidate,topic)
    if os.path.exists(candidate +"/"+topic+"/raw/tweets.pkl"):
        os.remove(candidate +"/"+topic+"/raw/tweets.pkl")
    if data is None:
        data = []
    data += tweets
    TweetHelpers.pickle_data(candidate +"/"+topic+"/raw/tweets.pkl", tweets)

def getRecentTweets(handle):
	tweets = api.user_timeline(id=handle,tweet_mode="extended")
	return tweets

def gather_tweets_from_candidates():
    for c, h in zip(TweetHelpers.candidates, TweetHelpers.handles):
        for t in TweetHelpers.topics:
            get_premium_tweets(c, h, t)




'''
#result stream
rs = ResultStream(rule_payload=rule,
                  max_results=100,
                  max_pages=2,
                  **premium_search_args)
tweets = list(rs.stream())

			  '''
