import vl_convert as vlc
from api.utils import VlHandler
import json


class handler(VlHandler):
    def convert_vl(self, vl_spec, query_params):
        vl_version = query_params.get("vl_version", None)
        try:
            vg_spec = vlc.vegalite_to_vega(vl_spec, vl_version=vl_version)
            self.send_successful(json.dumps(vg_spec).encode(), "application/json")
        except Exception as e:
            self.send_exception(e)
