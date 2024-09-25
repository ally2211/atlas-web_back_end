#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
from typing import Tuple
# Import the base Auth class
from api.v1.auth.auth import Auth
# Import the BasicAuth class
from api.v1.auth.basic_auth import BasicAuth  # Import the BasicAuth class

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


# Get the value of AUTH_TYPE environment variable
auth_type = getenv('AUTH_TYPE')
auth = BasicAuth()
from api.v1.auth.session_auth import SessionAuth


# Initialize the correct Auth class based on the AUTH_TYPE
if auth_type == 'basic_auth':
    auth = BasicAuth()  # Use BasicAuth if AUTH_TYPE is set to 'basic_auth'
    print("Using BasicAuth for authentication")
elif auth_type == 'session_auth':
    auth = SessionAuth()  # Use BasicAuth if AUTH_TYPE is set to 'basic_auth'
    print("Using SessionAuth for authentication")
else:
    auth = Auth()  # Default to using the Auth class
    print("Using Auth for authentication")


@app.before_request
def before_request_handler():
    """
    This method is called before every request.
    It can be used to check
    """

    print("Running before_request handler")
    # List of paths where no authorization is required
    excluded_paths = ['/api/v1/status/',
                      '/api/v1/unauthorized/',
                      '/api/v1/forbidden/',
                      '/api/v1/auth_session/login/']

    # Assign the result of current_user to request.current_user
    request.current_user = auth.current_user(request)

    # Normalize the request path to avoid trailing slash issues
    request_path = request.path.rstrip('/')

    if request.path in excluded_paths:
        # Do nothing, simply proceed with the request
        return None

    # Check if the path requires authentication
    if not auth.require_auth(request_path,
                             [path.rstrip('/') for path in excluded_paths]):
        # Path is excluded, no authentication required
        return None

    # Check for Authorization header
    auth_header = auth.authorization_header(request)
    cookie_header = auth.session_cookie(request)
    print(f"Authorization Header found: {auth_header} cookie header: {cookie_header}")  # Debugging
    if auth_header is None and cookie_header is None:
        # If the Authorization header is missing, trigger 401
        print("No authorization header, aborting with 401")
        abort(401)
        
    if cookie_header is None:
        abort(403) # Forbidden

    # If the header exists but is invalid (e.g., "Basic test"), return 403
    base64_credentials = auth.extract_base64_authorization_header(auth_header)
    if base64_credentials is None:
        print("Invalid Base64 in authorization header, aborting with 403")
        abort(403)  # Forbidden access

    # Check for authenticated user
    user = auth.current_user(request)
    if user is None:
        # If no user is authenticated, trigger 401
        print("No user authenticated, aborting with 401")
        abort(401)


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized_error(error) -> str:
    """
    Custom error handler for 401 Unauthorized
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden_error(error) -> str:
    """
    Custom error handler for 403 forbidden
    """
    return jsonify({"error": "Forbidden"}), 403


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
    debug=True
