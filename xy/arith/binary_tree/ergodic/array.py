from . import Ergodic


class ArrayErgodic(Ergodic):
    @classmethod
    def depth_first_ergodic(cls, array):
        temp_array = list()
        if array:
            for i in array[0]:
                if array[1:]:
                    for j in cls.depth_first_ergodic(array[1:]):
                        temp_array.append([i, *j])
                else:
                    temp_array.append([i])
        return temp_array

    @classmethod
    def breadth_first_ergodic(cls, array):
        temp_array = list()
        if array:
            temp_list = list()
            for i in array[0]:
                temp_list.append(i)
            if array[1:]:
                for j in cls.breadth_first_ergodic(array[1:]):
                    for k in temp_list:
                        temp_array.append([k, *j])
            else:
                temp_array.extend([[i] for i in temp_list])
        return temp_array


