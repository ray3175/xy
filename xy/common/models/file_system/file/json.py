from typing import Union
import json
import aiofiles
from . import FileModel


class JsonModel(FileModel):
    def __init__(self, json_path: str, read_content: bool = False, read_data: bool = False, code_type: str = "utf-8"):
        super().__init__(json_path, read_content, read_data, code_type)

    def read_data(self, code_type: str = "utf-8") -> Union[list, dict]:
        with open(self.path, "r", encoding=code_type) as _json:
            self.data = json.load(_json)
        return self.data

    def write_data(self, code_type: str = "utf-8") -> Union[list, dict]:
        with open(self.path, "w", encoding=code_type) as _json:
            json.dump(self.data, _json)
        return self.data

    async def async_read_data(self, code_type: str = "utf-8") -> Union[list, dict]:
        async with aiofiles.open(self.path, "r", encoding=code_type) as _json:
            self.data = json.loads(await _json.read())
        return self.data

    async def async_write_data(self, code_type: str = "utf-8") -> Union[list, dict]:
        async with aiofiles.open(self.path, "w", encoding=code_type) as _json:
            await _json.write(json.dumps(self.data))
        return self.data

