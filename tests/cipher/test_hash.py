import pytest
from xy.cipher.hash import Hash
from xy.cipher.code import Code


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
        hash_bytes = b'\xcb\xf2\x15\x00\x02\xae\xf9k\xe7\xa8\x8c\x98\xdf6\t\x7f\xd5w\xdc\xaf\x0f\xcf\xa9\x1e\xd0\x8b2\x85\xee\xca\xb3/\xc3\x1f\x80.\xd2\xbf\xc0\xea\xc5>y\xba\xddV@\xcc\xe7\xd6K\xa3\xc0\x0fg?)"\xc6\xd5\xdde\xfb\xe9'
        hash_text = "cbf2150002aef96be7a88c98df36097fd577dcaf0fcfa91ed08b3285eecab32fc31f802ed2bfc0eac53e79badd5640cce7d64ba3c00f673f2922c6d5dd65fbe9"
        assert self.hash0.encrypt(self.__text.encode("utf-8")) == hash_bytes
        assert Code("hex").encode(hash_bytes).decode("utf-8") == hash_text

    def test_encrypt_1(self):
        hash_bytes = b'![\x8f}h\x12n\x174\xd8\xb4WsFU\x86\x0c\x9a\x8ckL`\x94\x06+p\x82#<l\xa7\x81mPBm)\xba#9\x9f\xeef&E4\xeb\xb5\xfbvG\x9d\xca\xba\xc1_J\xc46\xab\xb0Bv\xba'
        hash_text = "215b8f7d68126e1734d8b457734655860c9a8c6b4c6094062b7082233c6ca7816d50426d29ba23399fee66264534ebb5fb76479dcabac15f4ac436abb04276ba"
        assert self.hash1.encrypt(self.__text.encode("utf-8")) == hash_bytes
        assert Code("hex").encode(hash_bytes).decode("utf-8") == hash_text

    def test_encrypt_2(self):
        hash_bytes = b'X^.\xa9\xb3\xc7s\x94|Vo+\xeeG\xbe\xd2U\xac\x0c\x82w\t\x16Au`\x00\x158\x9e\x80e\x07\xc8\n_\x0b\xca\x8e\xcc\xad&\xa3MH\xf1\x1a\x0b\xd2c0J\xb6\x93\x1a\x17\xc5\x9d\xda\xf9\xf0\x91\x02\x80'
        hash_text = "585e2ea9b3c773947c566f2bee47bed255ac0c827709164175600015389e806507c80a5f0bca8eccad26a34d48f11a0bd263304ab6931a17c59ddaf9f0910280"
        assert self.hash2.encrypt(self.__text.encode("utf-8")) == hash_bytes
        assert Code("hex").encode(hash_bytes).decode("utf-8") == hash_text


if __name__ == "__main__":
    pytest.main(["-v", "-s", "test_hash.py"])


