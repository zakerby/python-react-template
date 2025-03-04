from lwca.schemas import ma
from lwca.models.user_settings import UserSettings

class UserSettingsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserSettings
        include_fk = True
        
    first_name = ma.auto_field()
    last_name = ma.auto_field()
    email = ma.auto_field()
    phone_number = ma.auto_field()
    bio = ma.auto_field()
    profile_picture = ma.auto_field()
    theme = ma.auto_field()
    