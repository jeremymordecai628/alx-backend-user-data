#!/usr/bin/env python3
"""
Route module for the API

This module defines the core API routing and configuration for the Flask application.
It handles:
    - Importing required modules
    - Flask app initialization
    - Blueprint registration (`app_views`) for API endpoints
    - CORS configuration
    - Authentication integration
    - Custom error handling for specific HTTP status codes
"""

from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
from api.v1.auth.auth import Auth
from api.v1.auth.basic_auth import BasicAuth
import os

# Create a Flask app instance
app = Flask(__name__)

# Register the API blueprint
app.register_blueprint(app_views)

# Enable CORS for the API routes
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

# Create an authentication instance
if os.getenv('AUTH_TYPE')== 'basic_auth' :
    auth =BasicAuth
else :
    auth =Auth

# Custom error handler for 401 Unauthorized
@app.errorhandler(401)
def unauthorized(error):
    """Handles 401 Unauthorized errors."""
    return jsonify({"error": "Unauthorized"}), 401

# Custom error handler for 403 Forbidden
@app.errorhandler(403)
def forbidden_error(error):
    """Handles 403 Forbidden errors."""
    return jsonify({"error": "Forbidden"})

# Before request hook for authentication and authorization
@app.before_request
def before_request():
    # Check if authentication is enabled
    if auth is None:
        return

    # Define excluded paths that don't require authentication
    excluded_paths = ['/api/v1/status/', '/api/v1/unauthorized/', '/api/v1/forbidden/']

    # Check if the current path is excluded
    if not auth.require_auth(request.path, excluded_paths):
        return

    # Check for authorization header
    if auth.authorization_header(request) is None:
        abort(401)  # Unauthorized

    # Check if the current user is authenticated
    if auth.current_user(request) is None:
        abort(403)  # Forbidden
    #Before request handler
    if auth :
        request.current_user = auth.current_user(request)

# Run the Flask app
if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)