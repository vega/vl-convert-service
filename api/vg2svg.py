import vl_convert as vlc

from pathlib import Path
from api.utils import ALLOWED_BASE_URLS, VgHandler

vlc.register_font_directory(str(Path("fonts").absolute()))


class handler(VgHandler):
    def convert_vg(self, vg_spec, query_params):
        try:
            svg = vlc.vega_to_svg(
                vg_spec,
                allowed_base_urls=ALLOWED_BASE_URLS,
            )
            self.send_successful(svg.encode(), 'image/svg+xml')
        except Exception as e:
            self.send_exception(e)
