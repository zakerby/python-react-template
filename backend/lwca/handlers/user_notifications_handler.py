from flask_jwt_extended import get_jwt_identity
from http import HTTPStatus
from datetime import datetime
from lwca.models.user_notification import UserNotification
from lwca.models.user import User

from lwca.schemas.user_notification import UserNotificationSchema

user_notifications_schema = UserNotificationSchema(many=True)

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
    return user_notifications

def  handle_get_user_notifications():
    current_user_id = get_jwt_identity()
    # Get all user notifications for the current user
    user = User.query.get(current_user_id)
    return user_notifications_schema.dump(user.user_notifications), HTTPStatus.OK