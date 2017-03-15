import os
import webapp2
import jinja2
import re

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape=True)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class MainPage(Handler):
    def get(self):
        self.render("signup.html")

    def post(self):
        user_name = self.request.get('username')
        user_pass = self.request.get('password')
        user_veri = self.request.get('verify')
        user_email = self.request.get('email')

        error_msg = error_gen(user_name, user_pass, user_veri, user_email)

        if(error_msg[4]):
            self.redirect('/welcome' + "?user_name=" + user_name)
        else:
            self.render("signup.html", user_name=user_name, user_pass="", user_veri= "",
                        user_email=user_email, error_1=error_msg[0], error_2=error_msg[1],
                        error_3=error_msg[2], error_4=error_msg[3])

class WelcomeHandler(Handler):
    def get(self):
        user_name = self.request.get("user_name")
        self.render("welcome.html", user_name=user_name)

def valid_input(input, type):
    if type == "username":
        USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
        return USER_RE.match(input)
    elif type == "password":
        USER_RE = re.compile(r"^.{3,20}$")
        return USER_RE.match(input)
    elif type == "email":
        USER_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")
        return USER_RE.match(input)

def error_gen(user_name, user_pass, user_veri, user_email):
    error_msg = ["","","","", True]
    if (valid_input(user_name, "username") == None):
        error_msg[0] = "That's not a valid username"

    if (valid_input(user_pass, "password") == None):
        error_msg[1] = "That wasn't a valid password"
    else:
        if user_pass != user_veri:
            error_msg[2] = "Your passwords didn't match"

    if (valid_input(user_email, "email") == None):
        error_msg[3] = "That's not a valid email"

    if (error_msg[0] == "" and error_msg[1] == "" and error_msg[2] == "" and error_msg[3] == ""):
        error_msg[4] = True
    else:
        error_msg[4] = False

    return error_msg

app = webapp2.WSGIApplication([('/', MainPage),
                               ('/welcome', WelcomeHandler)],
                              debug=True)