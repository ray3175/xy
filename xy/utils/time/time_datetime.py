from typing import Union
import time
import datetime as dt
from .time_function import TimeFunction


class TimeDateTime(TimeFunction):
    def __init__(self, timer=None, format="%Y-%m-%d %H:%M:%S", *args, init_date_time=True, **kwargs):
        super(TimeDateTime, self).__init__(timer, format, *args, **kwargs)
        self.__datetime = None
        if init_date_time:
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

    def __add__(self, other: Union[dict, dt.timedelta]):
        """
        :param other:
            dict类型： 当前类self.datetime + datetime.timedelta(**dict)
                key只能为： ["days", "seconds", "microseconds", "milliseconds", "minutes", "hours", "weeks"]
            datetime.timedelta类型： 当前类self.datetime + other
        :return: 返回新的 TimeDateTime 实例。
        """
        if isinstance(other, dict):
            other = self.get_timedelta(**other)
        return self.__class__(self.__datetime + other)

    def __sub__(self, other: Union[dict, dt.timedelta]):
        """
        :param other:
            dict类型： 当前类self.datetime + datetime.timedelta(**dict)
                key只能为： ["days", "seconds", "microseconds", "milliseconds", "minutes", "hours", "weeks"]
            datetime.timedelta类型： 当前类self.datetime + other
        :return: 返回新的 TimeDateTime 实例。
        """
        if isinstance(other, dict):
            other = self.get_timedelta(**other)
        return self.__class__(self.__datetime - other)

    @property
    def datetime(self):
        return self.__datetime

    def to_datetime(self) -> dt.datetime:
        return self.__datetime

    def get_timedelta(self, days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0):
        """
        :param days: 天（24 hours）
        :param seconds: 秒（1000 milliseconds）
        :param microseconds: 微妙
        :param milliseconds: 毫秒（1000 microseconds）
        :param minutes: 分钟（60 seconds）
        :param hours: 小时（60 minutes）
        :param weeks: 周（7 days）
        """
        return dt.timedelta(days=days, seconds=seconds, microseconds=microseconds, milliseconds=milliseconds, minutes=minutes, hours=hours, weeks=weeks)


