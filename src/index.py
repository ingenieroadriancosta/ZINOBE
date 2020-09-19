from http.server import BaseHTTPRequestHandler, HTTPServer
class WebServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith(""):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write( open("index.html", "rb", buffering=0).read() )
            self.wfile.write( open("index.html", "rb", buffering=0).read() )
        else:
            self.send_error(404, 'File Not Found: %s' % self.path)
def main():
    try:
        port = 8000
        server = HTTPServer(('', port), WebServerHandler)
        print ("Web Server running on port %s" % port)
        print ("http://localhost:%s/" % port)
        server.serve_forever()
    except KeyboardInterrupt:
        print (" ^C entered, stopping web server....")
        server.socket.close()

if __name__ == '__main__':
    main()