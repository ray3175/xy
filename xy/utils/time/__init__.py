import datetime
from ...exception import XYException
from .time_stamp import TimeStamp
from .time_struct_time import TimeStructTime
from .time_datetime import TimeDateTime
from .time_string import TimeString


class Time(TimeStamp, TimeStructTime, TimeDateTime, TimeString):
    def __init__(self, timer=None, format="%Y-%m-%d %H:%M:%S"):
        self.__timer = timer
        self.__format = format
        super(Time, self).__init__(timer, format)

    def __str__(self):
        return self.to_string()

    def __add__(self, other: (int, float, dict, datetime.timedelta)):
        """
        :param other:
            (int, float)类型： 当前类self.time_stamp + (int, float)
            dict类型： 当前类self.datetime + datetime.timedelta(**dict)
                key只能为： ["days", "seconds", "microseconds", "milliseconds", "minutes", "hours", "weeks"]
            datetime.timedelta类型： 当前类self.datetime + other
        :return: 返回新的 Time 实例。
        """
        timer = None
        if isinstance(other, (int, float)):
            timer = self.time_stamp + other
        elif isinstance(other, (dict, datetime.timedelta)):
            if isinstance(other, dict):
                other = self.get_timedelta(**other)
            timer = self.datetime + other
        return self.__class__(timer, self.__format)

    def __sub__(self, other: (float, dict, datetime.timedelta)):
        """
        :param other:
            (int, float)类型： 当前类self.time_stamp - (int, float)
            dict类型： 当前类self.datetime - datetime.timedelta(**dict)
                key只能为： ["days", "seconds", "microseconds", "milliseconds", "minutes", "hours", "weeks"]
            datetime.timedelta类型： 当前类self.datetime - other
        :return: 返回新的 Time 实例。
        """
        timer = None
        if isinstance(other, (int, float)):
            timer = self.time_stamp - other
        elif isinstance(other, (dict, datetime.timedelta)):
            if isinstance(other, dict):
                other = self.get_timedelta(**other)
            timer = self.datetime - other
        return self.__class__(timer, self.__format)

    def __check_compare_type(self, other):
        if not isinstance(other, self.__class__):
            raise XYException("比较类型必须为 xy.utils.time.Time！")

    def __eq__(self, other):
        """
        other: xy.utils.time.Time()
        """
        self.__check_compare_type(other)
        return self.time_stamp == other.to_time_stamp()

    def __ne__(self, other):
        """
        other: xy.utils.time.Time()
        """
        self.__check_compare_type(other)
        return self.time_stamp != other.to_time_stamp()

    def __gt__(self, other):
        """
        other: xy.utils.time.Time()
        """
        self.__check_compare_type(other)
        return self.time_stamp > other.to_time_stamp()

    def __lt__(self, other):
        """
        other: xy.utils.time.Time()
        """
        self.__check_compare_type(other)
        return self.time_stamp < other.to_time_stamp()

    def __ge__(self, other):
        """
        other: xy.utils.time.Time()
        """
        self.__check_compare_type(other)
        return self.time_stamp >= other.to_time_stamp()

    def __le__(self, other):
        """
        other: xy.utils.time.Time()
        """
        self.__check_compare_type(other)
        return self.time_stamp <= other.to_time_stamp()

    @property
    def timer(self):
        return self.__timer

    @timer.setter
    def timer(self, timer):
        self.set_timer(timer)

    @timer.deleter
    def timer(self):
        self.set_timer()

    @property
    def format(self):
        return self.__format

    @format.setter
    def format(self, format):
        self.set_format(format)

    @format.deleter
    def format(self):
        self.set_format()

    def init(self, timer=None, format="%Y-%m-%d %H:%M:%S"):
        self.__timer = timer
        self.__format = format
        self.init_time_stamp(timer, format)
        self.init_struct_time(timer, format)
        self.init_datetime(timer, format)
        self.init_time_string(timer, format)

    def set_timer(self, timer=None):
        self.init(timer, self.__format)

    def set_format(self, format="%Y-%m-%d %H:%M:%S"):
        self.init(self.__timer, format)

    def to_string(self, format=None) -> str:
        if format:
            return self.datetime2string(self.datetime, format)
        return super().to_string()

