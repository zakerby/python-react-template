from flask_jwt_extended import get_jwt_identity
from http import HTTPStatus
from datetime import datetime
from lwca.models.user_notification import UserNotification


def handle_init_user_notifications(user_id):
    """
        Initialize user notifications when a user is created
    """
    user_notifications = [
        UserNotification(
            user_id=user_id, 
            title='Welcome to the app', 
            message='Welcome to the app, we hope you enjoy it!',
            date=datetime.now()
        ),
        UserNotification(
            user_id=user_id, 
            title='New feature', 
            message='We have added a new feature to the app, check it out!',
            date=datetime.now()
        ),
        UserNotification(
            user_id=user_id, 
            title='Feedback', 
            message='We would love to hear your feedback, please let us know what you think!',
            date=datetime.now()
        )
    ]
    for user_notification in user_notifications:
        user_notification.save()

def  handle_get_user_notifications():
    current_user_id = get_jwt_identity()
    user_notifications = UserNotification.query.filter_by(user_id=current_user_id).all()
    # TODO: Use schema instead of naive serialization
    return [user_notification.to_dict() for user_notification in user_notifications], HTTPStatus.OK