import pytest
import numpy
from xy.arith.numpy.linear_algebra import LinearAlgebra


class Test_LinearAlgebra:
    def setup_class(self):
        self.linear_algebra = LinearAlgebra()

    def teardown_class(self):
        pass

    def setup(self):
        pass

    def teardown(self):
        pass

    def test_is_equal_row_col(self):
        tmp_0 = [
            [1, 2, 3],
            [4, 5, 6]
        ]
        tmp_1 = [
            [1, 2],
            [3, 4],
            [5, 6]
        ]
        tmp_np_0 = numpy.asarray(tmp_0)
        tmp_np_1 = numpy.asarray(tmp_1)
        assert self.linear_algebra.is_equal_row_col(tmp_0) is False
        assert self.linear_algebra.is_equal_row_col(tmp_1) is False
        assert self.linear_algebra.is_equal_row_col(tmp_np_0) is False
        assert self.linear_algebra.is_equal_row_col(tmp_np_1) is False

    def test_determinant(self):
        array_0 = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        array_1 = [
            [1, 2, 3],
            [3, 3, 3],
            [3, 3, 3]
        ]
        matrix_0 = numpy.asarray(array_0)
        matrix_1 = numpy.asarray(array_1)
        assert self.linear_algebra.determinant(array_0) == self.linear_algebra.determinant(array_1)
        assert self.linear_algebra.determinant(matrix_0) == self.linear_algebra.determinant(matrix_1)

    def test_inverse(self):
        """
        求逆矩阵过程：
            [
                [1, 2, 0 | 1, 0, 0],
                [2, 0, 1 | 0, 1, 0],
                [1, 3, 1 | 0, 0, 1]
            ]
            [
                [1, 3, 1 | 0, 0, 1],
                [1, 2, 0 | 1, 0, 0],
                [2, 0, 1 | 0, 1, 0]
            ]
            [
                [1,  3,  1 |  0, 0,  1],
                [0, -1, -1 |  1, 0, -1],
                [0,  0,  5 | -6, 1,  4]
            ]
            [
                [1,  3,  1 |  0, 0,  1],
                [0, -1, -1 |  1, 0, -1],
                [0,  0,  5 | -6, 1,  4]
            ]
            [
                [1,  0, 0 |  3/5, 2/5, -2/5],
                [0, -1, 0 | -1/5, 1/5, -1/5],
                [0,  0, 5 |   -6,   1,    4]
            ]
            [
                [1, 0, 0 |  3/5,  2/5, -2/5],
                [0, 1, 0 |  1/5, -1/5,  1/5],
                [0, 0, 1 | -6/5,  1/5,  4/5]
            ]
            matrix^-1 = [
                [ 3/5,  2/5, -2/5],
                [ 1/5, -1/5,  1/5],
                [-6/5,  1/5,  4/5]
            ]
        """
        tmp = [
            [1, 2, 0],
            [2, 0, 1],
            [1, 3, 1]
        ]
        tmp_inverse = [
            [3/5, 2/5, -2/5],
            [1/5, -1/5, 1/5],
            [-6/5, 1/5, 4/5]
        ]
        assert [[round(j) for j in i] for i in self.linear_algebra.inverse(tmp).tolist()] == [[round(j) for j in i] for i in numpy.asarray(tmp_inverse).tolist()]

    def test_adjugate(self):
        """
        求伴随矩阵过程：
            A11 = (-1)^(1+1)[
                [0, 1],
                [3, 1]
            ]
            A12 = (-1)^(1+2)[
                [2, 1],
                [1, 1]
            ]
            A13 = (-1)^(1+3)[
                [2, 0],
                [1, 3]
            ]
            A21 = (-1)^(2+1)[
                [2, 0],
                [3, 1]
            ]
            A22 = (-1)^(2+2)[
                [1, 0],
                [1, 1]
            ]
            A23 = (-1)^(2+3)[
                [1, 2],
                [1, 3]
            ]
            A31 = (-1)^(3+1)[
                [2, 0],
                [0, 1]
            ]
            A32 = (-1)^(3+2)[
                [1, 0],
                [2, 1]
            ]
            A33 = (-1)^(3+3)[
                [1, 2],
                [2, 0]
            ]
            matrix* = [
                [A11, A21, A31],
                [A12, A22, A32],
                [A13, A23, A33]
            ]
        """
        tmp = [
            [1, 2, 0],
            [2, 0, 1],
            [1, 3, 1]
        ]
        A11 = (-1)**(1+1) * self.linear_algebra.determinant([[0, 1], [3, 1]])
        A12 = (-1)**(1+2) * self.linear_algebra.determinant([[2, 1], [1, 1]])
        A13 = (-1)**(1+3) * self.linear_algebra.determinant([[2, 0], [1, 3]])
        A21 = (-1)**(2+1) * self.linear_algebra.determinant([[2, 0], [3, 1]])
        A22 = (-1)**(2+2) * self.linear_algebra.determinant([[1, 0], [1, 1]])
        A23 = (-1)**(2+3) * self.linear_algebra.determinant([[1, 2], [1, 3]])
        A31 = (-1)**(3+1) * self.linear_algebra.determinant([[2, 0], [0, 1]])
        A32 = (-1)**(3+2) * self.linear_algebra.determinant([[1, 0], [2, 1]])
        A33 = (-1)**(3+3) * self.linear_algebra.determinant([[1, 2], [2, 0]])
        tmp_adjugate = [
            [A11, A21, A31],
            [A12, A22, A32],
            [A13, A23, A33]
        ]
        assert [[round(j) for j in i] for i in self.linear_algebra.adjugate(tmp).tolist()] == [[round(j) for j in i] for i in numpy.asarray(tmp_adjugate).tolist()]


if __name__ == "__main__":
    pytest.main(["-v", "-s", "test_linear_algebra.py"])


