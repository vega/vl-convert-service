from http.server import BaseHTTPRequestHandler
from urllib import parse
import vl_convert as vlc

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        query_params = dict(parse.parse_qsl(parse.urlsplit(s).query))

        # Extract query params
        if "vl_spec" not in query_params:
            self.send_response(400)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("vl_spec query parameter required".encode())
        else:
            vl_spec = query_params.get("vl_spec")
            vl_version = query_params.get("vl_version", None)
            scale = query_params.get("scale", None)

            try:
                png_data = vlc.vegalite_to_png(vl_spec, vl_version=vl_version, scale=float(scale))
                self.send_response(200)
                self.send_header('Content-type', 'image/png')
                self.end_headers()
                self.wfile.write(png_data)
            except Exception as e:
                self.send_response(400)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(f"conversion failed: {str(e)}".encode())

        return
