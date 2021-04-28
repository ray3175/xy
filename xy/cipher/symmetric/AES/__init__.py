from typing import Callable, Union, Optional
import Crypto.Cipher.AES        # pip install pycryptodome
import Crypto.Random
from ...code import Code
from .pad import Pad, UnPad


class AES:
    def __init__(self, key: Union[bytes, str] = "abcdefgh12345678", iv: Union[bytes, str, None] = None, cipher_method: Union[str, int] = "MODE_ECB", pad_method: str = "default", code_method: Optional[str] = None):
        """
        :param key: 密钥，长度16，24，32位。分别对应 AES-128，AES-192，AES-256。
            MODE_CBC，MODE_CFB，MODE_OFB，只能为16位。
            MODE_SIV模式为32，48，64
        :param iv: 向量，长度与密钥一致。
            MODE_CBC，MODE_CFB，MODE_OFB，MODE_OPENPGP模式才需要。
        :param cipher_method: 加密方式，["MODE_ECB"|"MODE_CBC"|"MODE_CFB"|"MODE_OFB"|"MODE_CTR"|"MODE_OPENPGP"|"MODE_CCM"|"MODE_EAX"|"MODE_SIV"|"MODE_GCM"|"MODE_OCB"]。
        :param pad_method: 填充方式，["default"|"PKCS5Padding"]。
        :param code_method: 编码方式，["base64"|"hex"]。
        """
        self.__key = self.__str2bytes(key)
        self.__iv = self.__str2bytes(iv)
        if isinstance(cipher_method, str):
            cipher_method = getattr(Crypto.Cipher.AES, cipher_method)
        self.__cipher_method = cipher_method
        self.__pad_func = Pad()[pad_method]
        self.__unpad_func = UnPad()[pad_method]
        self.__code_func = Code(code_method) if code_method else code_method

    def new_random_iv(self):
        return Crypto.Random.new().read(Crypto.Cipher.AES.block_size)

    def __str2bytes(self, value):
        if isinstance(value, str):
            value = value.encode("utf-8")
        return value

    def __new_cipher(self):
        return Crypto.Cipher.AES.new(self.__key, self.__cipher_method, iv=self.__iv) if self.__cipher_method in [2, 3, 5, 7] else Crypto.Cipher.AES.new(self.__key, self.__cipher_method)

    def __text_verify(self, text):
        key_length = len(self.__key)
        while len(text) > key_length:
            text_slice = text[:key_length]
            text = text[key_length:]
            yield text_slice
        else:
            if len(text) == key_length:
                yield text
            else:
                yield self.__pad_func(text, key_length)

    def encrypt(self, text: bytes, *args, encode_func: Optional[Callable] = None) -> bytes:
        cipher = self.__new_cipher()
        cipher_text = cipher.encrypt(b"".join(self.__text_verify(text)))
        if encode_func or (encode_func := self.__code_func.encode if self.__code_func else self.__code_func):
            cipher_text = encode_func(cipher_text)
        return cipher_text

    def decrypt(self, cipher_text: bytes, unpad: Optional[bool] = True, *args, decode_func: Optional[Callable] = None) -> bytes:
        cipher = self.__new_cipher()
        if decode_func or (decode_func := self.__code_func.decode if self.__code_func else self.__code_func):
            cipher_text = decode_func(cipher_text)
        text = cipher.decrypt(cipher_text)
        return self.__unpad_func(text) if unpad else text


