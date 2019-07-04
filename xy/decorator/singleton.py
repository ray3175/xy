class Singleton:
    __cls = dict()

    def __init__(self, cls):
        self.__key = cls

    def __call__(self, *args, **kwargs):
        if self.__key not in self.__cls:
            self.__cls[self.__key] = self.__key(*args, **kwargs)
        return self.__cls[self.__key]
