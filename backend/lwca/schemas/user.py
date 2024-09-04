from lwca.schemas import ma
from lwca.models.user import User

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User