from lwca.models import db
from lwca.models.base import Base

import datetime
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

# The User class is a data model for user accounts
class User(Base):
    """Data model for user accounts."""

    __tablename__ = "users"
    
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    email = db.Column(db.String(80), index=True, unique=True, nullable=False)
    password = db.Column(db.String(500), nullable=False)
    
    projects = db.relationship('Project', backref='user', lazy=True, cascade="all, delete-orphan")

    def __init__(self, **kwargs):
        """
        The function takes in a dictionary of keyword arguments and assigns the values to the class
        attributes
        """
        self.username = kwargs.get("username")
        self.email = kwargs.get("email")
        self.password = kwargs.get("password")

    def __repr__(self):
        """
        The __repr__ function is used to return a string representation of the object
        :return: The username of the user.
        """
        return "<User {}>".format(self.username)
    
    def to_dict(self):
        """
        The function returns a dictionary representation of the object
        :return: The dictionary representation of the object.
        """
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "created": self.created,
            "updated": self.updated,
        }

    def hash_password(self):
        """
        It takes the password that the user has entered, hashes it, and then stores the hashed password in
        the database
        """
        self.password = generate_password_hash(self.password).decode("utf8")

    def check_password(self, password):
        """
        It takes a plaintext password, hashes it, and compares it to the hashed password in the database
        
        :param password: The password to be hashed
        :return: The password is being returned.
        """
        return check_password_hash(self.password, password)