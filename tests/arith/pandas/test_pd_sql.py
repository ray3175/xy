import pytest
import pandas
from xy.arith.pandas.pd_sql import PdSQL


class Test_PdSQL:
    def setup_class(self):
        self.pd_sql = PdSQL()
        columns = ["a", "b", "c"]
        values = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.pd_sql.save_table("test_pd_sql", pandas.DataFrame(values, columns=columns))

    def teardown_class(self):
        pass

    def setup(self):
        pass

    def teardown(self):
        pass

    def test_sql(self):
        new_table = self.pd_sql.sql("select a from test_pd_sql where c in (3, 9)", "new_test_pd_sql")
        select_new_table = self.pd_sql.sql("select * from new_test_pd_sql")
        assert select_new_table.equals(new_table) is True


if __name__ == "__main__":
    pytest.main(["-v", "-s", "test_pd_sql.py"])


