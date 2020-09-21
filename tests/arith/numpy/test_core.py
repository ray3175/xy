import pytest
import numpy
from xy.arith.numpy.core import Core


class Test_Core:
    def setup_class(self):
        self.core = Core()
        self.__list = [[1, 2], [3, 4]]
        self.__np = numpy.asarray(self.__list)
        self.__np_bytes = b"\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00\x04\x00\x00\x00"

    def teardown_class(self):
        pass

    def setup(self):
        pass

    def teardown(self):
        pass

    def test_new_np_0(self):
        assert isinstance(self.core.new_np(self.__list), type(self.__np))

    def test_new_np_1(self):
        assert isinstance(self.core.new_np(self.__np), type(self.__np))

    def test_np2list_0(self):
        assert self.core.np2list(self.__np) == self.__list

    def test_np2list_1(self):
        assert self.core.np2list(self.__list) == []

    def test_np2bytes_0(self):
        assert self.core.np2bytes(self.__np) == self.__np_bytes

    def test_np2bytes_1(self):
        assert self.core.np2bytes(self.__list) == b""


if __name__ == "__main__":
    pytest.main(["-v", "-s", "test_core.py"])


