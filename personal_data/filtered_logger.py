#!/usr/bin/env python3
"""
connection to sql database
"""
import mysql.connector
from mysql.connector import Error


def get_db():
    try:
        # Establish connection
        connection = mysql.connector.connect(
            host='host.docker.internal',  # MySQL is running on Docker, accessible via localhost
            user='root',       # Replace with your MySQL username
            password='',       # Replace with your MySQL password, empty string in your case
            database='my_db'   # Replace with the actual database name
        )
        if connection.is_connected():
            # print("Connected to MySQL database")
            return connection
        else:
            print("Failed to connect to MySQL database")
            return None
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None
