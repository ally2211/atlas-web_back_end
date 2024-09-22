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


# Initialize the correct Auth class based on the AUTH_TYPE
if auth_type == 'basic_auth':
    auth = BasicAuth()  # Use BasicAuth if AUTH_TYPE is set to 'basic_auth'
    print("Using BasicAuth for authentication")
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
                      '/api/v1/unauthorized/', '/api/v1/forbidden/']

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
    if auth_header is None:
        # If the Authorization header is missing, trigger 401
        print("No authorization header, aborting with 401")
        abort(401)

    # Custom logic to check for specific Authorization header
    if auth_header is not None:
        print("Invalid authorization header, aborting with 403")
        abort(403)

    # Check for authenticated user
    user = auth.current_user(request)
    if user is None:
        # If no user is authenticated, trigger 401
        print("No user authenticated, aborting with 401")
        abort(401)

    if user is None:
        # Return 401 if user is not authenticated
        print("No user authenticated, aborting with 401")
        return abort(401)


# Example route for users
@app.route('/api/v1/users', methods=['GET'])
def get_users():
    return jsonify([])  # Empty list to simulate users


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
