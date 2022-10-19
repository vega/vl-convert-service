from http.server import BaseHTTPRequestHandler
import vl_convert as vlc
import os
from pathlib import Path

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        p = Path("fonts")
        children = repr(list(p.rglob("*")))
        msg = f"""
        {os.path.exists("/fonts")}
        {os.path.exists("fonts")}
        {os.path.exists("fonts/liberation-mono")}
        {os.path.exists("fonts/liberation-mono/LiberationMono-Bold.ttf")}
        {children}
        """

        # msg = vlc.__version__

        self.wfile.write(msg.encode())
