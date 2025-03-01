from flask_jwt_extended import get_jwt_identity
from http import HTTPStatus

from lwca.models.user_notification import UserNotification


def  handle_get_user_notifications():
    current_user_id = get_jwt_identity()
    user_notifications = UserNotification.query.filter_by(user_id=current_user_id).all()
    # TODO: Use schema instead of naive serialization
    return [user_notification.to_dict() for user_notification in user_notifications], HTTPStatus.OK