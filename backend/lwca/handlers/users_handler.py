from flask_jwt_extended import get_jwt_identity, create_access_token
from http import HTTPStatus

from lwca.models.user import User
from lwca.models.user_settings import UserSettings

from lwca.logging import log_info, log_error
from lwca.handlers.constants import (
    USER_NOT_FOUND,
    USER_DELETED,
    ERROR_CREATING_USER,
    USER_ALREADY_EXISTS
)
from lwca.handlers.user_notifications_handler import handle_init_user_notifications

from lwca.schemas.user import UserSchema

user_schema = UserSchema()


def handle_get_user():
    current_user_id = get_jwt_identity()
    user = User.query.filter_by(id=current_user_id).first()
    if user is not None:
        return {'user': user_schema.dump(user)}, HTTPStatus.OK
    else:
        return {'message': USER_NOT_FOUND}, HTTPStatus.NOT_FOUND

def handle_delete_user():
    current_user_id = get_jwt_identity()
    user = User.query.filter_by(id=current_user_id).first()
    if user is not None:
        try:
            user.delete()
            log_info(f'User {user.username} deleted by user {current_user_id}')
            return {'message': USER_DELETED}, HTTPStatus.OK
        except Exception as e:
            log_error(f'Error deleting user: {str(e)}')
            return {'message': str(e)}, HTTPStatus.INTERNAL_SERVER_ERROR
    else:
        return {'message': USER_NOT_FOUND}, HTTPStatus.NOT_FOUND
    

def handle_create_user(username: str, email: str, password: str):
    """
        Handle the creation of a user
        Description:
            - The function check if the user exists in the database
            - If the user does not exists, it creates a new user
    """
    try:
        user = User.query.filter_by(username=username).first()
        if user is None:
            user = User(username=username, email=email, password=password)
            user.hash_password()
            
            user_settings = UserSettings(user_id=user.id, email=email)
            user.user_settings = user_settings
            user.user_notifications  = handle_init_user_notifications(user.id)
            user.save()
                  
            # Generate a JWT token to allow auto login
            access_token = create_access_token(identity=user.id)
            return {'access_token': access_token, 'user': user.to_dict()}, HTTPStatus.OK
        else:
            return {'message': USER_ALREADY_EXISTS}, HTTPStatus.CONFLICT
    except Exception as e:
        return {'message': ERROR_CREATING_USER.format(str(e))}, HTTPStatus.INTERNAL_SERVER_ERROR