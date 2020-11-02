import time
import datetime as dt
from .time_function import TimeFunction


class TimeDateTime(TimeFunction):
    def __init__(self, timer=None, format="%Y-%m-%d %H:%M:%S"):
        super(TimeDateTime, self).__init__(timer, format)
        self.init_datetime(timer, format)

    def init_datetime(self, timer, format="%Y-%m-%d %H:%M:%S"):
        if isinstance(timer, (int, float)):
            self.__datetime = self.timestamp2datetime(timer)
        elif isinstance(timer, time.struct_time):
            self.__datetime = self.struct_time2datetime(timer)
        elif isinstance(timer, dt.datetime):
            self.__datetime = timer
        elif isinstance(timer, dt.date):
            self.__datetime = self.date2datetime(timer)
        elif isinstance(timer, str):
            self.__datetime = self.string2datetime(timer, format)
        else:
            self.__datetime = self.timestamp2datetime(time.time())

    @property
    def datetime(self):
        return self.__datetime

    def to_datetime(self) -> dt.datetime:
        return self.__datetime

