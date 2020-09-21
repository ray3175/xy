import pandasql     # pip install pandasql
from .tables import Tables


class PdSQL:
    def __init__(self):
        self.__tables = Tables()
        self.__sql = lambda sql, table=self.__tables: pandasql.sqldf(sql, table)

    def sql(self, sql, name=None):
        pd = self.__sql(sql)
        if name:
            self.save_table(name, pd)
        return pd

    def save_table(self, name, pd):
        return self.__tables.save_table(name, pd)




