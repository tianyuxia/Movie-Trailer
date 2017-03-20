import os
import jinja2
import webapp2
import hashlib
import hmac
import string
import random
from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               autoescape=True)

SECRET = 'imsosecret'

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **kw):
        t = jinja_env.get_template(template)
        return t.render(kw)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class MainPage(Handler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        visits = 0
        visit_cookie_val = self.request.cookies.get('visits')
        if visit_cookie_val:
            cookie_val = check_secure_val(visit_cookie_val)
            if cookie_val:
                visits = int(cookie_val)

        visits += 1

        new_cookie_val = make_secure_val(str(visits))
        self.response.headers.add_header('Set-Cookie', 'visits=%s' % new_cookie_val)

        if visits > 10:
            self.write("You're the Best!")
        else:
            self.write("You've benn here %s times" % visits)

def hash_str(s):
    return hmac.new(SECRET, s).hexdigest()

def make_secure_val(s):
    return "%s|%s" % (s, hash_str(s))

def check_secure_val(h):
    val = h.split('|')[0]
    if (h == make_secure_val(val)):
        return val

def make_salt():
    return ''.join((random.choice(string.letters)) for x in xrange(5))

def make_pw_hash(name, pw, salt = None):
    if not salt:
        salt = make_salt()
    return "%s,%s" % (hashlib.sha256(name + pw + salt).hexdigest(), salt)

def valid_pw(name, pw, h):
    salt = h.split(',')[1]
    if (h == make_pw_hash(name, pw, salt)):
        return True




app = webapp2.WSGIApplication([('/', MainPage)], debug=True)