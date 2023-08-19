import pyodbc
from pyodbc import Error

class DatabaseManager:
    DRIVER = "{SQL SERVER}"
    SERVER = "localhost"
    DATABASE = "dbLake"
    conn = None

    @classmethod
    def get_connection(cls) -> pyodbc.Connection:
        if not cls.conn:
            connection_string = f"DRIVER={cls.DRIVER};SERVER={cls.SERVER};DATABASE={cls.DATABASE};TRUSTED_CONNECTION=yes;"
            cls.conn = pyodbc.connect(connection_string, encoding="utf-8")
        return cls.conn
    
    @classmethod
    def get_cursor(cls) -> pyodbc.Cursor:
        return cls.get_connection().cursor()
    
    @classmethod
    def check_database_exists(cls) -> bool:
        try:
            connection_string = f"DRIVER={cls.DRIVER};SERVER={cls.SERVER};DATABASE={cls.DATABASE};TRUSTED_CONNECTION=yes;"
            conn = pyodbc.connect(connection_string, encoding="utf-8", autocommit=True)
            conn.close()
            return True
        except:
            return False
        
    @classmethod
    def create_database(cls):
        connection_string = f"DRIVER={cls.DRIVER};SERVER={cls.SERVER};TRUSTED_CONNECTION=yes;"
        conn = pyodbc.connect(connection_string, encoding="utf-8", autocommit=True)
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE dbLake COLLATE Persian_100_CI_AI")
        with open("queries.sql") as sql_file:
            commands = sql_file.read().split("GO")
            for command in commands:
                cursor.execute(command)
        cursor.commit()
        conn.close()