import numpy


class RayList(list):
    def __mul__(self, other):
        if isinstance(other, int):
            result = self.__class__([i * other for i in self])
        elif isinstance(other, self.__class__):
            result = self.__class__([[i, j] for i in self for j in other])
        else:
            result = self.__class__(numpy.asarray(self) * numpy.asarray(other))
        return result

    def __pos__(self):
        return self.__class__([[i, j] for i in self for j in self[self.index(i)+1:]])

    def __invert__(self):
        return self.__class__(sorted(self))

    def __neg__(self):
        return self[::-1]

    def to_list(self):
        return list(self)
