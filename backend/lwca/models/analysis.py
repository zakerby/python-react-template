from lwca.models import db

class Analysis(db.Model):
    """
        Analysis SQLAlchemy model
    """
    __tablename__ = 'analyses'

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    status = db.Column(db.String(255))
    results = db.Column(db.JSON)
    revision = db.Column(db.String(255))

    # Relationships
    project = db.relationship('Project', back_populates='analyses')