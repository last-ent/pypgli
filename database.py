import psycopg2


class Database:
    connection = None

    def __init__(self, config):
        self.__config = config
        self.reset_connection()

    def get_new_cursor(self):
        return self.connection.cursor()

    def reset_connection(self):
        if self.connection:
            self.connection.close()
        self.connection = self.get_connection(
            self.__config.database,
            self.__config.user,
            self.__config.password
        )

    def execute(self, cursor, stmt):
        print("Executing... {}".format(stmt))
        cursor.execute(stmt)
        return cursor

    def get_connection(self, connection, auto_commit=False):
        print("Starting pgsql connection.")
        print(connection)
        conn = psycopg2.connect(
            database=connection.database,
            user=connection.user,
            password=connection.password
        )
        conn.autocommit = auto_commit
        return conn

    def get_all_user_tables(self, cursor):
        print("Getting all User Tables.")
        return self.execute(cursor, USER_TABLES).fetchall()

    def get_table_columns(self, cursor, table_name):
        print("Retrieving table columns")
        return self.execute(
            cursor, TABLE_COLUMNS_TEMPLATE.format(table_name)
        ).fetchall()

    def compile(self, auto_commit=False):
        conn = self.get_connection(self.__connection, auto_commit)
        user_tables = self.get_all_user_tables(conn.cursor())

        tables = {}

        for utable in user_tables:
            table_name = utable[0]
            tables[table_name] = self.get_table_columns(conn.cursor(), table_name)
        self.tables = tables

        return self

