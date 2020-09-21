import pytest
from xy.cipher.hash import Hash


class Test_Hash:
    def setup_class(self):
        self.__text = "Hash测试文本！"
        self.hash0 = Hash()
        self.hash1 = Hash(salt="xy")
        self.hash2 = Hash(salt="xy", iterations=9)

    def teardown_class(self):
        pass

    def setup(self):
        pass

    def teardown(self):
        pass

    def test_encrypt_0(self):
        hash_text = "cbf2150002aef96be7a88c98df36097fd577dcaf0fcfa91ed08b3285eecab32fc31f802ed2bfc0eac53e79badd5640cce7d64ba3c00f673f2922c6d5dd65fbe9"
        assert self.hash0.encrypt(self.__text) == hash_text

    def test_encrypt_1(self):
        hash_text = "215b8f7d68126e1734d8b457734655860c9a8c6b4c6094062b7082233c6ca7816d50426d29ba23399fee66264534ebb5fb76479dcabac15f4ac436abb04276ba"
        assert self.hash1.encrypt(self.__text) == hash_text

    def test_encrypt_2(self):
        hash_text = "585e2ea9b3c773947c566f2bee47bed255ac0c827709164175600015389e806507c80a5f0bca8eccad26a34d48f11a0bd263304ab6931a17c59ddaf9f0910280"
        assert self.hash2.encrypt(self.__text) == hash_text


if __name__ == "__main__":
    pytest.main(["-v", "-s", "test_hash.py"])


