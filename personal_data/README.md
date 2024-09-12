## Personal data

## Learning Objectives
### Examples of Personally Identifiable Information (PII)
Personally Identifiable Information (PII) refers to any data that can be used to identify a specific individual. Examples of PII include:

1. **Full Name**: First name, last name, and middle name.
2. **Social Security Number (SSN)** or other government-issued ID numbers.
3. **Email Addresses**.
4. **Phone Numbers**.
5. **Home or Office Address**.
6. **Date of Birth**.
7. **Bank Account Numbers** or Credit Card Details.
8. **Driver’s License Number**.
9. **Login Credentials**: Usernames, passwords, or any authentication information.

### How to Implement a Log Filter that Will Obfuscate PII Fields

Obfuscating PII in logs can prevent sensitive data exposure. Here's how to create a simple log filter in Python that can obfuscate PII fields like email addresses or credit card numbers:

1. Define a regex pattern to identify PII fields.
2. Replace the identified PII with a masked string.
3. Use a custom log filter.

Here's an example using Python's logging library:

```python
import logging
import re

class PiiFilter(logging.Filter):
    # Define regex patterns for PII fields
    EMAIL_REGEX = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    CREDIT_CARD_REGEX = r'\b(?:\d[ -]*?){13,16}\b'

    def filter(self, record):
        record.msg = re.sub(self.EMAIL_REGEX, '[EMAIL REDACTED]', record.msg)
        record.msg = re.sub(self.CREDIT_CARD_REGEX, '[CREDIT CARD REDACTED]', record.msg)
        return True

# Set up logging with the PII filter
logger = logging.getLogger('pii_logger')
logger.addFilter(PiiFilter())
logger.setLevel(logging.INFO)

# Example log message
logger.info('User email: john.doe@example.com, Credit Card: 1234 5678 9012 3456')
```

### How to Encrypt a Password and Check the Validity of an Input Password

To securely handle passwords, you should encrypt (hash) them using a strong hashing algorithm like bcrypt. Bcrypt is a popular choice because it automatically salts the passwords and is resistant to brute force attacks. Below is an example of how to use bcrypt for password hashing and validation:

1. **Install the bcrypt library**: `pip install bcrypt`.

2. **Password Hashing**:
```python
import bcrypt

def hash_password(plain_password: str) -> str:
    # Generate salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(plain_password.encode(), salt)
    return hashed_password.decode()

# Example usage
hashed_pw = hash_password('MySecurePassword')
print('Hashed Password:', hashed_pw)
```

3. **Password Validation**:
```python
def check_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode(), hashed_password.encode())

# Example usage
is_valid = check_password('MySecurePassword', hashed_pw)
print('Password is valid:', is_valid)
```

### How to Authenticate to a Database Using Environment Variables

Storing database credentials in your source code is a security risk. A better approach is to store credentials in environment variables and read them at runtime. Here's an example of how to authenticate to a PostgreSQL database using environment variables in Python.

1. **Set Environment Variables**:
   You can set environment variables in your shell or a `.env` file (using `python-dotenv`).
   Example `.env` file:
   ```
   DB_USER=your_username
   DB_PASSWORD=your_password
   DB_HOST=localhost
   DB_PORT=5432
   DB_NAME=your_database
   ```

2. **Load Environment Variables in Python**:
   Install the `python-dotenv` library: `pip install python-dotenv`.

   ```python
   import os
   from dotenv import load_dotenv
   import psycopg2

   # Load environment variables from the .env file
   load_dotenv()

   # Get database credentials from environment variables
   db_user = os.getenv('DB_USER')
   db_password = os.getenv('DB_PASSWORD')
   db_host = os.getenv('DB_HOST')
   db_port = os.getenv('DB_PORT')
   db_name = os.getenv('DB_NAME')

   # Connect to the PostgreSQL database
   connection = psycopg2.connect(
       user=db_user,
       password=db_password,
       host=db_host,
       port=db_port,
       database=db_name
   )

   # Example query
   cursor = connection.cursor()
   cursor.execute("SELECT version();")
   db_version = cursor.fetchone()
   print(f"Connected to {db_version}")

   # Close the connection
   cursor.close()
   connection.close()
   ```

This approach ensures that sensitive credentials are not exposed in your code and can be securely managed through environment variables.

Task 0:  Regex-ing
Write a function called filter_datum that returns the log message obfuscated:

Arguments:
fields: a list of strings representing all fields to obfuscate
redaction: a string representing by what the field will be obfuscated
message: a string representing the log line
separator: a string representing by which character is separating all fields in the log line (message)
The function should use a regex to replace occurrences of certain field values.
filter_datum should be less than 5 lines long and use re.sub to perform the substitution with a single regex.

```output
./main.py
name=egg;email=eggmin@eggsample.com;password=xxx;date_of_birth=xxx;
name=bob;email=bob@dylan.com;password=xxx;date_of_birth=xxx;
```

he re.sub() function in Python allows you to search for a pattern using a regular expression and replace it with a specified string. It’s a versatile way to perform substitutions, particularly useful for tasks like obfuscating sensitive data (such as PII) or manipulating strings based on specific patterns.

import re

re.sub(pattern, replacement, string, count=0, flags=0)


## Task 2  Create logger

Implement a get_logger function that takes no arguments and returns a logging.Logger object.

The logger should be named "user_data" and only log up to logging.INFO level. It should not propagate messages to other loggers. It should have a StreamHandler with RedactingFormatter as formatter.

Create a tuple PII_FIELDS constant at the root of the module containing the fields from user_data.csv that are considered PII. PII_FIELDS can contain only 5 fields - choose the right list of fields that can are considered as “important” PIIs or information that you must hide in your logs. Use it to parameterize the formatter.

```output
 ./main.py
<class 'logging.Logger'>
PII_FIELDS: 5
```

## Task 3 connect to database
Database credentials should NEVER be stored in code or checked into version control. One secure option is to store them as environment variable on the application server.

In this task, you will connect to a secure holberton database to read a users table. The database is protected by a username and password that are set as environment variables on the server named PERSONAL_DATA_DB_USERNAME (set the default as “root”), PERSONAL_DATA_DB_PASSWORD (set the default as an empty string) and PERSONAL_DATA_DB_HOST (set the default as “localhost”).

The database name is stored in PERSONAL_DATA_DB_NAME.

Implement a get_db function that returns a connector to the database (mysql.connector.connection.MySQLConnection object).

Use the os module to obtain credentials from the environment
Use the module mysql-connector-python to connect to the MySQL database (pip3 install mysql-connector-python)
