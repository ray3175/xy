from .is_pd import IsPd


class Compare:
    @classmethod
    def equal(cls, pd0, pd1):
        """
        :param pd0: pandas.core.frame.DataFrame
        :param pd1: pandas.core.frame.DataFrame
        :return: bool
        """
        _return = None
        if IsPd.is_pd(pd0) and IsPd.is_pd(pd1):
            _return = pd0.equals(pd1)
        return _return
