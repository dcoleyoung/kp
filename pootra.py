from pootra_ext import *
from random import choice
from tweepy import OAuthHandler


#fantasizr classes import filename without .py

instagram_urls = ['http://instagr.am/p/OQEHmCOMdW/','instagr.am/p/OQCtaguMcQ/','http://instagr.am/p/OQCsojuMcO/','http://instagr.am/p/OQCr7aOMcM/',
                  'http://instagr.am/p/OQCrLluMcL/','http://instagr.am/p/OQCqWvOMcK/','http://instagr.am/p/OQCpeKOMcJ/','http://instagr.am/p/OQA8eBOMas/',
                  'http://instagr.am/p/OQA7emuMar/','http://instagr.am/p/OQA6x3uMao/','http://instagr.am/p/OQA5-pOMan/','http://instagr.am/p/OP-BTSuMYI/',
                  'http://instagr.am/p/OP9x3nOMX_/','http://instagr.am/p/OP9tqZuMX8/',
                  'http://instagr.am/p/OP9qyVuMX4/','http://instagr.am/p/OP9jcGOMX1/','http://t.co/oG02UQ7P',
                  'http://instagr.am/p/OYCn9quMUi/','http://instagr.am/p/OYC42bOMUv/','http://instagr.am/p/OYC8OwuMUx/',
                  'http://instagr.am/p/OYC_vuuMU0/','http://instagr.am/p/OYDEtxuMU3/','http://instagr.am/p/OYDoPbOMVK/'] 

messages = ['The most important poop is the next one', 'Who is your daily inspiration?', 'Creativity originates in the bumbum.', 'Being born butt-first is a sign of greatness.',
'What is your favorite smell?', 'Have you hugged your toilet today?']

class UpdateStatus(webapp.RequestHandler):
    def get(self):
	    #twitter api
        tweeted_at = Ulist.get_or_insert('kp_tweet')
        consumer_key="pUjTX2iCEF9E4XyfEBcKw"
        consumer_secret="lHcfPB8VnQ0znXtbJHrLYSIeuCFJ2Z2D7gBsdBGJKQY"
	
        access_token="864056234-bohqxmADXgvxwYNsWukefbfUCQHZKDiJ554J8Tf9"
        access_token_secret="AHdVEW5vt4Id1tbzeg4L4V1gTuYHrl39bjvLLdQkzlI"
	
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API(auth)

		# If the authentication was successful, you should
		# see the name of the account print out
	    #print api.me().name
	    #api.update_status('Updating using OAuth authentication via Tweepy!')
	    #results = api.search("#pooping")
        results = api.search("#pooping +exclude:retweets")
        self.response.headers['Content-Type'] = 'text/plain'
        tweet = results[0]
        this_user = api.get_user(tweet.from_user)
        if this_user.id_str not in tweeted_at.users: #don't tweet at anyone tweeted at before
            api.retweet(tweet.id)
            tweeted_at.users.append(this_user.id_str)
            db.put(tweeted_at)
        else:
            self.response.out.write('dup')
	    #  tweet.from_user_id
	    #api.update_status("@dcoleyoung test", in_reply_to_status_id=234369329532137473)
	    #api.update_status("@dcoleyoung " + msg + ' ' + instagram , in_reply_to_status_id=234369329532137473)
        #self.response.out.write(tweeted_at.users)

class FollowSomebody(webapp.RequestHandler):
    def get(self):
	    #twitter api
        tweeted_at = Ulist.get_or_insert('kp_tweet')
        consumer_key="pUjTX2iCEF9E4XyfEBcKw"
        consumer_secret="lHcfPB8VnQ0znXtbJHrLYSIeuCFJ2Z2D7gBsdBGJKQY"
	
        access_token="864056234-bohqxmADXgvxwYNsWukefbfUCQHZKDiJ554J8Tf9"
        access_token_secret="AHdVEW5vt4Id1tbzeg4L4V1gTuYHrl39bjvLLdQkzlI"
	
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API(auth)

		# If the authentication was successful, you should
		# see the name of the account print out
	    #print api.me().name
	    #api.update_status('Updating using OAuth authentication via Tweepy!')
	    #results = api.search("#pooping")
        results = api.search("#pooping +exclude:retweets")
        self.response.headers['Content-Type'] = 'text/plain'
        tweet = results[0]
        this_user = api.get_user(tweet.from_user)
        if this_user.id_str not in tweeted_at.users: #don't tweet at anyone tweeted at before
            api.create_friendship(this_user.id_str)
            tweeted_at.users.append(this_user.id_str)
            db.put(tweeted_at)
        else:
            self.response.out.write('dup')
	    #  tweet.from_user_id
	    #api.update_status("@dcoleyoung test", in_reply_to_status_id=234369329532137473)
	    #api.update_status("@dcoleyoung " + msg + ' ' + instagram , in_reply_to_status_id=234369329532137473)
        #self.response.out.write(tweeted_at.users)
class GenStatus(webapp.RequestHandler):
    def get(self):
	    #twitter api
        tweeted_at = Ulist.get_or_insert('kp_tweet')
        consumer_key="pUjTX2iCEF9E4XyfEBcKw"
        consumer_secret="lHcfPB8VnQ0znXtbJHrLYSIeuCFJ2Z2D7gBsdBGJKQY"
	
        access_token="864056234-bohqxmADXgvxwYNsWukefbfUCQHZKDiJ554J8Tf9"
        access_token_secret="AHdVEW5vt4Id1tbzeg4L4V1gTuYHrl39bjvLLdQkzlI"
	
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API(auth)
        msg = choice(messages)
        instagram = choice(instagram_urls)
        api.update_status(msg + ' ' + instagram + ' ' + '#poop')

class MainPage(webapp.RequestHandler):
    def get(self): 
        tweeted_at = Ulist.get_or_insert('kp_tweet')
        template_values = {'count': tweeted_at.no_tweets}
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))
		
application = webapp.WSGIApplication([
  ('/*', MainPage),
  ('/kp_tweet', UpdateStatus),
  ('/follow', FollowSomebody),
  ('/genstatus', GenStatus),
  
], debug=True)



def main():
  run_wsgi_app(application)


if __name__ == '__main__':
  main()


