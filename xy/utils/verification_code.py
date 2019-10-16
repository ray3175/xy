import random
from PIL import Image, ImageDraw, ImageFont     # pip install pillow
from ..common._io import RayBytesIO


class VerificationCode:
    """
    生成验证码小工具！
    """
    __chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, img_mode="RGB", img_size=(90, 30), img_color=(255, 255, 255)):
        self.__image_mode = img_mode
        self.__image_size = img_size
        self.__image_color = img_color

    def __rand_color(self):
        return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

    def __rand_x(self, start=0):
        return random.randint(start, self.__image_size[0])

    def __rand_y(self, start=0):
        return random.randint(start, self.__image_size[-1])

    def __draw_in_code(self, code_length, code_style):
        def get_radom_code():
            index = random.randrange(0, len(self.__chars) - 1)
            return self.__chars[index]

        width_max = self.__image_size[0] / code_length
        width = lambda i: random.uniform(width_max * i, width_max * (i + 1) * 2 / 3)
        for i in range(code_length):
            font_size = random.randint(self.__rand_y(self.__image_size[-1] * 2 / 3), self.__image_size[-1])
            height = random.uniform(0, self.__image_size[-1] - font_size)
            char = get_radom_code()
            self.__code += char
            self.__draw.text([width(i), height], char, self.__rand_color(), ImageFont.truetype(code_style, font_size))

    def __draw_in_point(self, interferen_pos_number):
        for i in range(interferen_pos_number):
            x = self.__rand_x()
            y = self.__rand_y()
            self.__draw.point([x, y], self.__rand_color())

    def __draw_in_arc(self, interferen_arc):
        for i in range(interferen_arc):
            x = self.__rand_x()
            y = self.__rand_y()
            self.__draw.arc([x, y, x + 4, y + 4], 0, 90, self.__rand_color())

    def __draw_in_line(self, interferen_line):
        for i in range(interferen_line):
            x1 = self.__rand_x()
            y1 = self.__rand_y()
            x2 = self.__rand_x()
            y2 = self.__rand_y()
            self.__draw.line([x1, y1, x2, y2], self.__rand_color())

    def __get_image_info_with_memory(self, _type):
        return RayBytesIO.pil_image_to_bytes_with_memory(self.__image, _type)

    def new(self, code_length=4, code_style=None, image_type="png", interferen_pos_number=20, interferen_arc=20, interferen_line=5):
        self.__code = ""
        if not isinstance(code_length, int) and code_length <= 0:
            code_length = 4
        self.__image = Image.new(mode=self.__image_mode, size=self.__image_size, color=self.__image_color)
        self.__draw = ImageDraw.Draw(self.__image, self.__image_mode)
        self.__draw_in_code(code_length, code_style)
        self.__draw_in_point(interferen_pos_number)
        self.__draw_in_arc(interferen_arc)
        self.__draw_in_line(interferen_line)
        return self.__code,  self.__get_image_info_with_memory(image_type)


