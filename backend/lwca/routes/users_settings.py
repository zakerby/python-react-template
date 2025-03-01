from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

blueprint  = Blueprint('users_settings', __name__)

@blueprint.route('/api/v1/user/settings', methods=['GET'])
@jwt_required()
def get_user_settings():
    """
    Get User Settings endpoint
    ---
    tags:
      - Users
    description: |
      Allows a user to get their own settings.
      Requires a valid JWT token for authentication.
    security:
      - JWT: []
    responses:
      200:
        description: User settings retrieved successfully.
        schema:
          type: object
          properties:
            id:
              type: integer
              example: 1
            first_name:
              type: string
              example: John
            last_name:
              type: string
              example: Doe
            email:
              type: string
              example:
            phone_number:
              type: string
              example:
            bio:
              type: string
              example:
            profile_picture:
              type: string
              example:
            theme:
              type: string
              example:
      401:
        description: Unauthorized.  Missing or invalid JWT token.
        schema:
          type: object
          properties:
            message:
              type: string
              example: Missing Authorization Header
      500:
        description: Internal server error.
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Failed to retrieve user settings"
    """
    if request.method == 'GET':
        return jsonify({}), 200


@blueprint.route('/api/v1/user/settings', methods=['PUT'])
@jwt_required()
def update_user_settings():
    """
    Update User Settings endpoint
    ---
    tags:
      - Users
    description: |
      Allows a user to update their own settings.
      Requires a valid JWT token for authentication.
    security:
      - JWT: []
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              first_name:
                type: string
                example: John
              last_name:
                type: string
                example: Doe
              email:
                type: string
                example:
              phone_number:
                type: string
                example:
              bio:
                type: string
                example:
              profile_picture:
                type: string
                example:
              theme:
                type: string
                example:
    responses:
      200:
        description: User settings updated successfully.
        schema:
          type: object
          properties:
            message:
              type: string
              example: User settings updated successfully
      401:
        description: Unauthorized.  Missing or invalid JWT token.
        schema:
          type: object
          properties:
            message:
              type: string
              example: Missing Authorization Header
      500:
        description: Internal server error.
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Failed to update user settings"
    """
    if request.method == 'PUT':
        return jsonify({}), 200