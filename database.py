import psycopg2

class Database:
    def __init__(self, config):
        self.__config = config
        self.reset_connection()

    def get_new_cursor(self):
        return self.connection.cursor()

    def reset_connection(self):
        self.connection = self.get_connection(
            self.__config.database,
            self.__config.user,
            self.__config.password
        )

    def execute(self, cursor, stmt):
        print("Executing... {}".format(stmt))
        cursor.execute(stmt)
        return cursor

    def get_connection(self, database, user, password):
        print("Starting pgsql connection.")
        print(database, user, password)
        return psycopg2.connect(database=database, user=user, password=password)

    def get_all_user_tables(self, cursor):
        print("Getting all User Tables.")
        return self.execute(cursor, USER_TABLES).fetchall()

    def get_table_columns(self, cursor, table_name):
        print("Retrieving table columns")
        return self.execute(
            cursor, TABLE_COLUMNS_TEMPLATE.format(table_name)
        ).fetchall()

    def compile(self):
        conn = get_connection()
        user_tables = get_all_user_tables(conn.cursor())

        tables = {}

        for utable in user_tables:
            table_name = utable[0]
            tables[table_name] = get_table_columns(conn.cursor(), table_name)
        return tables

