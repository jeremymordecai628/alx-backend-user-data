#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, abort
from api.v1.views import app_views
import requests

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """ GET /api/v1/status
    Return:
      - the status of the API
    """
    return jsonify({"status": "OK"})

@app_views.route('/stats/', strict_slashes=False)
def stats() -> str:
    """ GET /api/v1/stats
    Return:
      - the number of each objects
    """
    from models.user import User
    stats = {}
    stats['users'] = User.count()
    return jsonify(stats)

@app_views.route('/unauthorized', methods=['GET'], strict_slashes=False)
def unauthorized() -> None:
    """ GET /api/v1/unauthorized
    Triggers a 401 Unauthorized error
    """
    abort(401)

@app_views.route('/forbidden', methods=['GET'], strict_slashes=False)
def forbidden() ->None:
    """Get /api/v1/forbidden
    Triggers a 403 forbidden error
    """
    abort(403) 

@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """ Retrieves a user by ID or 
    
    'me' for authenticated user """
    if user_id == "me":
        if not request.current_user:
            abort(404)
        return jsonify(request.current_user.to_dict())
    user = User.get(user_id)
    if not user:
        abort(404)
    return jsonify(user.to_dict())