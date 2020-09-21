import pytest
from xy.cipher.one_dimension_cipher import OneDimensionCipher


class Test_OneDimensionCipher:
    def setup_class(self):
        self.__data = "哈喽哈喽，大家好啊！"
        self.one_dimension_cipher0 = OneDimensionCipher(self.__data)
        self.one_dimension_cipher1 = OneDimensionCipher(self.__data, iv="我是偏移量")

    def teardown_class(self):
        pass

    def setup(self):
        pass

    def teardown(self):
        pass

    def test_encrypt(self):
        text = "这是test_encrypt测试数据！"
        encrypt_data = self.one_dimension_cipher0.encrypt(text)
        assert encrypt_data == "񃥢񍂔񋛏񋛞񋛈񋛏񋛤񋛞񋛕񋛘񋛉񋛂񋛋񋛏񍯰񃵮񍏋񍗕񄦺"
        assert self.one_dimension_cipher0.decrypt(encrypt_data) == text

    def test_encrypt_iv(self):
        text = "这是test_encrypt_iv测试数据！"
        encrypt_data = self.one_dimension_cipher1.encrypt(text)
        assert encrypt_data == "񣤢񭃔񫚏񫚞񫚈񫚏񫚤񫚞񫚕񫚘񫚉񫚂񫚋񫚏񫚤񫚒񫚍񭮰񣴮񭎋񭖕񤧺"
        assert self.one_dimension_cipher1.decrypt(encrypt_data) == text

    def test_not_equal(self):
        text = "这是test_not_equal测试数据！"
        encrypt_data_0 = self.one_dimension_cipher0.encrypt(text)
        encrypt_data_1 = self.one_dimension_cipher1.encrypt(text)
        assert encrypt_data_0 != encrypt_data_1
        assert self.one_dimension_cipher0.decrypt(encrypt_data_0) == self.one_dimension_cipher1.decrypt(encrypt_data_1)


if __name__ == "__main__":
    pytest.main(["-v", "-s", "test_one_dimension_cipher.py"])


