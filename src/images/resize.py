from io import BytesIO

from PIL import Image


class Resizer:
    def __init__(self):
        self.__src_img: Image.Image | None = None

    def set_src_img(self, b: bytes) -> None:
        self.__src_img = Image.open(BytesIO(b))

    def __get_bytes(self, img) -> BytesIO:
        arr = BytesIO()
        img.save(arr, format=self.__src_img.format)
        arr.seek(0)
        return arr

    def change_sizes(self, sizes: tuple) -> BytesIO:
        return self.__get_bytes(self.__src_img.resize(sizes))
