from lwca.models import db
from lwca.models.base import Base


class UserNotification(Base):
    """
        UserNotification SQLAlchemy model
    """
    __tablename__ = 'users_notifications'

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    message = db.Column(db.String(500), nullable=False)
    read = db.Column(db.Boolean, default=False)