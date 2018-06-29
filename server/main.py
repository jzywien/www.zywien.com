import logging
import webapp2 as webapp
import server.controllers as controllers

logging.getLogger().setLevel(logging.DEBUG)
application = webapp.WSGIApplication([
        ('/', controllers.IndexController),
        ], debug=True)
