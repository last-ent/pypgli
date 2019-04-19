import psycopg2
import toml

USER_TABLES = """
SELECT table_name
FROM information_schema.tables
WHERE table_type = 'BASE TABLE'
AND table_name NOT LIKE 'pg_%'
AND table_name NOT LIKE 'sql_%'
"""

TABLE_COLUMNS_TEMPLATE = """
SELECT column_name, data_type
FROM information_schema.columns
WHERE table_name = '{}'
"""

class Query:
    query = ""
    args = []
    desc = ""

    def __init__(self, dct):
        self.__dict.__.update(dct)

class TableQuerySet:
    queries = {}
    table = None

    def __init__(self, table_name, queries):
        self.table = table_name
        self.__dict__.update(queries)
        self.queries = queries
