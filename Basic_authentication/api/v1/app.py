#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os
from typing import Tuple


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None

if auth:
    from api.v1.auth.auth import Auth
    auth = Auth()

@app.before_request
def before_request_handler():
    """
    This method is called before every request. It can be used to check
    if the request should be processed, for example, by verifying authorization.
    """

    
    if auth is None:
        return None
    
    # List of paths where no action is required
    excluded_paths = ['/api/v1/status/', '/api/v1/unauthorized/', '/api/v1/forbidden/']
    if request.path in excluded_paths:
        # Do nothing, simply proceed with the request
        return None

    if not auth.require_auth(request.path, excluded_paths):
        return None  # No authentication required, proceed with the request

    # Example: Retrieve the Authorization header
    auth_header = auth.authorization_header(request)
    if auth_header is None:
        # Return 401 Unauthorized if missing
        return abort(401)

    # Example logic for verifying the user (current_user method can be implemented in Auth)
    user = auth.current_user(request)
    if user is None:
        # Return 401 if user is not authenticated
        return abort(401)


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
