from lwca.models import db
from lwca.models.base import Base


class UserNotification(Base):
    """
        UserNotification SQLAlchemy model
    """
    __tablename__ = 'users_notifications'

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    title = db.Column(db.String(64), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    message = db.Column(db.String(500), nullable=False)
    is_read = db.Column(db.Boolean, default=False)
    
    def __repr__(self):
        """
            Return a string representation of the object
        """
        return "<UserNotification id: {}, message: {}>".format(self.id, self.message)
    
    def to_dict(self):
        """
            Return a dictionary representation of the object
        """
        return {
            'id': self.id,
            'date': self.date,
            'title': self.title,
            'message': self.message,
            'read': self.is_read
        }