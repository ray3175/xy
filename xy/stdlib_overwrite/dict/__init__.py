class Dict(dict):
    def __setattr__(self, key, value):
        self[key] = value
        return True

    def __delattr__(self, item):
        del self[item]

    def __getattr__(self, item):
        return self[item]

    def __missing__(self, key):
        return None

