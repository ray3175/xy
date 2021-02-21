import os
import shutil
import re
from .. import FileSystem
from ..file import FileModel


class DirectoryModel(FileSystem):
    def __init__(self, directory_path, scan_directory=False, scan_iterate=False, directory_regex=None, exclude_directory_regex=None, file_regex=None, exclude_file_regex=None, file_model=FileModel):
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
        self._make_directory()
        if scan_directory:
            self.scan_directory(scan_iterate, directory_regex, exclude_directory_regex, file_regex, exclude_file_regex, file_model)

    def _make_directory(self):
        if not os.path.exists(self.path):
            os.makedirs(self.path)

    def _is_valid_directory(self, name, directory_regex, exclude_directory_regex):
        _return =True
        if exclude_directory_regex:
            _return = not re.compile(exclude_directory_regex).search(name)
        if _return and directory_regex:
            _return = re.compile(directory_regex).search(name)
        return _return

    def _is_valid_file(self, name, file_regex, exclude_file_regex):
        _return = True
        if exclude_file_regex:
            _return = not re.compile(exclude_file_regex).search(name)
        if _return and file_regex:
            _return = re.compile(file_regex).search(name)
        return _return

    def scan_directory(self, scan_iterate=False, directory_regex=None, exclude_directory_regex=None, file_regex=None, exclude_file_regex=None, file_model=FileModel):
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

    def rename(self, new_name) -> bool:
        if _return:=super().rename(new_name):
            self._make_directory()
        return _return

    def remove(self):
        shutil.rmtree(self.path)

