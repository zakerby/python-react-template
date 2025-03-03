from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from flasgger import swag_from

from lwca.handlers.user_settings_handler import handle_get_user_settings

blueprint  = Blueprint('users_settings', __name__)

@blueprint.route('/api/v1/user/settings', methods=['GET'])
@jwt_required()
@swag_from('../docs/users_settings/get_user_settings.yml')
def get_user_settings():
    """
    Get User Settings endpoint
    ---
    """
    if request.method == 'GET':
        user_settings, error_code = handle_get_user_settings()
        return jsonify(user_settings), error_code

@blueprint.route('/api/v1/user/settings', methods=['PUT'])
@jwt_required()
@swag_from('../docs/users_settings/update_user_settings.yml')
def update_user_settings():
    """
    Update User Settings endpoint
    ---

    """
    if request.method == 'PUT':
        return jsonify({}), 200