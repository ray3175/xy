import pytest
from xy.cipher.two_dimension_cipher import TwoDimensionCipher


class Test_TwoDimensionCipher:
    def setup_class(self):
        self.__key = "hello world"
        self.two_dimension_cipher0 = TwoDimensionCipher(self.__key)
        self.two_dimension_cipher1 = TwoDimensionCipher(self.__key, iv="iv")
        self.two_dimension_cipher2 = TwoDimensionCipher(self.__key, iv="iv", cut=8)

    def teardown_class(self):
        pass

    def setup(self):
        pass

    def teardown(self):
        pass

    def test_encrypt(self):
        text = "这是test_encrypt测试数据！"
        encrypt_data = self.two_dimension_cipher0.encrypt(text)
        assert encrypt_data == "讅扳ШйЯШЃй𐚂𐚏𐚞𐚕𐚜𐚘𖮧𘴹򔔨򔌶򝽙"
        assert self.two_dimension_cipher0.decrypt(encrypt_data) == text

    def test_encrypt_iv(self):
        text = "这是test_encrypt_iv测试数据！"
        encrypt_data = self.two_dimension_cipher1.encrypt(text)
        assert encrypt_data == "謆拰ҫҺҬҫҀҺ𐦂𐦏𐦞𐦕𐦜𐦘𐦳𐦅򄳆򂇻򌝥򂧀򂿞򋎱"
        assert self.two_dimension_cipher1.decrypt(encrypt_data) == text

    def test_encrypt_cut(self):
        text = "这是test_encrypt_cut测试数据！"
        encrypt_data = self.two_dimension_cipher2.encrypt(text)
        assert encrypt_data == "謆拰ҫҺҬҫҀҺұҼҭҦүҫҀҼҪҫ榔輊憯枱ﯞ"
        assert self.two_dimension_cipher2.decrypt(encrypt_data) == text

    def test_not_equal(self):
        text = "这是test_not_equal测试数据！"
        encrypt_data_0 = self.two_dimension_cipher0.encrypt(text)
        encrypt_data_1 = self.two_dimension_cipher1.encrypt(text)
        encrypt_data_2 = self.two_dimension_cipher2.encrypt(text)
        assert encrypt_data_0 != encrypt_data_1 != encrypt_data_2
        assert self.two_dimension_cipher0.decrypt(encrypt_data_0) == self.two_dimension_cipher1.decrypt(encrypt_data_1) == self.two_dimension_cipher2.decrypt(encrypt_data_2)


if __name__ == "__main__":
    pytest.main(["-v", "-s", "test_two_dimension_cipher.py"])


