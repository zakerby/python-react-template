from flask_jwt_extended import get_jwt_identity
from http import HTTPStatus

from lwca.models.user import User
from lwca.logging import log_info, log_error
from lwca.handlers.constants import (
    USER_NOT_FOUND,
    USER_DELETED
)

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