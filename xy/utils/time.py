import time
import datetime
from ..exception import XYException


class Time:
    def __init__(self, timer=None, format="%Y-%m-%d %H:%M:%S", unit="days"):
        """
        :param unit: days | seconds | microseconds | milliseconds | minutes | hours | weeks | fold
        """
        self.__format = format
        self.__unit = unit
        if isinstance(timer, (int, float)):
            self.__time = timer
        elif isinstance(timer, str):
            self.__time = time.mktime(time.strptime(timer, format))
        elif isinstance(timer, datetime.datetime):
            self.__time = time.mktime(timer.utctimetuple())
        elif isinstance(timer, datetime.date):
            self.__time = time.mktime(timer.timetuple())
        elif isinstance(timer, time.struct_time):
            self.__time = time.mktime(timer)
        else:
            self.__time = time.time()

    def __str__(self):
        return self.to_string()

    def __add__(self, other: float):
        return self.__class__(datetime.datetime.fromtimestamp(self.to_time_stamp()) + datetime.timedelta(**{self.__unit: other}), self.__format, self.__unit)

    def __sub__(self, other: float):
        return self.__class__(datetime.datetime.fromtimestamp(self.to_time_stamp()) - datetime.timedelta(**{self.__unit: other}), self.__format, self.__unit)

    def __check_compare_type(self, other):
        if not isinstance(other, self.__class__):
            raise XYException("比较类型必须为xy.utils.time.Time")

    def __eq__(self, other):
        self.__check_compare_type(other)
        return self.__time == other.to_time_stamp()

    def __ne__(self, other):
        self.__check_compare_type(other)
        return self.__time != other.to_time_stamp()

    def __gt__(self, other):
        self.__check_compare_type(other)
        return self.__time > other.to_time_stamp()

    def __lt__(self, other):
        self.__check_compare_type(other)
        return self.__time < other.to_time_stamp()

    def __ge__(self, other):
        self.__check_compare_type(other)
        return self.__time >= other.to_time_stamp()

    def __le__(self, other):
        self.__check_compare_type(other)
        return self.__time <= other.to_time_stamp()

    def set_format(self, format="%Y-%m-%d %H:%M:%S"):
        self.__format = format

    def set_unit(self, unit="days"):
        self.__unit = unit

    def to_time(self) -> time.struct_time:
        return time.localtime(self.__time)

    def to_string(self, format=None) -> str:
        if not format:
            format = self.__format
        return time.strftime(format, self.to_time())

    def to_time_stamp(self) -> float:
        return self.__time

    def to_datetime(self, format=None) -> datetime.datetime:
        if not format:
            format = self.__format
        return datetime.datetime.strptime(self.to_string(), format)

