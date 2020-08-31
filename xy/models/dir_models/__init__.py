import os
import shutil
from ...stdlib_overwrite.dict import Dict
from ...common.directory import Directory


class DirModel:
    def __init__(self, dir_path, dir_regex=None, file_regex=None, exclude_dir_regex=None, exclude_file_regex=None):
        """
        :param dir_path: 文件夹路径
        :param dir_regex: 文件夹正则表达式
        :param file_regex: 文件正则表达式
        :param exclude_dir_regex: 排除文件夹正则表达式
        :param exclude_file_regex: 排除文件正则表达式
        """
        self.__path = dir_path
        self.__name = os.path.split(self.__path)[-1]
        self.__make_dir()
        directory = Directory(self.__path, dir_regex, file_regex, exclude_dir_regex, exclude_file_regex)
        self.__name, self.__data = directory.get_name(), self.__generate_data(self.__path, directory.get_data())

    def __generate_data(self, path, directory_data):
        model_data = Dict()
        for obj in directory_data:
            if isinstance(obj, dict):
                for key, value in obj.items():
                    model_data.update({key: self.__generate_data(os.path.join(path, key), value)})
            else:
                model_data.update({obj: os.path.join(path, obj)})
        return model_data

    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, path):
        self.__path = path

    @path.deleter
    def path(self):
        self.__path = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @name.deleter
    def name(self):
        self.__name = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @data.deleter
    def data(self):
        self.__data = None

    def __make_dir(self):
        if not os.path.exists(self.__path):
            os.makedirs(self.__path)

    def rename(self, new_name):
        _return = None
        new_path = os.path.join(self.__dir, new_name)
        if not os.path.exists(new_path):
            os.rename(self.__path, new_path)
            self.__path = new_path
            _return = True
        return _return

    def remove(self):
        shutil.rmtree(self.__path)