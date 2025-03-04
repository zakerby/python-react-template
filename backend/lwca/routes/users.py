from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from flasgger import swag_from

from lwca.handlers.users_handler import handle_delete_user, handle_get_user

blueprint = Blueprint('users', __name__)

@blueprint.route('/api/v1/user', methods=['GET'])
@jwt_required()
@swag_from('../docs/users/get_user.yml')
def get_user():
  """
  Get User endpoint
  ---
  """
  if request.method == 'GET':
      user, error_code = handle_get_user()
      return jsonify(user), error_code

@blueprint.route('/api/v1/user', methods=['DELETE'])
@jwt_required()
@swag_from('../docs/users/delete_user.yml')
def delete_user():
  """
  Delete User endpoint
  ---
  """
  if request.method == 'DELETE':
      message, error_code = handle_delete_user()
      return jsonify(message), error_code
