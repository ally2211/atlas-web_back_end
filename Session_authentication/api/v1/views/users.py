#!/usr/bin/env python3
""" Module of Users views
"""
from api.v1 import app
from api.v1.auth.basic_auth import BasicAuth
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
from os import getenv
auth_type = getenv('AUTH_TYPE')


@app_views.route('/users/me', methods=['GET'])
def get_current_user():
    """
    Retrieve the authenticated user object.
    """
    print("Starting /users/me route")  # Debugging
    # Get the authenticated user
    if (auth_type == 'session_auth'):
        # Retrieve the session ID from the session cookie
        print("getusercurrent session")
        session_id = auth.session_cookie(request)
    
        if session_id is None:
            abort(401, description="Unauthorized")  # No session ID, return 401 Unauthorized
        
        # Retrieve the user ID associated with the session ID
        user_id = auth.user_id_for_session_id(session_id)
        
        if user_id is None:
            abort(403, description="Forbidden")  # No user associated with this session, return 403 Forbidden
        
        # Retrieve the user details from the user_id (assuming there's a User model to retrieve user data)
        user = User.get_user_by_id(user_id)  # Implement this logic in your User model
        
        if user is None:
            abort(403, description="Forbidden")  # User not found, return 403 Forbidden
        
        # Return user information
        return jsonify({
            "user_id": user.id,
            "email": user.email,
            "name": user.name
        })
        
    else:
        # Initialize the BasicAuth instance
        auth = BasicAuth()
        user = auth.current_user(request)
        if user is None:
            print("No authenticated user found")  # Debugging
            abort(401)
            
        print(f"Authenticated user: {user.email}, ID: {user.id}")
        # Return user information
        return jsonify({
            'email': user.email,
            'password': user.password,
            'id': user.id
        })

@app_views.route('/users', methods=['GET'], strict_slashes=False)
def view_all_users() -> str:
    """ GET /api/v1/users
    Return:
      - list of all User objects JSON represented
    """
    all_users = [user.to_json() for user in User.all()]
    return jsonify(all_users)


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def view_one_user(user_id: str = None) -> str:
    """ GET /api/v1/users/:id
    Path parameter:
      - User ID
    Return:
      - User object JSON represented
      - 404 if the User ID doesn't exist
    """
    if user_id is None:
        abort(404)
    user = User.get(user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_json())


@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id: str = None) -> str:
    """ DELETE /api/v1/users/:id
    Path parameter:
      - User ID
    Return:
      - empty JSON is the User has been correctly deleted
      - 404 if the User ID doesn't exist
    """
    if user_id is None:
        abort(404)
    user = User.get(user_id)
    if user is None:
        abort(404)
    user.remove()
    return jsonify({}), 200


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user() -> str:
    """ POST /api/v1/users/
    JSON body:
      - email
      - password
      - last_name (optional)
      - first_name (optional)
    Return:
      - User object JSON represented
      - 400 if can't create the new User
    """
    rj = None
    error_msg = None
    try:
        rj = request.get_json()
    except Exception as e:
        rj = None
    if rj is None:
        error_msg = "Wrong format"
    if error_msg is None and rj.get("email", "") == "":
        error_msg = "email missing"
    if error_msg is None and rj.get("password", "") == "":
        error_msg = "password missing"
    if error_msg is None:
        try:
            user = User()
            user.email = rj.get("email")
            user.password = rj.get("password")
            user.first_name = rj.get("first_name")
            user.last_name = rj.get("last_name")
            user.save()
            return jsonify(user.to_json()), 201
        except Exception as e:
            error_msg = "Can't create User: {}".format(e)
    return jsonify({'error': error_msg}), 400


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_user(user_id: str = None) -> str:
    """ PUT /api/v1/users/:id
    Path parameter:
      - User ID
    JSON body:
      - last_name (optional)
      - first_name (optional)
    Return:
      - User object JSON represented
      - 404 if the User ID doesn't exist
      - 400 if can't update the User
    """
    # If user_id is 'me'
    # and there's no authenticated user, return 404
    if user_id == 'me':
        if request.current_user is None:
            abort(404)
        else:
            # Return the authenticated user's
            # information
            return jsonify({
                'id': request.current_user.id,
                'email': request.current_user.email,
                'password': request.current_user_password
            })
            
    if user_id is None:
        abort(404)
    user = User.get(user_id)
    if user is None:
        abort(404)
    rj = None
    try:
        rj = request.get_json()
    except Exception as e:
        rj = None
    if rj is None:
        return jsonify({'error': "Wrong format"}), 400
    if rj.get('first_name') is not None:
        user.first_name = rj.get('first_name')
    if rj.get('last_name') is not None:
        user.last_name = rj.get('last_name')
    user.save()
    return jsonify(user.to_json()), 200
