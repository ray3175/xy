import os


class FileModel:
    def __init__(self, file_path):
        self.__id = None
        self.__path = file_path
        self.__dir, self.__name = os.path.split(self.__path)
        self.__init_file()

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, _id):
        self.__id = _id if isinstance(_id, int) else None

    @id.deleter
    def id(self):
        self.__id = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @name.deleter
    def name(self):
        self.__name = None

    def set_dir(self, dir):
        self.__dir = dir

    def get_dir(self):
        return self.__dir

    def set_path(self, path):
        self.__path = path

    def get_path(self):
        return self.__path

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @data.deleter
    def data(self):
        self.__data = None

    def __init_file(self):
        if os.path.exists(self.__path):
            with open(self.__path, "r+", encoding="utf-8") as file:
                self.data = file.read()
                file.close()
        else:
            with open(self.__path, "w+", encoding="utf-8") as file:
                self.data = None
                file.close()

    def rename(self, new_name):
        _return = None
        new_path = os.path.join(self.__dir, new_name)
        if not os.path.exists(new_path):
            os.rename(self.__path, new_path)
            self.__path = new_path
            _return = True
        return _return

    def remove(self):
        _return = None
        if os.path.exists(self.__path):
            os.remove(self.__path)
            self.__path = None
            _return = True
        return _return
