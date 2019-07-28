class RayDict(dict):
    def __add__(self, other):
        if isinstance(other, dict):
            self.update(other)
        elif isinstance(other, list):
            self.update({tuple(other): None})
        else:
            self.update({other: None})

    def __missing__(self, key):
        return None
