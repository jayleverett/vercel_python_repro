from http.server import BaseHTTPRequestHandler
import numpy as np

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write("hello from Python".encode())
        return
