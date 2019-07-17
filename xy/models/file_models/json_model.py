import json
from . import FileModel


class JsonModel(FileModel):
    def __init__(self, json_path):
        super().__init__(json_path)
        self.__init_data()

    @property
    def path(self):
        return self.get_path()

    @path.setter
    def path(self, path):
        self.set_path(path)

    @path.deleter
    def path(self):
        self.set_path(None)

    def __init_data(self):
        if self.path:
            with open(self.path, "r", encoding="utf-8") as _json:
                try:
                    self.data = json.load(_json)
                except json.decoder.JSONDecodeError:
                    self.data = {}
                _json.close()

    def save(self):
        __return = None
        if self.path:
            with open(self.get_path(), "w", encoding="utf-8") as _json:
                json.dump(self.data, _json)
                _json.close()
            __return = True
        return __return


