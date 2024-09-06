from flask_restful import Resource, reqparse, marshal_with, fields

from lwca.handlers.auth_handler import handle_register_user

register_parser = reqparse.RequestParser()
register_parser.add_argument('username', type=str, required=True)
register_parser.add_argument('email', type=str, required=True)
register_parser.add_argument('password', type=str, required=True)
register_parser.add_argument('confirm_password', type=str, required=True)

class RegisterResource(Resource):
    def post(self):
        args = register_parser.parse_args()
        message, error_code = handle_register_user(args)
        return message, error_code