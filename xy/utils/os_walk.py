import os
import re


class OSWalk:
    __name = ""
    __path = ""
    __data = dict()

    def __init__(self, path, dir_regex=None, file_regex=None):
        self.__path = path
        self.__name = os.path.split(path)[-1]
        self.__re_dir = re.compile(dir_regex) if dir_regex else None
        self.__re_file = re.compile(file_regex) if file_regex else None
        self.__init_data()

    def __init_data(self):
        temp_data = dict([[i[0], i[1:]] for i in os.walk(self.__path)])
        self.__data.update({self.__name: self.__recursive_with_return_list(None, self.__path, temp_data)})

    def __recursive_with_return_list(self, name, path, temp_data):
        __return = list()
        if name:
            path = self.__join_path(path, name)
        for _dir in temp_data[path][0]:
            if self.__is_dir_regex(_dir):
                __return.append({_dir: self.__recursive_with_return_list(_dir, path, temp_data)})
        for file in temp_data[path][-1]:
            if self.__is_file_regex(file):
                __return.append(file)
        return __return

    def __is_dir_regex(self, _dir):
        __return = True
        if self.__re_dir:
            __return = self.__re_dir.search(_dir)
        return __return

    def __is_file_regex(self, file):
        __return = True
        if self.__re_file:
            __return = self.__re_file.search(file)
        return __return

    def __join_path(self, path, name):
        return os.path.join(path, name)

    def get_name(self):
        return self.__name

    def get_path(self):
        return self.__path

    def get_data(self):
        return self.__data
