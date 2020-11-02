import rsa


class RSAPrivate:
    def __init__(self, private_key: bytes, methods="PEM"):
        """
        :param methods: ["PEM"|"DER"]
            需要和private_key的类型一致。
        """
        super().__init__()
        self.__key = rsa.PrivateKey.load_pkcs1(private_key, methods)

    def decrypt(self, cipher_text: bytes) -> bytes:
        return rsa.decrypt(cipher_text, self.__key)

    def sign(self, text: bytes, hash_method="SHA-512") -> bytes:
        """
        :param hash_method: ["MD5"|"SHA-1"|"SHA-224"|"SHA-256"|"SHA-384"|"SHA-512"]
        """
        return rsa.sign(text, self.__key, hash_method=hash_method)

