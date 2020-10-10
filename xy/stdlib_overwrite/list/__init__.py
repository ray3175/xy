class List(list):
    def __lshift__(self, other):
        """
        self << other
        在 list 末端插入 other
        """
        self.append(other)
        return self

    def __rshift__(self, other):
        """
        self >> other
        从 list 末端开始，删除第一个 other
        成功返回 True，失败返回 False
        """
        for i in range(len(self)-1, -1, -1):
            if self[i] == other:
                self.pop(i)
                return True
        return False

    def __rrshift__(self, other):
        """
        other >> self
        在 list 首端插入 other
        """
        self.insert(0, other)
        return self

    def __rlshift__(self, other):
        """
        other << self
        从 list 首端开始，删除第一个 other
        成功返回 True，失败返回 False
        """
        if other in self:
            self.remove(other)
            return True
        return False


