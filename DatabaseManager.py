import pyodbc

class DatabaseManager:
    DRIVER = "{SQL SERVER}"
    SERVER = "localhost"
    DATABASE = "dbLake"
    conn = None

    @classmethod
    def get_connection(cls):
        if not cls.conn:
            connection_string = f"DRIVER={cls.DRIVER};SERVER={cls.SERVER};DATABASE={cls.DATABASE};TRUSTED_CONNECTION=yes;"
            cls.conn = pyodbc.connect(connection_string, encoding="utf-8")
        return cls.conn
    
    @classmethod
    def get_cursor(cls):
        return cls.get_connection().cursor()