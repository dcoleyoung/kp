import os
from google.appengine.ext.webapp import template
from google.appengine.api import mail
from google.appengine.api import urlfetch
from google.appengine.api import namespace_manager
import cgi
import datetime
from datetime import timedelta
import time
import urllib
import wsgiref.handlers
import csv
import urlparse
import re
import urllib2
import httplib
import tweepy

from google.appengine.ext import db
from google.appengine.ext.db import polymodel
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class Ulist(db.Model):
  users = db.ListProperty(str)
  no_tweets = db.IntegerProperty()