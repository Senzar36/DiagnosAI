from fastapi import params
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="KinCare"
)

cursor = connection.cursor()

class DatabaseConnector:
    def __init__(self):
        self.connection = connection
        self.cursor = cursor

    def execute_query(self, query, params=None):
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            return self.cursor.fetchall()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None
    
    def retrieve_data(self, query, params=None):
        try:
            self.cursor.execute(query, params)
            return self.cursor.fetchall()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None
    
    def close_connection(self):
        self.cursor.close()
        self.connection.close()