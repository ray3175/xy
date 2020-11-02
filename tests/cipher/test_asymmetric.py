import pytest
import os
import shutil
import tempfile
from xy.cipher.asymmetric.rsa import RSA
from xy.cipher.asymmetric.rsa.rsa_public import RSAPublic
from xy.cipher.asymmetric.rsa.rsa_private import RSAPrivate


class Test_RSA:
    def setup_class(self):
        def read(path):
            with open(path, "rb") as x:
                text = x.read()
                x.close()
            return text
        self.__text = "RSA测试文本！"
        self.__path = tempfile.mkdtemp()
        pubilc_key_pem_path = os.path.join(self.__path, "pubilc_key.pem")
        pubilc_key_der_path = os.path.join(self.__path, "pubilc_key.der")
        private_key_pem_path = os.path.join(self.__path, "private_key.pem")
        private_key_der_path = os.path.join(self.__path, "private_key.der")
        self.rsa = RSA()
        self.rsa.write_in_file(public_key_path=pubilc_key_pem_path, private_key_path=private_key_pem_path)
        self.rsa.write_in_file(public_key_path=pubilc_key_der_path, private_key_path=private_key_der_path, methods="DER")
        self.public_pem = RSAPublic(read(pubilc_key_pem_path), "PEM")
        self.public_der = RSAPublic(read(pubilc_key_der_path), "DER")
        self.private_pem = RSAPrivate(read(private_key_pem_path), "PEM")
        self.private_der = RSAPrivate(read(private_key_der_path), "DER")

    def teardown_class(self):
        if os.path.exists(self.__path):
            shutil.rmtree(self.__path)

    def setup(self):
        pass

    def teardown(self):
        pass

    def test_rsa_encrypt_decrypt(self):
        content = self.rsa.encrypt(self.__text.encode("utf-8"))
        assert self.rsa.decrypt(content).decode("utf-8") == self.__text

    def test_rsa_encrypt_decrypt_pem(self):
        content = self.public_pem.encrypt(self.__text.encode("utf-8"))
        assert self.private_pem.decrypt(content).decode("utf-8") == self.__text

    def test_encrypt_decrypt_der(self):
        content = self.public_der.encrypt(self.__text.encode("utf-8"))
        assert self.private_der.decrypt(content).decode("utf-8") == self.__text

    def test_sign_verify_sha256(self):
        sign_type = "SHA-256"
        sign = self.private_pem.sign(self.__text.encode("utf-8"), sign_type)
        assert self.public_pem.verify(self.__text.encode("utf-8"), sign) == sign_type

    def test_sign_verify_md5(self):
        sign_type = "MD5"
        sign = self.private_der.sign(self.__text.encode("utf-8"), sign_type)
        assert self.public_der.verify(self.__text.encode("utf-8"), sign) == sign_type


if __name__ == "__main__":
    pytest.main(["-v", "-s", "test_asymmetric.py"])


