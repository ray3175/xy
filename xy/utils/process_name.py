import setproctitle     # pip install setproctitle


class ProcessName:
    @classmethod
    def set_name(cls, name):
        setproctitle.setproctitle(name)

    @classmethod
    def get_name(cls):
        return setproctitle.getproctitle()

