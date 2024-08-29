import datetime
from json import JSONEncoder

from lwca.models import db

class Base(db.Model, JSONEncoder):
    """
        Base class for all models
        Description:
            Define common fields for all models
            Implements useful method that will be used by all models
    """
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=True)
    updated = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=True)
    
    # To make the entity serializable in JSON
    def default(self, o):
        return o.__dict__

    # Save methods
    def before_save(self, *args, **kwargs):
        pass

    def after_save(self, *args, **kwargs):
        pass

    def save(self, commit=True):
        self.before_save()
        db.session.add(self)
        if commit:
            try:
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                raise e
        self.after_save()

    # Update methods
    def before_update(self, *args, **kwargs):
        pass

    def after_update(self, *args, **kwargs):
        pass

    def update(self, *args, **kwargs):
        self.before_update(self, *args, **kwargs)
        db.session.commit()
        self.after_update(self, *args, **kwargs)

    # Delete methods
    def delete(self, commit=True):
        db.session.delete(self)
        if commit:
            db.session.commit()