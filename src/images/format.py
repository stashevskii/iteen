from io import BytesIO
from PIL import Image


class FormatChanger:
    def __init__(self):
        self.__src_img: Image.Image | None = None

    def set_src_img(self, b: bytes) -> None:
        self.__src_img = Image.open(BytesIO(b))

    def __get_bytes(self, fmt: str) -> BytesIO:
        img = self.__src_img.copy()
        arr = BytesIO()
        img.save(arr, format=fmt)
        arr.seek(0)
        return arr

    def change_format(self, fmt: str) -> BytesIO:
        return self.__get_bytes(fmt)
