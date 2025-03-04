from lwca.schemas import ma
from lwca.models.user import User

from lwca.schemas.user_settings import UserSettingsSchema

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        exclude = ('password',  'created', 'updated',)
    
    id = ma.auto_field()
    username = ma.auto_field()
    email = ma.auto_field()
    
    user_settings = ma.Nested('UserSettingsSchema', only=('first_name', 'last_name', 'email', 'phone_number', 'bio', 'profile_picture', 'theme'), dump_only=True)
        
    # projects = ma.Nested('ProjectSchema', many=True, only=('id', 'name'), dump_only=True)