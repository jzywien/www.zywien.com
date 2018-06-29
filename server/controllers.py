import webapp2 as webapp
import logging
from google.appengine.api import users
from google.appengine.api import mail
from google.appengine.api import urlfetch
import jinja2
import json
import urllib
import os

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), '../views')),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class IndexController(webapp.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render())
