import pytest
from xy.utils.time import Time


class Test_Time:
    def setup_class(self):
        self.__time_string = "2020-09-28 22:18:19"
        self.time = Time(self.__time_string)

    def teardown_class(self):
        pass

    def setup(self):
        pass

    def teardown(self):
        pass

    def test_to_time(self):
        obj_time = self.time.to_time()
        assert obj_time.tm_year == 2020
        assert obj_time.tm_mon == 9
        assert obj_time.tm_mday == 28
        assert obj_time.tm_hour == 22
        assert obj_time.tm_min == 18
        assert obj_time.tm_sec == 19

    def test_to_string(self):
        assert self.time.to_string() == self.__time_string
        assert str(self.time) == self.__time_string

    def test_to_time_stamp(self):
        time_stamp = self.time.to_time_stamp()
        assert time_stamp == 1601302699.0

    def test_to_datetime(self):
        obj_date_time = self.time.to_datetime()
        assert obj_date_time.year == 2020
        assert obj_date_time.month == 9
        assert obj_date_time.day == 28
        assert obj_date_time.hour == 22
        assert obj_date_time.minute == 18
        assert obj_date_time.second == 19

    def test_arithmetic_weeks(self):
        self.time.set_unit("weeks")
        time_add_1 = self.time + 1
        time_sub_1 = self.time - 1
        assert str(time_add_1) == "2020-10-05 22:18:19"
        assert str(time_sub_1) == "2020-09-21 22:18:19"

    def test_arithmetic_days(self):
        self.time.set_unit("days")
        time_add_1 = self.time + 1
        time_sub_1 = self.time - 1
        assert str(time_add_1) == "2020-09-29 22:18:19"
        assert str(time_sub_1) == "2020-09-27 22:18:19"

    def test_arithmetic_hours(self):
        self.time.set_unit("hours")
        time_add_1 = self.time + 1
        time_sub_1 = self.time - 1
        assert str(time_add_1) == "2020-09-28 23:18:19"
        assert str(time_sub_1) == "2020-09-28 21:18:19"

    def test_arithmetic_minutes(self):
        self.time.set_unit("minutes")
        time_add_1 = self.time + 1
        time_sub_1 = self.time - 1
        assert str(time_add_1) == "2020-09-28 22:19:19"
        assert str(time_sub_1) == "2020-09-28 22:17:19"

    def test_arithmetic_seconds(self):
        self.time.set_unit("seconds")
        time_add_1 = self.time + 1
        time_sub_1 = self.time - 1
        assert str(time_add_1) == "2020-09-28 22:18:20"
        assert str(time_sub_1) == "2020-09-28 22:18:18"


if __name__ == "__main__":
    pytest.main(["-v", "-s", "test_time.py"])


