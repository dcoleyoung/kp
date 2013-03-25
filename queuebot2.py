import random
from google.appengine.api import taskqueue
taskqueue.add(url='/genstatus', method='GET', countdown=(random.randrange(0,43200)))