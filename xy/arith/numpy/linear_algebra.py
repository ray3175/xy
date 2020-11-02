import numpy
from .is_np import IsNp


class LinearAlgebra:
    @classmethod
    def is_equal_row_col(cls, array):
        """
        判断矩阵 row 和 col 是否相等。
        """
        row, col = 1, 0
        if IsNp.is_np(array):
            row, col = array.shape
        elif isinstance(array, list):
            row = len(array)
            col = row
            for i in array:
                if len(i) != col:
                    return False
        return row == col

    @classmethod
    def determinant(cls, array, validate=True) -> numpy.float64:
        """
        求行列式的值。
        :param array: 可以是list类型，可以是numpy.ndarray类型。
        """
        _return = None
        if (not validate) or cls.is_equal_row_col(array):
            _return = numpy.linalg.det(array)
        return _return

    @classmethod
    def inverse(cls, array, validate=True) -> numpy.ndarray:
        """
        求逆矩阵。
        :param array: 可以是list类型，可以是numpy.ndarray类型。
        :return: 如果矩阵不可逆，则返回False。
        """
        _return = None
        if (not validate) or cls.is_equal_row_col(array):
            try:
                _return = numpy.linalg.inv(array)
            except numpy.linalg.LinAlgError:
                _return = False
        return _return

    @classmethod
    def adjugate(cls, array, validate=True) -> numpy.ndarray:
        """
        求伴随矩阵。
        :param array: 可以是list类型，可以是numpy.ndarray类型。
        :return: 如果矩阵不可逆，则返回False。
        """
        _return = None
        if (not validate) or cls.is_equal_row_col(array):
            _return = cls.determinant(array, validate=False) * inverse if ((inverse:=cls.inverse(array, validate=False)) is not False) else False
        return _return

