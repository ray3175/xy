import pytest
import os
import tempfile
from xy.utils.qrcode import QRCode
from xy.utils.qrcode.extract import QRCodeExtract


class Test_QRCode:
    def setup_class(self):
        self.__data = "xy"
        self.qrcode = QRCode()
        self.qrcode_extract = QRCodeExtract()
        self.__dir = tempfile.mkdtemp()

    def teardown_class(self):
        pass

    def setup(self):
        pass

    def teardown(self):
        pass

    def test_new(self):
        qrcode_file_path = os.path.join(self.__dir, "xy_qrcode.png")
        assert self.qrcode.new(self.__data, qrcode_file_path) is True
        assert self.qrcode_extract.get_data_from_file(qrcode_file_path) == self.__data

    def test_new_with_bytes(self):
        bytes_data = self.qrcode.new_with_bytes(self.__data)
        assert self.qrcode_extract.get_data_from_content(bytes_data) == self.__data


if __name__ == "__main__":
    pytest.main(["-v", "-s", "test_qrcode.py"])


