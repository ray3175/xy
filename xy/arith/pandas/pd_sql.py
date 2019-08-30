import pandasql     # pip install pandasql
from .tables import Tables


class PdSQL:
    __tables = Tables()
    __sql = lambda sql, table=__tables: pandasql.sqldf(sql, table)

    @classmethod
    def sql(cls, sql, name=None):
        pd = cls.__sql(sql)
        if name:
            cls.save_table(name, pd)
        return pd

    @classmethod
    def save_table(cls, name, pd):
        return cls.__tables.save_table(name, pd)




