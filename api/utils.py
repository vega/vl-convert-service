from http.server import BaseHTTPRequestHandler
from urllib import parse

ALLOWED_BASE_URLS = ["https://vega.github.io/vega-datasets/"]


class BaseHandler(BaseHTTPRequestHandler):
    def query_params(self):
        s = self.path
        return dict(parse.parse_qsl(parse.urlsplit(s).query))

    def send_exception(self, e):
        self.send_response(400)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(f"conversion failed: {str(e)}".encode())

    def send_successful(self, content, content_type):
        self.send_response(200)
        self.send_header('Content-type', content_type)
        self.end_headers()
        self.wfile.write(content)


class VlHandler(BaseHandler):
    def do_POST(self):
        query_params = self.query_params()
        content_len = int(self.headers.get('Content-Length', 0))
        if content_len == 0:
            self.send_response(400)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("POST body must be a Vega-Lite spec".encode())
        else:
            vl_spec = self.rfile.read(content_len).decode("utf8")
            self.convert_vl(vl_spec, query_params)

    def convert_vl(self, vl_spec, query_params):
        raise NotImplementedError


class VgHandler(BaseHandler):
    def do_POST(self):
        query_params = self.query_params()
        content_len = int(self.headers.get('Content-Length', 0))
        if content_len == 0:
            self.send_response(400)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("POST body must be Vega spec".encode())
        else:
            vl_spec = self.rfile.read(content_len).decode("utf8")
            self.convert_vg(vl_spec, query_params)

    def convert_vg(self, vl_spec, query_params):
        raise NotImplementedError
