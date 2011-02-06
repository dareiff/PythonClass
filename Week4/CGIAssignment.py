import cgi, time, json, CGIHTTPServer
import BaseHTTPServer, sys, urlparse
#cgi.test()

class Handler(CGIHTTPServer.CGIHTTPRequestHandler):
    cgi_directories = ["/cgi-bin"]

    def do_GET(self):
         print self.path
         self.send_response(200)
         self.send_header("Content-type", "text/json")
         self.end_headers()
         try:
             stdout = sys.stdout
             sys.stdout = self.wfile
             self.make_page()
         finally:
             sys.stdout = stdout

    def make_page(self):
        variables = urlparse.parse_qs(self.path).values()
        something = 0
        while len(variables) > 0:
                something += int(variables.pop()[0])
        print """{\n\t"result": %s,\n\t"uwnetid": "dareiff",\n\t"time": %s\n}""" % (something, time.time())

httpd = BaseHTTPServer.HTTPServer(("", 8000), Handler)

httpd.serve_forever()