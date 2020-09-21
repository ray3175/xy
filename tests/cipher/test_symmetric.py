import pytest
from xy.cipher.symmetric.AES import AES


class Test_AES:
    def setup_class(self):
        self.__text = "AES测试文本！"
        key = "abcdefgh12345678"
        iv = key[::-1]
        self.aes_ecb_0 = AES(key, cipher_method="MODE_ECB")
        self.aes_ecb_1 = AES(key, cipher_method="MODE_ECB", pad_method="PKCS5Padding")
        self.aes_ecb_2 = AES(key, cipher_method="MODE_ECB", pad_method="PKCS5Padding", code_method="hex")
        self.aes_cbc_0 = AES(key, cipher_method="MODE_CBC")
        self.aes_cbc_1 = AES(key, iv=iv, cipher_method="MODE_CBC")
        self.aes_cbc_2 = AES(key, iv=iv, cipher_method="MODE_CBC", pad_method="PKCS5Padding")
        self.aes_cbc_3 = AES(key, iv=iv, cipher_method="MODE_CBC", pad_method="PKCS5Padding", code_method="hex")

    def teardown_class(self):
        pass

    def setup(self):
        pass

    def teardown(self):
        pass

    def test_ecb_0(self):
        encrypt_text = "dMcCQS2EV710szNmQTt44m66I1QXh1eJGYqX1SnaE80="
        assert self.aes_ecb_0.encrypt(self.__text) == encrypt_text
        assert self.aes_ecb_0.decrypt(encrypt_text) == self.__text

    def test_ecb_1(self):
        encrypt_text = "dMcCQS2EV710szNmQTt44mDZxOO39Tf4Px9u+8E4rS8="
        assert self.aes_ecb_1.encrypt(self.__text) == encrypt_text
        assert self.aes_ecb_1.decrypt(encrypt_text) == self.__text

    def test_ecb_2(self):
        encrypt_text = "74c702412d8457bd74b33366413b78e260d9c4e3b7f537f83f1f6efbc138ad2f"
        assert self.aes_ecb_2.encrypt(self.__text) == encrypt_text
        assert self.aes_ecb_2.decrypt(encrypt_text) == self.__text

    def test_cbc_0(self):
        encrypt_text = self.aes_cbc_0.encrypt(self.__text)
        assert self.aes_cbc_0.decrypt(encrypt_text) == self.__text

    def test_cbc_1(self):
        encrypt_text = "x3uzdJ1+1p0IJwPmKOsj5tym5Rh2kx26Hvs1xZ4m8hk="
        assert self.aes_cbc_1.encrypt(self.__text) == encrypt_text
        assert self.aes_cbc_1.decrypt(encrypt_text) == self.__text

    def test_cbc_2(self):
        encrypt_text = "x3uzdJ1+1p0IJwPmKOsj5mK2r9Zwj56k9p9ExbosHKg="
        assert self.aes_cbc_2.encrypt(self.__text) == encrypt_text
        assert self.aes_cbc_2.decrypt(encrypt_text) == self.__text

    def test_cbc_3(self):
        encrypt_text = "c77bb3749d7ed69d082703e628eb23e662b6afd6708f9ea4f69f44c5ba2c1ca8"
        assert self.aes_cbc_3.encrypt(self.__text) == encrypt_text
        assert self.aes_cbc_3.decrypt(encrypt_text) == self.__text


if __name__ == "__main__":
    pytest.main(["-v", "-s", "test_symmetric.py"])


