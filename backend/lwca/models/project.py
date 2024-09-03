
from lwca.models import db
from lwca.models.base import Base


class Project(Base):
    """
        Project SQLAlchemy model
    """
    __tablename__ = 'projects'

    name = db.Column(db.String(64))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    

    def to_dict(self):
        """
            Return a dictionary representation of the object
        """
        return {
            'id': self.id,
            'name': self.name,
        }