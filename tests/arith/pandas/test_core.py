import pytest
import os
import shutil
import tempfile
import numpy
import pandas
from xy.arith.pandas.core import Core


class Test_Core:
    def setup_class(self):
        self.core = Core()
        self.__columns = columns = ["a", "b", "c"]
        self.__values = values = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.__values_transpose = numpy.asarray(self.__values).transpose().tolist()
        self.__dict = {columns[0]: tuple(values[0]), columns[1]: tuple(values[1]), columns[2]: tuple(values[2])}
        self.__dicts = [{columns[0]: values[0][0], columns[1]: values[1][0], columns[2]: values[2][0]}, {columns[0]: values[0][1], columns[1]: values[1][1], columns[2]: values[2][1]}, {columns[0]: values[0][2], columns[1]: values[1][2], columns[2]: values[2][2]}]
        self.__pd = pandas.DataFrame(self.__dict)

    def teardown_class(self):
        pass

    def setup(self):
        pass

    def teardown(self):
        pass

    def test_new_pd(self):
        assert isinstance(self.core.new_pd(self.__columns, self.__values), pandas.DataFrame)

    def test_new_pd_with_dict(self):
        assert isinstance(self.core.new_pd_with_dict(self.__dict), pandas.DataFrame)

    def test_get_pd_columns(self):
        assert self.core.get_pd_columns(self.__pd) == self.__columns

    def test_get_pd_values(self):
        assert self.core.get_pd_values(self.__pd) == self.__values_transpose

    def test_pd2dict(self):
        assert self.core.pd2dict(self.__pd) == self.__dict

    def test_pd2dicts(self):
        assert self.core.pd2dicts(self.__pd) == self.__dicts

    def test_pd2excel_excel2pd(self):
        path = tempfile.mkdtemp()
        file = os.path.join(path, "file-test_core-Test_ArrayErgodic-test_pd2excel.xlsx")
        assert self.core.pd2excel(self.__pd, file) == True
        pd = self.core.excel2pd(file)
        assert self.core.get_pd_columns(pd)[1:] == self.__columns
        assert [value[1:] for value in self.core.get_pd_values(pd)] == self.__values_transpose
        shutil.rmtree(path)


if __name__ == "__main__":
    pytest.main(["-v", "-s", "test_core.py"])


