import os


class FileSystem:
    def __init__(self, path: str):
        self._init_path(path)

    def _init_path(self, path: str):
        self.__path = path
        self.__directory, self.__name = os.path.split(path)

    def __bool__(self):
        return os.path.exists(self.__path)

    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path

    @property
    def directory(self):
        return self.__directory

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @name.deleter
    def name(self):
        self.__name = None

    def rename(self, new_name: str) -> bool:
        new_path = os.path.join(self.directory, new_name)
        if not os.path.exists(new_path):
            os.rename(self.path, new_path)
            self._init_path(new_path)
            return True
        return False

