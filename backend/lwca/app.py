from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flasgger import Swagger


from lwca import routes, utils as u
from lwca.models import db
from lwca.schemas import ma
from lwca.settings import Settings as S
from lwca.tasks import make_celery

from lwca.config.swagger import get_swagger_config
from lwca.config.routes import register_routes

class Application:
    """
    The main application class
    Description:
        - Initializes the Flask app
        - Initializes the routes
        - Initializes the database
    """
    @classmethod
    def boot(cls):
        """Begin the application"""
        app = cls()
        app.run()
        return app

    def __init__(self):
        self.init_flask()

    def init_flask(self):
        # Init Flask
        self.flask_app = Flask(__name__, static_url_path='/static')
        self.flask_app.config.from_object(S)
        # Register the public routes
        register_routes(self.flask_app)
        self.init_extensions()
        
    def init_extensions(self):
        """
            Define the extensions used in the application:
            - Celery
            - Flask-SQLAlchemy
            - Flask-Migrate
            - CORS
            - JWT
            - Swagger
        """
        # Init Celery
        self.celery = make_celery(self.flask_app)
        # Init Flask-SQLAlchemy
        self.db = db
        self.db.init_app(self.flask_app)
        # Init Marshmallow
        self.ma = ma
        self.ma.init_app(self.flask_app)
        # Init Flask-Migrate
        u.wait_for_service('postgres', 5432, timeout=30.0)
        self.migrate = Migrate(self.flask_app, self.db)
        # Init CORS
        CORS(self.flask_app)
        # Init JWT
        self.jwt = JWTManager(self.flask_app)
        # Init Swagger
        Swagger(self.flask_app, config=get_swagger_config())
        

