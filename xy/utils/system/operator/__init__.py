import pyautogui        # pip install pyautogui
from ....stdlib_overwrite.dict import Dict
from .timing import TimingFunction


class SystemOperator:
    @staticmethod
    def size() -> pyautogui.Size:
        """ 获取屏幕尺寸 """
        return pyautogui.size()

    @staticmethod
    def mouse_position() -> pyautogui.Point:
        """ 获取鼠标当前位置 """
        return pyautogui.position()

    @staticmethod
    def move_to(x: (int, float), y: (int, float), duration: (int, float) = 0.0, tween: callable = TimingFunction.liner) -> None:
        """
            将鼠标移动到（x, y）绝对位置。
            duration：持续时间。
            tween：移动轨迹。
        """
        pyautogui.moveTo(x=x, y=y, duration=duration, tween=tween)

    @staticmethod
    def move_to_rel(x: (int, float), y: (int, float), duration: (int, float) = 0.0, tween: callable = TimingFunction.liner) -> None:
        """
            将鼠标移动到（x, y）相对位置。
            duration：持续时间。
            tween：移动轨迹。
        """
        pyautogui.moveRel(x=x, y=y, duration=duration, tween=tween)

    @staticmethod
    def mouse_down():
        """ 按下鼠标（左键） """
        pyautogui.mouseDown()

    @staticmethod
    def mouse_up():
        """ 松开鼠标（左键） """
        pyautogui.mouseUp()

    @staticmethod
    def click():
        """ 当前位置进行单击（左键） """
        pyautogui.click()

    @staticmethod
    def left_click():
        """ 当前位置进行单击（左键） """
        pyautogui.leftClick()

    @staticmethod
    def middle_click():
        """ 当前位置进行单击（中键） """
        pyautogui.middleClick()

    @staticmethod
    def right_click():
        """ 当前位置进行单击（右键） """
        pyautogui.rightClick()

    @staticmethod
    def double_click(button="left"):
        """
            当前位置进行双击
            button：["left", "middle", "right", "primary", "secondary"]
                left：左键
                middle：中键
                right：右键
                primary：主键
                secondary: 辅键
        """
        pyautogui.doubleClick(button=button)

    @staticmethod
    def triple_click(button="left"):
        """
            当前位置进行三击
            button：["left", "middle", "right", "primary", "secondary"]
                left：左键
                middle：中键
                right：右键
                primary：主键
                secondary: 辅键
        """
        pyautogui.tripleClick(button=button)

    @staticmethod
    def drag_to(x: (int, float), y: (int, float), duration: (int, float) = 0.0, tween: callable = TimingFunction.liner, button="primary"):
        """
            触发当前button键，将鼠标移动到（x, y）绝对位置，随后释放按键。
            duration：持续时间。
            tween：移动轨迹。
            button：["left", "middle", "right", "primary", "secondary"]
                left：左键
                middle：中键
                right：右键
                primary：主键
                secondary: 辅键
        """
        pyautogui.dragTo(x=x, y=y, duration=duration, tween=tween, button=button)

    @staticmethod
    def drag_rel(x: (int, float), y: (int, float), duration: (int, float) = 0.0, tween: callable = TimingFunction.liner, button="primary"):
        """
            触发当前button键，将鼠标移动到（x, y）相对位置，随后释放按键。
            duration：持续时间。
            tween：移动轨迹。
            button：["left", "middle", "right", "primary", "secondary"]
                left：左键
                middle：中键
                right：右键
                primary：主键
                secondary: 辅键
        """
        pyautogui.dragRel(x=x, y=y, duration=duration, tween=tween, button=button)

    @staticmethod
    def scroll(clicks: int):
        """
            滚动鼠标滚轮
            clicks： 滚动次数。
                正数向上滚。
                负数向下滚
        """
        pyautogui.scroll(clicks)

    @staticmethod
    def key_down(key):
        """ 按下关键字，如ctrl、shift等 """
        pyautogui.keyDown(key)

    @staticmethod
    def key_up(key):
        """ 释放关键字，如ctrl、shift等 """
        pyautogui.keyUp(key)

    @staticmethod
    def press(keys: (str, list), presses: int = 1, interval: (int, float) = 0.0):
        """
            按下关键字，随后释放
            keys：要按下的键
                str：单键
                list：多键
            presses：重复几次
            interval：每次的时间间隔
        """
        pyautogui.press(keys, presses=presses, interval=interval)

    @staticmethod
    def hotkey(*args, **kwargs):
        """ 组合键，如 hotkey("ctrl", "a") """
        pyautogui.hotkey(*args, **kwargs)

    @staticmethod
    def typewrite(string: str, interval: (int, float) = 0.0):
        """
            输入字符串
            interval：各字符间输入间隔
        """
        pyautogui.typewrite(string, interval=interval)

    @staticmethod
    def get_size() -> Dict:
        """ 获取屏幕尺寸 """
        size = SystemOperation.size()
        return Dict(x=size.width, y=size.height)

    @staticmethod
    def get_mouse_position() -> Dict:
        """ 获取鼠标当前位置 """
        position = SystemOperation.mouse_position()
        return Dict(x=position.x, y=position.y)

