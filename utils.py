import mysql.connector

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="MysqlPassword@123",
            database="EduSchema"
        )
        print("Database connection successful")
        return connection
    except mysql.connector.Error as err:
        print(f"Database connection error: {err}")
        return None
