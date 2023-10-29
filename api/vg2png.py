import vl_convert as vlc
from pathlib import Path

from api.utils import ALLOWED_BASE_URLS, VgHandler

vlc.register_font_directory(str(Path("fonts").absolute()))


class handler(VgHandler):
    def convert_vg(self, vg_spec, query_params):
        scale = query_params.get("scale", None)

        try:
            png_data = vlc.vega_to_png(
                vg_spec,
                scale=float(scale) if scale is not None else None,
                allowed_base_urls=ALLOWED_BASE_URLS
            )
            self.send_successful(png_data, 'image/png')
        except Exception as e:
            self.send_exception(e)
