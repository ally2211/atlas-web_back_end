#!/usr/bin/env python3
"""
Regex
"""
import re


def myfilter_datum(fields: list, redaction: str, message: str,
                 separator: str) -> str:
    '''
    Obfuscates values in the specified fields from the message.
    '''
    # split the message
    key_value_pairs = message.split(separator)

    # init empty list
    obfuscated_pairs = []

    # itirate over each key-value pair
    for pair in key_value_pairs:
        # split each pair into key and value
        if '=' in pair:
            # '1' ensures we split only at the first '='
            key, value = pair.split('=', 1)
        
            if key in fields:
                obfuscated_pairs.append(f"{key}={redaction}")
            else:
                obfuscated_pairs.append(pair)

    # join pairs back to a single string
    return separator.join(obfuscated_pairs)
