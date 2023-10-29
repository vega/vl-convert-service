import vl_convert as vlc

from pathlib import Path
from api.utils import ALLOWED_BASE_URLS, VlHandler

vlc.register_font_directory(str(Path("fonts").absolute()))


class handler(VlHandler):
    def convert_vl(self, vl_spec, query_params):
        vl_version = query_params.get("vl_version", None)

        try:
            svg = vlc.vegalite_to_svg(
                vl_spec,
                vl_version=vl_version,
                allowed_base_urls=ALLOWED_BASE_URLS,
            )
            self.send_successful(svg.encode(), 'image/svg+xml')
        except Exception as e:
            self.send_exception(e)