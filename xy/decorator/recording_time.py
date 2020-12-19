from typing import Callable
from functools import wraps
import time


class RecordingTime:
    def __init__(self, name=""):
        self.__name = name

    def print(self, start_call: Callable = lambda: "开始计时！", end_call: Callable = lambda: "结束计时，", info_call: Callable = lambda interval: "耗时：{}秒！".format(interval)):
        def interval(func):
            @wraps(func)
            def recording(*args, **kwargs):
                print("{}{}".format(self.__name, start_call()))
                start = time.time()
                _return = func(*args, **kwargs)
                end = time.time()
                print("{}{}{}".format(self.__name, end_call(), info_call(end - start)))
                return _return
            return recording
        return interval

