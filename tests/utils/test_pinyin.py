import pytest
from xy.utils.pinyin import PinYin
from xy.utils.pinyin.single_dictionary import active as single_active
from xy.utils.pinyin.phrases_dictionary import active as phrases_active


class Test_PinYin:
    def setup_class(self):
        single_active()
        phrases_active()
        self.pinyin0 = PinYin("爷")
        self.pinyin1 = PinYin("睿爷")
        self.pinyin2 = PinYin("睿睿爷")
        self.pinyin3 = PinYin("睿睿睿爷")

    def teardown_class(self):
        pass

    def setup(self):
        pass

    def teardown(self):
        pass

    def test_get_origin_bopomofo_array(self):
        assert self.pinyin0.get_origin_bopomofo_array() == [["ye"]]
        assert self.pinyin1.get_origin_bopomofo_array() == [["rui", "ray"], ["ye"]]
        assert self.pinyin2.get_origin_bopomofo_array() == [["rui", "ray"], ["rui", "ray"], ["ye"]]
        assert self.pinyin3.get_origin_bopomofo_array() == [["rui", "ray"], ["rui", "ray"], ["rui", "ray"], ["ye"]]
        assert self.pinyin0.get_origin_bopomofo_array(heteronym=False) == [["ye"]]
        assert self.pinyin1.get_origin_bopomofo_array(heteronym=False) == [["rui"], ["ye"]]
        assert self.pinyin2.get_origin_bopomofo_array(heteronym=False) == [["rui"], ["rui"], ["ye"]]
        assert self.pinyin3.get_origin_bopomofo_array(heteronym=False) == [["rui"], ["rui"], ["rui"], ["ye"]]

    def test_get_origin_logogram_array(self):
        assert self.pinyin0.get_origin_logogram_array() == [["y"]]
        assert self.pinyin1.get_origin_logogram_array() == [["r"], ["y"]]
        assert self.pinyin2.get_origin_logogram_array() == [["r"], ["r"], ["y"]]
        assert self.pinyin3.get_origin_logogram_array() == [["r"], ["r"], ["r"], ["y"]]
        assert self.pinyin0.get_origin_logogram_array(heteronym=False) == [["y"]]
        assert self.pinyin1.get_origin_logogram_array(heteronym=False) == [["r"], ["y"]]
        assert self.pinyin2.get_origin_logogram_array(heteronym=False) == [["r"], ["r"], ["y"]]
        assert self.pinyin3.get_origin_logogram_array(heteronym=False) == [["r"], ["r"], ["r"], ["y"]]

    def test_to_bopomofo_array(self):
        assert self.pinyin0.to_bopomofo_array() == [["ye"]]
        assert self.pinyin1.to_bopomofo_array() == [["rui", "ye"], ["ray", "ye"]]
        assert self.pinyin2.to_bopomofo_array() == [["rui", "rui", "ye"], ["ray", "rui", "ye"], ["rui", "ray", "ye"], ["ray", "ray", "ye"]]
        assert self.pinyin3.to_bopomofo_array() == [["rui", "rui", "rui", "ye"], ["ray", "rui", "rui", "ye"], ["rui", "ray", "rui", "ye"], ["ray", "ray", "rui", "ye"], ["rui", "rui", "ray", "ye"], ["ray", "rui", "ray", "ye"], ["rui", "ray", "ray", "ye"], ["ray", "ray", "ray", "ye"]]
        assert self.pinyin0.to_bopomofo_array(heteronym=False) == [["ye"]]
        assert self.pinyin1.to_bopomofo_array(heteronym=False) == [["rui", "ye"]]
        assert self.pinyin2.to_bopomofo_array(heteronym=False) == [["rui", "rui", "ye"]]
        assert self.pinyin3.to_bopomofo_array(heteronym=False) == [["rui", "rui", "rui", "ye"]]

    def test_to_logogram_array(self):
        assert self.pinyin0.to_logogram_array() == [["y"]]
        assert self.pinyin1.to_logogram_array() == [["r", "y"]]
        assert self.pinyin2.to_logogram_array() == [["r", "r", "y"]]
        assert self.pinyin3.to_logogram_array() == [["r", "r", "r", "y"]]
        assert self.pinyin0.to_logogram_array(heteronym=False) == [["y"]]
        assert self.pinyin1.to_logogram_array(heteronym=False) == [["r", "y"]]
        assert self.pinyin2.to_logogram_array(heteronym=False) == [["r", "r", "y"]]
        assert self.pinyin3.to_logogram_array(heteronym=False) == [["r", "r", "r", "y"]]


if __name__ == "__main__":
    pytest.main(["-v", "-s", "test_pinyin.py"])


