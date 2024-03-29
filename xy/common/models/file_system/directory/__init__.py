from typing import Union
import os
import shutil
from re import compile, Pattern
from .. import FileSystem
from ..file import FileModel


class DirectoryModel(FileSystem):
    def __init__(self, directory_path: str, scan_directory: bool = False, scan_iterate: bool = False, directory_regex: Union[Pattern, str, None] = None, exclude_directory_regex: Union[Pattern, str, None] = None, file_regex: Union[Pattern, str, None] = None, exclude_file_regex: Union[Pattern, str, None] = None, file_model=FileModel, *, makedirs: bool = False):
        """
        :param directory_path: 文件夹路径
        :param scan_directory: 是否扫描文件夹下的所有文件
        :param scan_iterate: 开启扫描时，是否递归扫描
        :param directory_regex: 开启扫描时，文件夹正则表达式
        :param exclude_directory_regex: 开启扫描时，排除文件夹正则表达式
        :param file_regex: 开启扫描时，文件正则表达式
        :param exclude_file_regex: 开启扫描时，排除文件正则表达式
        """
        super().__init__(directory_path)
        if makedirs:
            self._make_directory()
        if scan_directory:
            self.scan_directory(scan_iterate, directory_regex, exclude_directory_regex, file_regex, exclude_file_regex, file_model)

    def __bool__(self):
        return os.path.isdir(self.path)

    def _make_directory(self):
        if not self:
            os.makedirs(self.path)

    def _is_valid_directory(self, name, directory_regex, exclude_directory_regex):
        _return =True
        if exclude_directory_regex:
            if isinstance(exclude_directory_regex, str):
                exclude_directory_regex = compile(exclude_directory_regex)
            _return = not exclude_directory_regex.search(name)
        if _return and directory_regex:
            if isinstance(directory_regex, str):
                directory_regex = compile(directory_regex)
            _return = directory_regex.search(name)
        return _return

    def _is_valid_file(self, name, file_regex, exclude_file_regex):
        _return = True
        if exclude_file_regex:
            if isinstance(exclude_file_regex, str):
                exclude_file_regex = compile(exclude_file_regex)
            _return = not exclude_file_regex.search(name)
        if _return and file_regex:
            if isinstance(file_regex, str):
                file_regex = compile(file_regex)
            _return = file_regex.search(name)
        return _return

    def scan_directory(self, scan_iterate: bool = False, directory_regex: Union[Pattern, str, None] = None, exclude_directory_regex: Union[Pattern, str, None] = None, file_regex: Union[Pattern, str, None] = None, exclude_file_regex: Union[Pattern, str, None] = None, file_model=FileModel):
        self.documents = list()
        names = os.listdir(self.path)
        self.number_document = len(names)
        self.number_directory = 0
        self.number_file = 0
        for name in names:
            path = os.path.join(self.path, name)
            if os.path.isdir(path):
                if self._is_valid_directory(name, directory_regex, exclude_directory_regex):
                    self.number_directory += 1
                    self.documents.append(self.__class__(path, scan_iterate, scan_iterate, directory_regex, exclude_directory_regex, file_regex, exclude_file_regex, file_model))
            elif os.path.isfile(path):
                if self._is_valid_file(name, file_regex, exclude_file_regex):
                    self.number_file += 1
                    self.documents.append(file_model(path))

    def rename(self, new_name: str) -> bool:
        if _return := super().rename(new_name):
            self._make_directory()
        return _return

    def remove(self):
        shutil.rmtree(self.path)

