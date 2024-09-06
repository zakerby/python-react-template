from flask_restful import Resource, reqparse, marshal_with, fields

from lwca.handlers.auth_handler import handle_register_user

register_parser = reqparse.RequestParser()
register_parser.add_argument('username', type=str, required=True)
register_parser.add_argument('email', type=str, required=True)
register_parser.add_argument('password', type=str, required=True)
register_parser.add_argument('confirm_password', type=str, required=True)

register_resource_fields = {
    'message': fields.String,
    'access_token': fields.String,
    'user': fields.Nested({
        'id': fields.Integer,
        'username': fields.String,
        'email': fields.String
    })
}

class RegisterResource(Resource):
    @marshal_with(register_resource_fields)
    def post(self):
        args = register_parser.parse_args()
        message, error_code = handle_register_user(args)
        return message, error_code