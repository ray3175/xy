class XYException(Exception):
    def __call__(self, *args, **kwargs):
        return self.message

    @property
    def message(self):
        return str(self)


class XYError(XYException):
    pass


class XYWarning(XYError):
    pass


class XYInfo(XYWarning):
    pass


class XYDebug(XYInfo):
    pass

