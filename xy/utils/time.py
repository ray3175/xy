import time
import datetime


class Time:
    @classmethod
    def time_stamp2time(cls, time_stamp):
        return time.localtime(time_stamp)

    @classmethod
    def time2time_stamp(cls, _time):
        return time.mktime(_time)

    @classmethod
    def time2string(cls, _time, format="%Y-%m-%d"):
        return time.strftime(format, _time)

    @classmethod
    def string2time(cls, string, format="%Y-%m-%d"):
        return time.strptime(string, format)

    @classmethod
    def datetime2string(cls, _datetime, format="%Y-%m-%d"):
        return _datetime.strftime(format)

    @classmethod
    def string2datetime(cls, string, format="%Y-%m-%d"):
        return datetime.datetime.strptime(string, format)


