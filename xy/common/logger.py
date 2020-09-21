import os
import sys
import re
import time
import logging
from logging.handlers import TimedRotatingFileHandler


class Logger:
    LEVEL_DICT = {
        "NOTSET": logging.NOTSET,
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
        "CRITICAL": logging.CRITICAL
    }

    def __init__(self, set_level=None,
                 name=os.path.split(os.path.splitext(sys.argv[0])[0])[-1],
                 log_name=time.strftime("%Y-%m-%d.log", time.localtime()),
                 log_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), "log"),
                 encoding="utf-8", use_console=True,
                 use_timed_rotating=False, timed_rotating_params={}):
        """
        :param set_level: 日志级别["NOTSET"|"DEBUG"|"INFO"|"WARNING"|"ERROR"|"CRITICAL"]，默认为INFO
        :param name: 日志中打印的name，默认为运行程序的name
        :param log_name: 日志文件的名字，默认为当前时间（年-月-日.log）
        :param log_path: 日志文件夹的路径，默认为logger.py同级目录中的log文件夹
        :param use_console: 是否在控制台打印，默认为True
        :param use_timed_rotating: 是否基于时间输出日志，默认为False
        """
        if set_level is None:
            level_key = os.environ.get("xy")
            set_level = self.LEVEL_DICT.get(level_key, logging.INFO)
        self.__logger = logging.getLogger(name)
        self.__logger.setLevel(self.LEVEL_DICT[set_level] if set_level in self.LEVEL_DICT else set_level)
        if not os.path.exists(log_path):        # 创建日志目录
            os.makedirs(log_path)
        handlers = list()
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        path = os.path.join(log_path, log_name)
        if use_timed_rotating:
            handlers.append(self._timed_rotating_file_handler(path, encoding=encoding, **timed_rotating_params))
        else:
            handlers.append(logging.FileHandler(path, encoding=encoding))
        if use_console:
            handlers.append(logging.StreamHandler())
        for handler in handlers:
            handler.setFormatter(formatter)
            self.__logger.addHandler(handler)

    def __getattr__(self, item):
        return getattr(self.__logger, item)

    def _timed_rotating_file_handler(self, path, when="S", suffix="%Y-%m-%d(%H %M %S).log", extMatch=re.compile(r"^\d{4}-\d{2}-\d{2}\(\d{2}\s\d{2}\s\d{2}\)"), backupCount=30, encoding="utf-8"):
        file_handler = RayTimedRotatingFileHandler(path, when=when, interval=1, backupCount=backupCount, encoding=encoding)
        file_handler.suffix = suffix
        file_handler.extMatch = extMatch
        return file_handler


class RayTimedRotatingFileHandler(TimedRotatingFileHandler):
    def __init__(self, path, when="S", interval=1, backupCount=30, encoding="utf-8"):
        super().__init__(path, when, interval, backupCount, encoding)


