import time
import datetime


class Time:
    @classmethod
    def get_local_time_with_string(cls, format="%Y-%m-%d") -> str:
        return cls.time2string(time.localtime(), format)

    @classmethod
    def time_stamp2time(cls, time_stamp: float) -> time.struct_time:
        return time.localtime(time_stamp)

    @classmethod
    def time2time_stamp(cls, _time: time.struct_time) -> float:
        return time.mktime(_time)

    @classmethod
    def time2string(cls, _time: time.struct_time, format="%Y-%m-%d") -> str:
        return time.strftime(format, _time)

    @classmethod
    def string2time(cls, string, format="%Y-%m-%d") -> time.struct_time:
        return time.strptime(string, format)

    @classmethod
    def datetime2string(cls, _datetime: datetime.datetime, format="%Y-%m-%d") -> str:
        return _datetime.strftime(format)

    @classmethod
    def string2datetime(cls, string, format="%Y-%m-%d") -> datetime.datetime:
        return datetime.datetime.strptime(string, format)

