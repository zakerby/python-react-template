from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from flasgger import swag_from

from lwca.handlers.user_notifications_handler import handle_get_user_notifications

blueprint = Blueprint('user_notifications', __name__)

@blueprint.route('/api/v1/user/notifications', methods=['GET'])
@jwt_required()
@swag_from('../docs/user_notifications/get_user_notifications.yml')
def get_user_notifications():
    """
    Get User Notifications endpoint
    ---
    """
    if request.method == 'GET':
        user_notifications, error_code = handle_get_user_notifications()
        return jsonify(user_notifications), error_code