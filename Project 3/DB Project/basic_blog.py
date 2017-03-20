import os
import webapp2
import jinja2
from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape=True)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **kw):
        t = jinja_env.get_template(template)
        return t.render(kw)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class Blog(db.Model):
    subject = db.StringProperty(required = True)
    content = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)

class MainPage(Handler):
    def render_blog(self, blogs=""):
        blogs = db.GqlQuery("select * from Blog order by created desc")
        self.render("blog.html", blogs=blogs)

    def get(self):
        self.render_blog()

    def post(self):
        self.redirect('/blog/newpost')

class NewpostPage(Handler):
    def render_newpost(self, subject="", content="", error=""):
        self.render("newpost.html", subject=subject, content=content, error=error)

    def get(self):
        self.render_newpost()

    def post(self):
        content = self.request.get("content")
        subject = self.request.get("subject")

        if content and subject:
            blog = Blog(subject = subject, content = content)
            blog.put()
            blog_id = blog.key().id()
            self.redirect('/blog/' + str(blog_id))
        else:
            error = "Subject and content, please!"
            self.render_newpost(error=error, content=content, subject=subject)

class SinglePostPage(Handler):
    def render_single_post(self):
        self.render

app = webapp2.WSGIApplication([('/blog', MainPage),
                               ('/blog/newpost', NewpostPage),
                               ('/blog/(\d+)', SinglePostPage)])