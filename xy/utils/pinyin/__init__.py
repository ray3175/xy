from typing import List
from pypinyin import pinyin, Style      # pip install pypinyin


class PinYin:
    def __init__(self, hans: str):
        self.__hans = hans

    @staticmethod
    def depth_first_ergodic(array, _iter=False):
        """ 模拟深度优先遍历，速度慢于广度优先遍历 """
        return [[i, *j] if len(array[1:]) > 1 else [i, j] for i in array[0] for j in PinYin.depth_first_ergodic(array[1:], True)] if len(array) > 1 else (array[0] if _iter else array) if array else []

    @staticmethod
    def breadth_first_ergodic(array, _iter=False):
        """ 模拟广度优先遍历，速度快于深度优先遍历 """
        return [[i, *j] if len(array[1:]) > 1 else [i, j] for j in PinYin.breadth_first_ergodic(array[1:], True) for i in array[0]] if len(array) > 1 else (array[0] if _iter else array) if array else []

    def get_origin_bopomofo_array(self, style=Style.NORMAL, heteronym=True) -> List[List[str]]:
        """
        输出原生全拼
            style： 拼音风格
            heteronym： 是否输出多音字
        """
        return pinyin(self.__hans, style=style, heteronym=heteronym)

    def get_origin_logogram_array(self, style=Style.FIRST_LETTER, heteronym=True) -> List[List[str]]:
        """
        输出原生简拼
            style： 拼音风格
            heteronym： 是否输出多音字
        """
        return pinyin(self.__hans, style=style, heteronym=heteronym)

    def to_bopomofo_array(self, style=Style.NORMAL, heteronym=True) -> List[List[str]]:
        """
        输出遍历原生全拼矩阵
            style： 拼音风格
            heteronym： 是否输出多音字
        """
        origin_bopomofo_array = self.get_origin_bopomofo_array(style, heteronym)
        return PinYin.breadth_first_ergodic(origin_bopomofo_array)

    def to_logogram_array(self, style=Style.FIRST_LETTER, heteronym=True) -> List[List[str]]:
        """
        输出遍历原生简拼矩阵
            style： 拼音风格
            heteronym： 是否输出多音字
        """
        origin_logogram_array = self.get_origin_logogram_array(style, heteronym)
        return PinYin.breadth_first_ergodic(origin_logogram_array)


