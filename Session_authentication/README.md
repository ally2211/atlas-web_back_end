# Simple API

Simple HTTP API for playing with `User` model.


## Files

### `models/`

- `base.py`: base of all models of the API - handle serialization to file
- `user.py`: user model

### `api/v1`

- `app.py`: entry point of the API
- `views/index.py`: basic endpoints of the API: `/status` and `/stats`
- `views/users.py`: all users endpoints


## Setup

```
$ pip3 install -r requirements.txt
```


## Run

```
$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
```


## Routes

- `GET /api/v1/status`: returns the status of the API
- `GET /api/v1/stats`: returns some stats of the API
- `GET /api/v1/users`: returns the list of users
- `GET /api/v1/users/:id`: returns an user based on the ID
- `DELETE /api/v1/users/:id`: deletes an user based on the ID
- `POST /api/v1/users`: creates a new user (JSON parameters: `email`, `password`, `last_name` (optional) and `first_name` (optional))
- `PUT /api/v1/users/:id`: updates an user based on the ID (JSON parameters: `last_name` and `first_name`)
Here’s an overview of authentication, session authentication, and cookies, along with how to send and parse cookies.

### 1. What Authentication Means:
**Authentication** is the process of verifying the identity of a user or system before allowing access to resources. It typically involves checking credentials (such as a username and password) against a stored value to ensure that the entity accessing the system is who they claim to be.

#### Common Authentication Methods:
- **Password-based authentication**: Users provide a password to prove their identity.
- **Token-based authentication**: Users authenticate and receive a token (like a JWT), which is used in subsequent requests.
- **Multi-factor authentication (MFA)**: Combines multiple methods (like a password and a mobile phone code) for stronger security.

### 2. What Session Authentication Means:
**Session authentication** is a method where, after a user successfully logs in, a session is created on the server. The session holds information about the user’s authenticated state, such as their user ID. Instead of sending credentials with every request, the session ID is sent, which identifies the user on the server.

#### Key Characteristics:
- **Session ID**: Once authenticated, the server assigns a unique session ID, usually stored in a cookie. The session ID is sent with every subsequent request to validate the user.
- **Server-side session storage**: The session data is stored on the server (in memory, database, or file) with a unique session ID that the client sends back in each request.
  
### 3. What Cookies Are:
**Cookies** are small pieces of data that a server sends to a user's browser. The browser stores them and sends them back with every subsequent request to the same server. Cookies can store session information, preferences, or even tracking data.

#### Characteristics of Cookies:
- **Stored on the client**: Cookies are stored in the browser and are sent automatically with every request to the server that set them.
- **Key-value pairs**: Cookies are usually stored as key-value pairs.
- **Attributes**: Cookies can have attributes like expiration time (`Expires`), security (`Secure`, `HttpOnly`), or scope (`Domain`, `Path`).

### 4. How to Send Cookies:
Cookies are sent from the server to the client using the `Set-Cookie` header in the HTTP response. The browser then stores the cookie and sends it with every request to the server.

#### Example of Sending Cookies:
In a Python Flask app:

```python
from flask import Flask, make_response

app = Flask(__name__)

@app.route('/set_cookie')
def set_cookie():
    response = make_response("Cookie is set")
    response.set_cookie('session_id', 'abc123', max_age=3600)  # max_age is the lifetime of the cookie in seconds
    return response

if __name__ == '__main__':
    app.run(debug=True)
```

- `Set-Cookie: session_id=abc123; Max-Age=3600` will be sent in the response.
- The browser will store this cookie and send it with every subsequent request to the same domain.

### 5. How to Parse Cookies:
When the browser sends cookies back to the server, they are sent in the `Cookie` header of the HTTP request. On the server side, cookies can be parsed by extracting them from this header.

#### Example of Parsing Cookies:
In Python Flask:

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/get_cookie')
def get_cookie():
    session_id = request.cookies.get('session_id')  # Extract the session_id cookie
    return f'Session ID is: {session_id}'

if __name__ == '__main__':
    app.run(debug=True)
```

Here, `request.cookies.get('session_id')` retrieves the value of the `session_id` cookie sent by the client.

### Summary:
1. **Authentication** is the process of verifying identity using credentials.
2. **Session authentication** uses server-side sessions to manage user authentication, with session IDs stored in cookies.
3. **Cookies** are small pieces of data stored in the browser and sent with every request to the server, often used to maintain session information.
4. **To send cookies**, the server uses the `Set-Cookie` header, which the client stores and sends back in the `Cookie` header.
5. **To parse cookies**, the server extracts the cookie value from the incoming request’s `Cookie` header.
