import json
from . import FileModel


class JsonModel(FileModel):
    def __init__(self, json_path, read_content=False, read_data=False, code_type="utf-8"):
        super().__init__(json_path, read_content, read_data, code_type)

    def read_data(self, code_type="utf-8") -> (list, dict):
        with open(self.path, "r", encoding=code_type) as _json:
            self.data = json.load(_json)
            _json.close()
        return self.data

    def write_data(self, code_type="utf-8") -> (list, dict):
        with open(self.path, "w", encoding=code_type) as _json:
            json.dump(self.data, _json)
            _json.close()
        return self.data

