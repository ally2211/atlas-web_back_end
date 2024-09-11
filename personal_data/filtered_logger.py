#!/usr/bin/env python3
"""
Regex
"""
import re


def filter_datum(fields: list, redaction: str, message: str,
                 separator: str) -> str:
    '''
    Obfuscates values in the specified fields from the message.
    '''    # Create a pattern based on the fields to be obfuscated
    for field in fields:
        # Construct the regex pattern for the field to match everything after the key until the next separator
        pattern = rf'{field}=[^;]+'
        # Use re.sub() to replace the matched field's value with the redaction string
        message = re.sub(pattern, f'{field}={redaction}', message)

    return message

