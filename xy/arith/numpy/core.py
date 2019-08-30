import numpy        # pip install numpy
from .is_np import IsNp


class Core:
    @classmethod
    def new_np(cls, _list, dtype=None, order=None):
        """
        :param _list: []
        :param dtype: numpy.int32（default）, numpy.int64, numpy.float32, numpy.float64, ...
        :param order: "C"|"F"
        :return: numpy.ndarray
        """
        return numpy.asarray(_list, dtype, order)

    @classmethod
    def np2list(cls, np):
        """
        :param np: numpy.ndarray
        :return: []
        """
        _return = list()
        if IsNp.is_np(np):
            _return = np.tolist()
        return _return

    @classmethod
    def np2string(cls, np):
        """
        :param np: numpy.ndarray
        :return: str
        """
        _return = ""
        if IsNp.is_np(np):
            _return = np.tostring()
        return _return
