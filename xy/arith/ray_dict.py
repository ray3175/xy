import json


class RayDict(dict):
    def __init__(self, seq={}, **kwargs):
        if isinstance(seq, str):
            seq = json.loads(seq)
        super().__init__(seq, **kwargs)

    def __missing__(self, key):
        return None
