import chardet      # pip install chardet


class CodeCheck:
    """
    编码检查。
    """

    @classmethod
    def extract_encoding_from_bytes_str(cls, byte_str: bytes) -> str:
        return chardet.detect(byte_str)["encoding"]

    @classmethod
    def extract_encoding_from_file(cls, file_path: str) -> str:
        with open(file_path, "rb") as x:
            byte_str = x.read()
            x.close()
        return cls.extract_encoding_from_bytes_str(byte_str)

