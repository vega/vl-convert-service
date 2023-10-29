from http.server import BaseHTTPRequestHandler
from urllib import parse
import vl_convert as vlc
from pathlib import Path

from api.utils import ALLOWED_BASE_URLS, VlHandler

vlc.register_font_directory(str(Path("fonts").absolute()))


class handler(VlHandler):
    def convert_vl(self, vl_spec, query_params):
        vl_version = query_params.get("vl_version", None)
        scale = query_params.get("scale", None)

        try:
            png_data = vlc.vegalite_to_png(
                vl_spec,
                vl_version=vl_version,
                scale=float(scale) if scale is not None else None,
                allowed_base_urls=ALLOWED_BASE_URLS
            )
            self.send_successful(png_data, 'image/png')
        except Exception as e:
            self.send_exception(e)