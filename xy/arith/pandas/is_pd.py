import pandas


class IsPd:
    @classmethod
    def is_pd(cls, pd):
        """
        :param pd: pandas.core.frame.DataFrame
        :return: bool
        """
        return isinstance(pd, pandas.DataFrame)

    @classmethod
    def is_empty(cls, pd):
        """
        :param pd: pandas.core.frame.DataFrame
        :return: bool
        """
        _return = None
        if cls.is_pd(pd):
            _return = pd.empty
        return _return

