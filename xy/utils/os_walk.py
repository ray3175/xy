import os
import re


class OSWalk:
    def __init__(self, path: str, dir_regex=None, file_regex=None):
        self.__data = dict()
        self.__path = path
        self.__name = os.path.split(path)[-1]
        self.__re_dir = re.compile(dir_regex) if dir_regex else None
        self.__re_file = re.compile(file_regex) if file_regex else None
        self.__init_data()

    def __init_data(self):
        temp_data = dict([[i[0], i[1:]] for i in os.walk(self.__path)])
        self.__data.update({self.__name: self.__recursive_with_return_list(None, self.__path, temp_data)})

    def __recursive_with_return_list(self, name, path, temp_data):
        _return = list()
        if name:
            path = os.path.join(path, name)
        for _dir in temp_data[path][0]:
            if self.__is_dir_regex(_dir):
                _return.append({_dir: self.__recursive_with_return_list(_dir, path, temp_data)})
        for file in temp_data[path][-1]:
            if self.__is_file_regex(file):
                _return.append(file)
        return _return

    def __is_dir_regex(self, _dir):
        _return = True
        if self.__re_dir:
            _return = self.__re_dir.search(_dir)
        return _return

    def __is_file_regex(self, file):
        _return = True
        if self.__re_file:
            _return = self.__re_file.search(file)
        return _return

    def get_name(self) -> str:
        return self.__name

    def get_path(self) -> str:
        return self.__path

    def get_data(self) -> dict:
        return self.__data
