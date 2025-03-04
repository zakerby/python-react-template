from lwca.schemas import ma

from lwca.models.user_notification import UserNotification

class UserNotificationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserNotification