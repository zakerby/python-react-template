from flask_restful import Resource, reqparse, marshal_with, fields

from lwca.handlers.auth_handler import handle_login_user

login_parser = reqparse.RequestParser()
login_parser.add_argument('username', type=str, required=True)
login_parser.add_argument('password', type=str, required=True)

resource_fields = {
    'access_token': fields.String,
    'user': fields.Nested({
        'id': fields.Integer,
        'username': fields.String,
        'email': fields.String
    })
}

class LoginResource(Resource):
    @marshal_with(resource_fields)
    def post(self):
        args = login_parser.parse_args()
        message, error_code = handle_login_user(args)
        return message, error_code
    
