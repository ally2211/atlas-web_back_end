#!/usr/bin/env python3
"""
connection to sql database
"""
import os
import mysql.connector
from mysql.connector import MySQLConnection, Error
import re
from typing import List, Tuple
import logging

# Define the PII_FIELDS constant at the root of the module
PII_FIELDS: Tuple[str, ...] = ('name', 'email', 'phone', 'ssn', 'password')

class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class
    """
    REDACTION = "***"
    # FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)s: %(message)s"
    SEPARATOR = ";"

    def __init__(self,  fields: List[str]):
        """
        Initialize the RedactingFormatter
        with a list of fields to be redacted.
        """
        # Initialize the parent class with the specific format
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the log record and redact sensitive fields.

        :param record: The log record to format.
        :return: The formatted log message with sensitive fields redacted.
        """
        # Get the original log message
        original_message = super().format(record)
        # Redact sensitive fields
        redacted_message = self.filter_datum(original_message)
        return redacted_message

    def filter_datum(self, message: str) -> str:
        '''
        Obfuscates values in the specified fields from the message.
        :param message: The original log message.
        :return: The message with the specified fields' values obfuscated.
        '''
        # Create a pattern based on the fields to be obfuscated
        for field in self.fields:
            # regex pattern to match until the next separator
            pattern = rf'{field}=[^{RedactingFormatter.SEPARATOR}]+'
            
            # Use re.sub()  with the redaction string
            message = re.sub(
                pattern,
                f'{field}={RedactingFormatter.REDACTION}',
                message
            )
        # Remove any trailing separator
        if message.endswith(RedactingFormatter.SEPARATOR):
            message = message[:-len(RedactingFormatter.SEPARATOR)]
        return message

def get_logger() -> logging.Logger:
    """
    Create and return a logger named 'user_data' that logs up to INFO level.
    It uses RedactingFormatter to redact PII fields in the logs.

    :return: The configured logger object.
    """
    # Create a logger named 'user_data'
    logger = logging.getLogger('user_data')

    # Set the log level to INFO
    logger.setLevel(logging.INFO)

    # Ensure the logger does not propagate messages to other loggers
    logger.propagate = False

    # Create a StreamHandler
    stream_handler = logging.StreamHandler()

    # Set the formatter to RedactingFormatter using the PII_FIELDS
    formatter = RedactingFormatter(fields=list(PII_FIELDS))
    stream_handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(stream_handler)
    logger.setLevel(logging.INFO)
    # Set log level to INFO
    return logger

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
