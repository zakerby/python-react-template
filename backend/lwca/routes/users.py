from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

from lwca.handlers.users_handler import handle_delete_user

blueprint = Blueprint('users', __name__)

@blueprint.route('/api/v1/user', methods=['DELETE'])
@jwt_required()
def delete_user():
    """
    Delete User endpoint
    ---
    tags:
      - Users
    description: |
      Allows a user to delete their own account.
      Requires a valid JWT token for authentication.
    security:
      - JWT: []
    responses:
      200:
        description: User deleted successfully.
        schema:
          type: object
          properties:
            message:
              type: string
              example: User deleted successfully
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
              example: "Failed to delete user"
    """
    if request.method == 'DELETE':
        message, error_code = handle_delete_user()
        return jsonify(message), error_code
