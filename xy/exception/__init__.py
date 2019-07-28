class XYException(Exception):
    level = 10

    def __call__(self, *args, **kwargs):
        return self.msg

    @property
    def msg(self):
        return str(self)


class XYError(XYException):
    level = 9


class XYWarning(XYException):
    level = 6


class XYInfo(XYException):
    level = 3


class XYDebug(XYException):
    level = 0
