from .one_dimension_cipher import OneDimensionCipher


class TwoDimensionCipher(OneDimensionCipher):
    def __init__(self, key, iv=None, cut=3):
        self.__cut = 2 ** cut
        super().__init__(key, iv)
        self.__key = self.get_key()
        self.__iv = self.get_iv()

    def get_cut(self):
        return self.__cut

    def encrypt(self, text):
        key = self.__key
        start = 0
        _len = len(text)
        cipher_text = list()
        while stop:=self.__cut < _len:
            code_list = [key^ord(i) for i in text[start: stop]]
            cipher_text.extend(code_list)
            key = sum(code_list)
            start, stop = stop, stop + self.__cut
        else:
            code_list = [key^ord(i) for i in text[start: _len]]
            cipher_text.extend(code_list)
        return "".join([chr(i) for i in cipher_text])

    def decrypt(self, cipher_text):
        key = self.__key
        start = 0
        _len = len(cipher_text)
        text = list()
        while stop:=self.__cut < _len:
            _code_list = [ord(i) for i in cipher_text[start: stop]]
            code_list = [key^i for i in _code_list]
            key = sum(_code_list)
            text.extend(code_list)
            start, stop = stop, stop + self.__cut
        else:
            code_list = [key^ord(i) for i in cipher_text[start: _len]]
            text.extend(code_list)
        return "".join([chr(i) for i in text])


