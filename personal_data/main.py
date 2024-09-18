#!/usr/bin/env python3
"""
Main file
"""
import logging
import re

RedactingFormatter = __import__('filtered_logger').RedactingFormatter

get_logger = __import__('filtered_logger').get_logger
PII_FIELDS = __import__('filtered_logger').PII_FIELDS

get_db = __import__('filtered_logger').get_db

# Logger instance
logger = get_logger()
db = get_db()
cursor = db.cursor()
cursor.execute("SELECT name, email, phone, ssn, password, ip, last_login, user_agent FROM users;")
rows = cursor.fetchall()
for row in rows:
    name, email, phone, ssn, password, ip, last_login, user_agent = row
    # Create the message in "name=value;..." format
    msg = f"name={name};email={email};phone={phone};ssn={ssn};password={password};ip{ip};last_login{last_login};user_agent{user_agent}"
    # Log the message using logger.info (RedactingFormatter will redact sensitive info)
    
    # Create a LogRecord with the message
    log_record = logging.LogRecord("user_data", logging.INFO, None, None, msg, None, None)

    # Print the formatted and redacted log output
    print(logger.handlers[0].formatter.format(log_record))
    
    # logger.info(msg)
    # logger.info(f"[HOLBERTON]{row}")
cursor.close()
db.close()
