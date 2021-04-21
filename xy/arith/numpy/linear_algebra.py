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
            _return = cls.determinant(array, validate=False) * inverse if ((inverse := cls.inverse(array, validate=False)) is not False) else False
        return _return

    @classmethod
    def solve(cls, a, b):
        """
        设，解三元一次方程组：
            ① a[0][0]x + a[0][1]y + a[0][2]z = b[0]
            ② a[1][0]x + a[1][1]y + a[1][2]z = b[1]
            ③ a[2][0]x + a[2][1]y + a[2][2]z = b[2]
        :param a: 方程组x, y的系数。其值必须是方阵。
        :param b: 方程组的值。
        只有当方程组 x, y, z 有唯一解的时候才能解方程。
        :return: [x, y, z]
        """
        return numpy.linalg.solve(a, b)

