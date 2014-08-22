#!/usr/bin/python
import os
import texcaller # Python interface for compiling LaTeX documents

try:
    virtenv = os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'misc/virtenv/')
    virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
    try:
        execfile(virtualenv, dict(__file__=virtualenv))
    except IOError:
        pass
except KeyError: # The environment variable OPENSHIFT_PYTHON_DIR
    pass         # is undefined, so assume that we are running somewhere other
                 # than on OpenShift

#
# IMPORTANT: Put any additional includes below this line.  If placed above this
# line, it's possible required libraries won't be in your searchable path
#

import tornado.ioloop
import tornado.web

# Create a dummy latex document unicode string for testing
latex_doc = ur'''\documentclass{article}
\begin{document}
Hello world!
\end{document}'''


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('<html><body><form action="/myform" method="POST">'
                   '<input type="text" name="message">'
                   '<p><select name="problem_choice">'
                   '<option value=1 selected>1</option>'
                   '<option value=2>2</option>'
                   '</select></p>'
                   '<p><input type="submit" value="Submit"></p>'
                   '</form>'
                   '<p><form action="/pdf">'
                   '<input type="submit" value="Generate PDF"></form></p>'
                   '</body></html>')

    def post(self):
        self.set_header("Content-Type", "text/plain")
        self.write("You wrote " + self.get_body_argument("message") + "\n")
        self.write("You also chose " + self.get_body_argument("problem_choice"))

class PDFHandler(tornado.web.RequestHandler):
    def get(self):
        pdf, info = texcaller.convert(latex_doc, 'LaTeX', 'PDF', 5)
        #self.set_header("Content-Type", "text/plain")
        #self.write('PDF size:     %.1f KB' % (len(pdf) / 1024.0))
        #self.write('PDF content:  %s ... %s' % (pdf[:5], pdf[-6:]))
        self.set_header("Content-Type", "application/pdf")
        self.write(pdf)

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/myform", MainHandler),
    (r"/pdf", PDFHandler),
])

def main(port, address):
    application.listen(port, address)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    try:
      app_name = os.environ['OPENSHIFT_APP_NAME'].upper()
    except KeyError:
      app_name = "DIY"
    try:
      address = os.environ['OPENSHIFT_' + app_name + '_IP']
      if not address: # Test for empty string
        address = "127.0.0.1"
    except KeyError:
      address = "127.0.0.1"

    try:
      port = int(os.environ['OPENSHIFT_' + app_name + '_PORT'])
    except (KeyError, ValueError):
      port = 8080

    main(port, address)
