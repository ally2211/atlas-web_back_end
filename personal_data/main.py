#!/usr/bin/env python3
"""
Main file
"""

import logging
import re

RedactingFormatter = __import__('filtered_logger').RedactingFormatter

message = "name=Bob;email=bob@dylan.com;ssn=000-123-0000;password=bobby2019;"
log_record = logging.LogRecord("my_logger", logging.INFO, None, None, message, None, None)
formatter = RedactingFormatter(fields=("email", "ssn", "password"))
print(formatter.format(log_record))


redaction = "bbbbbb"
separator = "&"
fields1 = ["password", "ssn", "phone"]
message1 = "name=User&password=password&email=user@example.com&ssn=12345&phone=411&"
s1 = "name=User&password=bbbbbb&email=user@example.com&ssn=bbbbbb&phone=bbbbbb&"
print(formatter.format(log_record))