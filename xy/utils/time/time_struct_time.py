import time
import datetime
from .time_function import TimeFunction


class TimeStructTime(TimeFunction):
    def __init__(self, timer=None, format="%Y-%m-%d %H:%M:%S", *args, init_struct_time=True, **kwargs):
        super(TimeStructTime, self).__init__(timer, format, *args, **kwargs)
        self.__struct_time = None
        if init_struct_time:
            self.init_struct_time(timer, format)

    def init_struct_time(self, timer, format="%Y-%m-%d %H:%M:%S"):
        if isinstance(timer, (int, float)):
            self.__struct_time = self.timestamp2struct_time(timer)
        elif isinstance(timer, time.struct_time):
            self.__struct_time = timer
        elif isinstance(timer, datetime.datetime):
            self.__struct_time = self.datetime2struct_time(timer)
        elif isinstance(timer, datetime.date):
            self.__struct_time = self.date2struct_time(timer)
        elif isinstance(timer, str):
            self.__struct_time = self.string2struct_time(timer, format)
        else:
            self.__struct_time = self.timestamp2struct_time(time.time())

    @property
    def struct_time(self):
        return self.__struct_time

    def to_struct_time(self) -> time.struct_time:
        return self.__struct_time

