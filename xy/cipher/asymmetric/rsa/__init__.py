import os
import rsa      # pip install rsa


class RSA:
    def __init__(self, nbits=1024):
        """
        :param nbits: 位数，必须大于16，如需写入文件必须大于106位，位数越长，rsa.newkeys()执行时间越长。
        """
        super().__init__()
        self.__nbits = nbits
        self.__public_key, self.__private_key = rsa.newkeys(nbits)

    @property
    def nbits(self):
        return self.__nbits

    @property
    def public_key(self):
        return self.__public_key

    @property
    def private_key(self):
        return self.__private_key

    def encrypt(self, text: bytes, public_key=None) -> bytes:
        if not public_key:
            public_key = self.__public_key
        return rsa.encrypt(text, public_key)

    def decrypt(self, cipher_text: bytes, private_key=None) -> bytes:
        if not private_key:
            private_key = self.__private_key
        return rsa.decrypt(cipher_text, private_key)

    def new_pkcs1(self, methods="PEM") -> (bytes, bytes):
        """
        :param methods: ["PEM"|"DER"]
        :return: (public_pkcs1_key, private_pkcs1_key)
        """
        return self.__public_key.save_pkcs1(methods), self.__private_key.save_pkcs1(methods)

    def _write_in_file(self, file_path, data):
        with open(file_path, mode="wb") as x:
            x.write(data)
            x.close()

    def write_in_file(self, private_key_path=None, public_key_path=None, methods="PEM"):
        """
        :param methods: ["PEM"|"DER"]
        """
        if not private_key_path:
            private_key_path = os.path.join(os.getcwd(), "private.key")
        if not public_key_path:
            public_key_path = os.path.join(os.getcwd(), "public.key")
        public_key, private_key = self.new_pkcs1(methods)
        self._write_in_file(public_key_path, public_key)
        self._write_in_file(private_key_path, private_key)

