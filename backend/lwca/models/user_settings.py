from lwca.models import db
from lwca.models.base import Base

class UserSettings(Base):
    """
        UserSettings SQLAlchemy model
    """
    __tablename__ = 'users_settings'

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    email = db.Column(db.String(80))
    phone_number = db.Column(db.String(15))
    
    bio = db.Column(db.String(500))
    profile_picture = db.Column(db.String(500))
    
    theme = db.Column(db.String(64))
    
    
    def __repr__(self):
        """
            Return a string representation of the object
        """
        return "<UserSettings id: {}, first name: {} last name: {}>".format(self.id, self.first_name, self.last_name)
    
    def to_dict(self):
        """
            Return a dictionary representation of the object
        """
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'phone_number': self.phone_number,
            'bio': self.bio,
            'profile_picture': self.profile_picture,
            'theme': self.theme
        }