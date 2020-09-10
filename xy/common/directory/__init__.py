import os
import re
from ...stdlib_overwrite.list import List


class SystemSetting:
    def __init__(self, name, path):
        self.__name = name
        self.__path = path

    def __str__(self):
        return self.__name

    def __repr__(self):
        return self.__str__()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, path):
        self.__path = path


class Directory(SystemSetting):
    class _File(SystemSetting):
        def __init__(self, name, path):
            super().__init__(name, path)

    class _Directory(SystemSetting):
        def __init__(self, name, path, value):
            super().__init__(name, path)
            self.__value = value

        def __repr__(self):
            return {self.name: self.__value}.__str__()

        @property
        def value(self):
            return self.__value

        @value.setter
        def value(self, value):
            self.__value = value

    def __init__(self, path: str, dir_regex=None, file_regex=None, exclude_dir_regex=None, exclude_file_regex=None):
        """
        :param path: 文件夹路径
        :param dir_regex: 文件夹正则表达式
        :param file_regex: 文件正则表达式
        :param exclude_dir_regex: 排除文件夹正则表达式
        :param exclude_file_regex: 排除文件正则表达式
        """
        self.__data = List()
        super().__init__(os.path.split(path)[-1], path)
        self.__re_dir = re.compile(dir_regex) if dir_regex else None
        self.__re_file = re.compile(file_regex) if file_regex else None
        self.__ex_re_dir = re.compile(exclude_dir_regex) if exclude_dir_regex else None
        self.__ex_re_file = re.compile(exclude_file_regex) if exclude_file_regex else None
        self.__init_data()

    def __str__(self):
        return self.__data

    def __init_data(self):
        temp_data = dict([[i[0], i[1:]] for i in os.walk(self.path)])
        self.__data = self.__recursive_with_return_list(self.path, temp_data)

    def __recursive_with_return_list(self, path, temp_data):
        _return = List()
        for _dir in temp_data[path][0]:
            if self.__is_valid_dir(_dir):
                dir_path = os.path.join(path, _dir)
                _return.append(self._Directory(_dir, dir_path, self.__recursive_with_return_list(dir_path, temp_data)))
        for file in temp_data[path][-1]:
            if self.__is_valid_file(file):
                _return.append(self._File(file, os.path.join(path, file)))
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

    def get_data(self) -> List:
        return self.__data

