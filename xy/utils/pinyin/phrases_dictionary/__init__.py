from pypinyin import load_phrases_dict
from .a_0 import a_0


PHRASES_DICTIONARY = dict()

PHRASES_DICTIONARY.update(a_0)


def active():
    """
    激活自定义短语多音字。
    """
    load_phrases_dict(PHRASES_DICTIONARY)

