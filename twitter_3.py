# -*- coding: utf-8 -*-
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
#import MySQLdb
import time
import json

#conn = MySQLdb.connect ('nyub', 'nyub', 'nyub', 'nyub', charset='utf8')

#c = conn.cursor()

ckey = ""
csecret = ""
atoken = ""
asecret = ""

class listener (StreamListener):

    def on_data(self, data):
        try:
            tweet = json.loads(data)
            print(data)

            created_at = tweet ["created_at"]
            identity = tweet ["id"]
            text = tweet ["text"]
            status_reply = tweet ["in_reply_to_status_id"]
            user_reply = tweet ["in_reply_to_user_id"]
            screen_name_reply = tweet ["in_reply_to_screen_name"]

            user_id = tweet ["user"]["id"]
            user_screen_name = tweet["user"]["screen_name"]
            user_location = tweet["user"]["location"]
            user_url = tweet["user"]["url"]
            user_description = tweet["user"]["description"]
            user_followers = tweet["user"]["followers_count"]
            user_friends = tweet["user"]["friends_count"]
            user_statuses = tweet["user"]["statuses_count"]
            user_created = tweet["user"]["created_at"]
            user_lang =  tweet["user"]["lang"]

            coordinates = tweet ["coordinates"]
            place = tweet ["place"]
            rt_count = tweet ["retweet_count"]
            fav_count = tweet ["favorite_count"]

            hashtags = []

            for hashtag in tweet ["entities"]["hashtags"]:
                hashtags.append(hashtag["text"])

            urls = []

            for url in tweet ["entities"]["urls"]:
                urls.append(url["expanded_url"])

            #c.execute ("INSERT INTO luck (timestamp, tweet_created_at, tweet_id, tweet_text, in_reply_status, in_reply_user_id, in_reply_screen_name, user_id, user_screen_name, user_location, user_url, user_description, user_followers_count, user_friends_count, users_statuses_count, user_created_at, user_lang, tweet_coords, tweet_place, tweet_retweet_count, tweet_fav_count, hashtags, urls) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                      # ((time.time()), created_at, identity, text, status_reply, user_reply, screen_name_reply, user_id, user_screen_name, user_location, user_url, user_description, user_followers, user_friends, user_statuses, user_created, user_lang, coordinates, place, rt_count, fav_count, str(hashtags), str(urls)))

            #conn.commit ()

            print (text)

            return True
        except BaseException, e:
            print "failed on data", str(e)
            time.sleep(5)

    def on_error (self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=[u"trump"])