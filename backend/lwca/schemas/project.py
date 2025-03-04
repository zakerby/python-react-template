from lwca.schemas import ma
from lwca.models.project import Project

from lwca.schemas.user import UserSchema

class ProjectSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Project
        include_fk = True
    
    name = ma.auto_field()
    # Replace the user field with a nested field that only includes basic user info
    user = ma.Nested('UserSchema', only=('id', 'username'), dump_only=True)
