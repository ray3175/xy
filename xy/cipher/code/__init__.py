import binascii


class Code:
    ENCODE_DICT = {
        "base64": binascii.b2a_base64,
        "hex": binascii.b2a_hex
    }
    DECODE_DICT = {
        "base64": binascii.a2b_base64,
        "hex": binascii.a2b_hex
    }

    def __init__(self, method: str = "base64"):
        """
        method: ["base64"|"hex"]
        """
        self.__method = method

    def encode(self, _bytes: bytes) -> bytes:
        return self.ENCODE_DICT[self.__method](_bytes)

    def decode(self, _bytes: bytes) -> bytes:
        return self.DECODE_DICT[self.__method](_bytes)


