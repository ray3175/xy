import os
import re
import json
from ...stdlib_overwrite.list import List
from ...stdlib_overwrite.dict import Dict


class Directory:
    def __init__(self, path: str, dir_regex=None, file_regex=None, exclude_dir_regex=None, exclude_file_regex=None):
        """
        :param path: 文件夹路径
        :param dir_regex: 文件夹正则表达式
        :param file_regex: 文件正则表达式
        :param exclude_dir_regex: 排除文件夹正则表达式
        :param exclude_file_regex: 排除文件正则表达式
        """
        self.__data = List()
        self.__path = path
        self.__name = os.path.split(path)[-1]
        self.__re_dir = re.compile(dir_regex) if dir_regex else None
        self.__re_file = re.compile(file_regex) if file_regex else None
        self.__ex_re_dir = re.compile(exclude_dir_regex) if exclude_dir_regex else None
        self.__ex_re_file = re.compile(exclude_file_regex) if exclude_file_regex else None
        self.__init_data()

    def __str__(self):
        return json.dumps(self.__data, indent=4)

    def __init_data(self):
        temp_data = dict([[i[0], i[1:]] for i in os.walk(self.__path)])
        self.__data = self.__recursive_with_return_list(None, self.__path, temp_data)

    def __recursive_with_return_list(self, name, path, temp_data):
        _return = List()
        if name:
            path = os.path.join(path, name)
        for _dir in temp_data[path][0]:
            if self.__is_valid_dir(_dir):
                _return.append(Dict({_dir: self.__recursive_with_return_list(_dir, path, temp_data)}))
        for file in temp_data[path][-1]:
            if self.__is_valid_file(file):
                _return.append(file)
        return _return

    def __is_valid_dir(self, _dir):
        _return = True
        if self.__ex_re_dir:
            _return = not self.__ex_re_dir.search(_dir)
        if _return and self.__re_dir:
            _return = self.__re_dir.search(_dir)
        return _return

    def __is_valid_file(self, file):
        _return = True
        if self.__ex_re_file:
            _return = not self.__ex_re_file.search(file)
        if _return and self.__re_file:
            _return = self.__re_file.search(file)
        return _return

    def get_name(self) -> str:
        return self.__name

    def get_path(self) -> str:
        return self.__path

    def get_data(self) -> List:
        return self.__data

