import mysql.connector

class Database:
    connection = None
    def __init__(self):
        pass

    @staticmethod
    def connect():
        try:
            if Database.connection is None:
                Database.connection = mysql.connector.connect(user='root', password='',
                                                host='localhost',
                                                port=3309,
                                                database='iti-python-lab3',)
                Database.create_emp_table()
        except Exception as err:
            print(err)
        return Database.connection


   
    @staticmethod
    def create_emp_table():
        try:
            cursor = Database.connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS employees (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    first_name VARCHAR(50),
                    last_name VARCHAR(50),
                    age INT,
                    department VARCHAR(50),
                    salary DECIMAL(10, 2),
                    managed_department VARCHAR(50)
                )
            """)
        except Exception as err:
            print(err)
        finally:
            cursor.close()

    @staticmethod
    def close():
        Database.connection.close()