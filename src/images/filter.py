from io import BytesIO
from PIL import Image, ImageFilter


class Filter:
    def __init__(self):
        self.__src_img: Image.Image | None = None

    def set_src_img(self, b: bytes) -> None:
        self.__src_img = Image.open(BytesIO(b))

    def __get_bytes(self, img: Image.Image) -> BytesIO:
        arr = BytesIO()
        img.save(arr, format=self.__src_img.format)
        arr.seek(0)
        return arr

    def __black_white(self) -> BytesIO:
        return self.__get_bytes(self.__src_img.convert("L"))

    def add_filter(self, filter_name: str) -> BytesIO:
        if filter_name == "BW":
            return self.__black_white()

        ntc = {
            "EMBOSS": ImageFilter.EMBOSS,
            "BLUR": ImageFilter.BLUR,
            "SHARPEN": ImageFilter.SHARPEN
        }
        return self.__get_bytes(self.__src_img.filter(ntc[filter_name]))
