import rsa


class RSAPublic:
    def __init__(self, public_key: bytes, methods="PEM"):
        """
        :param methods: ["PEM"|"DER"]
            需要和public_key的类型一致。
        """
        super().__init__()
        self.__key = rsa.PublicKey.load_pkcs1(public_key, methods)

    def encrypt(self, text: bytes) -> bytes:
        return rsa.encrypt(text, self.__key)

    def verify(self, text: bytes, sign: bytes) -> str:
        """
        :param text: 与私钥sign函数text参数一致。
        :param sign: 私钥RSAPrivate().sign(text, hash_method)的返回值。
        text与sign如果不配对，将抛出异常：
            rsa.pkcs1.VerificationError: Verification failed
        配对则返回hash_method值。
        """
        return rsa.verify(text, sign, self.__key)


