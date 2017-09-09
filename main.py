#!/usr/bin/python3

import tweepy 
import twipy 

if __name__ == "__main__":
	api = twipy.make("tomo_iwa.json")
	api.update_profile_image(filename="./test.jpg")
	api.update_profile_banner(filename="./test.jpg")
#	try:
#		api.update_profile_background_image(filename="./test.jpg", use=1, tile=0)
#	except tweepy.error.TweepError as err:
#		if err[0][0]['code'] == 131:
#			print( "resulted in "+err+".")
#			sleep(1)
#		else:
#			raise

