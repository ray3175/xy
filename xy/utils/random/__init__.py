from typing import Iterable, Callable
import random
import copy


class Random:
    def __init__(self):
        pass

    def random(self) -> float:
        """ 获取 0 - 1 之间的随机数 """
        return random.random()

    def randint(self, min: int, max: int) -> int:
        """ 获取 min - max 之间的随机数 min <= max """
        return random.randint(min, max)

    def uniform(self, a: float, b: float) -> float:
        """ 获取 a - b 之间的随机数 """
        return random.uniform(a, b)

    def choice(self, obj: Iterable):
        """ 获取可迭代参数中的某个值 """
        return random.choice(obj)

    def randrange(self, min: int, max: int, step: int = 1) -> int:
        """ 获取 min - max 之间步长为 step 的随机数 min < max """
        return random.randrange(min, max, step)

    def shuffle_string(self, string: str, factor: Callable) -> str:
        """ 获取乱序字符串 """
        return "".join(self.shuffle(list(string), factor))

    def shuffle(self, obj: (list, bytearray, str), factor: Callable = None, copy_type: int = 0):
        """
        :param obj: 可迭代参数
        :param factor: 可 call 的对象，call 后的值为 0 - 1 之间。该值影响乱序结果，如果该值唯一，则返回结果唯一。
        :param copy_type: 0（不需要复制） 1（浅复制） 2（深复制）
        :return: 获取可迭代参数的乱序
        """
        if isinstance(obj, str):
            return self.shuffle_string(obj, factor)
        if copy_type == 1:
            obj = copy.copy(obj)
        elif copy_type == 2:
            obj = copy.deepcopy(obj)
        random.shuffle(obj, factor)
        return obj


