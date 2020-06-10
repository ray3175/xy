import time
import datetime


class Time:
    def __init__(self, timer=time.time(), format="%Y-%m-%d %H:%M:%S", unit="days"):
        """
        :param unit: days | seconds | microseconds | milliseconds | minutes | hours | weeks | fold
        """
        self.__format = format
        self.__unit = unit
        if isinstance(timer, (int, float)):
            self.__time = time.localtime(timer)
        elif isinstance(timer, str):
            self.__time = time.strptime(timer, format)
        elif isinstance(timer, datetime.datetime):
            self.__time = timer.utctimetuple()
        elif isinstance(timer, datetime.date):
            self.__time = timer.timetuple()
        else:
            self.__time = timer

    def __str__(self):
        return self.to_string()

    def __add__(self, other: float):
        return self.__class__(datetime.datetime.fromtimestamp(self.to_time_stamp()) + datetime.timedelta(**{self.__unit: other}), self.__format, self.__unit)

    def __sub__(self, other: float):
        return self.__class__(datetime.datetime.fromtimestamp(self.to_time_stamp()) - datetime.timedelta(**{self.__unit: other}), self.__format, self.__unit)

    def set_format(self, format="%Y-%m-%d %H:%M:%S"):
        self.__format = format

    def set_unit(self, unit="days"):
        self.__unit = unit

    def to_string(self, format=None) -> str:
        if not format:
            format = self.__format
        return time.strftime(format, self.__time)

    def to_time_stamp(self) -> float:
        return time.mktime(self.__time)

    def to_datetime(self, format=None) -> datetime.datetime:
        if not format:
            format = self.__format
        return datetime.datetime.strptime(self.to_string(), format)

