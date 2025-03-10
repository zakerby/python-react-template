from flask_jwt_extended import get_jwt_identity
from http import HTTPStatus

from lwca.models.user_settings import UserSettings
from lwca.handlers.constants import (
    USER_NOT_FOUND
)

from lwca.schemas.user_settings import UserSettingsSchema

user_settings_schema = UserSettingsSchema()

def handle_get_user_settings():
    current_user_id = get_jwt_identity()
    user_settings = UserSettings.query.filter_by(user_id=current_user_id).first()
    if user_settings is not None:
        return user_settings_schema.dump(user_settings), HTTPStatus.OK
    else:
        return {'message': USER_NOT_FOUND}, HTTPStatus.NOT_FOUND