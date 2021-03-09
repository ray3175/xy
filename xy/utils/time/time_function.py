from typing import Union
import time
import datetime


class TimeFunction:
    def __init__(self, *args, **kwargs):
        pass

    def timestamp2struct_time(self, timestamp: Union[int, float]) -> time.struct_time:
        return time.localtime(timestamp)

    def timestamp2datetime(self, timestamp: Union[int, float], tz=None) -> datetime.datetime:
        return datetime.datetime.fromtimestamp(timestamp, tz)

    def timestamp2string(self, timestamp: Union[int, float], format="%Y-%m-%d %H:%M:%S") -> str:
        return self.struct_time2string(self.timestamp2struct_time(timestamp), format)

    def struct_time2time_stamp(self, struct_time: time.struct_time) -> float:
        return time.mktime(struct_time)

    def struct_time2datetime(self, struct_time: time.struct_time) -> datetime.datetime:
        return datetime.datetime(year=struct_time.tm_year, month=struct_time.tm_mon, day=struct_time.tm_mday, hour=struct_time.tm_hour, minute=struct_time.tm_min, second=struct_time.tm_sec)

    def struct_time2string(self, struct_time: time.struct_time, format="%Y-%m-%d %H:%M:%S") -> str:
        return time.strftime(format, struct_time)

    def datetime2timestamp(self, datetime: datetime.datetime) -> float:
        return datetime.timestamp()

    def datetime2struct_time(self, datetime: datetime.datetime) -> time.struct_time:
        return datetime.timetuple()

    def datetime2date(self, datetime: datetime.datetime) -> datetime.date:
        return datetime.date()

    def datetime2string(self, datetime: datetime.datetime, format="%Y-%m-%d %H:%M:%S") -> str:
        return datetime.strftime(format)

    def date2timestamp(self, date: datetime.date) -> float:
        return self.struct_time2time_stamp(date.timetuple())

    def date2struct_time(self, date: datetime.date) -> time.struct_time:
        return date.timetuple()

    def date2datetime(self, date: datetime.date) -> datetime.datetime:
        return datetime.datetime(year=date.year, month=date.month, day=date.day)

    def date2string(self, date: datetime.date, format="%Y-%m-%d %H:%M:%S") -> str:
        return date.strftime(format)

    def string2time_stamp(self, string: str, format="%Y-%m-%d %H:%M:%S") -> float:
        return self.struct_time2time_stamp(self.string2struct_time(string, format))

    def string2struct_time(self, string: str, format="%Y-%m-%d %H:%M:%S") -> time.struct_time:
        return time.strptime(string, format)

    def string2datetime(self, string: str, format="%Y-%m-%d %H:%M:%S") -> datetime.datetime:
        return datetime.datetime.strptime(string, format)

