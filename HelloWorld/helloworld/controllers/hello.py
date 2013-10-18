import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from helloworld.lib.base import BaseController, render

# Added for development sake
import helloworld.lib.helpers as h
from pylons import app_globals
from pylons import config

log = logging.getLogger(__name__)

class HelloController(BaseController):

    def index(self):
        response.content_type = 'text/plain'
        return 'Hello from the index() action!'

    def environ(self):
        response.content_type = 'text/plain'
        return h.format_environ(request.environ)

    def app_globals_test(self):
        app_globals.visits += 1
        return "You are visitor number %s." % app_globals.visits
