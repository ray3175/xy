import os
import rsa      # pip install rsa


class RSA:
    @classmethod
    def __read_in_file(cls, file_path, data_type="rb"):
        with open(file_path, data_type) as x:
            _return = x.read()
            x.close()
        return _return

    @classmethod
    def __write_in_file(cls, file_path, data, data_type="wb"):
        with open(file_path, data_type) as x:
            x.write(data)
            x.close()

    @classmethod
    def newkeys(cls, nbits=1024, private_key_path=None, public_key_path=None, private_is_der=False, public_is_der=False):
        pubilc_key, private_key = rsa.newkeys(nbits)
        if not private_key_path:
            private_key_path = os.path.join(os.getcwd(), "private_key.pem" if not private_is_der else "private_key.der")
        if not public_key_path:
            public_key_path = os.path.join(os.getcwd(), "public_key.pem" if not public_is_der else "public_key.der")
        private_key, pubilc_key = private_key.save_pkcs1("PEM" if not private_is_der else "DER"), pubilc_key.save_pkcs1("PEM" if not public_is_der else "DER")
        cls.__write_in_file(private_key_path, private_key)
        cls.__write_in_file(public_key_path, pubilc_key)

    @classmethod
    def __load_key(cls, key_path, key_type="private", _type="PEM"):
        if key_type == "private":
            _return = rsa.PrivateKey.load_pkcs1(cls.__read_in_file(key_path), _type)
        else:
            _return = rsa.PublicKey.load_pkcs1(cls.__read_in_file(key_path), _type)
        return _return

    @classmethod
    def encrypt(cls, text, public_key_path, _type="PEM"):
        return rsa.encrypt(text.encode("utf-8"), cls.__load_key(public_key_path, "public", _type))

    @classmethod
    def decrypt(cls, cipher_text_with_byte, private_key_path, _type="PEM"):
        return rsa.decrypt(cipher_text_with_byte, cls.__load_key(private_key_path, _type=_type)).decode("utf-8")

    @classmethod
    def sign(cls, text, private_key_path, sign_type="SHA-512", _type="PEM"):
        return rsa.sign(text.encode("utf-8"), cls.__load_key(private_key_path, _type=_type), sign_type)

    @classmethod
    def verify(cls, text, sign, public_key_path, _type="PEM"):
        return rsa.verify(text.encode("utf-8"), sign, cls.__load_key(public_key_path, "public", _type))
