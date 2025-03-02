from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

from lwca.handlers.user_notifications_handler import handle_get_user_notifications

blueprint = Blueprint('user_notifications', __name__)

@blueprint.route('/api/v1/user/notifications', methods=['GET'])
@jwt_required()
def get_user_notifications():
    """
    Get User Notifications endpoint
    ---
    tags:
      - Users
    description: |
      Allows a user to get their own notifications.
      Requires a valid JWT token for authentication.
    security:
      - JWT: []
    responses:
      200:
        description: User notifications retrieved successfully.
        schema:
          type: object
          properties:
            id:
              type: integer
              example: 1
            title:
              type: string
              example: New Notification
            date:
              type: string
              example: 2021-01-01T12:00:00
            message:
              type: string
              example: This is a new notification
            read:
              type: boolean
              example: false
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
    """
    if request.method == 'GET':
        user_notifications, error_code = handle_get_user_notifications()
        return jsonify(user_notifications), error_code