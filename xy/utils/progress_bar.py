class ProgressBar:
    """
    进度条小工具！
    """
    def __init__(self, rate=20, read_symbol="*", unread_symbol="-"):
        self.__rate = rate
        self.__read_symbol = read_symbol
        self.__unread_symbol = unread_symbol

    def update(self, data):
        if 0 <= data <= 100:
            num = int(data * self.__rate / 100)
            read = self.__read_symbol * num
            unread = self.__unread_symbol * (self.__rate - num)
            _data = str(data).rjust(3, " ")
            print(f"\r{read}{unread} {_data}%", end="" if data != 100 else "\n")
        else:
            print(f"{self.__read_symbol * self.__rate} 100%")

