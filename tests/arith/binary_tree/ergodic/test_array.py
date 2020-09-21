import pytest
from xy.arith.binary_tree.ergodic.array import ArrayErgodic


class Test_ArrayErgodic:
    def setup_class(self):
        self.array_ergodic = ArrayErgodic()
        self.__params_0 = []
        self.__params_1 = [
            ["a", "b"]
        ]
        self.__params_2 = [
            ["a", "b"],
            ["c", "d"]
        ]
        self.__params_3 = [
            ["a", "b", "c"],
            ["d", "e", "f"],
            ["g", "h", "i"]
        ]

    def teardown_class(self):
        pass

    def setup(self):
        pass

    def teardown(self):
        pass

    def test_depth_first_ergodic_0(self):
        assert self.array_ergodic.depth_first_ergodic(self.__params_0) == []

    def test_depth_first_ergodic_1(self):
        assert self.array_ergodic.depth_first_ergodic(self.__params_1) == ["a", "b"]

    def test_depth_first_ergodic_2(self):
        assert self.array_ergodic.depth_first_ergodic(self.__params_2) == [["a", "c"], ["a", "d"], ["b", "c"], ["b", "d"]]

    def test_depth_first_ergodic_3(self):
        assert self.array_ergodic.depth_first_ergodic(self.__params_3) == [["a", "d", "g"], ["a", "d", "h"], ["a", "d", "i"], ["a", "e", "g"], ["a", "e", "h"], ["a", "e", "i"], ["a", "f", "g"], ["a", "f", "h"], ["a", "f", "i"], ["b", "d", "g"], ["b", "d", "h"], ["b", "d", "i"], ["b", "e", "g"], ["b", "e", "h"], ["b", "e", "i"], ["b", "f", "g"], ["b", "f", "h"], ["b", "f", "i"], ["c", "d", "g"], ["c", "d", "h"], ["c", "d", "i"], ["c", "e", "g"], ["c", "e", "h"], ["c", "e", "i"], ["c", "f", "g"], ["c", "f", "h"], ["c", "f", "i"]]

    def test_breadth_first_ergodic_0(self):
        assert self.array_ergodic.breadth_first_ergodic(self.__params_0) == []

    def test_breadth_first_ergodic_1(self):
        assert self.array_ergodic.breadth_first_ergodic(self.__params_1) == ["a", "b"]

    def test_breadth_first_ergodic_2(self):
        assert self.array_ergodic.breadth_first_ergodic(self.__params_2) == [["a", "c"], ["b", "c"], ["a", "d"], ["b", "d"]]

    def test_breadth_first_ergodic_3(self):
        assert self.array_ergodic.breadth_first_ergodic(self.__params_3) == [["a", "d", "g"], ["b", "d", "g"], ["c", "d", "g"], ["a", "e", "g"], ["b", "e", "g"], ["c", "e", "g"], ["a", "f", "g"], ["b", "f", "g"], ["c", "f", "g"], ["a", "d", "h"], ["b", "d", "h"], ["c", "d", "h"], ["a", "e", "h"], ["b", "e", "h"], ["c", "e", "h"], ["a", "f", "h"], ["b", "f", "h"], ["c", "f", "h"], ["a", "d", "i"], ["b", "d", "i"], ["c", "d", "i"], ["a", "e", "i"], ["b", "e", "i"], ["c", "e", "i"], ["a", "f", "i"], ["b", "f", "i"], ["c", "f", "i"]]


if __name__ == "__main__":
    pytest.main(["-v", "-s", "test_array.py"])


