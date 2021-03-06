import os
from .. import FileSystem


class FileModel(FileSystem):
    def __init__(self, file_path, read_content=False, read_data=False, code_type="utf-8"):
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
            file.close()
        return self.content

    def read_data(self, code_type="utf-8") -> str:
        with open(self.path, "r", encoding=code_type) as file:
            self.data = file.read()
            file.close()
        return self.data

    def write(self) -> bytes:
        with open(self.path, "wb") as file:
            file.write(self.content)
            file.close()
        return self.content

    def write_data(self, code_type="utf-8") -> str:
        with open(self.path, "w", encoding=code_type) as file:
            file.write(self.data)
            file.close()
        return self.data

    def remove(self) -> bool:
        if os.path.exists(self.path):
            os.remove(self.path)
            return True
        return False

