from typing import Union
import json
from . import FileModel


class JsonModel(FileModel):
    def __init__(self, json_path: str, read_content: bool = False, read_data: bool = False, code_type: str = "utf-8"):
        super().__init__(json_path, read_content, read_data, code_type)

    def read_data(self, code_type: str = "utf-8") -> Union[list, dict]:
        with open(self.path, "r", encoding=code_type) as _json:
            self.data = json.load(_json)
            _json.close()
        return self.data

    def write_data(self, code_type: str = "utf-8") -> Union[list, dict]:
        with open(self.path, "w", encoding=code_type) as _json:
            json.dump(self.data, _json)
            _json.close()
        return self.data

