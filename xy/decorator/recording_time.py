from typing import Callable
from functools import wraps
import time


class RecordingTime:
    def __init__(self, name=""):
        self.__name = name

    def record(self, record_call: Callable = print, start_call: Callable = lambda *args, **kwargs: "开始计时！", end_call: Callable = lambda interval, *args, **kwargs: "结束计时，耗时：{}秒！".format(interval)):
        def interval(func):
            @wraps(func)
            def recording(*args, **kwargs):
                record_call("{}{}".format(self.__name, start_call(*args, **kwargs)))
                start = time.time()
                _return = func(*args, **kwargs)
                end = time.time()
                record_call("{}{}".format(self.__name, end_call(end - start, *args, **kwargs)))
                return _return
            return recording
        return interval

