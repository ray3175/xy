import qrcode       # pip install qrcode


class QRCode:
    def __init__(self, version=None, box_size=2, border=1):
        self.__qrcode = qrcode.QRCode(version, box_size=box_size, border=border)

    def new(self, data, save_path, optimize=0):
        self.__qrcode.clear()
        self.__qrcode.add_data(data, optimize)
        self.__qrcode.make()
        self.__qrcode.make_image().save(save_path)

