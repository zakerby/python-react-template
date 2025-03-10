from flask import Blueprint, request, jsonify
from flasgger import swag_from

from lwca.handlers.auth_handler import handle_login_user, handle_register_user, handle_jwt_refresh

blueprint = Blueprint('auth', __name__)

@blueprint.route('/api/v1/auth/login', methods=['POST'])
@swag_from('../docs/auth/login.yml')
def login():
  """
  Login endpoint
  ---
  """
  if request.method == 'POST':
      payload = request.json
      message, error_code = handle_login_user(payload)
      return jsonify(message), error_code


@blueprint.route('/api/v1/auth/register', methods=['POST'])
@swag_from('../docs/auth/register.yml')
def register():
  """
  Register endpoint
  ---
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


