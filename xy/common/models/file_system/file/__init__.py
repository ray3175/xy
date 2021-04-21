import os
import aiofiles     # pip install aiofiles
from .. import FileSystem


class FileModel(FileSystem):
    def __init__(self, file_path: str, read_content: bool = False, read_data: bool = False, code_type: str = "utf-8"):
        """
        :param file_path: 文件路径
        :param read_content: 是否以bytes读取文件
        :param read_data: 是否以str读取文件
        :param code_type: 以str读取文件时，指定文件的编码格式
        """
        super().__init__(file_path)
        self.content = None
        self.data = None
        if read_content:
            self.read()
        if read_data:
            self.read_data(code_type)

    def read(self) -> bytes:
        with open(self.path, "rb") as file:
            self.content = file.read()
        return self.content

    def read_data(self, code_type: str = "utf-8") -> str:
        with open(self.path, "r", encoding=code_type) as file:
            self.data = file.read()
        return self.data

    def write(self) -> bytes:
        with open(self.path, "wb") as file:
            file.write(self.content)
        return self.content

    def write_data(self, code_type: str = "utf-8") -> str:
        with open(self.path, "w", encoding=code_type) as file:
            file.write(self.data)
        return self.data

    def remove(self) -> bool:
        if os.path.exists(self.path):
            os.remove(self.path)
            return True
        return False

    async def async_read(self) -> bytes:
        async with aiofiles.open(self.path, "rb") as file:
            self.content = await file.read()
        return self.content

    async def async_read_data(self, code_type: str = "utf-8") -> str:
        async with aiofiles.open(self.path, "r", encoding=code_type) as file:
            self.data = await file.read()
        return self.data

    async def async_write(self) -> bytes:
        async with aiofiles.open(self.path, "wb") as file:
            await file.write(self.content)
        return self.content

    async def async_write_data(self, code_type: str = "utf-8") -> str:
        async with aiofiles.open(self.path, "w", encoding=code_type) as file:
            await file.write(self.data)
        return self.data

