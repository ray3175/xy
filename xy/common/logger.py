import os
import sys
import time
import logging


class Logger:
    __level_dict = {
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
                 use_console=True):
        """
        :param set_level: 日志级别["NOTSET"|"DEBUG"|"INFO"|"WARNING"|"ERROR"|"CRITICAL"]，默认为INFO
        :param name: 日志中打印的name，默认为运行程序的name
        :param log_name: 日志文件的名字，默认为当前时间（年-月-日.log）
        :param log_path: 日志文件夹的路径，默认为logger.py同级目录中的log文件夹
        :param use_console: 是否在控制台打印，默认为True
        """
        if set_level is None:
            set_level = self._exec_type()       # 设置set_level为None，自动获取当前运行模式
        self.__logger = logging.getLogger(name)
        self.__logger.setLevel(self.__level_dict[set_level] if set_level in self.__level_dict else set_level)
        if not os.path.exists(log_path):        # 创建日志目录
            os.makedirs(log_path)
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        handlers = list()
        handlers.append(logging.FileHandler(os.path.join(log_path, log_name), encoding="utf-8"))
        if use_console:
            handlers.append(logging.StreamHandler())
        for handler in handlers:
            handler.setFormatter(formatter)
            self.__logger.addHandler(handler)

    def _exec_type(self):
        return "DEBUG" if os.environ.get("IPYTHONENABLE") else "INFO"

    def log(self, level, msg, *args, **kwargs):
        self.__logger.log(level, msg, *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        self.__logger.critical(msg, *args, **kwargs)

    def exception(self, msg, *args, exc_info=True, **kwargs):
        self.__logger.exception(msg, *args, exc_info=exc_info, **kwargs)

    def error(self, msg, *args, **kwargs):
        self.__logger.error(msg, *args, **kwargs)

    def warn(self, msg, *args, **kwargs):
        self.warning(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        self.__logger.warning(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        self.__logger.info(msg, *args, **kwargs)

    def debug(self, msg, *args, **kwargs):
        self.__logger.debug(msg, *args, **kwargs)
