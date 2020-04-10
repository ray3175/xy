class XYException(Exception):
    level = 10

    def __call__(self, *args, **kwargs):
        return self.msg

    @property
    def msg(self):
        return str(self)


class XYError(XYException):
    level = 9


class XYWarning(XYError):
    level = 6


class XYInfo(XYWarning):
    level = 3


class XYDebug(XYInfo):
    level = 0


