#!/usr/bin/env python3
"""
Regex
"""
import re
from typing import List



def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    '''
    Obfuscates values in the specified fields from the message.
    '''
    # Create a pattern based on the fields to be obfuscated
    for field in fields:
        # regex pattern to match until the next separator
        pattern = rf'{field}=[^{separator}]+'
        # Use re.sub()  with the redaction string

        message = re.sub(pattern, f'{field}={redaction}', message)

    return message
