from flask import Blueprint, request, jsonify
from flasgger import swag_from

from lwca.handlers.auth_handler import handle_login_user, handle_register_user, handle_jwt_refresh

blueprint = Blueprint('auth', __name__)

@blueprint.route('/api/v1/auth/login', methods=['POST'])
def login():
    """
    Login endpoint
    ---
    tags:
      - Authentication
    description: |
      Allows a user to log in using their username and password.
      Generates a JWT token for the user upon successful authentication.
    parameters:
      - in: body
        name: credentials
        description: User login credentials
        required: true
        schema:
          type: object
          properties:
            username:
              type: string
              example: johndoe
            password:
              type: string
              example: password123
    responses:
      200:
        description: Authentication successful. Returns a JWT token.
        schema:
          type: object
          properties:
            access_token:
              type: string
              example: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
      401:
        description: Invalid credentials.
        schema:
          type: object
          properties:
            message:
              type: string
              example: Invalid username or password
    """
    if request.method == 'POST':
        payload = request.json
        message, error_code = handle_login_user(payload)
        return jsonify(message), error_code


@blueprint.route('/api/v1/auth/register', methods=['POST'])
def register():
    """
    Register endpoint
    ---
    tags:
      - Authentication
    description: Allows a new user to register.
    parameters:
      - in: body
        name: user
        description: User registration details
        required: true
        schema:
          type: object
          properties:
            username:
              type: string
              example: newuser
            password:
              type: string
              example: securepassword
            confirm_password:
              type: string
              example: securepassword
            email:
              type: string
              example: newuser@example.com
    responses:
      201:
        description: User registered successfully.
        schema:
          type: object
          properties:
            message:
              type: string
              example: User registered successfully
      400:
        description: Bad request (e.g., username already exists, invalid email).
        schema:
          type: object
          properties:
            message:
              type: string
              example: Username already exists
    """
    if request.method == 'POST':
        payload = request.json
        message, error_code = handle_register_user(payload)
        return jsonify(message), error_code
    
# @blueprint.after_app_request
# def refresh_jwt_token(response):
#     """
#         Description:
#             Refresh the JWT token if the user is logged in
#     """
#     handle_jwt_refresh(response)

@blueprint.route('/api/v1/auth/logout', methods=['POST'])
def logout():
    return 'logout'


