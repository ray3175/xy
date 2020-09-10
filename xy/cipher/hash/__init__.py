import hashlib
import binascii


class Hash:
    def __init__(self, hash_type="sha512", salt=None, iterations=1):
        """
        :param hash_type: Hash类型。["md5", "sha1", "sha256", "sha512", ...]
        :param salt: 盐值。
        :param iterations: 迭代次数。
        """
        self.__type = hash_type
        self.__salt = salt
        self.__iterations = iterations

    def encrypt(self, text: str) -> str:
        return self.encrypt_bytes(text.encode("utf-8"))

    def encrypt_bytes(self, _bytes: bytes) -> str:
        return binascii.hexlify(hashlib.pbkdf2_hmac(self.__type, _bytes, self.__salt.encode("utf-8"), self.__iterations)).decode("utf-8") if self.__salt else getattr(hashlib, self.__type)(_bytes).hexdigest()
