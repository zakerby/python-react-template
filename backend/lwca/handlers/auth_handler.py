import datetime
from datetime import timezone, timedelta, datetime
from http import HTTPStatus

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt, get_jwt_identity, set_access_cookies

from lwca.models.user import User
from lwca.handlers.users_handler import handle_create_user
from lwca.handlers.constants import (
    INCORRECT_PASSWORD,
    USER_NOT_FOUND,
    USERNAME_OR_PASSWORD_MISSING,
    NO_PAYLOAD_PROVIDED,
    PASSWORDS_DO_NOT_MATCH,
)
from lwca.schemas.user import UserSchema

user_schema = UserSchema()

def handle_login_user(data):
    """
        Handle the login of a user
        Description:
            - The function check if the payload contains the keys 'username' and 'password'
            - If the payload is correct, it checks if the user exists in the database
            - If the user exists, it checks if the password is correct, if so, it generates a JWT token
    """
    if data is not None:
        username = data.get('username')
        password = data.get('password')

        if username is not None and password is not None:
            user = User.query.filter_by(username=username).first()
            if user is not None:
                if user.check_password(password):
                    access_token = create_access_token(identity=user.id)
                    return {'access_token': access_token, 'user': user_schema.dump(user)}, HTTPStatus.OK
                else:
                    return {'message': INCORRECT_PASSWORD}, HTTPStatus.UNAUTHORIZED
            else:
                return {'message': USER_NOT_FOUND}, HTTPStatus.NOT_FOUND
        else:
            return {'message': USERNAME_OR_PASSWORD_MISSING}, HTTPStatus.BAD_REQUEST
    else:
        return {'message': NO_PAYLOAD_PROVIDED}, HTTPStatus.BAD_REQUEST

def handle_register_user(data):
    """
        Handle the registration of a user
        Description:
            - The function check if the payload contains the keys 'username' and 'password'
            - If the payload is correct, it checks if the user exists in the database
            - If the user does not exists, it creates a new user
    """
    if data is not None:
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        if password != confirm_password:
            return {'message': PASSWORDS_DO_NOT_MATCH}, HTTPStatus.BAD_REQUEST

        if username is not None and password is not None:
            message, http_code = handle_create_user(username, email, password)
            return {'message': message}, http_code
        else:
            return {'message': USERNAME_OR_PASSWORD_MISSING}, HTTPStatus.BAD_REQUEST
    else:
        return {'message': NO_PAYLOAD_PROVIDED}, HTTPStatus.BAD_REQUEST

def handle_jwt_refresh(response):
    """
        Handle the refresh of a JWT token
        Description:
            - The function refresh the JWT token
    """
    try:
        exp_timestamp = get_jwt()['exp']
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
            set_access_cookies(response, access_token)
        return response
        
    except (RuntimeError, KeyError):
        return response
