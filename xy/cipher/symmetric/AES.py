import base64
import binascii
import Crypto.Cipher.AES
import Crypto.Random


class AES:
    __lambda_pad = {
        "default": lambda x, y: x + (y - len(x) % y) * " ".encode("utf-8"),
        "PKCS5Padding": lambda x, y: x + (y - len(x) % y) * chr(y - len(x) % y).encode("utf-8")
    }
    __lambda_unpad = {
        "default": lambda x: x.rstrip(),
        "PKCS5Padding": lambda x: x[:-ord(x[-1])]
    }
    __encode = {
        "base64": base64.encodebytes,
        "hex": binascii.b2a_hex
    }
    __decode = {
        "base64": base64.decodebytes,
        "hex": binascii.a2b_hex
    }

    def __init__(self, key=None, iv=None, cipher_method=1, pad_method="default", code_method=None):
        """
        :param key: 密钥，长度16位。
        :param iv: 向量，长度与密钥一致。
        :param cipher_method: 加密方式，["MODE_ECB"|"MODE_CBC"|"MODE_CFB"]。
        :param pad_method: 填充方式，["default"|"PKCS5Padding"]。
        :param code_method: 编码方式，["base64"|"hex"]。
        """
        self.__key = key if key else "abcdefgh12345678"
        self.__iv = iv if iv else Crypto.Random.new().read(Crypto.Cipher.AES.block_size)
        if isinstance(cipher_method, str):
            cipher_method = getattr(Crypto.Cipher.AES, cipher_method)
        self.__cipher_method = cipher_method
        self.__pad_method = pad_method
        self.__code_method = code_method

    def __get_cipher(self):
        if self.__cipher_method == 1:
            cipher = Crypto.Cipher.AES.new(self.__key.encode("utf-8"), 1)
        else:
            cipher = Crypto.Cipher.AES.new(self.__key.encode("utf-8"), 2, self.__iv.encode("utf-8"))
        return cipher

    def __text_verify(self, text):
        while len(text) > len(self.__key):
            text_slice = text[:len(self.__key)]
            text = text[len(self.__key):]
            yield text_slice
        else:
            if len(text) == len(self.__key):
                yield text
            else:
                yield self.__pad(text)

    def __pad(self, text):
        return self.__lambda_pad[self.__pad_method](text, len(self.__key))

    def encrypt(self, text):
        cipher = self.__get_cipher()
        cipher_text = b"".join([cipher.encrypt(i) for i in self.__text_verify(text.encode("utf-8"))])
        encode_func = self.__encode.get(self.__code_method)
        if encode_func:
            cipher_text = encode_func(cipher_text)
        return cipher_text.decode("utf-8").rstrip()

    def __unpad(self, cipher_text):
        return self.__lambda_unpad[self.__pad_method](cipher_text)

    def decrypt(self, cipher_text):
        cipher = self.__get_cipher()
        cipher_text = cipher_text.encode("utf-8")
        decode_func = self.__decode.get(self.__code_method)
        if decode_func:
            cipher_text = decode_func(cipher_text)
        return self.__unpad(cipher.decrypt(cipher_text).decode("utf-8"))
