from lwca.schemas import ma
from lwca.models.user import User

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        exclude = ('password',  'created', 'updated',)
    
    id = ma.auto_field()
    username = ma.auto_field()
    email = ma.auto_field()
        
    # projects = ma.Nested('ProjectSchema', many=True, only=('id', 'name'), dump_only=True)