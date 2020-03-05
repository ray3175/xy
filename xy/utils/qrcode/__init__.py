import qrcode       # pip install qrcode
from ...common._io import RayBytesIO


class QRCode:
    def __init__(self, version=None, box_size=2, border=1):
        self.__qrcode = qrcode.QRCode(version, box_size=box_size, border=border)

    def __new(self, data, optimize=0):
        self.__qrcode.clear()
        self.__qrcode.add_data(data, optimize)
        self.__qrcode.make()

    def new(self, data, save_path, optimize=0):
        self.__new(data, optimize)
        self.__qrcode.make_image().save(save_path)

    def new_with_bytes(self, data, optimize=0, img_type="jpeg"):
        self.__new(data, optimize)
        return RayBytesIO.pil_image_to_bytes_with_memory(self.__qrcode.make_image(), img_type)


