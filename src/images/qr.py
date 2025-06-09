import qrcode
from io import BytesIO


class QR:
    def __init__(self):
        self.version = 1
        self.error_correction = qrcode.constants.ERROR_CORRECT_L
        self.box_size = 10
        self.border = 4

    def __render_qr(self, link: str):
        qr = qrcode.QRCode(
            version=self.version,
            error_correction=self.error_correction,
            box_size=self.box_size,
            border=self.border
        )
        qr.add_data(link)
        qr.make(fit=True)
        return qr.make_image(fill_color="black", back_color="white")

    @staticmethod
    def __get_bytes(img) -> BytesIO:
        arr = BytesIO()
        img.save(arr, format="PNG")
        arr.seek(0)
        return arr

    def get_qr(self, link: str) -> BytesIO:
        return self.__get_bytes(self.__render_qr(link))
