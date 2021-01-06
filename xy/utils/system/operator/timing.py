import pytweening


class TimingFunction:
    @staticmethod
    def liner(n):
        """ 速度均匀 """
        return pytweening.linear(n)

    @staticmethod
    def ease_in_quad(n):
        """ 开始慢，结尾快（二次方倍速） """
        return pytweening.easeInQuad(n)

    @staticmethod
    def ease_out_quad(n):
        """ 开始快，结尾慢（二次方倍速） """
        return pytweening.easeOutQuad(n)

    @staticmethod
    def ease_in_out_quad(n):
        """ 两端快，中间慢（二次方倍速） """
        return pytweening.easeInOutQuad(n)

    @staticmethod
    def ease_in_cubic(n):
        """ 开始慢，结尾快（三次方倍速） """
        return pytweening.easeInCubic(n)

    @staticmethod
    def ease_out_cubic(n):
        """ 开始快，结尾慢（三次方倍速） """
        return pytweening.easeOutCubic(n)

    @staticmethod
    def ease_in_out_cubic(n):
        """ 两端快，中间慢（三次方倍速） """
        return pytweening.easeInOutCubic(n)

    @staticmethod
    def ease_in_quart(n):
        """ 开始慢，结尾快（四次方倍速） """
        return pytweening.easeInQuart(n)

    @staticmethod
    def ease_out_quart(n):
        """ 开始快，结尾慢（四次方倍速） """
        return pytweening.easeOutQuart(n)

    @staticmethod
    def ease_in_out_quart(n):
        """ 两端快，中间慢（四次方倍速） """
        return pytweening.easeInOutQuart(n)

    @staticmethod
    def ease_in_quint(n):
        """ 开始慢，结尾快（五次方倍速） """
        return pytweening.easeInQuint(n)

    @staticmethod
    def ease_out_quint(n):
        """ 开始快，结尾慢（五次方倍速） """
        return pytweening.easeOutQuint(n)

    @staticmethod
    def ease_in_out_quint(n):
        """ 两端快，中间慢（五次方倍速） """
        return pytweening.easeInOutQuint(n)

    @staticmethod
    def ease_in_sine(n):
        """ 开始慢，结尾快（正弦函数） """
        return pytweening.easeInSine(n)

    @staticmethod
    def ease_out_sine(n):
        """ 开始快，结尾慢（正弦函数） """
        return pytweening.easeOutSine(n)

    @staticmethod
    def ease_in_out_sine(n):
        """ 两端快，中间慢（正弦函数） """
        return pytweening.easeInOutSine(n)

    @staticmethod
    def ease_in_expo(n):
        """ 开始慢，结尾快（指数函数） """
        return pytweening.easeInExpo(n)

    @staticmethod
    def ease_out_expo(n):
        """ 开始快，结尾慢（指数函数） """
        return pytweening.easeOutExpo(n)

    @staticmethod
    def ease_in_out_expo(n):
        """ 两端快，中间慢（指数函数） """
        return pytweening.easeInOutExpo(n)

    @staticmethod
    def ease_in_circ(n):
        """ 开始慢，结尾快（圆函数） """
        return pytweening.easeInCirc(n)

    @staticmethod
    def ease_out_circ(n):
        """ 开始快，结尾慢（圆函数） """
        return pytweening.easeOutCirc(n)

    @staticmethod
    def ease_in_out_circ(n):
        """ 两端快，中间慢（圆函数） """
        return pytweening.easeInOutCirc(n)

    @staticmethod
    def ease_in_elastic(n):
        """ 开始慢，结尾快（弹性函数） """
        return pytweening.easeInElastic(n)

    @staticmethod
    def ease_out_elastic(n):
        """ 开始快，结尾慢（弹性函数） """
        return pytweening.easeOutElastic(n)

    @staticmethod
    def ease_in_out_elastic(n):
        """ 两端快，中间慢（弹性函数） """
        return pytweening.easeInOutElastic(n)

    @staticmethod
    def ease_in_back(n):
        """ 开始缓慢反向，然后加速移动到目标 """
        return pytweening.easeInBack(n)

    @staticmethod
    def ease_out_back(n):
        """ 开始快速移动到目标，然后减速反向缓冲 """
        return pytweening.easeOutBack(n)

    @staticmethod
    def ease_in_out_back(n):
        """ 开始缓慢反向，然后加速移动到目标，然后减速反向缓冲 """
        return pytweening.easeInOutBack(n)

    @staticmethod
    def ease_in_bounce(n):
        """ 开始缓慢跳跃，然后加速移动到目标 """
        return pytweening.easeInBounce(n)

    @staticmethod
    def ease_out_bounce(n):
        """ 开始快速移动，然后减速跳跃到目标 """
        return pytweening.easeOutBounce(n)

    @staticmethod
    def ease_in_out_bounce(n):
        """ 匀速跳跃至目标 """
        return pytweening.easeInOutBounce(n)

