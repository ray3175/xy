class OneDimensionCipher:
    def __init__(self, key, iv=None):
        self.__key = self.__str2int_with_ord_by_sum(key)
        self.__iv = iv
        if self.__iv:
            self.__key = self.__key | self.__str2int_with_ord_by_sum(self.__iv)

    def __str2int_with_ord_by_sum(self, string):
        return sum([ord(i) for i in string])

    def get_key(self):
        return self.__key

    def get_iv(self):
        return self.__iv

    def encrypt(self, text):
        return "".join([chr(self.__key^ord(i)) for i in text])

    def decrypt(self, cipher_text):
        return self.encrypt(cipher_text)
