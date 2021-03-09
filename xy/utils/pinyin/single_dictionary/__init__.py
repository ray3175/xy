from pypinyin import load_single_dict
from .a_0 import a_0


SINGLE_DICTIONARY = dict()

SINGLE_DICTIONARY.update(a_0)


def active():
    """
    激活自定义单词多音字。
    """
    load_single_dict(SINGLE_DICTIONARY)

