import pandas


class IsPd:
    @classmethod
    def is_pd(cls, pd):
        """
        :param pd: pandas.core.frame.DataFrame
        :return: bool
        """
        _return = None
        if isinstance(pd, pandas.DataFrame):
            _return = True
        return _return

    @classmethod
    def is_not_pd(cls, pd):
        """
        :param pd: pandas.core.frame.DataFrame
        :return: bool
        """
        _return = None
        if not isinstance(pd, pandas.DataFrame):
            _return = True
        return _return

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

    @classmethod
    def is_not_empty(cls, pd):
        """
        :param pd: pandas.core.frame.DataFrame
        :return: bool
        """
        return not cls.is_empty(pd)
