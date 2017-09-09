#!/usr/bin/python3

import tweepy 
import twipy 
import urllib
import json

API_KEY = "1569AB145D7B6E3A8F1D049372D96ED81B653130"
def feel_api(text):
	url = "http://ap.mextractr.net/ma9/emotion_analyzer?out=json"
	params_txt = urllib.parse.urlencode(
		{'apikey':API_KEY,
		 'text':text})
	print(url+params_txt)
	response = urllib.request.urlopen(url+"&"+params_txt)
	return response.read()

USER_NAME = "titan_FF"
if __name__ == "__main__":

	api = twipy.make("tomo_iwa.json")

	timelines = api.home_timeline()
	my_status = list(filter(lambda x: x.user.screen_name == USER_NAME,timelines))
	status_feel = feel_api(my_status[0].text)
	feel_dict = json.loads(status_feel.decode('utf-8'))
	print(feel_dict)

#	
#	if first_char == 'a':
#		api.update_profile_banner(filename="./test.jpg")
#	else:
#		api.update_profile_banner(filename="./std_banner.jpg")

#	api.update_profile_image(filename="./.jpg")
#	api.update_profile_banner(filename="./std_banner.jpg")
