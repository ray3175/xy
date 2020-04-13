import setproctitle     # pip install setproctitle


class ProcessName:
    @classmethod
    def set_name(cls, name: str) -> bool:
        setproctitle.setproctitle(name)
        return True

    @classmethod
    def get_name(cls) -> str:
        return setproctitle.getproctitle()

