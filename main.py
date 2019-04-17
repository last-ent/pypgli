import psycopg2

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

def get_connection():
    print("Starting pgsql connection.")
    conn = psycopg2.connect(database="mydb", user="ent", password="")
    return conn

def get_all_user_tables(cursor):
    print("Getting all User Tables.")
    cursor.execute(USER_TABLES)
    return cursor.fetchall()

def get_table_columns(cursor, table_name):
    print("Retrieving table columns")
    cursor.execute(TABLE_COLUMNS_TEMPLATE.format(table_name))
    return cursor.fetchall()

def compile():
    conn = get_connection()
    user_tables = get_all_user_tables(conn.cursor())

    tables = {}

    for utable in user_tables:
        table_name = utable[0]
        tables[table_name] = get_table_columns(conn.cursor(), table_name)
    return tables



