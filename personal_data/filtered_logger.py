#!/usr/bin/env python3
"""
connection to sql database
"""
import mysql.connector
from mysql.connector import MySQLConnection, Error
from typing import Optional


def get_db() -> mysql.connector.connection.MySQLConnection:
    try:
        # Establish connection
        connection: MySQLConnection = mysql.connector.connect(
            host='localhost', # 'host.docker.internal'
            user='root',
            password='',
            database='my_db'
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
