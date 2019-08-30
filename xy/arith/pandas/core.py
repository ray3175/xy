import pandas       # pip install pandas
from .is_pd import IsPd
from ..numpy.core import Core as np_core


class Core:
    @classmethod
    def new_pd(cls, columns, values):
        """
        :param columns: [col0, col1, ...]
        :param values: [[], [], ...]
        :return: pandas.core.frame.DataFrame
        """
        return pandas.DataFrame(values, columns=columns)

    @classmethod
    def new_pd_with_dict(cls, _dict):
        """
        :param _dict: {col0: [], col1: [], ...}
        :return: pandas.core.frame.DataFrame
        """
        return pandas.DataFrame(_dict)

    @classmethod
    def pd2dict(cls, pd):
        """
        :param pd: pandas.core.frame.DataFrame
        :return: {col0: [], col1: [], ...}
        """
        _return = dict()
        if IsPd.is_pd(pd):
            key = cls.get_pd_columns(pd)
            value = cls.get_pd_values(pd)
            _return = dict(zip(key, zip(*value)))
        return _return

    @classmethod
    def pd2dicts(cls, pd):
        """
        :param pd: pandas.core.frame.DataFrame
        :return: [{}, {}, ...]
        """
        _return = list()
        if IsPd.is_pd(pd):
            key = cls.get_pd_columns(pd)
            value = cls.get_pd_values(pd)
            _return = [dict(zip(key, _value)) for _value in value]
        return _return

    @classmethod
    def get_pd_columns(cls, pd):
        """
        :param pd: pandas.core.frame.DataFrame
        :return: []
        """
        _return = list()
        if IsPd.is_pd(pd):
            _return = np_core.np2list(pd.columns.values)
        return _return

    @classmethod
    def get_pd_values(cls, pd):
        """
        :param pd: pandas.core.frame.DataFrame
        :return: [[], [], ...]
        """
        _return = None
        if IsPd.is_pd(pd):
            _return = np_core.np2list(pd.values)
        return _return
