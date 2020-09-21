import pytest
import os
import re
import tempfile
from xy.common.logger import Logger


class Test_Logger:
    def setup_class(self):
        pass

    def teardown_class(self):
        pass

    def setup(self):
        self.__logger_dir = tempfile.mkdtemp()

    def teardown(self):
        pass

    def test_normal_logger(self):
        name = "测试日志"
        log_name = "测试日志文件.txt"
        logger = Logger(name=name, log_name=log_name, log_path=self.__logger_dir, use_console=False)
        logger.debug("这是一个DEBUG！")
        logger.info("这是一个提示！")
        logger.warning("这是一个警告！")
        logger.error("这是一个错误！")
        logger.critical("这是一个严重错误！")
        log_path = os.path.join(self.__logger_dir, log_name)
        assert os.path.exists(log_path) is True

    def test_timed_rotating_logger(self):
        name = "测试轮转日志"
        log_name = "测试轮转日志文件"
        logger = Logger(name=name, log_name=log_name, log_path=self.__logger_dir, use_console=False, use_timed_rotating=True, timed_rotating_params={"when": "d", "suffix": "%Y-%m-%d.log", "extMatch": re.compile(r"^\d{4}-\d{2}-\d{2}"), "backupCount": 30})
        logger.debug("这是一个DEBUG！")
        logger.info("这是一个提示！")
        logger.warning("这是一个警告！")
        logger.error("这是一个错误！")
        logger.critical("这是一个严重错误！")
        log_path = os.path.join(self.__logger_dir, log_name)
        assert os.path.exists(log_path) is True



if __name__ == "__main__":
    pytest.main(["-v", "-s", "test_logger.py"])


