from http.server import BaseHTTPRequestHandler
import vl_convert as vlc

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(vlc.__version__.encode())
