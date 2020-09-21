import pytest
import os
import shutil
import tempfile
from xy.cipher.asymmetric._rsa import RSA


class Test_RSA:
    def setup_class(self):
        self.__text = "RSA测试文本！"
        self.__path = tempfile.mkdtemp()
        self.__private_key_pem_path = os.path.join(self.__path, "private_key.pem")
        self.__private_key_der_path = os.path.join(self.__path, "private_key.der")
        self.__pubilc_key_pem_path = os.path.join(self.__path, "pubilc_key.pem")
        self.__pubilc_key_der_path = os.path.join(self.__path, "pubilc_key.der")
        self.rsa = RSA()
        self.rsa.newkeys(private_key_path=self.__private_key_pem_path, public_key_path=self.__pubilc_key_pem_path)
        self.rsa.newkeys(private_key_path=self.__private_key_der_path, public_key_path=self.__pubilc_key_der_path, private_is_der=True, public_is_der=True)

    def teardown_class(self):
        if os.path.exists(self.__path):
            shutil.rmtree(self.__path)

    def setup(self):
        pass

    def teardown(self):
        pass

    def test_encrypt_decrypt_pem(self):
        content = self.rsa.encrypt(self.__text, self.__pubilc_key_pem_path)
        assert self.rsa.decrypt(content, self.__private_key_pem_path) == self.__text

    def test_encrypt_decrypt_der(self):
        content = self.rsa.encrypt(self.__text, self.__pubilc_key_der_path, _type="DER")
        assert self.rsa.decrypt(content, self.__private_key_der_path, _type="DER") == self.__text

    def test_sign_verify_pem(self):
        sign_type = "SHA-256"
        sign_content = self.rsa.sign(self.__text, self.__private_key_pem_path, sign_type)
        assert self.rsa.verify(self.__text, sign_content, self.__pubilc_key_pem_path) == sign_type

    def test_sign_verify_der(self):
        sign_type = "MD5"
        sign_content = self.rsa.sign(self.__text, self.__private_key_der_path, sign_type, _type="DER")
        assert self.rsa.verify(self.__text, sign_content, self.__pubilc_key_der_path, _type="DER") == sign_type


if __name__ == "__main__":
    pytest.main(["-v", "-s", "test_asymmetric.py"])


