import pytest
import numpy
from xy.arith.numpy.compare import Compare


class Test_Compare:
    def setup_class(self):
        self.compare = Compare()
        list_0 = [[1, 2], [3, 4]]
        self.__np_0 = numpy.asarray(list_0)
        list_1 = [[1, 2], [3, 4]]
        self.__np_1 = numpy.asarray(list_1)
        list_2 = [[1, 3], [2, 4]]
        self.__np_2 = numpy.asarray(list_2)

    def teardown_class(self):
        pass

    def setup(self):
        pass

    def teardown(self):
        pass

    def test_equal_0(self):
        assert self.compare.equal(self.__np_0, self.__np_1).tolist() == [[True, True], [True, True]]

    def test_equal_1(self):
        assert self.compare.equal(self.__np_0, self.__np_2).tolist() == [[True, False], [False, True]]

    def test_array_equal_0(self):
        assert self.compare.array_equal(self.__np_0, self.__np_1) is True

    def test_array_equal_1(self):
        assert self.compare.array_equal(self.__np_0, self.__np_2) is False


if __name__ == "__main__":
    pytest.main(["-v", "-s", "test_compare.py"])


