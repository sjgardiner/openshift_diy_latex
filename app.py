#!/usr/bin/python
import os
import imp

try:
    texcaller = imp.load_source('texcaller', os.path.join(
        os.environ['LD_LIBRARY_PATH'], 'texcaller.py'))
except (IOError, KeyError):
    print("WARNING: Using binary copy of the texcaller module from the repository. The behavior of texcaller might not agree with recent source code changes.")
    import texcaller

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
        self.finish()

    def post(self):
        self.set_header("Content-Type", "text/plain")
        self.write("You wrote " + self.get_body_argument("message") + "\n")
        self.write("You also chose " + self.get_body_argument("problem_choice"))
        self.finish()

class PDFHandler(tornado.web.RequestHandler):
    def get(self):
        pdf, info = texcaller.convert(latex_doc, 'LaTeX', 'PDF', 5)
        self.set_header("Content-Type", "application/pdf")
        self.set_header("Content-Disposition",
            "attachment; filename=document.pdf")
        self.write(pdf)
        self.finish()

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
      address = os.environ['OPENSHIFT_DIY_IP']
      if not address: # Test for empty string
        address = "127.0.0.1"
    except KeyError:
      address = "127.0.0.1"

    try:
      port = int(os.environ['OPENSHIFT_DIY_PORT'])
    except (KeyError, ValueError):
      port = 8080

    print("\n===READY===\n")

    main(port, address)
