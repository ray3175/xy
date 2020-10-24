import datetime
from ...exception import XYException
from .time_stamp import TimeStamp
from .time_struct_time import TimeStructTime
from .time_datetime import TimeDateTime
from .time_string import TimeString


class Time(TimeStamp, TimeStructTime, TimeDateTime, TimeString):
    def __init__(self, timer=None, format="%Y-%m-%d %H:%M:%S", unit="days"):
        """
        :param unit: days | seconds | microseconds | milliseconds | minutes | hours | weeks | fold
        """
        self.__timer = timer
        self.__format = format
        self.__unit = unit
        super(Time, self).__init__(timer)

    def __str__(self):
        return self.to_string()

    def __add__(self, other: float):
        return self.__class__(self.datetime + datetime.timedelta(**{self.__unit: other}), self.__format, self.__unit)

    def __sub__(self, other: float):
        return self.__class__(self.datetime - datetime.timedelta(**{self.__unit: other}), self.__format, self.__unit)

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

    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, unit):
        self.__unit = unit

    def init(self, timer=None, format="%Y-%m-%d %H:%M:%S", unit="days"):
        self.__timer = timer
        self.__format = format
        self.__unit = unit
        self.init_time_stamp(timer, format)
        self.init_struct_time(timer, format)
        self.init_datetime(timer, format)
        self.init_time_string(timer, format)

    def set_timer(self, timer=None):
        self.init(timer, self.__format, self.__unit)

    def set_format(self, format="%Y-%m-%d %H:%M:%S"):
        self.init(self.__timer, format, self.__unit)

    def set_unit(self, unit="days"):
        self.__unit = unit

    def to_string(self, format=None) -> str:
        if format:
            return self.datetime2string(self.datetime, format)
        return super().to_string()

