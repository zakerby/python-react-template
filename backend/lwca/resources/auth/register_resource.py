from flask_restful import Resource

class RegisterResource(Resource):
    def post(self):
        return 'register'