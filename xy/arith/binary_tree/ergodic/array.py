from . import Ergodic


class ArrayErgodic(Ergodic):
    @classmethod
    def depth_first_ergodic(cls, array):
        if (len_array:=len(array)) > 1:
            return [[i, *j] for i in array[0] for j in cls.depth_first_ergodic(array[1:])]
        elif len_array == 1:
            return array[0]
        else:
            return []

    @classmethod
    def breadth_first_ergodic(cls, array):
        if (len_array:=len(array)) > 1:
            return [[i, *j] for j in cls.breadth_first_ergodic(array[1:]) for i in array[0]]
        elif len_array == 1:
            return array[0]
        else:
            return []


