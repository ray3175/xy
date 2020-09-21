import pytest
import numpy
from xy.arith.numpy.is_np import IsNp


class Test_IsNp:
    def setup_class(self):
        self.is_np = IsNp()
        self.__list_0 = [[1, 2], [3, 4]]
        self.__np_0 = numpy.asarray(self.__list_0)
        self.__list_1 = []
        self.__np_1 = numpy.asarray(self.__list_1)

    def teardown_class(self):
        pass

    def setup(self):
        pass

    def teardown(self):
        pass

    def test_is_np_0(self):
        assert self.is_np.is_np(self.__np_0) is True
        assert self.is_np.is_np(self.__np_1) is True

    def test_is_np_1(self):
        assert self.is_np.is_np(self.__list_0) is None
        assert self.is_np.is_np(self.__list_1) is None

    def test_is_not_np_0(self):
        assert self.is_np.is_not_np(self.__np_0) is None
        assert self.is_np.is_not_np(self.__np_1) is None

    def test_is_not_np_1(self):
        assert self.is_np.is_not_np(self.__list_0) is True
        assert self.is_np.is_not_np(self.__list_1) is True

    def test_is_empty_0(self):
        assert self.is_np.is_empty(self.__np_0) is False
        assert self.is_np.is_empty(self.__np_1) is True

    def test_is_empty_1(self):
        assert self.is_np.is_empty(self.__list_0) is None
        assert self.is_np.is_empty(self.__list_0) is None


if __name__ == "__main__":
    pytest.main(["-v", "-s", "test_is_np.py"])


