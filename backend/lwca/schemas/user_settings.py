from lwca.schemas import ma

from lwca.models.user_settings import UserSettings

class UserSettingsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserSettings