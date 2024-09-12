#!/usr/bin/env python3
"""
Main file
"""

filter_datum = __import__('filtered_logger').filter_datum

fields = ["password", "date_of_birth"]
messages = ["name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/1986;", "name=bob;email=bob@dylan.com;password=bobbycool;date_of_birth=03/04/1993;"]

for message in messages:
    print(filter_datum(fields, 'xxx', message, ';'))

redaction = "bbbbbb"
separator = "&"
fields1 = ["password", "ssn", "phone"]
message1 = "name=User&password=password&email=user@example.com&ssn=12345&phone=411&"
s1 = "name=User&password=bbbbbb&email=user@example.com&ssn=bbbbbb&phone=bbbbbb&"
print(filter_datum(fields1, redaction, message1, separator))
print("filter_datum worked as expected: {}".format(filter_datum(fields1, redaction, message1, separator) == s1))
