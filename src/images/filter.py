from io import BytesIO

from PIL import Image, ImageFilter


class Filter:
    def __init__(self):
        self.__src_img: Image.Image

    def __get_bytes(self, img):
        arr = BytesIO()
        img.save(arr, format=self.__src_img.format)
        arr.seek(0)
        return arr

    def set_src_img(self, b: bytes) -> None:
        self.__src_img = Image.open(BytesIO(b))

    def add_filter(self, filter_name: str) -> BytesIO:
        ntc = {
            "EMBOSS": ImageFilter.EMBOSS,
            "BLUR": ImageFilter.BLUR
        }
        return self.__get_bytes(self.__src_img.filter(ntc[filter_name]))
