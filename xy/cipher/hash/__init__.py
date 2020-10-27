import hashlib
import binascii


class Hash:
    def __init__(self, hash_type="sha512", salt: (bytes, str) = None, iterations: int = 1):
        """
        :param hash_type: Hash类型。["md5", "sha1", "sha256", "sha512", ...]
        :param salt: 盐值。
        :param iterations: 迭代次数。
        """
        self.__type = hash_type
        self.__salt = salt.encode("utf-8") if isinstance(salt, str) else salt
        self.__iterations = iterations

    @staticmethod
    def get_hex_call(decode=False, code_type="utf-8"):
        def hex_call(_bytes):
            hex_bytes = binascii.hexlify(_bytes)
            if decode:
                hex_bytes = hex_bytes.decode(code_type)
            return hex_bytes
        return hex_call

    def encrypt(self, _bytes: bytes, call=None) -> bytes:
        hash_bytes = hashlib.pbkdf2_hmac(self.__type, _bytes, self.__salt, self.__iterations) if self.__salt else getattr(hashlib, self.__type)(_bytes).digest()
        if callable(call):
            hash_bytes = call(hash_bytes)
        return hash_bytes

    def encrypt_str(self, text: str, code_type="utf-8", call=None) -> bytes:
        return self.encrypt(text.encode(code_type), call)

    def encrypt_2_hex(self, _bytes: bytes) -> bytes:
        return binascii.hexlify(self.encrypt(_bytes))

    def encrypt_str_2_hex(self, text: str, code_type="utf-8") -> bytes:
        return self.encrypt_2_hex(text.encode(code_type))

    def encrypt_2_hex_str(self, _bytes: bytes, code_type="utf-8") -> str:
        return self.encrypt_2_hex(_bytes).decode(code_type)

    def encrypt_str_2_hex_str(self, text: str, code_type="utf-8") -> str:
        return self.encrypt_2_hex_str(text.encode(code_type), code_type)

