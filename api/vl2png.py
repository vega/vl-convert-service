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
            self.convert(vl_spec, query_params)

    def to_POST(self):
        s = self.path
        query_params = dict(parse.parse_qsl(parse.urlsplit(s).query))
        content_len = int(self.headers.get('Content-Length', 0))
        if content_len == 0:
            self.send_response(400)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("POST body must be vl_spec".encode())
        else:
            vl_spec = self.rfile.read(content_len).decode("utf8")
            self.convert(vl_spec, query_params)

    def convert(self, vl_spec, query_params):
        vl_version = query_params.get("vl_version", None)
        scale = query_params.get("scale", None)

        try:
            png_data = vlc.vegalite_to_png(
                vl_spec,
                vl_version=vl_version,
                scale=float(scale) if scale is not None else None
            )
            self.send_response(200)
            self.send_header('Content-type', 'image/png')
            self.end_headers()
            self.wfile.write(png_data)
        except Exception as e:
            self.send_response(400)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(f"conversion failed: {str(e)}".encode())