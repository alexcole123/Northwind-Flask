from mysql.connector import connect  # pip install mysql-connector-python
from .app_config import AppConfig

# Data Access Layer - performs actions directly in the database:
class DAL:

    # Constructor (ctor) - create connection:
    def __init__(self):
        self.connection = connect(
            host=AppConfig.mysql_host, 
            user=AppConfig.mysql_user,
            password=AppConfig.mysql_password,
            database=AppConfig.mysql_database)
    
    # Get entire table:
    def get_table(self, sql, params=None):
        with self.connection.cursor(dictionary=True) as cursor:
            cursor.execute(sql, params)
            table = cursor.fetchall()
            return table

    # Get single value:
    def get_scalar(self, sql, params=None):
        with self.connection.cursor(dictionary=True) as cursor:
            cursor.execute(sql, params)
            scalar = cursor.fetchone()
            return scalar

    # Insert row:
    def insert(self, sql, params=None):
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            self.connection.commit() # Save to database now.
            last_row_id = cursor.lastrowid
            return last_row_id

    # Update row:
    def update(self, sql, params=None):
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            self.connection.commit() # Save to database now.
            row_count = cursor.rowcount
            return row_count

    # Delete row:
    def delete(self, sql, params=None):
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            self.connection.commit() # Save to database now.
            row_count = cursor.rowcount
            return row_count

    # Close connection:
    def close(self):
        self.connection.close()
