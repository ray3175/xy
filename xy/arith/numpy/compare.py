import numpy


class Compare:
    @classmethod
    def equal(cls, np0, np1):
        """
        :param np0: numpy.ndarray
        :param np1: numpy.ndarray
        :return: numpy.ndarray
        """
        return numpy.equal(np0, np1)

    @classmethod
    def array_equal(cls, np0, np1):
        """
        :param np0: numpy.ndarray
        :param np1: numpy.ndarray
        :return: bool
        """
        return numpy.array_equal(np0, np1)
