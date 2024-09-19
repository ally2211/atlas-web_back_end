#!/usr/bin/env python3
"""
Regex
"""
import re
from typing import List
import logging


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
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
