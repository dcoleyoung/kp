import random
from google.appengine.api import taskqueue
taskqueue.add(url='/kp_tweet', method='GET', countdown=(random.randrange(0,10800)))
#taskqueue.add(url='/follow', method='GET', countdown=(random.randrange(0,10800)))