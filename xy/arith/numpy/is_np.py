import numpy


class IsNp:
    @classmethod
    def is_np(cls, np):
        """
        :param np: numpy.ndarray
        :return: bool
        """
        _return = None
        if isinstance(np, numpy.ndarray):
            _return = True
        return _return

    @classmethod
    def is_not_np(cls, np):
        """
        :param np: numpy.ndarray
        :return: bool
        """
        _return = None
        if not isinstance(np, numpy.ndarray):
            _return = True
        return _return

    @classmethod
    def is_empty(cls, np):
        """
        :param np: numpy.ndarray
        :return: bool
        """
        _return = None
        if cls.is_np(np):
            _return = bool(np.size)
        return _return
