from abc import ABC, abstractmethod


class _Pad(ABC):
    __getitem__ = lambda self, item: getattr(self, item) if item and hasattr(self, item) else None

    @abstractmethod
    def default(self):
        pass

    @abstractmethod
    def PKCS5Padding(self):
        pass


class Pad(_Pad):
    def default(self, _bytes: bytes, key_length: int) -> bytes:
        return _bytes + (key_length - len(_bytes) % key_length) * " ".encode("utf-8")

    def PKCS5Padding(self, _bytes: bytes, key_length: int) -> bytes:
        return _bytes + (key_length - len(_bytes) % key_length) * chr(key_length - len(_bytes) % key_length).encode("utf-8")


class UnPad(_Pad):
    def default(self, _bytes: bytes) -> bytes:
        return _bytes.rstrip()

    def PKCS5Padding(self, _bytes: bytes) -> bytes:
        return _bytes[:-ord(_bytes.decode("utf-8")[-1])]

