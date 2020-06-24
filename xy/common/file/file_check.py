import chardet      # pip install chardet


class FileCheck:
    @classmethod
    def extract_encoding_from_bytes_str(cls, byte_str):
        return chardet.detect(byte_str)["encoding"]

    @classmethod
    def extract_encoding_from_file(cls, file_path):
        with open(file_path, "rb") as x:
            byte_str = x.read()
            x.close()
        return cls.extract_encoding_from_bytes_str(byte_str)

