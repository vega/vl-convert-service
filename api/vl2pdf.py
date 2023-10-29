import vl_convert as vlc
from api.utils import ALLOWED_BASE_URLS, VlHandler


class handler(VlHandler):
    def convert_vl(self, vl_spec, query_params):
        vl_version = query_params.get("vl_version", None)
        scale = query_params.get("scale", None)
        theme = query_params.get("theme", None)

        try:
            pdf_data = vlc.vegalite_to_pdf(
                vl_spec,
                vl_version=vl_version,
                scale=float(scale) if scale is not None else None,
                theme=theme,
                allowed_base_urls=ALLOWED_BASE_URLS,
            )
            self.send_successful(pdf_data, "application/pdf")
        except Exception as e:
            self.send_exception(e)
