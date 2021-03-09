from typing import Union
import hashlib


class Hash:
    def __init__(self, hash_type="sha512", salt: Union[bytes, str] = None, iterations: int = 1):
        """
        :param hash_type: Hash类型。["md5", "sha1", "sha256", "sha512", ...]
        :param salt: 盐值。
        :param iterations: 迭代次数。
        """
        self.__type = hash_type
        self.__salt = salt.encode("utf-8") if isinstance(salt, str) else salt
        self.__iterations = iterations

    def encrypt(self, _bytes: bytes) -> bytes:
        return hashlib.pbkdf2_hmac(self.__type, _bytes, self.__salt, self.__iterations) if self.__salt else getattr(hashlib, self.__type)(_bytes).digest()


