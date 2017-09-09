#!/usr/bin/python3
import json
import tweepy

def make(filename):
	f = open('tomo_iwa.json')
	key_dict = json.load(f)["ConsumerKey"]
	auth = tweepy.OAuthandler(key_dict["ConsumerKey"],key_dict["ConsumerSecret"])
	auth.set_access_token(key_dict["AccessToken"],key_dict["AccessTokenSecret"])
	return auth



