from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

from lwca.handlers.users_handler import handle_delete_user

blueprint = Blueprint('users', __name__)

@blueprint.route('/api/v1/user', methods=['DELETE'])
@jwt_required()
def delete_user():
    if request.method == 'DELETE':
        message, error_code = handle_delete_user()
        return jsonify(message), error_code
