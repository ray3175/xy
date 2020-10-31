import numba       # pip install numba


class JIT:
    """
    Just in time
    """

    @staticmethod
    def jit(*args, **kwargs):
        """
        nopython=True    默认为True，若不明确定义，遇到不支持的第三方库则会关闭。
        fastmath=True    牺牲精度，提升速度
        parallel=True    并行计算
        """
        return numba.jit(*args, **kwargs)




