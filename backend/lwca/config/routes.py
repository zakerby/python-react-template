from lwca import routes

def register_routes(flask_app):
    # Register the public routes
    # TODO: Update this to add url_prefix to organize the API
    # ex: app.register_blueprint(bp, url_prefix='/project')
    
    app_routes = [
        routes.auth,
        routes.users,
        routes.users_settings,
        routes.user_notifications,
        routes.projects
    ]
    
    for blueprint in app_routes:
        flask_app.register_blueprint(blueprint)
