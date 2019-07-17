import numpy
from .ray_list import RayList


class PlusList(RayList):
    def __matmul__(self, other):
        if isinstance(other, int):
            result = self.__class__([i * other for i in self])
        elif isinstance(other, self.__class__):
            result = self.__class__([[i, j] for i in self for j in other])
        else:
            result = self.__class__(numpy.asarray(self) * numpy.asarray(other))
        return result

    def __pos__(self):
        _max = len(self)
        return [[self[i], self[j]] for i in range(0, _max-1) for j in range(i+1, _max)]

    def __invert__(self):
        return self.__class__(sorted(self))

    def __neg__(self):
        return self[::-1]
