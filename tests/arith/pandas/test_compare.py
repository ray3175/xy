import pytest
import numpy
import pandas
from xy.arith.pandas.compare import Compare


class Test_Compare:
    def setup_class(self):
        self.compare = Compare()
        columns = ["a", "b", "c"]
        values = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.__dict1 = {columns[0]: values[0], columns[1]: values[1], columns[2]: values[2]}
        self.__pd0 = pandas.DataFrame(values, columns=columns)
        self.__pd1 = pandas.DataFrame(self.__dict1)
        self.__pd2 = pandas.DataFrame(numpy.asarray(values).transpose(), columns=columns)
        self.__pd3 = pandas.DataFrame(numpy.asarray(values).transpose().tolist(), columns=columns)

    def teardown_class(self):
        pass

    def setup(self):
        pass

    def teardown(self):
        pass

    def test_equal_0(self):
        assert self.compare.equal(self.__pd0, self.__pd1) is False

    def test_equal_1(self):
        assert self.compare.equal(self.__pd1, self.__pd2) is False

    def test_equal_2(self):
        assert self.compare.equal(self.__pd1, self.__pd3) is True

    def test_equal_3(self):
        assert self.compare.equal(self.__pd2, self.__dict1) is None


if __name__ == "__main__":
    pytest.main(["-v", "-s", "test_compare.py"])


