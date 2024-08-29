from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flasgger import Swagger


from lwca import routes, utils as u
from lwca.models import db
from lwca.settings import Settings as S
from lwca.tasks import make_celery


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
        self.init_routes()

    def init_flask(self):
        # Init Flask
        self.flask_app = Flask(__name__, static_url_path='/static')
        self.flask_app.config.from_object(S)
        # Register the public routes
        self.register_routes()
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
        # Init Flask-Migrate
        u.wait_for_service('postgres', 5432, timeout=30.0)
        self.migrate = Migrate(self.flask_app, self.db)
        # Init CORS
        CORS(self.flask_app)
        # Init JWT
        self.jwt = JWTManager(self.flask_app)
        # Init Swagger
        Swagger(self.flask_app)
        
    def register_routes(self):
        # Register the public routes
        # TODO: Update this to add url_prefix to organize the API
        # ex: app.register_blueprint(bp, url_prefix='/project')
        for blueprint in [routes.auth, routes.localstack, routes.projects]:
            self.flask_app.register_blueprint(blueprint)

    def init_routes(self):
        @self.flask_app.route('/')
        def home(key):
            return 'home'
