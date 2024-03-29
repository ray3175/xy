import time
import datetime
from .time_function import TimeFunction


class TimeStamp(TimeFunction):
    def __init__(self, timer=None, format="%Y-%m-%d %H:%M:%S", *args, init_time_stamp=True, **kwargs):
        super(TimeStamp, self).__init__(timer, format, *args, **kwargs)
        self.__time_stamp = None
        if init_time_stamp:
            self.init_time_stamp(timer, format)

    def init_time_stamp(self, timer, format="%Y-%m-%d %H:%M:%S"):
        if isinstance(timer, (int, float)):
            self.__time_stamp = timer
        elif isinstance(timer, time.struct_time):
            self.__time_stamp = self.struct_time2time_stamp(timer)
        elif isinstance(timer, datetime.datetime):
            self.__time_stamp = self.datetime2timestamp(timer)
        elif isinstance(timer, datetime.date):
            self.__time_stamp = self.date2timestamp(timer)
        elif isinstance(timer, str):
            self.__time_stamp = self.string2time_stamp(timer, format)
        else:
            self.__time_stamp = time.time()

    @property
    def time_stamp(self):
        return self.__time_stamp

    def to_time_stamp(self) -> float:
        return self.__time_stamp

