import time
import datetime
from .time_function import TimeFunction


class TimeString(TimeFunction):
    def __init__(self, timer=None, format="%Y-%m-%d %H:%M:%S", *args, init_time_string=True, **kwargs):
        super(TimeString, self).__init__(timer, format, *args, **kwargs)
        self.__time_string = None
        if init_time_string:
            self.init_time_string(timer, format)

    def init_time_string(self, timer, format="%Y-%m-%d %H:%M:%S"):
        if isinstance(timer, (int, float)):
            self.__time_string = self.timestamp2string(timer, format)
        elif isinstance(timer, time.struct_time):
            self.__time_string = self.struct_time2string(timer, format)
        elif isinstance(timer, datetime.datetime):
            self.__time_string = self.datetime2string(timer, format)
        elif isinstance(timer, datetime.date):
            self.__time_string = self.date2string(timer, format)
        elif isinstance(timer, str):
            self.__time_string = timer
        else:
            self.__time_string = self.timestamp2string(time.time(), format)

    @property
    def time_string(self):
        return self.__time_string

    def to_string(self) -> str:
        return self.__time_string

