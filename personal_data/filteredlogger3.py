#!/usr/bin/env python3
"""
connection to sql database
"""
import os
import mysql.connector
from mysql.connector import MySQLConnection, Error


def get_db() -> mysql.connector.connection.MySQLConnection:
    '''
    establish mysql connection using environment variables
    '''
    # Fetching environment variables with defaults if not set
    db_user: str = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    db_password: str = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    db_host: str = os.getenv('PERSONAL_DATA_DB_HOST', 'host.docker.internal')
    db_name: str = os.getenv('PERSONAL_DATA_DB_NAME', 'my_db')

    try:
        # Establish connection
        connection: MySQLConnection = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name
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
