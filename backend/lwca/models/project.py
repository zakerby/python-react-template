
from lwca.models import db
from lwca.models.base import Base


class Project(Base):
    """
        Project SQLAlchemy model
    """
    __tablename__ = 'projects'

    name = db.Column(db.String(64))
    repository_url = db.Column(db.String(255))
    analysis_status = db.Column(db.String(60))
    # For now, we store the initial analysis results as a JSON object
    analysis_results = db.Column(db.JSON)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    

    def to_dict(self):
        """
            Return a dictionary representation of the object
        """
        return {
            'id': self.id,
            'name': self.name,
            'repository_url': self.repository_url,
            'analysis_status': self.analysis_status,
            'analysis_results': self.analysis_results
        }