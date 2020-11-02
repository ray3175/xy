import numpy


class IsNp:
    @classmethod
    def is_np(cls, np):
        """
        :param np: numpy.ndarray
        :return: bool
        """
        return isinstance(np, numpy.ndarray)

    @classmethod
    def is_empty(cls, np):
        """
        :param np: numpy.ndarray
        :return: bool
        """
        _return = None
        if cls.is_np(np):
            _return = not bool(np.size)
        return _return
