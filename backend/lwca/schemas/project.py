from lwca.schemas import ma
from lwca.models.project import Project

class ProjectSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Project
        include_relationships = True
        load_instance = True
        exclude = ["user_id"]