from typing import Union
import qrcode       # pip install qrcode
                    # pip install pillow
from ...common._io import RayBytesIO


class QRCode:
    def __init__(self, version: int = None, box_size: int = 2, border: int = 1):
        self.__qrcode = qrcode.QRCode(version, box_size=box_size, border=border)

    def __new(self, data, optimize=0):
        self.__qrcode.clear()
        self.__qrcode.add_data(data, optimize)
        self.__qrcode.make()

    def new(self, data: Union[bytes, str], save_path: str, optimize: int = 0):
        self.__new(data, optimize)
        self.__qrcode.make_image().save(save_path)

    def new_with_bytes(self, data: Union[bytes, str], optimize: int = 0, img_type: str = "png") -> bytes:
        self.__new(data, optimize)
        return RayBytesIO.pil_image_to_bytes_with_memory(self.__qrcode.make_image(), img_type)


