#!/usr/bin/python3

import tweepy 
import twipy 

USER_NAME = "titan_FF"
if __name__ == "__main__":

	api = twipy.make("tomo_iwa.json")

	timelines = api.home_timeline()
	my_status = list(filter(lambda x: x.user.screen_name == USER_NAME,timelines))

	first_char = my_status[0].text[0]
	if first_char == 'a':
		api.update_profile_banner(filename="./test.jpg")
	else:
		api.update_profile_banner(filename="./std_banner.jpg")

#	api.update_profile_image(filename="./.jpg")
#	api.update_profile_banner(filename="./std_banner.jpg")
