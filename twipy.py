import json
import tweepy

def make(filename):
	f = open(filename)
	key_dict = json.load(f)
	auth = tweepy.OAuthHandler(str(key_dict["ConsumerKey"]),str(key_dict["ConsumerSecret"]))
	auth.set_access_token(key_dict["AccessToken"],key_dict["AccessTokenSecret"])
	return tweepy.API(auth)



