from io import BytesIO
from pyzbar import pyzbar       # pip install pyzbar
from PIL import Image       # pip install pillow


class QRCodeExtract:
    def __action(self, img):
        info = pyzbar.decode(img)
        return info[0].data.decode("utf-8")

    def get_data_from_file(self, file_path) -> str:
        img = Image.open(file_path)
        return self.__action(img)

    def get_data_from_content(self, content: bytes) -> str:
        _io = BytesIO(content)
        return self.get_data_from_file(_io)

