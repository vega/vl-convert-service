import vl_convert as vlc
from api.utils import ALLOWED_BASE_URLS, VgHandler


class handler(VgHandler):
    def convert_vg(self, vg_spec, query_params):
        scale = query_params.get("scale", None)

        try:
            pdf_data = vlc.vega_to_pdf(
                vg_spec,
                scale=float(scale) if scale is not None else None,
                allowed_base_urls=ALLOWED_BASE_URLS,
            )
            self.send_successful(pdf_data, "application/pdf")
        except Exception as e:
            self.send_exception(e)
